# RXI Rapid Thinking Storm — Requirements Engineering & Agentic Curriculum Architecture

**Date:** 2026-10-28  
**Type:** Rapid Thinking Storm (RTS)  
**Status:** Working Cognition Snapshot — Not Formal Baseline  
**Context:** Post-review reflection after RXI Curriculum v0.5 delivery

---

## 1. Core Discovery

The 2026-10-28 curriculum review revealed that RXI's primary problem is no longer simply curriculum design.

The deeper problem is **Requirements Engineering**.

Even if the curriculum successfully reconstructs:

Domain → STEM → Cognition Space → Course

this does not solve the fundamental problem if the requirements themselves remain weakly evidenced.

Current requirement sources have largely consisted of fragmented conversations, WeChat messages, partial stakeholder descriptions, informal suggestions, and engineering inference.

Therefore:

Stakeholder Statement ≠ Validated Requirement ≠ Design Decision ≠ Implementation

The next phase must continuously strengthen requirements gathering, validation, ownership, and change tracking.

A lightweight requirement record may eventually follow:

Requirement → Evidence → Owner → Status → Decision → Impact

---

## 2. Reinterpretation of Curriculum v0.5

Curriculum v0.5 should not be treated as a failed delivery.

Its architecture provided stakeholders with something concrete enough to react to and therefore exposed previously hidden requirements.

In this sense:

**v0.5 functioned as both a curriculum architecture and a Requirements Elicitation Prototype.**

The review revealed several important requirements that had not previously been sufficiently explicit:

- Project-Based learning is central.
- 1:1 mentorship is likely a primary instructional mechanism.
- Student projects and artifacts are major outcomes.
- Research and admission objectives may influence project configuration.
- Several original Concentration domains require revision.
- The curriculum probably needs to be smaller and more configurable than a university-style program.

Therefore, v0.5 should be **compressed and evolved rather than discarded**.

---

## 3. Academic Architecture vs Instructional Delivery

The next architecture should explicitly separate three layers.

### Academic Curriculum Architecture

- Core
- Concentrations
- Domains
- STEMs
- Cognition Spaces
- Elective / configurable components

### Instructional Delivery Architecture

- Project-Based Learning
- 1:1 Mentorship
- Milestones
- Assessment
- Iteration
- Student artifacts

### Outcome / Progression Architecture

- Project Success
- Research Orientation
- Admission-Oriented Outcomes

These layers interact but should not be collapsed into one concept.

In particular:

**Project-Based** describes an instructional mechanism.

**Research-Oriented** describes an intellectual or methodological orientation.

**Admission-Oriented** describes a downstream application of student evidence and artifacts.

A single project may contain all three.

---

## 4. Emerging Curriculum Compression

A promising candidate architecture is:

**Core = 2 + 1**

**Concentration = 1 + 1**

This remains a working hypothesis pending stakeholder validation.

### Core: 2 + 1

Candidate structure:

1. Fundamentals of Engineering
2. Systems Design and Abstract Modeling
3. Applied Convergence of Design and Technology — optional / advanced

The previous Seminar component can temporarily be removed from the required path.

The minimum shared curriculum may therefore contain two required Core courses, with the third available when appropriate.

### Concentration: 1 + 1

A Concentration may not need to behave like a university major containing many courses.

For RXI learners, a practical structure may be:

1. One Domain Learning Course
2. One Mentored Project Studio

The Domain Learning Course is configured from:

Domain + Selected STEM + Relevant Cognition Spaces → Course

The Project Studio then applies that knowledge through a guided project.

---

## 5. Domain, STEM, Cognition Space, and Course

These concepts should remain separate.

**Domain**  
Defines the broad academic or professional area.

**STEM**  
Defines a major knowledge trunk or direction within that domain.

**Cognition Space**  
Defines the concepts, methods, capabilities, reasoning structures, and dependencies required for learning.

**Course**  
Defines how selected knowledge and capabilities are packaged into an instructional experience.

Therefore:

Domain → STEM Selection → Cognition-Space Selection → Course Configuration

The curriculum data model should preserve these semantic boundaries.

---

## 6. Student Artifacts

An early hypothesis considered three student outputs:

- conceptual / storyboard artifact,
- mini research paper,
- implementation artifact.

However, these should not become mandatory file formats across all domains.

A more robust abstraction is:

### Conceptual Artifact
Evidence that the learner can frame a problem, organize concepts, and communicate a solution.

### Research Artifact
Evidence that the learner can formulate questions, investigate evidence, apply methods, and communicate findings.

### Implementation Artifact
Evidence that the learner can construct, test, demonstrate, or operationalize a solution.

The actual artifact format should depend on the Domain and Project.

