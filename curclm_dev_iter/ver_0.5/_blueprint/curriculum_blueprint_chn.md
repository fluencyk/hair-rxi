# RXI 课程体系蓝图（Curriculum Blueprint）

> **RXI-Lab｜学术增强型设计与技术融合课程体系**  
> **版本：** v0.1.0 — 初始交付草案  
> **状态：** 工作蓝图（Working Blueprint）  
> **结构依据：** `_construction/curriculum_construction.json`（当前 MVP 草案）  
> **面向对象：** 学术负责人 · 课程设计师 · 授课教师 · 设计团队 · 工程团队 · 业务负责人

> **文档定位：** 本文以课程构建 JSON 为结构依据，结合已有课程认知与设计讨论进行解释性扩展；并非从 JSON 自动、确定性生成的文件。文中“示例成果”“建议方向”“未来流程”不等同于已获批准的教学要求或已上线功能。

---

## 01. 执行概览（Executive Overview）

### 1.1 建立彼此连接的学习体验

RXI 课程体系通过结构化的学术学习与应用型项目实践，将**工程学、系统思维、设计、技术与研究**连接为一个跨学科学习框架。

它面向希望建立基础学术能力、探索专业方向，并通过可展示的成果支持未来学业发展与作品集建设的学习者。体系并非将课程简单排列，而是形成一条可以因人调整的能力发展路线：

**基础学习 → 专业探索 → 综合实践 → 学术与作品集成果**

不同背景、兴趣、学习准备度与发展目标的学生，可以采用不同的组合方式。上述路线表达的是能力发展逻辑，而非所有学生必须遵循的固定课程序列。

### 1.2 核心教育主张

| 维度 | 教育目的 | 预期价值 |
|---|---|---|
| 学术基础 | 建立工程、分析与研究导向的基本能力 | 提升后续学术学习的准备度 |
| 跨学科实践 | 连接设计、技术与专业领域知识 | 发展综合问题解决能力 |
| 成果发展 | 将学习转化为项目、研究证据与作品集 | 形成可观察、可解释的学习成果 |

> 学生不仅需要知道某一学科“包含什么”，还应逐步学会如何调查问题、形成解决方案、评价证据，以及清晰表达自己的工作。

---

## 02. 课程体系架构（Curriculum Architecture）

### 2.1 整体结构

当前课程模型由六个相互关联的部分构成：

```text
RXI CURRICULUM / RXI 课程体系
│
├── 01. CORE MODELS / 核心课程模型
│   ├── Model A — Foundation Core / 基础核心
│   │   ├── RXI-310 Fundamentals of Engineering
│   │   └── RXI-315 Systems Design and Abstract Modeling
│   └── Model B — Advanced Core / 进阶核心
│       ├── Foundation Core（继承基础核心）
│       ├── RXI-356 Applied Convergence of Design and Technology
│       └── RXI-SEM Research and Academic Seminar
│
├── 02. CONCENTRATIONS / 专业方向
│   ├── UI / UX / HCI
│   ├── Modern Software Development
│   ├── Applied AI and Intelligent Systems
│   ├── Robotics
│   ├── Industrial Design and Technologies
│   └── Business Intelligence and Analytics
│
├── 03. PATHWAYS / 学习路径
│   └── 专业方向的合理组合与目标成果
│
├── 04. ELECTIVES / 选修扩展
│   ├── Thematic Electives / 专题选修
│   └── Project-Based Electives / 项目选修
│
├── 05. AFTER-MODULE / 后续进阶模块
│   ├── Advanced Portfolio Training
│   └── Outcome-Based Course Packages
│
└── 06. VIP OFFERINGS / 高强度导师指导产品
    ├── Project Success — Cornerstone
    ├── Research Exploration — Milestone
    └── Admission Track — Capstone
```

这一架构区分了**共享学术基础、专业学习方向、个性化组合、灵活选修，以及面向特定成果的进阶支持**。它们相互关联，但不应混同为同一种课程对象。

### 2.2 六个部分各自解决什么问题？

| 组成部分 | 关键问题 | 主要职责 |
|---|---|---|
| Core Models | 学生首先需要具备哪些共通能力？ | 建立基础与进阶能力 |
| Concentrations | 学生希望探索什么专业领域？ | 提供学科化、专业化方向 |
| Pathways | 不同方向如何有意义地组合？ | 组织连贯的学习路线 |
| Electives | 还需要补充什么学习内容？ | 提供针对性扩展与灵活选择 |
| After-Module | 已有成果如何进一步深化？ | 支持高阶作品集与成果发展 |
| VIP Offerings | 哪些目标需要更密集的个性化指导？ | 提供导师驱动的学术支持 |

