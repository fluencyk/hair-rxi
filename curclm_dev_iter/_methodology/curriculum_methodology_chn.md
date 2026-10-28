# RXI Curriculum Construction Methodology

> **RXI-Lab｜课程体系构建方法论与方法流**  
> **Version:** 0.1.0 — Initial Delivery Draft  
> **Status:** Working Methodology / 待评审  
> **Scope:** Curriculum 0→1 Construction  
> **Related:** `_construction/curriculum_construction.json` · `_blueprint/curriculum_blueprint.md` · `_blueprint/curriculum_blueprint_chn.md`  
> **Audience:** Academic Leadership · Curriculum Design · Instructors · Design · Engineering · Business

---

## 01. 文档定位：我们究竟做了什么？

本文件记录 RXI-Lab 课程体系从初始需求到第一版结构化课程蓝图的**整体方法体系**。它不是某一项方法的介绍，也不是对当前成果的宣传性总结，而是一份可以被解释、复核、质疑和迭代的工作基准。

本阶段的核心问题并非“列出一些适合国际学校学生的课程”，而是：

> 如何在需求尚未完全明确、学科方向跨度较大、教学资源与商业约束尚待确认的条件下，建立一个结构清楚、可持续细化、可供不同角色共同理解的课程架构？

我们的初步回答是：**先建立认知与需求边界，再进行抽象建模，形成受控的结构化课程模型，最后将模型转化为可解释的课程蓝图；教学内容和交付能力在此基础上逐层建设。**

这是一套 **Curriculum Construction Methodology**：其内部包括若干方法（Methods）、模型（Models）、工作流（Workflows）、解释机制（Elucidation Mechanisms）和验证原则（Validation Principles）。

### 当前成果与边界

| 已形成的初步成果 | 尚未形成或验证的能力 |
|---|---|
| 课程总体结构与层级关系 | 完整的教学效果验证 |
| Foundation / Advanced Core 模型 | 全量课程大纲与学期 Syllabus |
| 六个 Concentrations 及示例 Pathways | 每周讲义、实验、作业、期中与期末评价体系 |
| Construction JSON 与 Blueprint 草案 | 教授专属讲义及其版本管理机制 |
| 初步 IPEU 解释方式 | 确定性自动生成与自动一致性校验 |

**边界声明：** 架构合理性不等于教学有效性，结构化数据不等于已经实现自动化产线，设计提案不等于已获组织审批。

---

## 02. 总体方法流：从模糊需求到可解释架构

```text
初始需求与业务语境
        │
        ▼
需求澄清与约束识别（Requirement Framing）
        │
        ▼
认知空间构建（Cognition Space Mapping）
        │
        ▼
抽象建模与结构选择（Abstraction & Architecture）
        │
        ▼
课程构建模型（curriculum_construction.json）
        │
        ▼
语义阐释与跨角色表达（IPEU / Blueprint）
        │
        ▼
审查、对齐与阶段性交付（Review & Alignment）
        │
        ▼
后续：Course Outline → Syllabus → Modules → Lectures / Assignments
        │
        ▼
后续：Teaching Pilot → Evidence → Iteration
```

**重要说明：** 这张图是对当前工作的规范化重构，不表示每一步在真实工作中都严格线性发生。实际过程包含反复回退、并行探索和阶段性重构。它是 **iterative workflow**，不是一次性瀑布流程。

---

## 03. 方法基座：三树三土（Three Trees & Three Soils）

“三树三土”是本项目采用的上层思考框架，用于提醒设计者：课程方案不能直接从零散主题或工具清单中拼装，而应在需求、认知与方案之间建立可追溯关系。

### 三树（Three Trees）

| 模型 | 核心问题 | 在课程构建中的作用 |
|---|---|---|
| Requirement Tree | 为什么需要这些课程？服务哪些学习者与目标？ | 梳理目标人群、业务要求、学习诉求与交付约束 |
| Cognition Tree | 对应领域有哪些值得学习的知识、方法与能力？ | 构建候选知识空间，识别概念、依赖与认知层级 |
| Solution Tree | 应如何组织课程、路径与教学产物？ | 将经过筛选的内容转化为课程结构及实施方案 |

### 三土（Three Soils）

“土”强调各树赖以成立的**上下文、证据与现实约束**，而不是另一套必须机械对应的字段表。当前草案将其作为三类审查视角：

