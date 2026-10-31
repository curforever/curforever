"""Check public-only contribution evidence and failed refresh preservation."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('metrics', Path(__file__).parents[1] / 'scripts/update_metrics.py')
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)


class RefreshBoundaryTests(unittest.TestCase):
    def test_contribution_example_survives_newer_pr_and_requires_verified_record(self):
        newest = {'repository': 'upstream/newer', 'number': 1,
                  'url': 'https://github.com/upstream/newer/pull/1'}
        example = {'repository': 'apache/logging-log4j2', 'number': 4401,
                   'url': 'https://github.com/apache/logging-log4j2/pull/4401'}
        for english in (False, True):
            card = metrics.contribution_card([newest, example], english)
            self.assertIn('Log4j', card)
            self.assertIn(example['url'], card)
            self.assertNotIn(newest['url'], card)
            self.assertIn('2 PRs merged', card)
            self.assertIn('regression tests' if english else '回归测试', card)
            fallback = metrics.contribution_card([newest], english)
            self.assertNotIn('Log4j', fallback)
            self.assertIn(newest['url'], fallback)
            self.assertNotIn('Log4j', metrics.contribution_card([], english))

    def test_repository_refresh_excludes_forks_private_and_other_owners(self):
        def repo(name, owner='curforever', private=False, fork=False):
            return {'name': name, 'owner': {'login': owner}, 'private': private, 'fork': fork}
        # The first page is full of forks: filtering must not stop pagination.
        first = [repo('fork-' + str(i), fork=True) for i in range(100)]
        second = [repo('own-project', owner='CurForever'), repo('private-tool', private=True),
                  repo('other-project', owner='upstream'), repo('leetcode-master', fork=True)]
        with patch.object(metrics, 'github_json', side_effect=[first, second]) as api:
            selected = metrics.github_public_repos()
        self.assertEqual([r['name'] for r in selected], ['own-project'])
        self.assertEqual(api.call_count, 2)
        for english in (False, True):
            table = metrics.project_index(selected, english)
            self.assertIn('own-project', table)
            self.assertNotIn('leetcode-master', table)
            self.assertNotIn('private-tool', table)
            self.assertNotIn('other-project', table)

    def test_private_unmerged_and_other_author_results_are_excluded(self):
        items = [{'repository_url': 'https://api.github.com/repos/' + repo, 'number': n, 'pull_request': {}}
                 for repo, n in [('hidden/project', 1), ('upstream/project', 2), ('upstream/project', 3), ('upstream/project', 4), ('upstream/project', 4)]]
        def api(path):
            if path.startswith('search/issues'):
                return {'total_count': len(items), 'incomplete_results': False, 'items': items}
            if path == 'repos/hidden/project':
                return {'private': True, 'owner': {'login': 'hidden'}}
            if path == 'repos/upstream/project':
                return {'private': False, 'owner': {'login': 'upstream'}}
            n = int(path.rsplit('/', 1)[1])
            if n == 1:
                raise AssertionError('Private PR contents must never be fetched')
            return {'merged_at': '2026-01-01T01:00:00Z' if n != 2 else None, 'merged': n != 2,
                    'user': {'login': 'another-author' if n == 3 else 'curforever'}, 'number': n,
                    'title': 'Public patch', 'html_url': 'https://github.com/upstream/project/pull/' + str(n)}
        with patch.object(metrics, 'github_json', side_effect=api):
            prs = metrics.github_public_contributions()
        self.assertEqual([p['number'] for p in prs], [4])
        self.assertNotIn('hidden', metrics.contribution_record(prs))

    def test_incomplete_search_does_not_replace_existing_refresh_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            outputs = ['README.md', 'README.en.md', 'assets/metrics/snapshot.json', 'contributions/README.md']
            for name in outputs:
                f = root / name
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_text('keep-existing', encoding='utf-8')
            with patch.object(metrics, 'ROOT', root), patch.object(metrics, 'github_public_repos', return_value=[]), patch.object(metrics, 'github_json', return_value={'total_count': 1, 'incomplete_results': True, 'items': []}):
                with self.assertRaises(RuntimeError):
                    metrics.main()
            for name in outputs:
                self.assertEqual((root / name).read_text(encoding='utf-8'), 'keep-existing')

    def test_new_repository_description_stays_plain_text_in_the_table(self):
        rows = metrics.project_index([{'name': 'new-public-tool', 'description': '<script>x</script> | [fake](url)\nnext', 'fork': False}])
        self.assertNotIn('<script>', rows)
        self.assertIn('&lt;script&gt;', rows)
        self.assertIn('\\|', rows)
        self.assertIn('\\[fake\\]', rows)
        self.assertEqual(len(rows.splitlines()), 3)

    def test_missing_contribution_marker_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            template = '<!-- PUBLIC_PROJECTS_START -->\nold\n<!-- PUBLIC_PROJECTS_END -->'
            for name in ['README.md', 'README.en.md']:
                (root / name).write_text(template, encoding='utf-8')
            with patch.object(metrics, 'ROOT', root), patch.object(metrics, 'github_public_repos', return_value=[]), patch.object(metrics, 'github_public_contributions', return_value=[]):
                with self.assertRaises(ValueError):
                    metrics.main()
            self.assertEqual((root / 'README.md').read_text(encoding='utf-8'), template)
            self.assertFalse((root / 'assets/metrics/snapshot.json').exists())


if __name__ == '__main__':
    unittest.main()