**边界说明：** 这些部分体现课程与服务的组织关系，不意味着每位学生必须完成全部六类内容。实际选课、先修、周期与学习负担，仍需依据项目方案和学生情况确定。

---

## 03. 构建模型与数据基础（Construction Model & Data Foundation）

### 3.1 为什么需要课程构建模型？

RXI 不希望课程体系仅散落在 Word、幻灯片和教师个人文档之中。因此，我们先建立可被机器读取、也可被团队共同理解的结构化课程构建模型。

它为学术规划、课程开发、跨团队沟通与未来内容生产提供统一的结构参照，帮助团队回答：有哪些课程实体、它们如何组织、有哪些专业方向、方向如何组合，以及哪些进阶服务可以支持学术与作品集成果。

### 3.2 模型字段本体

主要源文件：`_construction/curriculum_construction.json`

```json
{
  "meta": {},
  "curriculum": {
    "name": "",
    "description": "",
    "target_learners": "",
    "cores": {},
    "concentrations": {},
    "pathways": {},
    "electives": {},
    "after_module": {},
    "vip_offerings": {}
  }
}
```

**字段释义：** `meta` 描述模型元信息；`curriculum` 承载课程体系主体；其下六个关键节点分别对应前述六类课程与服务对象。

**设计解析：** JSON 负责描述结构与关键事实，Blueprint 则说明这些结构的教育意义、存在理由及关键关系。Blueprint 不应自行创造与 JSON 冲突的课程实体。

### 3.3 从结构数据到教学交付

```text
curriculum_construction.json
        │ 结构定义与关键事实
        ▼
curriculum_blueprint.md / curriculum_blueprint_chn.md
        │ 语义解释、设计理由、跨角色沟通
        ▼
Course Outlines / 课程大纲
        ▼
Syllabi / 教学纲要
        ▼
Learning Modules / 学习模块
        ▼
Teaching Materials / 教学材料
        ▼
Student Projects & Portfolio Deliverables
```

这里的箭头代表**设计与开发上的依赖**，并不表示完整的自动化生产管线已经实现。

### 3.4 工作原则

**先建立结构，再逐步增加细节。** 当前 MVP 暂不规定每次课的活动、评分细则、全部工具与资源，以免在早期制造过多建模负担。

---

## 04. Core Models：共享学术基础

### 4.1 核心课程模型是什么？

Core Models 规定后续专业学习所依赖的共通能力。当前分为 **Model A — Foundation Core（基础核心）** 和 **Model B — Advanced Core（进阶核心）**。两者表达能力发展的不同阶段，而非两组毫无关系的课程清单。

### 4.2 Model A — Foundation Core

**定位：** 建立工程素养、科学与定量推理、系统思维、抽象建模及结构化问题解决能力。

```json
{
  "core_model_a": {
    "name": "Foundation Core",
    "units": 2,
    "description": "Establish foundational engineering literacy, analytical reasoning, and systems-oriented problem-solving capabilities.",
    "courses": [
      {
        "id": "RXI-310",
        "name": "Fundamentals of Engineering",
        "role": "Introduce engineering principles, scientific reasoning, quantitative analysis, and evidence-based problem-solving."
      },
      {
        "id": "RXI-315",
        "name": "Systems Design and Abstract Modeling",
        "role": "Develop systems thinking, abstraction, model construction, and structured design reasoning."
      }
    ]
  }
}
```

#### RXI-310 — Fundamentals of Engineering（工程学基础）

**课程重点：** 将工程学作为一种理解和解决实际问题的系统性实践。学生接触科学推理、定量分析、工程约束、实验、原型制作与基于证据的评价。

**候选学习内容：** 问题识别与界定；科学与定量推理；需求与约束；调查与实验；原型和测试；技术记录与沟通。

**示例成果：** 问题陈述、实验记录、初步原型、工程计算与评价报告。

**设计边界：** 本课程不追求让学生一次性掌握某个工程专业的全部知识，而是发展可迁移的工程素养。

#### RXI-315 — Systems Design and Abstract Modeling（系统设计与抽象建模）

**课程重点：** 通过系统思维和抽象方法理解复杂对象之间的关系。学生学习确定系统边界、识别组成与交互、构建有目的的模型，并比较不同设计方案。

**候选学习内容：** 系统边界；抽象与表征；结构与行为建模；需求与依存关系；系统级设计推理；模型评价与沟通。

**示例成果：** 系统图、抽象模型、需求描述、备选设计表征及模型化解释。

