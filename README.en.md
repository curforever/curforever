<p align="right"><a href="README.md">简体中文</a> · <b>English</b></p>

<img src="assets/header.svg" width="100%" alt="curforever — Backend, Tools & Human Experience" />

**Hi, I'm curforever 👋** · Interested in Java backend engineering, developer tools and human–computer interaction.

I enjoy breaking complex problems into things I can verify, and turning repeated work into reusable tools. This is a collection of my engineering practice, research and useful experiments.

<p>
  <img src="assets/badges/backend-en.svg" alt="Focus: Java backend" />
  <img src="assets/badges/tools-en.svg" alt="Exploring: AI tools" />
  <img src="assets/badges/bugs-en.svg" alt="Daily: debugging" />
  <img src="assets/badges/learning-en.svg" alt="Input: source code and books" />
</p>

[🏆 Selected work](#user-content-work) · [🧰 Toolkit](#user-content-stack) · [📦 Repositories](#user-content-projects) · [📚 Beyond code](#user-content-beyond) · [💬 Say hello](https://github.com/curforever/curforever/issues)

<a name="work"></a>
## 🏆 Selected projects & practice

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/curforever/curforever-skills"><img src="assets/skills-card.svg" width="100%" alt="Agent Skills — reusable developer workflows" /></a>
<b>Agent Skills · Reusable ways of working</b><br />
A categorized collection of skills for development, learning, communication and project handoffs, giving AI agents a more structured workflow.<br /><br />
<code>Planning</code> <code>Code review</code> <code>Knowledge</code><br /><br />
<a href="https://github.com/curforever/curforever-skills/tree/main/skills/development/code-reviewer">Code review skill →</a> · <a href="https://github.com/curforever/curforever-skills">Full catalog →</a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/curforever/CangQiongWaiMai-Java"><img src="assets/backend-card.svg" width="100%" alt="Java Backend — business flows and framework internals" /></a>
<b>Food delivery platform · Java practice</b><br />
Employee, menu and order management, with practice in caching and Spring internals. Based on the Heima Sky Take Out course.<br /><br />
<code>Spring Boot</code> <code>MyBatis</code> <code>Redis</code><br /><br />
<a href="https://github.com/curforever/CangQiongWaiMai-Java/blob/master/sky-take-out/sky-server/src/main/java/com/sky/aspect/AutoFillAspect.java">AOP field filling →</a> · <a href="https://github.com/curforever/CangQiongWaiMai-Java/blob/master/sky-take-out/sky-server/src/main/java/com/sky/task/OrderTask.java">Scheduled order handling →</a>
</td>
</tr>
</table>

### 🚄 Ticketing system practice · Data & concurrency

`Spring Boot` `Spring Cloud` `MySQL` `Redis` `RocketMQ`

- **Data access:** practiced sharding with composite keys, Snowflake IDs and encoded routing information to support user-ID and order-ID queries.
- **State consistency:** used Binlog and messaging for database/cache synchronization, and delayed messages for unpaid-order cancellation.
- **Concurrency:** refined distributed-lock granularity by train seat type to reduce interference between different seat categories.

<sub>Practice experience; source code is not currently available in my public repositories.</sub>

### 🥽 VR / HCI research · The person using the system

Studied how virtual characters' movement and voice realism influence user perception and experience in multi-user VR cinemas. The resulting paper appeared at **CSCWD 2025, with me as first author**.

This experience keeps me interested in HCI: after implementing a system, I also want to understand how people perceive and use it.

<a name="stack"></a>
## 🧰 Toolkit · Organized by purpose

| Area | Tools & technologies | What I explore |
| :--- | :--- | :--- |
| **Language & fundamentals** | ![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![JVM](https://img.shields.io/badge/JVM-475569?style=flat-square) | Collections and HashMap internals, reflection, CAS / AQS, locking |
| **Backend** | ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![Spring Cloud](https://img.shields.io/badge/Spring_Cloud-16A34A?style=flat-square) ![MyBatis](https://img.shields.io/badge/MyBatis-334155?style=flat-square) | IoC / DI, AOP, APIs and business flows, scheduled jobs |
| **Data & distributed systems** | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white) ![RocketMQ](https://img.shields.io/badge/RocketMQ-C2410C?style=flat-square&logo=apache&logoColor=white) | Indexes and transactions, cache consistency, sharding, lock granularity |
| **System fundamentals** | ![Networking](https://img.shields.io/badge/Network-0369A1?style=flat-square) ![OS](https://img.shields.io/badge/OS-475569?style=flat-square) | TCP / HTTP, processes and threads, I/O multiplexing |
| **Tools & interaction** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![Agent Skills](https://img.shields.io/badge/Agent_Skills-7C3AED?style=flat-square) ![VR HCI](https://img.shields.io/badge/VR_%2F_HCI-0D9488?style=flat-square) | Reusable workflows, documentation and knowledge, user perception |

<a name="projects"></a>
## 📦 Repository index · One clear purpose each

| Project | Stars | Forks | Purpose & scope |
| :--- | :---: | :---: | :--- |
| [Agent Skills](https://github.com/curforever/curforever-skills) | ![Stars](assets/metrics/curforever-skills-stars.svg) | ![Forks](assets/metrics/curforever-skills-forks.svg) | Reusable development, learning and project-management skills |
| [Java practice](https://github.com/curforever/CangQiongWaiMai-Java) | ![Stars](assets/metrics/CangQiongWaiMai-Java-stars.svg) | ![Forks](assets/metrics/CangQiongWaiMai-Java-forks.svg) | Course-based practice: business flows, caching and Spring |
| [Keyboard](https://github.com/curforever/Keyboard) | ![Stars](assets/metrics/Keyboard-stars.svg) | ![Forks](assets/metrics/Keyboard-forks.svg) | Switch-testing photos and component lists |
| [CSS examples](https://github.com/curforever/CSSLearning) | ![Stars](assets/metrics/CSSLearning-stars.svg) | ![Forks](assets/metrics/CSSLearning-forks.svg) | Small CSS examples and interface experiments |

<sub>![Metrics updated](assets/metrics/updated-en.svg) · GitHub API data, refreshed weekly.</sub>

<a name="beyond"></a>
## 📚 Beyond code · Curiosity needs input

| Category | What I do | A concrete example |
| :--- | :--- | :--- |
| **Technical writing** | Organize knowledge from source code, practice and retrospectives | [Code-reading skill](https://github.com/curforever/curforever-skills/tree/main/skills/development/code-reading-coach) · [Reading-coach skill](https://github.com/curforever/curforever-skills/tree/main/skills/learning/read-coach) |
| **Learning & growth** | Long-term reading and English learning; an interest in work methods and business development | Turn reading into knowledge I can explain and apply, and connect reflection with the next experiment |
| **Useful tinkering** | Custom mechanical keyboards and switch selection | [Photos and component lists](https://github.com/curforever/Keyboard) · Input devices deserve thoughtful tuning too |

<details>
<summary><b>🎓 Background · Education & selected achievements</b></summary>

- **Southeast University · School of Software Engineering** | 2023–2026; master's research in VR / HCI.
- **Hefei University of Technology · School of Computer Science** | 2019–2023.
- **Research:** first-author paper at CSCWD 2025 on virtual-character perception and experience in multi-user VR cinemas.
- **Selected awards:** National Scholarship, national third prize in China Software Cup, provincial second prizes in mathematical modeling and Lanqiao Cup.
- **English:** CET-4 and CET-6 both 600+; second prize in the National English Competition for College Students.

</details>

---

**💬 Ideas, questions or opportunities?** Start a conversation in [Issues](https://github.com/curforever/curforever/issues).

<sub>Keeping the toolbox growing. Sometimes reinventing a wheel; hopefully one that turns. 🛠️</sub>