- **需求之土：** 学生画像、学校与家长诉求、资源条件、商业与时间边界。
- **认知之土：** 学科知识、教学经验、可核查的研究与实践证据、知识的适用范围。
- **方案之土：** 教师能力、课程时长、工具设施、交付成本、评价方式与组织执行能力。

以上“三土”的命名是当前文档的**操作性阐释**，仍需与后续正式 `BASELINE.md` 和方法论定义校准；不应被视为已经冻结的唯一术语版本。

### 运行原则

1. 不允许 Solution Tree 脱离 Requirement Tree 自行扩张。
2. 不允许 Cognition Tree 中的全部候选知识自动成为必教内容。
3. 任何课程设计都必须接受现实资源与教学可行性的约束。
4. 三树之间允许反馈修正，不能假设一次建模就永久正确。

---

## 04. Cognition Space：先建立候选认知空间，再做课程取舍

Cognition Space（认知空间）不是 Syllabus，也不是最终授课内容。它是课程设计之前的**候选知识与能力地图**。

在现阶段，相关文档分布于 `_cognition_space/`，涵盖核心课程与六个专业方向。其任务是支持设计者回答：某一领域的关键概念是什么、方法是什么、可能形成什么能力、哪些内容值得进入课程，以及哪些内容应暂缓。

候选维度可包括：

| 维度 | 示例性问题 |
|---|---|
| Disciplinary Knowledge | 该领域的基础知识体系是什么？ |
| Concepts & Theories | 哪些概念与理论具有解释力？ |
| Research Methods | 如何形成问题、收集和解释证据？ |
| Processes & Practices | 有哪些可训练的实践过程？ |
| Tools & Technologies | 哪些工具用于实现，而不是替代知识目标？ |
| Artifacts & Deliverables | 学生能够留下什么可观察的成果？ |
| Competencies | 这些学习活动证明了什么能力？ |
| Levels & Prerequisites | 内容之间是否存在必要的认知先后关系？ |

**筛选规则：** 从 Cognition Space 进入课程结构的内容，应经过学习目标相关性、认知负荷、先修关系、实施成本和可评价性等判断。候选知识清单不直接等于教学承诺。

---

## 05. Abstraction Modeling：把课程清单转化为课程系统

在抽象建模阶段，我们不急于规定每周课时和教学工具，而先识别具有相对稳定身份的课程实体及其关系。

### 关键抽象对象

- **Core Models：** 公共基础能力与进阶能力结构。
- **Concentrations：** 相对独立的学科探索方向。
- **Pathways：** 将不同方向组织成面向学习目标的组合路径。
- **Electives：** 针对特定学习需求的灵活扩展。
- **After-Module：** 面向既有学习成果的进一步深化。
- **VIP Offerings：** 以个性化指导和结果导向为核心的服务性课程产品。

### 结构选择的主要理由

**Foundation Core / Advanced Core：** 通过共享基础能力降低方向课之间的重复建设。Advanced Core 在当前模型中继承 Foundation Core，`units: 4` 表示包含两门基础课与两门进阶课的累计四单元结构，不应误读为额外四门课程或四学分。

**Concentrations / Pathways：** Concentration 回答“学什么领域”；Pathway 回答“如何组合不同领域以支持某种目标”。两者不等价，Pathway 也不必自动成为一门独立课程。

**Electives / After-Module / VIP：** 分别承担灵活补充、成果深化与高强度个性化指导的作用。当前 JSON 将其列为并列结构；它们在业务表达上可能有关联，但不应在未经模型修改的情况下宣称存在硬编码的包含关系。

### 抽象边界

课程实体、课程包、教学服务、教授讲义、评价活动属于不同层次。若在初始 JSON 中一次性塞入所有细节，会造成模型膨胀、职责混乱和维护成本上升。因此采取 **Minimum Viable Model（最小可用模型）** 与 **Progressive Elaboration（渐进细化）**。

---

## 06. Structured Construction：以 JSON 承载结构事实

`_construction/curriculum_construction.json` 是当前课程结构的主要机器可读基准，其作用是稳定实体身份、名称、组织层级和部分显式引用关系。

```json
{
  "meta": {},
  "curriculum": {
    "cores": {},
    "concentrations": {},
    "pathways": {},
    "electives": {},
    "after_module": {},
    "vip_offerings": {}
  }
}
```