**设计边界：** 课程核心不是某种绘图软件的操作培训，而是学习如何利用模型理解系统并支持设计决策。

### 4.3 为什么这两门课程要组合？

| 工程学基础 | 系统设计与抽象建模 |
|---|---|
| 调查并解决工程问题 | 理解并表征系统 |
| 运用科学和定量推理 | 运用抽象与结构化推理 |
| 开发、测试并评价方案 | 分析关系并比较备选设计 |
| 形成工程实践证据 | 形成系统级模型与解释 |

二者互补：一门强化工程问题解决，一门强化系统层面的理解与设计表达，为后续综合项目提供共同基础。

### 4.4 Model B — Advanced Core

**定位：** 在基础核心之上，进一步发展设计与技术整合、应用调查、研究性推理和学术沟通能力。

```json
{
  "core_model_b": {
    "name": "Advanced Core",
    "units": 4,
    "description": "Extend foundational capabilities into interdisciplinary design-technology practice and research-oriented communication.",
    "includes": ["core_model_a"],
    "courses": [
      {
        "id": "RXI-356",
        "name": "Applied Convergence of Design and Technology",
        "role": "Integrate design and technology to investigate needs, develop solutions, prototype, and evaluate outcomes."
      },
      {
        "id": "RXI-SEM",
        "name": "Research and Academic Seminar",
        "role": "Develop inquiry, critical reading, evidence-based argumentation, academic discussion, and research communication."
      }
    ],
    "progression": "Foundation Core + Advanced Core"
  }
}
```

**关键解释：** `units: 4` 在当前草案中表示 Model B 所覆盖的**四个课程单元总量**：基础核心的两门，加上进阶部分新增的两门；不是额外增加四门，也不是四个学分。`includes: ["core_model_a"]` 表示继承关系，避免在数据中重复定义基础课程。

#### RXI-356 — Applied Convergence of Design and Technology（设计与技术的应用融合）

**课程重点：** 将设计调查与技术实现连接到一个可检验的问题解决过程，综合考虑人的需求、设计意图、技术可能性及评价证据。

**候选学习内容：** 设计调查与问题界定；用户和利益相关者需求；设计标准与技术要求；技术选择和集成；原型迭代；测试、评价与表达。

**示例成果：** 数字或实体综合原型、设计文档、技术实现证据及项目展示。

**设计边界：** 不局限于某一类设计或技术专业；核心在于有目的的跨领域整合，而非简单拼接工具。

#### RXI-SEM — Research and Academic Seminar（研究与学术研讨）

**课程重点：** 培养学术探究、批判性解释、证据支持的论证及研究沟通能力。

**候选学习内容：** 研究问题形成；文献与来源解读；批判性阅读和综合；证据推理；学术讨论；研究伦理；反思与表达。

**示例成果：** 研究简报、批判性综述、学术海报、口头报告或入门级学术手稿。

**设计边界：** 并不要求每名学生都产出达到正式发表水平的论文。Seminar 的职责是发展探究与学术交流能力，而不只是项目成果展示。

### 4.5 核心能力发展关系

```text
Foundation Core / 基础核心
├── 工程素养
├── 分析推理
├── 系统思维
└── 抽象建模
        │
        ▼
Advanced Core / 进阶核心
├── 设计与技术整合
├── 应用调查
├── 研究性推理
└── 学术沟通
        │
        ▼
专业探索与高阶项目准备
```

这是能力发展模型，不是固定的学期安排。

---

## 05. Concentrations：专业学习方向

### 5.1 专业方向的定义

Concentration 是相对明确的学科探索与专业化方向，让学生在共享基础能力之上进入特定领域。它不应仅仅是一份软件工具清单或流行技术目录。

### 5.2 字段表达

```json
{
  "concentrations": {
    "description": "Specialized learning directions that apply the shared core capabilities within distinct disciplinary and professional contexts.",
    "options": [
      {
        "id": "ui_ux_hci",
        "name": "UI/UX/HCI",
        "focus": "Human-computer interaction, user experience, interface design, and human-centered systems."
      },
      {
        "id": "modern_software_development",
        "name": "Modern Software Development",
        "focus": "Software engineering, application development, and contemporary development practices."
      }
    ]
  }
}
```

上例仅展示两个对象的字段形式；完整 MVP 模型包含六个方向。`id` 是供 Pathways 引用的稳定标识符，`name` 用于展示，`focus` 概括方向定位。

### 5.3 六个专业方向

#### 01 — UI / UX / HCI（用户界面、用户体验与人机交互）