For Modern Software Development, an implementation artifact may be a demo, prototype, application, or small platform.

---

## 7. Student Academic Orientation

A major new system component should be explored:

**Student Academic Orientation**

"Orientation" is preferred over "Wizard" because the function is academic rather than merely procedural.

The Orientation should gather structured learner information such as:

- interests,
- prior knowledge,
- technical readiness,
- academic readiness,
- preferred domains,
- project interests,
- research interests,
- available time,
- expected difficulty,
- future academic goals,
- preferred artifact types.

The Orientation should produce structured data:

Student → Academic Orientation Web UI → `student_profile.json`

This profile becomes the input to downstream curriculum and project configuration.

The purpose is not to allow an LLM to make authoritative judgments about a student.

It is to provide structured evidence for a **Learner-to-Project Mapping** process that remains subject to mentor review.

---

## 8. Learner-to-Project Mapping

Secondary-school students generally require stronger scaffolding than graduate students when defining meaningful academic projects.

RXI therefore needs a guided process such as:

Learner Profiling  
→ Academic Orientation  
→ Domain Selection  
→ STEM Selection  
→ Cognition-Space Matching  
→ Project Scoping  
→ Mentor Review  
→ Personalized Learning Path

This may eventually become an important part of RXI's educational product.

---

## 9. Modern Software Development as the First Vertical Slice

The next implementation should not attempt to complete all Concentrations simultaneously.

**Modern Software Development** should be used as the first reference Domain.

Reasons:

- strong existing Software Engineering expertise,
- relatively mature internal cognition-space material,
- clear engineering artifacts,
- easy observation of project outcomes,
- suitable for testing an end-to-end AI-assisted curriculum pipeline.

The objective is to prove one complete vertical slice before expanding horizontally.

---

## 10. Three Parallel Workstreams

The next phase can proceed through three synchronized workstreams.

### A. Requirements Alignment

Continuously gather and validate requirements with stakeholders.

Do not passively wait for requirements.

Actively perform:

- stakeholder clarification,
- requirement elicitation,
- decision confirmation,
- domain validation,
- teaching-model validation,
- artifact validation,
- product-definition validation.

If requirements are not coming to engineering, engineering must actively obtain them.

### B. Curriculum Compression and Knowledge Modeling

Refactor v0.5 toward the compact architecture.

Initial path:

Core Compression  
→ Modern Software Development Domain  
→ STEM Modeling  
→ Cognition-Space Modeling  
→ Stable Curriculum JSON

The structured curriculum model becomes the grounding layer for AI generation.

### C. Agentic Engineering MVP

Build a small executable vertical slice:

Student Academic Orientation  
→ Student Profile JSON  
→ Curriculum Knowledge Retrieval  
→ LLM Reasoning  
→ Personalized Course Specification  
→ Syllabus  
→ 30–40 Slide Specifications

The first version should remain deliberately lightweight.

A complex Multi-Agent System is not required merely to demonstrate Agent Engineering.

---

## 11. Agent and Tool Boundary

The initial system should distinguish deterministic tools from LLM reasoning.

### Tools

Potential responsibilities:

- load curriculum models,
- validate JSON schemas,
- query Domains,
- query STEMs,
- retrieve Cognition Spaces,
- evaluate deterministic constraints,
- retrieve external resources,
- validate generated course specifications,
- render artifact manifests.

### Agent / LLM Reasoning

Potential responsibilities:

- interpret learner interests,
- synthesize learner needs,
- recommend academic direction,
- configure learning paths,
- propose project scope,
- explain recommendation rationale,
- generate syllabus structures,
- generate slide-level instructional specifications.

The LLM should reason **within structured curriculum constraints**, not invent the curriculum freely.

---

## 12. JSON as the System Contract

The emerging system should be JSON-driven.

Candidate objects include:

### `student_profile.json`

Represents:

- learner background,
- interests,
- readiness,
- goals,
- constraints,
- project preferences,
- research preferences.

### `curriculum_knowledge.json`

Represents:

- Domains,
- STEMs,
- Cognition Spaces,
- Core requirements,
- dependencies,
- constraints,
- relationships.

### `course_specification.json`

Represents the personalized curriculum decision:

- selected Domain,
- selected STEM,
- selected Cognition Spaces,
- learning outcomes,
- prerequisites,
- project objectives,
- milestones,
- assessment,
- deliverables,
- syllabus structure,
- slide specifications.

### `slide_artifact_manifest.json`

Represents slide-level production requirements such as:

- slide ID,
- learning objective,
- Cognition Space references,
- content requirements,
- evidence requirements,
- visual anchors,
- engineering anchors,
- Notebook anchors,
- data anchors,
- generation status,
- validation status.

---