上述仅为**结构示意**，不是完整 Schema，也不应覆盖原文件中的其他属性。

### 为什么使用 JSON？

1. 减少多份文字材料之间的课程实体命名漂移。
2. 为后续文档生成、校验、检索和系统集成提供可解析输入。
3. 让结构事实与人类解释分离，降低一次修改引起的连锁歧义。
4. 为未来 Agentic Workflow 提供可控的数据边界。

### 不应夸大的能力

当前 JSON 不是成熟的课程数据库，不具备天然的 Schema Validation、自动版本同步、教学质量评估或自动生成完整课程的能力。上述能力属于未来工程建设任务。

---

## 07. IPEU：从数据结构到人类可理解的解释

**IPEU — In-Page Elucidation Unit（页内阐释单元）** 是当前 Blueprint 写作中使用的一种解释组织方式。它强调围绕一个有意义的课程概念或结构单元，形成相对完整的解释，而不是对每个 JSON 字段机械逐条注释。

一个 IPEU 可以按需要组合：

| 元素 | 回答的问题 |
|---|---|
| Title / Identity | 这是什么？ |
| Description / Purpose | 为什么存在？ |
| Elucidation | 其教育逻辑是什么？ |
| Field / Structure Embodiment | 它在模型中如何表达？ |
| Dependencies / Couplings | 与哪些对象有关？ |
| Bounded Expansion | 可以进一步发展什么、当前不能承诺什么？ |

这些元素是**解释素材**，不是每一页都必须重复的六段式模板。

### 示例：Foundation Core

- **结构事实：** Foundation Core 包含 `RXI-310` 与 `RXI-315` 两个课程单元。
- **教育阐释：** 前者强调工程问题分析与证据，后者强调系统边界、抽象与关系建模。
- **关系说明：** Advanced Core 通过 `includes: ["core_model_a"]` 引用基础模型。
- **边界说明：** 这种关系表示当前架构中的课程递进设计，不自动等于每位学生都必须遵循同一教学日历。

### 解释性内容的证据分级

- **Model Fact：** 可在 JSON 中直接核对的结构事实。
- **Grounded Interpretation：** 根据字段语义及已确认设计共识作出的合理解释。
- **Design Proposal：** 为后续讨论提出的建议，尚未成为正式决定。
- **Open Question：** 尚待学术、业务或教学团队确认的问题。

**核心纪律：解释可以帮助理解结构，但不能在没有审批的情况下制造新的结构事实。**

---

## 08. Source of Truth 与一致性治理

项目中至少存在三种不同类型的权威性：

| 资料 | 负责什么 | 不负责什么 |
|---|---|---|
| Construction JSON | 课程实体、层级、显式关系与结构事实 | 全部教育理由与教学质量 |
| Baseline（拟建立） | 已确认决策、版本、边界与待决事项 | 自动替代实际课程模型 |
| Methodology（本文） | 方法、工作流、解释规则与审查原则 | 擅自改写课程实体 |
| Blueprint | 面向人的课程架构解释与沟通 | 独立宣布未经确认的新政策 |
| Cognition Space | 候选知识、方法、能力与学科认知 | 自动等同已批准 Syllabus |

### 典型漂移风险

- **Structural Drift：** JSON 改了课程数，Blueprint 仍写旧数字。
- **Semantic Drift：** JSON 只是示例成果，文字却将其描述成强制毕业标准。
- **Decision Drift：** 曾经的讨论假设在后续版本中被误当作正式决策。
- **Instructional Drift：** 教授变体偏离课程共同学习目标或最低评价要求。

### 推荐的工作纪律

```text
READ → ALIGN → MODIFY → VALIDATE → DELIVER
```

1. **Read：** 读取真实仓库文件及版本，不凭聊天记忆替代原文。
2. **Align：** 对齐当前 Baseline、JSON、Methodology 和相关 Cognition Space。
3. **Modify：** 明确本轮修改范围，避免无关重写。
4. **Validate：** 核查 ID、数量、引用、概念、版本及待决假设。
5. **Deliver：** 交付文件并说明修改范围、仍未解决的问题和验证状态。

此处是**拟采用的协作规范**；尚不表示已完成 GitHub 自动连接或自动校验。

---

## 09. 可观测边界、真实边界与分层交付