**定位：** 以人为中心的数字体验设计。关注理解用户、设计交互、评价可用性和形成有意义的数字体验。

**候选内容：** 用户研究、信息架构、界面设计、交互设计、原型与可用性评价。

**可能成果：** 交互原型、UX 研究报告、界面系统与人本设计案例。

#### 02 — Modern Software Development（现代软件开发）

**定位：** 软件工程与应用开发。关注现代软件系统的设计、构建、集成与评价。

**候选内容：** 编程基础、应用架构、前后端开发、开发工作流、测试与协作式软件工程。

**可能成果：** 可运行应用、软件原型、技术文档与实现作品集。

#### 03 — Applied AI and Intelligent Systems（应用人工智能与智能系统）

**定位：** 将人工智能概念与技术应用于有实际意义的问题。

**候选内容：** 机器学习基础、数据准备、AI 应用、智能代理、系统评价与负责任的 AI 实践。

**可能成果：** AI 应用原型、智能系统演示、分析报告与评价记录。

#### 04 — Robotics（机器人技术）

**定位：** 传感、计算、控制、机械结构与物理交互的系统集成。

**候选内容：** 机器人组成、传感器与执行器、控制原理、嵌入式系统、系统集成与测试。

**可能成果：** 机器人原型、系统演示、工程记录与综合技术项目。

#### 05 — Industrial Design and Technologies（工业设计与技术）

**定位：** 将设计调查、材料认知、制作技术与工程考量用于产品开发。

**候选内容：** 产品研究、形态与功能、材料、制造过程、CAD、原型制作与评价。

**可能成果：** 产品概念、数字或实体模型、原型、设计开发记录与作品集案例。

#### 06 — Business Intelligence and Analytics（商业智能与分析）

**定位：** 以数据分析和解释支持组织理解与决策。

**候选内容：** 数据素养、探索性分析、数据可视化、商业智能、分析建模与结果解读。

**可能成果：** 分析报告、仪表板、可视化作品、决策支持原型与证据驱动的建议。

### 5.4 专业方向的设计边界

目前 Concentrations 定义的是**可探索的专业方向**，并未最终规定授课周数、统一技术栈、全部评分标准、保证获得的作品集成果或普遍适用的先修顺序。这些属于后续课程设计与交付规划。

---

## 06. Pathways：连接专业方向与学习成果

### 6.1 Pathway 是什么？

Pathway（学习路径）将一个或多个 Concentrations 组织成具有明确目标的学习安排。

**Concentration 回答“学习什么方向”，Pathway 回答“如何组合这些方向以达成某种成果”。** 例如，人本数字产品可以组合 HCI 与软件开发；智能实体产品可以组合机器人与工业设计。

### 6.2 字段本体与引用关系

```json
{
  "id": "human_centered_digital_products",
  "name": "Human-Centered Digital Products",
  "concentrations": [
    "ui_ux_hci",
    "modern_software_development"
  ],
  "outcome": "A user-centered digital product supported by design rationale and implementation evidence."
}
```

`concentrations` 数组通过 ID 引用已有专业方向，不重复复制其定义。这是当前模型最明确的跨对象引用关系之一。

### 6.3 示例学习路径

| Pathway | 专业方向组合 | 示例成果 |
|---|---|---|
| Human-Centered Digital Products（以人为中心的数字产品） | UI/UX/HCI + Modern Software Development | 有设计依据与实现证据的数字产品 |
| AI-Enabled Systems（AI 赋能系统） | Applied AI + Modern Software Development | AI 应用或智能系统原型 |
| Intelligent Physical Products（智能实体产品） | Robotics + Industrial Design and Technologies | 实体或机器人集成原型 |
| Data-Driven Decision Systems（数据驱动决策系统） | Business Intelligence and Analytics + Modern Software Development | 分析解决方案或决策支持应用 |

这些是**示例组合**，不是完整、排他的路径目录，也不是对具体成果的交付保证。

### 6.4 Pathway 的实际价值

Pathways 将课程架构与个性化学习规划连接起来，使团队能够讨论：哪些组合在学术上合理、如何将学生兴趣转化为连贯的学习方向、哪些项目能体现跨学科能力，以及基础课程如何支持专业成果。

```text
共享核心能力
     │
     ▼
专业方向 A ──┐
            ├──► Pathway ──► 应用型学习成果
专业方向 B ──┘
```

**边界：** Pathway 是学习规划结构，不必然是一门新的独立课程。实际实施取决于学生准备度、项目范围、资源与导师条件。

---

## 07. Electives：灵活选修扩展