## 13. Syllabus and Slides Are Different Objects

A Syllabus defines the educational contract.

It should include concepts such as:

- Learning Outcomes
- Project Objectives
- Prerequisites
- Mentorship Model
- Milestones
- Deliverables
- Assessment
- Academic / Admission Alignment

Slides are instructional resources derived from that contract.

Therefore:

Student Profile  
→ Course Specification  
→ Syllabus  
→ Slide Specifications  
→ Instructional Artifacts

The data model should preserve this distinction.

---

## 14. Two-Stage Generative Architecture

The generative pipeline should be divided into two major stages.

### Stage 1 — Curriculum Planning / Specification Generation

Determine:

- what this learner should study,
- why it should be studied,
- which Domain and STEM are appropriate,
- which Cognition Spaces are required,
- what project should organize the learning process,
- what the Syllabus should contain,
- what each slide should accomplish.

This stage should be strongly grounded in RXI's internal structured curriculum model.

### Stage 2 — Instructional Content / Artifact Generation

Once the course specification is stable:

Slide Specification  
→ External RAG  
→ Content Generation  
→ Artifact Generation

Possible artifacts include:

- Jupyter Notebooks,
- code examples,
- charts,
- data visualizations,
- diagrams,
- generated images,
- engineering references,
- design references,
- research evidence,
- external learning resources.

The system should avoid asking one unconstrained LLM call to simultaneously understand the learner, design the curriculum, perform research, write all content, generate artifacts, and design the final slide deck.

---

## 15. RAG Strategy

The first internal retrieval layer may not require a vector database.

For the Modern Software Development vertical slice, structured retrieval may initially be sufficient:

JSON + Relationships + Schema-Grounded Queries

Vector retrieval should be introduced only when semantic retrieval becomes genuinely necessary.

External RAG can later enrich validated slide specifications with current knowledge, references, examples, and instructional resources.

The internal curriculum model should remain deterministic and inspectable wherever possible.

---

## 16. MVP Success Condition

The first engineering experiment should answer:

> Can a learner complete Student Academic Orientation and receive a coherent, explainable, personalized Project-Based learning package grounded in the RXI curriculum model?

A successful vertical slice should demonstrate:

Student  
→ Orientation Web UI  
→ Student Profile JSON  
→ Modern Software Development Knowledge Model  
→ Course Configuration  
→ Project Recommendation  
→ Personalized Syllabus  
→ 30–40 Slide Specifications

Several synthetic learner profiles should eventually be tested to verify that meaningfully different learner inputs produce meaningfully different curriculum outputs.

---

## 17. AI-Assisted Engineering Changes the Estimation Model

An earlier classical Software Engineering estimate did not sufficiently model AI as a development productivity factor.

In the emerging workflow:

### Human Responsibilities

- Requirements Engineering
- Domain Judgment
- Architecture
- Acceptance Criteria
- Stakeholder Alignment
- Validation

### AI Responsibilities

- code generation,
- boilerplate implementation,
- refactoring,
- test generation,
- implementation assistance,
- rapid iteration.

Therefore traditional coding-effort assumptions should not be transferred mechanically into the current environment.

However:

> AI compresses implementation time much more strongly than it compresses requirements uncertainty, stakeholder latency, integration risk, and validation effort.

---

## 18. Engineering Effort Model

The intuitive minimum technical implementation estimate is:

**24 engineering hours**

This represents a near-ideal or **Zero-Factor Outcome** under conditions such as:

- stable requirements,
- stable architecture,
- prepared JSON,
- minimal interruption,
- fast AI-assisted coding,
- no major integration failure,
- little requirement rework.

Therefore:

**24h = Ideal / Feasibility Engineering Estimate**

It is not a delivery commitment.

A more realistic planning baseline is:

**72 engineering hours**

Conceptually:

`E_planned = E_base × TF × OF`

Where:

**TF — Technical Factors**

May include:

- framework integration,
- API behavior,
- schema evolution,
- structured-output reliability,
- RAG integration,
- UI integration,
- testing,
- debugging,
- deployment.

**OF — Other Factors**

Contains at least two important subcategories.

### Noise Factors

- context switching,
- stakeholder availability,
- meetings,
- fragmented communication,
- organizational interruptions,
- development-environment problems.

### Requirements Engineering Refinement Factors

- newly discovered requirements,
- contradictions,
- stakeholder corrections,
- domain changes,
- architecture revisions,
- curriculum reconfiguration,
- validation feedback,
- requirement-driven rework.

The exact mathematical composition of these factors is not yet formally defined.

For current planning:

**24h = Zero-Factor / Ideal Outcome**

**72h = Realistic Planning Baseline**