课程开发至少存在两种不同的成熟度边界：

**可观测边界（Observable Boundary）：** 从 Curriculum Blueprint 到 Course Outline、Syllabus、Module Plan 等可阅读、可审核的教学设计文档。它说明团队已经能够描述课程如何被组织。

**真实边界（Operational / Real Boundary）：** 进入实际可用的讲义、实验环境、作业、评价标准、教师授课、学生反馈和学习证据。它说明课程开始具备真实教学运行条件。

二者不能混淆。漂亮的 Syllabus 不等于学生真的能完成实验；完整的幻灯片不等于教师能够高质量授课。

### 建议的分层产物

| 层级 | 主要交付物 | 核心验收问题 |
|---|---|---|
| Architecture | JSON、Blueprint | 结构是否自洽且可解释？ |
| Course Design | Outline、Syllabus | 学习目标与教学活动是否匹配？ |
| Instructional Assets | Lectures、Labs、Assignments | 教师是否能够实际授课与评价？ |
| Teaching Execution | 真实授课与反馈 | 学生是否发生可观察的学习？ |
| Evidence & Iteration | 作业表现、Rubrics、修订记录 | 课程效果是否得到证据支持？ |

---

## 10. 教学护城河：Assignment System 与 Professor Variants

课程架构本身是必要条件，但不是教育产品的最终竞争力。后续的核心建设集中在两个方向。

### 10.1 Assignment & Assessment Architecture

一门课的教学闭环应逐步连接：

```text
Learning Outcomes
      ↓
Weekly Lectures / Labs
      ↓
Weekly Assignments
      ↓
Midterm Assessment
      ↓
Final Project / Examination
      ↓
Rubrics + Feedback + Student Evidence
```

关键不在于作业数量，而在于**Cognitive Progression（认知递进）**：从理解、应用、建模、分析，逐步发展到独立整合、评价与表达。具体层级须依据学科、学生年龄与课程目标设计，不能一套模板通吃。

### 10.2 Professor-Specific Instructional Variants

同一门课程可以有共享的 **Course Baseline**，并允许不同教师在讲义叙事、案例、练习、研究方向和课堂组织上形成不同版本。

**Invariant（建议保持一致）：** 课程身份、经批准的核心学习目标、最低覆盖要求、评价公平性与质量标准。

**Variant（允许差异化）：** 教师案例、解释路径、授课节奏、补充材料、练习组织与适当的教学风格。

这一机制目前只是**后续架构方向**，尚未建设真实的教师版本管理、审批或评价系统。

---

## 11. AI-Assisted Development：人机协作的角色分工

当前从 0 到 1 的产物形成，包含人工问题定义、专业判断、AI 辅助组织与表达、反复对齐和人工决策。

### 人类负责

- 定义业务与学术目标、识别隐性约束。
- 判断哪些知识与课程组合具有教育价值。
- 审核学术正确性、教学可行性和组织成本。
- 批准课程规则、商业承诺和对外表述。

### AI 可以辅助

- 归纳已有需求与 Cognition Space。
- 建议抽象结构和备选方案。
- 起草 JSON、Blueprint、Outline 等初稿。
- 发现字段、命名、引用和解释之间的潜在不一致。
- 协助多语言表达与版本差异说明。

### 不可越界的责任

AI 不能凭生成内容自动证明教学质量，不能将未经核实的假设包装成已批准事实，也不能代替实际授课教师与学术负责人承担教学责任。

长期目标不是永远高成本地“重新对齐”，而是把有效对齐固化为**可复用的文件、可追溯的决策和可验证的检查规则**。

---

## 12. 从方法论走向 Explainability

本文件回答：**我们使用什么方法构建课程，为什么这样做？**

未来可能建设的 `curriculum_explainability.md` / `curriculum_explainability.json` 则回答：**某个具体课程、字段、关系或决策，是依据什么产生的？**

一个潜在的解释记录可以包含：

```json
{
  "decision_id": "example-core-b-inheritance",
  "subject": "curriculum.cores.core_model_b.includes",
  "claim": "Advanced Core includes Foundation Core",
  "evidence_type": "model_fact",
  "source_path": "_construction/curriculum_construction.json",
  "rationale": "Preserve shared foundations without duplicating course definitions.",
  "status": "draft",
  "review_required": true
}
```