### 7.1 目的

Electives 为核心课程与专业方向之外的具体需求提供补充学习机会，使课程体系可以灵活扩展，而不必频繁重构整体架构。

### 7.2 字段本体

```json
{
  "electives": {
    "description": "Flexible learning opportunities that extend the core curriculum and concentration pathways according to learner needs.",
    "categories": [
      {
        "id": "thematic_electives",
        "name": "Thematic Electives",
        "description": "Focused modules addressing selected topics, methods, or technologies."
      },
      {
        "id": "project_electives",
        "name": "Project-Based Electives",
        "description": "Applied learning organized around a defined problem, project, or demonstrable outcome."
      }
    ]
  }
}
```

### 7.3 Thematic Electives（专题选修）

围绕某一知识主题、研究方法或技术开展集中学习，例如特定设计方法、新兴技术、研究工具或补充性技术基础。适合需要有针对性补足能力的学生。

### 7.4 Project-Based Electives（项目选修）

围绕明确问题或项目目标开展应用学习，可包含调查、设计、实现、评价与展示。适合希望进一步获得实践经验或探索特定项目方向的学生。

### 7.5 设计边界

选修内容应补充而非重复 Core Models 与 Concentrations。具体主题可以迭代更新，而无需每次都修改课程体系的顶层结构。

---

## 08. After-Module：进阶成果发展

### 8.1 定位

After-Module 为完成相关课程学习后的学生提供进一步深化、整合和展示学习成果的机会，尤其适用于需要强化作品集质量、学科深度或学术证据的学习者。

### 8.2 字段本体

```json
{
  "after_module": {
    "description": "Advanced, outcome-oriented offerings available after relevant core or concentration learning.",
    "offerings": [
      {
        "id": "advanced_portfolio_training",
        "name": "Advanced Portfolio Training",
        "description": "Customized advanced training to strengthen portfolio quality, disciplinary depth, and project evidence."
      },
      {
        "id": "outcome_based_packages",
        "name": "Outcome-Based Course Packages",
        "description": "Integrated learning packages organized around specific academic, research, or portfolio outcomes."
      }
    ]
  }
}
```

### 8.3 Advanced Portfolio Training（高阶作品集训练）

侧重提高学生既有作品的质量、连贯性与证据强度。可能涉及项目精修、技术或设计改进、研究记录、评价验证、作品集叙事与展示沟通。

其目标并非单纯美化作品，而是强化**作品、能力与证据之间的联系**。

### 8.4 Outcome-Based Course Packages（成果导向课程包）

围绕明确的学术、研究或作品集目标，组合必要的学习、项目实践、导师指导、文档和展示准备。具体课程包应依据学生评估与学术规划确定。

### 8.5 边界

After-Module 是课程体系的进阶扩展，不自动等同于正式 Concentration，也不必然属于某个固定 Core Model。

---

## 09. VIP Offerings：导师驱动的个性化学术发展

### 9.1 定位

VIP Offerings 为需要更密集项目指导、研究支持或升学材料整合的学习者提供个性化服务。当前区分三个产品：

- **Project Success — Cornerstone Course（项目成功／基石课程）**
- **Research Exploration — Milestone Course（研究探索／里程碑课程）**
- **Admission Track — Capstone Course（升学路径／综合收束课程）**

三种称谓体现目标复杂度和服务重点，不代表所有学生都必须按顺序购买或完成。

### 9.2 字段本体

```json
{
  "vip_offerings": {
    "description": "Premium, mentorship-oriented electives designed around progressively more demanding academic and portfolio outcomes.",
    "shared_prerequisites": ["Pre-Academic Writing"],
    "courses": [
      {
        "id": "project_success",
        "name": "Project Success",
        "level": "Cornerstone",
        "mentoring": "1:1 instructor mentoring",
        "outcome": "A completed project with clearly documented objectives, process, and deliverables."
      },
      {
        "id": "research_exploration",
        "name": "Research Exploration",
        "level": "Milestone",
        "mentoring": "Research-oriented instructor guidance",
        "outcome": "A structured research project with a mini-paper or preprint-style manuscript."
      },
      {
        "id": "admission_track",
        "name": "Admission Track",
        "level": "Capstone",
        "mentoring": "2:1 instructor and advisor mentoring",
        "outcome": "An admission-oriented academic or portfolio package aligned with the learner's target programs."
      }
    ]
  }
}
```

**结构说明：** 在当前 JSON 中，`vip_offerings` 与 `electives` 是 `curriculum` 下的并列节点；但 VIP 的产品定位具有选修与个性化服务属性。此处保持既有结构，不擅自重构嵌套关系。