The multiplier is heuristic and should later be calibrated against actual development logs.

---

## 19. Delivery Target

A reasonable near-term demonstration target is:

> A stakeholder can act as a hypothetical student, operate the Student Academic Orientation Web UI, and observe the system generate a personalized Project-Based curriculum package.

The visible flow should eventually become:

Student opens Web UI  
→ completes Academic Orientation  
→ system creates Student Profile  
→ system configures curriculum  
→ system proposes project direction  
→ system generates personalized Syllabus  
→ system generates 30–40 Slide Specifications  
→ downstream generators produce or retrieve instructional artifacts.

The first demonstration does not require every artifact generator to be production-grade.

The objective is to prove the complete **vertical causal chain**.

---

## 20. Scope Control

The first implementation should NOT attempt to complete:

- all Concentrations,
- all Cognition Spaces,
- production-grade RAG,
- complex Multi-Agent architecture,
- perfect visual slide generation,
- fully automated research validation,
- production deployment.

The first vertical slice should remain:

**ONE Domain:** Modern Software Development  
**ONE Orientation Workflow**  
**ONE Structured Knowledge Model**  
**ONE Course-Configuration Workflow**  
**ONE Project Recommendation Workflow**  
**ONE Personalized Syllabus**  
**ONE 30–40 Slide Specification Pipeline**

Only after this works reliably should the architecture expand horizontally.

---

## 21. Key Engineering Lesson

The major lesson from Curriculum v0.5 is not that engineering moved too quickly.

The problem is **when acceleration occurs**.

Before requirements are sufficiently validated:

Elicit → Prototype → Question → Model → Validate

After requirements become sufficiently stable:

Implement → Automate → Generate → Integrate → Deliver

Therefore the correct principle is not:

> Slow down.

It is:

> **Accelerate at the correct stage.**

---

## 22. Current Working Hypothesis

RXI may ultimately be building something closer to:

**Academic Curriculum Engineering  
+ Student Academic Orientation  
+ Structured Knowledge Modeling  
+ Project-Based Mentorship  
+ Agentic Course Configuration  
+ RAG-Grounded Content Generation  
+ Artifact Generation**

This could eventually become a configurable AI-assisted academic project learning system.

However, this remains a **working hypothesis**, not a validated product definition.

The organization still needs to determine whether the commercial product is primarily:

- a standardized course package,
- a 1:1 project mentorship service,
- a long-term academic development program,
- an admission-oriented research / portfolio service,
- or a configurable combination of these.

This must be established through stakeholder evidence rather than engineering intuition alone.

---

## 23. Immediate Next Direction

### Requirements

Continue active stakeholder alignment and validate:

- product definition,
- Core compression,
- Concentration structure,
- Project-Based mentorship,
- expected student artifacts,
- Domain selection.

### Curriculum

Preserve v0.5 as historical reference.

Develop the next version separately rather than destructively rewriting v0.5.

Begin with:

**Modern Software Development**

### Engineering

Build the smallest executable vertical slice:

Orientation Web UI  
→ Student Profile JSON  
→ Curriculum Knowledge Query  
→ LLM Reasoning  
→ Validated Course Specification JSON  
→ Syllabus  
→ Slide Specifications

### Estimation

Track actual effort against:

- 24h Ideal Baseline
- 72h Planning Baseline

Record deviations according to:

- Technical Factors
- Noise Factors
- Requirements Engineering Refinement Factors

This will allow future AI-assisted engineering estimates to become evidence-based rather than purely intuitive.

---

# RTS Anchor

The central cognition from this session is:

> RXI's current challenge is not primarily curriculum writing. It is a coupled Requirements Engineering, Curriculum Engineering, Knowledge Modeling, Project-Based Instructional Design, and Agentic Software Engineering problem.

Curriculum v0.5 was not wasted effort.

It created sufficient structure to expose previously hidden requirements.

Therefore:

**v0.5 was not merely a curriculum delivery.  
It was also a requirements probe.**

The next iteration should transform those discovered requirements into a validated curriculum-and-delivery system.

The working engineering loop is:

**Evidence → Requirement → Model → Prototype → Stakeholder Validation → Refinement → Implementation**

And the current engineering estimation anchor is:

**24h tells us what AI-assisted engineering may achieve under ideal conditions.**

**72h tells us what real engineering should currently plan for.**

The difference between them is where technical uncertainty, organizational noise, and Requirements Engineering refinement live.

---

**RTS Status:** Captured  
**Suggested File:** `_hair_rxi/sessions/rapid-thinking-storm/RTS.md`  
**Promotion Rule:** Only sufficiently validated decisions should later be promoted from RTS into `BASELINE_GLOBAL.md`, formal methodology documents, or production curriculum structures.