**注意：** 这是未来 Explainability Schema 的**示意**，不是当前仓库已存在的正式结构。`rationale` 也属于设计解释，不能仅凭 JSON 字段本身证明其历史决策过程。

建议未来逐步建立：Source Traceability、Decision Provenance、Dependency Explanation、Change Impact、Review Status 五类能力。

---

## 13. 阶段性方法复盘：已实践、待验证与未来计划

| 方法或机制 | 当前判断 | 说明 |
|---|---|---|
| 需求与认知空间分离 | 已用于草案工作 | 仍需补齐正式需求证据与评审 |
| 三树三土作为思考框架 | 已用于架构推演 | 术语与操作规范仍需冻结 |
| 抽象建模与课程分层 | 已形成初稿 | 需接受业务和教学团队审查 |
| JSON 结构化表达 | 已形成初稿 | 尚未建立完整 Schema 和自动校验 |
| IPEU 语义阐释 | 已用于 Blueprint | 尚未验证跨角色理解效果 |
| Source of Truth 治理 | 已提出规范 | GitHub 工作流与版本校验尚待落实 |
| Syllabus / Assignment 产线 | 待建设 | 应先选择一门核心课程试点 |
| 教师专属讲义变体 | 未来方向 | 需要真实教师参与与质量控制 |
| Explainability JSON | 未来方向 | 需要来源记录与决策证据机制 |
| 教学效果验证 | 尚未开始 | 需要真实授课、学习数据与反馈 |

---

## 14. 下一阶段建议：先验证一门课的完整闭环

在现有架构稳定后，建议优先选择 `RXI-310` 或 `RXI-315` 作为纵向试点，而不是同时铺开六个 Concentrations。

**建议试点路径：**

1. 确认课程目标、适用学生、先修条件与教学时长。
2. 从 Cognition Space 中筛选必要知识与能力。
3. 编写 Course Outline 与学期 Syllabus。
4. 制定每周 Lecture / Lab / Assignment 关系。
5. 建立期中、期末任务及 Rubrics。
6. 由真实教师审阅、试讲或小范围试点。
7. 根据学习证据修订课程及上游方法论。

**验收标准应当是教学可用性和证据质量，而不是文档数量。**

---

## 15. 本次交付说明

本文件与 `curriculum_construction.json`、`curriculum_blueprint.md` 共同构成当前阶段的三类互补产物：

- **Construction Model：** 我们构建了什么结构？
- **Blueprint：** 这些结构对人意味着什么？
- **Methodology：** 我们为什么、以及如何走到这个结构？

三者共同支持跨角色沟通和后续迭代，但不代表课程已完成教学实施。

**当前交付的实质是：形成可讨论、可解释、可继续建设的课程河床；真正的教学堤坝仍有赖于课程内容、教师能力、评价体系与真实教学反馈。**

---

## Appendix A — 建议的仓库文档关系

```text
_methodology/
└── curriculum_methodology.md        # 本文件：方法体系与方法流

_construction/
├── curriculum_construction.json     # 结构化课程事实
└── curriculum_construction.md       # JSON 字段与语义说明（拟完善）

_blueprint/
├── curriculum_blueprint.md          # 英文解释性蓝图
└── curriculum_blueprint_chn.md      # 简体中文解释性蓝图

_cognition_space/
└── ...                               # 课程与方向的候选认知空间

BASELINE.md                           # 已确认决策与状态（拟建立）
SKILL.md                              # AI 协作流程（拟建立）
```

此目录树为**建议组织方式**，不声称所有文件或目录均已在 GitHub 中存在。

## Appendix B — 文档治理与变更规则

- **版本：** `0.1.0`，Initial Delivery Draft。
- **维护原则：** 方法发生变化时，说明变化原因、适用范围和对既有产物的影响。
- **来源原则：** 明确区分已确认事实、当前推断、设计提案和待决事项。
- **一致性原则：** 涉及课程实体的变更，优先核查 Construction JSON 与 Blueprint。
- **审查原则：** 不将未经真实文件核验的历史推理描述为已被证实的决策来源。
- **交付原则：** 对外表达聚焦可理解的课程结构与阶段成果，不夸大自动化程度或教学成熟度。

---

*RXI-Lab — Curriculum Development Initiative*  
*End of Curriculum Construction Methodology v0.1.0*