### 9.3 Project Success — Cornerstone

**指导模式：** 1:1 授课导师指导。

**主要目标：** 帮助学生界定、推进并完成有意义的项目，强调项目定义、执行规划、迭代改进与过程记录。

**预期成果：** 完成项目，并能够清楚说明目标、过程、挑战与成果。

### 9.4 Research Exploration — Milestone

**指导模式：** 研究导向的导师指导；具体师生配置尚未在 JSON 中固定。

**主要目标：** 引导学生经历较为结构化的研究过程，包括研究问题形成、文献检索与阅读、方法选择、调查分析、结果解释及学术写作。

**预期成果：** 具有相应研究证据的 mini-paper 或 preprint-style manuscript（预印本风格手稿）。

**边界：** 这是一种学习成果形式，不保证正式发表、同行评审通过或学术会议录用。

### 9.5 Admission Track — Capstone

**指导模式：** 2:1 授课导师与升学顾问联合指导。

**主要目标：** 将学生已有学术成果、项目证据与作品集材料整合为面向目标院校或专业的申请准备方案。

**预期成果：** 结构连贯、与目标项目相匹配的学术及作品集准备材料。

**边界：** 院校录取由外部教育机构决定，课程不保证录取结果。

### 9.6 三类产品的能力发展示意

```text
Cornerstone / 项目开发与完成
           │
           ▼
Milestone / 研究探索与学术表达
           │
           ▼
Capstone / 学术与作品集综合整合
```

这是一种复杂度递进的解释，不是强制的选课依赖链。

### 9.7 关于 Pre-Academic Writing

当前 JSON 草案将 `Pre-Academic Writing` 列为 `shared_prerequisites`。但其课程内容、达成标准及对三个 VIP 产品是否均适用，尚待正式确认。**不得将这一草案字段直接宣传为已生效的统一入学门槛。**

---

## 10. 从课程结构走向学习成果

### 10.1 课程不只是名称清单

有意义的课程体系需要把学习目标与可观察的学生表现联系起来。后续课程开发可以采用以下概念链路：

```text
Learning Objectives / 学习目标
             │
             ▼
Learning Activities / 学习活动
             │
             ▼
Student Artifacts / 学生交付物
             │
             ▼
Evaluation Evidence / 评价证据
             │
             ▼
Demonstrated Capabilities / 已展示的能力
```

**重要区别：** 上述概念尚未全部作为字段写入当前 MVP JSON；它们是后续 Syllabus 与 Module 设计的对齐原则，而非已经实施的数据约束。

### 10.2 什么是学生交付物（Artifact）？

Artifact 是学习或项目活动形成的可观察结果。

| 学习情境 | 可能的交付物 |
|---|---|
| 工程学 | 原型、实验记录、技术报告 |
| 系统设计 | 系统模型、架构图、需求分析 |
| HCI / UX | 交互原型、用户研究报告、可用性评价 |
| 软件开发 | 应用程序、源代码、测试结果、文档 |
| 应用 AI | AI 原型、评价报告、模型演示 |
| 机器人 | 集成原型、测试证据、工程记录 |
| 工业设计 | 产品模型、原型、设计案例 |
| 商业分析 | 仪表板、分析报告、数据可视化 |
| 学术研讨 | 研究简报、文献综合、海报、学术手稿 |

交付物的存在不等于学习质量已经得到证明；还需要结合推理过程、设计选择、证据和学生解释能力进行判断。

### 10.3 成果对齐原则

后续课程设计应逐步保证：目标明确且适龄；活动支持目标能力；交付物能够提供证据；评价标准与目标相匹配；成果要求与学生水平及资源条件相称。

当前 Blueprint 仅确立这一原则，不提前规定所有课程使用同一套评分方法。

---

## 11. 课程开发工作流（Curriculum Development Workflow）

### 11.1 从学术规划到教学材料

```text
课程构建模型（JSON）
         │
         ▼
课程蓝图（Blueprint）
         │
         ▼
课程大纲（Course Outline）
         │
         ▼
教学纲要（Syllabus）
         │
         ▼
学习模块（Learning Modules）
         │
         ▼
教学与学习材料
         │
         ▼
学生实践与项目
         │
         ▼
学习证据与最终交付物
```

各阶段逐步增加教育设计细节，同时与上游课程定位保持一致。这里表达的是**建议的开发顺序**，而不是已实现的自动执行链。

### 11.2 跨角色职责

