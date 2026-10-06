<p align="right"><b>简体中文</b> · <a href="README.en.md">English</a></p>

<img src="assets/header.svg" width="100%" alt="curforever — Backend, Tools & Human Experience" />

**你好，我是 curforever 👋** · 关注 Java 后端、开发者工具与人机交互。

喜欢把复杂问题拆成能验证的小问题，也喜欢把反复做的事变成顺手的工具。这里收纳我的工程实践、研究经历和一些有用的折腾。

<p>
  <img src="assets/badges/backend.svg" alt="主线：Java 后端" />
  <img src="assets/badges/tools.svg" alt="副本：AI 工具实践" />
  <img src="assets/badges/bugs.svg" alt="日常：与 Bug 对线" />
  <img src="assets/badges/learning.svg" alt="习惯：读源码，也读书" />
</p>

[🏆 核心实践](#work) · [🧰 技术栈](#stack) · [📦 项目索引](#projects) · [📚 技术之外](#beyond) · [💬 交流](https://github.com/curforever/curforever/issues)

<a name="work"></a>
## 🏆 核心项目与实践

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/curforever/curforever-skills"><img src="assets/skills-card.svg" width="100%" alt="Agent Skills — 把工作方法变成可复用技能" /></a>
<b>Agent Skills · 可复用的工作方法</b><br />
把开发、学习、沟通与项目交接中的方法整理成技能目录，让 AI Agent 的工作更有章法。<br /><br />
<code>规划</code> <code>代码审查</code> <code>知识沉淀</code><br /><br />
<a href="https://github.com/curforever/curforever-skills/tree/main/skills/development/code-reviewer">看代码审查技能 →</a> · <a href="https://github.com/curforever/curforever-skills">完整目录 →</a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/curforever/CangQiongWaiMai-Java"><img src="assets/backend-card.svg" width="100%" alt="Java Backend — 从业务流程走到框架机制" /></a>
<b>外卖平台 · Java 工程实践</b><br />
围绕员工、菜品与订单管理，练习业务实现、缓存处理与 Spring 机制。基于黑马《苍穹外卖》课程。<br /><br />
<code>Spring Boot</code> <code>MyBatis</code> <code>Redis</code><br /><br />
<a href="https://github.com/curforever/CangQiongWaiMai-Java/blob/master/sky-take-out/sky-server/src/main/java/com/sky/aspect/AutoFillAspect.java">看 AOP 字段填充 →</a> · <a href="https://github.com/curforever/CangQiongWaiMai-Java/blob/master/sky-take-out/sky-server/src/main/java/com/sky/task/OrderTask.java">订单定时处理 →</a>
</td>
</tr>
</table>

### 🚄 购票系统实践 · 在数据与并发之间找平衡

`Spring Boot` `Spring Cloud` `MySQL` `Redis` `RocketMQ`

- **数据怎么查**：复合分片键结合雪花算法与基因法，练习按用户 ID、订单号查询的分库分表方案。
- **状态怎么对齐**：通过 Binlog 与消息队列同步数据库和缓存；用延时消息处理超时未支付订单。
- **并发怎么收敛**：按列车座位类型细化分布式锁粒度，减少不同座位类型之间的互相阻塞。

<sub>实践经历，尚未在当前公开仓库中展示源码。</sub>

### 🥽 VR / HCI 研究 · 代码之外，还有人的体验

研究多用户 VR 影院中，虚拟角色的动作与声音真实感如何影响用户感知与体验。相关论文发表于 **CSCWD 2025，第一作者**。

这段经历让我持续关注人机交互：系统实现之后，还要思考用户怎样感知、理解和使用它。

<a name="stack"></a>
## 🧰 技术栈 · 工具箱按用途收纳

| 方向 | 工具与技术 | 我关注的问题 |
| :--- | :--- | :--- |
| **语言与基础** | ![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![JVM](https://img.shields.io/badge/JVM-475569?style=flat-square) | 集合与 HashMap 源码、反射、CAS / AQS、锁机制 |
| **后端开发** | ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![Spring Cloud](https://img.shields.io/badge/Spring_Cloud-16A34A?style=flat-square) ![MyBatis](https://img.shields.io/badge/MyBatis-334155?style=flat-square) | IoC / DI、AOP、接口与业务流程、定时任务 |
| **数据与分布式** | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white) ![RocketMQ](https://img.shields.io/badge/RocketMQ-C2410C?style=flat-square&logo=apache&logoColor=white) | 索引与事务、缓存一致性、分库分表、锁粒度 |
| **系统基础** | ![Networking](https://img.shields.io/badge/Network-0369A1?style=flat-square) ![OS](https://img.shields.io/badge/OS-475569?style=flat-square) | TCP / HTTP、进程与线程、I/O 多路复用 |
| **工具与交互探索** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![Agent Skills](https://img.shields.io/badge/Agent_Skills-7C3AED?style=flat-square) ![VR HCI](https://img.shields.io/badge/VR_%2F_HCI-0D9488?style=flat-square) | 可复用工作流、文档与知识整理、用户感知与体验 |

<a name="projects"></a>
## 📦 项目索引 · 每个仓库，一句话说明白

| 项目 | Stars | Forks | 用途与边界 |
| :--- | :---: | :---: | :--- |
| [Agent Skills](https://github.com/curforever/curforever-skills) | ![Stars](assets/metrics/curforever-skills-stars.svg) | ![Forks](assets/metrics/curforever-skills-forks.svg) | 开发、学习与项目管理技能集 |
| [外卖平台](https://github.com/curforever/CangQiongWaiMai-Java) | ![Stars](assets/metrics/CangQiongWaiMai-Java-stars.svg) | ![Forks](assets/metrics/CangQiongWaiMai-Java-forks.svg) | Java 课程实践：业务、缓存与 Spring |
| [键盘记录](https://github.com/curforever/Keyboard) | ![Stars](assets/metrics/Keyboard-stars.svg) | ![Forks](assets/metrics/Keyboard-forks.svg) | 试轴照片、体验与选型清单 |
| [CSS 案例](https://github.com/curforever/CSSLearning) | ![Stars](assets/metrics/CSSLearning-stars.svg) | ![Forks](assets/metrics/CSSLearning-forks.svg) | CSS 学习案例与界面探索 |

<sub>![指标更新时间](assets/metrics/updated.svg) · 数据来自 GitHub API，每周刷新。</sub>

<a name="beyond"></a>
## 📚 技术之外 · 好奇心也需要输入

| 分类 | 我在做什么 | 一个具体入口或例子 |
| :--- | :--- | :--- |
| **写作** | 从源码、实践和复盘中整理知识 | [代码阅读技能](https://github.com/curforever/curforever-skills/tree/main/skills/development/code-reading-coach) · [阅读技能](https://github.com/curforever/curforever-skills/tree/main/skills/learning/read-coach) |
| **学习** | 长期阅读与英语学习，关注工作方法和企业发展 | 把“读过”变成能解释、能应用的知识，用复盘连接下一次实践 |
| **折腾** | 客制化机械键盘，研究手感与选型 | [试轴照片与清单](https://github.com/curforever/Keyboard) · 输入设备也值得认真调校 |

<details>
<summary><b>🎓 履历速览 · 教育与代表性成果</b></summary>

- **东南大学 · 软件学院**｜2023–2026，硕士阶段研究方向为 VR / HCI。
- **合肥工业大学 · 计算机学院**｜2019–2023。
- **研究成果：**CSCWD 2025 第一作者论文，多用户 VR 影院中的虚拟角色感知与体验。
- **代表性荣誉：**国家级奖学金、中国软件杯国家三等奖、数学建模与蓝桥杯省二等奖。
- **英语：**CET-4 / CET-6 均 600+，全国大学生英语竞赛二等奖。

</details>

---

**💬 有想法、问题或合作机会？** 欢迎在 [Issues](https://github.com/curforever/curforever/issues) 留言。

<sub>持续更新工具箱。偶尔造轮子，希望轮子能转。 🛠️</sub>