| 角色 | 主要职责 |
|---|---|
| 学术负责人 | 课程方向、学术一致性与质量把关 |
| 课程设计师 | 学习目标、课程结构、Syllabus 设计 |
| 授课教师 | 教学实施、导师指导与学习评价 |
| 设计团队 | 信息呈现、视觉沟通、教学材料设计 |
| 工程团队 | 结构化数据、内容工作流、生成与校验支持 |
| 业务负责人 | 产品理解、资源规划与交付优先级 |

同一份 Blueprint 应支持不同角色从各自视角理解课程体系，而不需要维护彼此矛盾的定义。

### 11.3 数据支持的内容生产

```text
结构化课程数据
      │
      ▼
内容理解与语义映射
      │
      ▼
草案生成
      │
      ▼
学术审核
      │
      ▼
设计与教师精修
      │
      ▼
正式交付材料
```

未来可能支持课程大纲起草、Syllabus 草案、模块组织、教学材料编排、一致性检查及文档维护。

**现状边界：** 这些属于可发展的工程能力，不能据此宣称 RXI 已拥有完整自动化课程生产系统。AI 辅助可提升效率，但不能替代学术审核。

---

## 12. 模型关系与设计边界

### 12.1 关键关系

| 关系 | 含义 |
|---|---|
| Advanced Core → Foundation Core | 进阶模型包含基础学习内容 |
| Concentrations → Core Capabilities | 专业化学习应与共享基础能力衔接 |
| Pathways → Concentrations | 学习路径组合既有专业方向 |
| Electives → Learning Needs | 选修满足特定补充学习需求 |
| After-Module → Prior Learning | 进阶产品深化既有学习与成果 |
| VIP Offerings → Individual Objectives | 导师支持围绕个性化目标组织 |

这些关系并不都需要成为 JSON 的硬编码引用。

### 12.2 三种不同的关系

**结构依存（Structural Dependency）**：模型明确记录的对象引用，例如：

```json
{
  "includes": ["core_model_a"]
}
```

**语义耦合（Semantic Alignment）**：两个部分在教育设计上需要协调，例如专业方向应适当地衔接基础能力，但不一定存在直接字段引用。

**开发依赖（Development Dependency）**：一个交付物为另一个交付物提供依据，例如 Course Outline 支撑 Syllabus，Syllabus 支撑 Module 规划。

三者不能不加区分地压缩成同一种数据关系。

### 12.3 MVP 已覆盖与尚未覆盖的范围

**当前已覆盖：** 课程架构、核心课程身份、六个专业方向、示例路径、选修类别、进阶产品类别和 VIP 指导产品。

**尚未完整覆盖：** 详细学习成果、课时与学分、周计划、模块活动、评分量规、人员与资源配置、完整先修规则、定价和商业包装，以及自动化生产实现。

这些留白是当前交付阶段的主动取舍，并非宣称上述工作已经完成。

---

## 13. 实施路线图（Implementation Roadmap）

### Phase 1 — Curriculum Foundation（课程体系基础）

**目标：** 形成结构清晰、能够被不同角色理解的课程架构。

**主要交付：** 课程构建 JSON、Blueprint、Core Models、Concentrations、初步 Pathways，以及 Electives 和进阶产品结构。

**当前状态：** MVP 初始草案；内容仍需后续审核与完善。

### Phase 2 — Course Development（课程开发）

**目标：** 将课程架构转化为可教学的课程定义。

**重点工作：** 精修课程定位、确定学习目标、编写 Course Outlines 和 Syllabi、建立初步 Modules、识别代表性学生成果。

### Phase 3 — Teaching Material Development（教学材料开发）

**目标：** 形成支持真实教学的内容与活动。

**重点工作：** 教学内容、案例与练习、项目活动、评价方法、教学一致性检查、视觉与交互材料完善。

### Phase 4 — Pilot & Iteration（试点与迭代）

**目标：** 验证教学可行性并持续改进。

**重点工作：** 试点课程或模块、收集师生反馈、分析学生成果、识别课程缺口、调整课程及材料，并同步更新 JSON 与 Blueprint。

路线图描述的是建议推进顺序。实际时间与范围取决于人力、资源和业务优先级。

---

## 14. 课程设计原则（Design Principles）

### 01 — Academic Coherence（学术一致性）

课程与学习方向应形成可解释的教育结构，而不是随意拼接知识主题。

### 02 — Progressive Capability Development（能力渐进发展）

从基础理解逐步走向更独立的调查、整合、实践与沟通。

### 03 — Interdisciplinary Integration（跨学科整合）

在具有教育意义的地方连接设计、工程、技术和研究；避免将跨学科误解为对不相关内容的浅层堆砌。

### 04 — Evidence-Based Outcomes（证据支持的学习成果）

学生的能力表现应尽可能由可观察的工作、推理、记录与评价证据支持。

### 05 — Flexible Personalization（灵活个性化）

允许学生按需要组合基础课程、专业学习、项目与导师指导，但个性化方案必须在学术上合理、运营上可行。

### 06 — Iterative Development（迭代式开发）

课程构建是持续设计过程。先形成可用的结构基线，再根据教学证据和资源条件提升精度与交付质量。

---

## 15. 当前交付基线（Current Delivery Baseline）

### 15.1 当前草案已建立的内容

| 领域 | 已形成的初步内容 |
|---|---|
| 课程愿景 | 学术增强型跨学科设计与技术学习框架 |
| 核心架构 | Foundation Core + Advanced Core |
| 核心课程 | 四课程单元的整体进阶结构 |
| 专业方向 | 六个 Concentrations |
| 综合学习 | 四个示例 Pathways |
| 灵活扩展 | 两类 Electives |
| 高阶发展 | After-Module 产品方向 |
| 个性化指导 | 三类 VIP Offerings |
| 数据基础 | 结构化 JSON 课程构建草案 |
| 开发方向 | Course Outline → Syllabus → Module 工作流 |

**交付口径：** “已形成初步模型与文档草案”不等于“全部课程已经完成设计、验证并可直接开课”。

### 15.2 下一阶段优先级

1. 核心课程大纲与 Syllabi。
2. 专业方向的课程规划。
3. 学习目标与代表性交付物。
4. 初步教学模块。
5. 学术审核与试点准备。

下一阶段的重点不是继续增加顶层类别，而是提高现有课程实体的教育定义质量与交付准备度。

### 15.3 结语

RXI Curriculum 的目标是一套**相互连接的学术学习体系**，而不只是一份课程目录。

它将基础能力、专业探索、跨学科实践和成果导向发展组织在同一个框架之中。Construction JSON 提供结构基准；Blueprint 则让学术、设计、工程与业务角色能够共同理解、讨论并推进这一框架。

**长期目标：建立一套学术上连贯、工程上可开发、学习路径可适配、并能够产生有意义学习证据的课程体系。**

---

## 附录 A — 课程模型与认知空间参考

**课程构建文件：** `_construction/curriculum_construction.json`  
**英文蓝图：** `_blueprint/curriculum_blueprint.md`  
**中文蓝图：** `_blueprint/curriculum_blueprint_chn.md`

**认知空间文件：**

```text
_cognition_space/
├── curclm_cogn_space.md
├── ccs_funda_eng.md
├── ccs_sysdes_absmod.md
├── ccs_applconv_destech.md
├── ccs_seminar.md
├── ccs_hci_ux_ui.md
├── ccs_mdn_ssw_dev.md
├── ccs_aai_intelsys.md
├── ccs_robotics.md
├── ccs_indstrl_design.md
└── ccs_bia.md
```

Cognition Space 用于调查、收集和筛选候选知识、方法、技能与成果形式，**不自动等同于已批准的 Syllabus 或教学模块**。

---

## 附录 B — 版本、治理与维护

| 项目 | 说明 |
|---|---|
| 文档 | RXI Curriculum Blueprint — Simplified Chinese |
| 版本 | v0.1.0 |
| 状态 | 初始交付草案 |
| 结构依据 | `curriculum_construction.json` MVP 草案 |
| 主要用途 | 学术架构阐释与跨角色沟通 |
| 下一轮修订重点 | 课程定义、学习成果、交付规划、源文件一致性 |

### B.1 维护原则

当课程架构变化时，应优先更新 Construction JSON，再审查对应的英文与中文 Blueprint；当仅修改解释性文字且不影响结构事实时，可以独立编辑 Blueprint。

### B.2 当前尚未实现的治理能力

本版本尚未建立自动化的 JSON → Blueprint 生成、双语同步与一致性校验。因此，文档更新需要人工或 AI 辅助核对，不能假定它们天然同步。

### B.3 In-Page Elucidation Unit（IPEU）说明

本文采用“页面内阐释单元”的表达思路：按需要组合**标题、描述、设计解析、字段本体、关键依存关系与有限展开**。IPEU 是本项目的工作性术语，不是声称已经确立的行业标准，也不是要求每个字段都单独拥有六个固定区块。

---

*RXI-Lab — Curriculum Development Initiative*  
*End of Simplified Chinese Blueprint v0.1.0*
