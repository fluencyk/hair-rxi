
# RXI Baseline
## Artslink Workspace & RXI-Lab

- **Document Type:** Cognitive and Engineering Baseline
- **Scope:** Artslink / RXI-Lab / 睿思实验室
- **Status:** Initial Baseline — Subject to Iteration
- **Version:** 0.1
- **Last Updated:** 2026-10-14

---

## 1. Purpose

This document establishes a reusable cognitive and engineering baseline
for discussions, planning, and implementation related to RXI.

Its purpose is to preserve established terminology, architectural
decisions, engineering principles, project boundaries, and unresolved
questions across ChatGPT Sessions.

This document is not a transcript of previous conversations.
It is a structured representation of the working knowledge established
through human-AI collaboration.

Future Sessions should use this baseline as an initial alignment
reference while remaining open to new evidence, revised requirements,
and explicit decisions made by the user.

## 2. Terminology and Identity

### 2.1 RXI

RXI is the standard short name for the Artslink / RXI-Lab / 睿思实验室
working context.

The forms `RXI` and `rxi` are equivalent and case-insensitive.

### 2.2 Artslink Workspace

Artslink Workspace is the broader working domain for professional work,
research-oriented development, technical learning, and project delivery
associated with Artslink.

### 2.3 RXI-Lab

RXI-Lab is the internal research and development hub within the Artslink
working domain.

It connects practical requirements, applied investigation, engineering
implementation, technical learning, and iterative improvement.

RXI-Lab should not be treated merely as a directory collection.
It is an organized working environment for translating real problems
into structured workflows, verifiable results, and reusable assets.

## 3. Relationship to Personal Research

The user's personal research root is:

`~/mac_workspace/research/`

The Artslink working domain is organized separately:

`~/mac_workspace/artslink/`

The two domains must remain distinguishable in filesystem organization,
project ownership, repositories, and handling of research materials.

The existence of a shared technical interest does not automatically
authorize the transfer of work-related code, documents, datasets, or
other assets into personal research projects.

Work-related materials must be handled according to applicable
organizational policies, intellectual-property requirements,
confidentiality obligations, and authorization rules.

Any intended conversion of work experience into academic research,
personal portfolio material, or public output requires appropriate
review and authorization.

## 4. Workspace Architecture

The currently recommended logical structure is:

```text
~/mac_workspace/
├── research/
│   └── 27-fall-phd-adm/
│       └── repo-phd-adm/
│
└── artslink/
    ├── README.md
    ├── artslink.code-workspace
    │
    └── rxi-lab/
        ├── README.md
        ├── curriculum/
        │   └── repo-curclm/
        ├── research/
        │   └── pro-folio/
        ├── projects/
        ├── learning/
        │   ├── google-adk/
        │   └── langgraph/
        ├── tools/
        └── misc/
```

This is the recommended logical structure, not proof that every
directory, repository, or configuration file has been created.

### 4.1 Directory Responsibilities

- `artslink/`: Root of the Artslink working domain.
- `rxi-lab/`: Main work, research, development, and learning hub.
- `curriculum/`: Curriculum design, instructional materials, and related
  deliverables.
- `research/`: Research-oriented development and methodological
  exploration, currently including the planned ProFolio initiative.
- `projects/`: Other projects with bounded implementation objectives.
- `learning/`: Technical learning, framework experiments, and notes.
- `tools/`: Utilities with demonstrated reuse value.
- `misc/`: Temporary or unclassified materials awaiting review.

### 4.2 Naming

Use `research/` rather than `rsch/`.

The full paths already distinguish the two namespaces:

- `~/mac_workspace/research/`
- `~/mac_workspace/artslink/rxi-lab/research/`

Readability is preferable to unnecessary abbreviation when the
directory hierarchy already expresses the intended distinction.

### 4.3 VS Code Workspace

The planned workspace file is:

`~/mac_workspace/artslink/artslink.code-workspace`

Initially, the workspace may contain `rxi-lab/` as its principal folder.
Additional folders can be introduced if cross-project work makes a
multi-root workspace useful.

A VS Code Workspace is an editor-level organizational mechanism.
It does not independently isolate Git repositories, filesystem
permissions, Python dependencies, or confidential information.

### 4.4 Python Environments

Prefer project-level virtual environments when projects have distinct
dependencies or version requirements.

Example:

```text
rxi-lab/
├── research/
│   └── pro-folio/
│       └── .venv/
└── learning/
    └── google-adk/
        └── .venv/
```

Shared environments should be considered only when multiple projects
demonstrably share compatible dependencies and execution requirements.

Virtual environments should be excluded from version control.
Project dependencies and reproducible setup instructions should be
maintained separately.

## 5. RXI-Lab Mission and Working Model

RXI-Lab focuses on the intersection of engineering practice,
applied research, and AI-enabled development.

Its mission is to investigate practical problems and translate useful
findings into structured workflows, technical implementations,
verifiable results, and reusable engineering assets.

The baseline working process is:

**Problem Definition
→ Requirement Analysis
→ Design
→ Implementation
→ Verification
→ Refinement**

This process should remain lightweight and adaptable.

The purpose is not to maximize architectural complexity or framework
adoption. Engineering mechanisms should be introduced when they solve
demonstrated problems.

## 6. Engineering Principles

### 6.1 Requirement-Driven Development

Establish the problem, intended outcome, constraints, and acceptance
criteria before committing to an implementation approach.

### 6.2 Minimum Viable Loop

Prioritize a small, functioning end-to-end loop before expanding the
architecture.

A working loop provides evidence for subsequent design decisions and
reduces the risk of speculative overengineering.

### 6.3 Reproducibility

Maintain explicit dependencies, configuration, and execution
instructions so that relevant results can be reproduced.

### 6.4 Verifiability

Evaluate outcomes using evidence, tests, and observable behavior.
Do not treat an implementation as successful merely because code
has been written or a framework has been installed.

### 6.5 Controlled Iteration

Maintain version history, project boundaries, and recoverable changes.

Use Git and other appropriate mechanisms to preserve source history
and make changes reviewable.

### 6.6 Evidence-Based Research

Distinguish among:

- Established facts
- Working hypotheses
- Experimental observations
- Implemented functionality
- Verified results
- Unresolved questions

Do not present a hypothesis as a demonstrated result or an unfinished
implementation as a mature deliverable.

## 7. Work Areas

### 7.1 Curriculum

Location:

`rxi-lab/curriculum/`

Purpose:

- Curriculum architecture
- Instructional design
- Teaching materials
- Curriculum-related development and delivery

The planned repository is `repo-curclm/`.

### 7.2 Research and ProFolio

Location:

`rxi-lab/research/pro-folio/`

ProFolio is a planned research-oriented development initiative
associated with Agentic Development practice and the exploration of
engineering workflows and supporting foundations.

Its current placement under `research/` reflects the planned emphasis
on methodological exploration and engineering foundations.

Its implementation status and concrete deliverables must be verified
separately. Directory creation or conceptual planning does not imply
that a mature system or validated result already exists.

If the initiative later becomes primarily a bounded business-delivery
project, its organizational placement can be reconsidered.

### 7.3 Projects

Location:

`rxi-lab/projects/`

This area accommodates other projects with explicit problem
definitions, implementation boundaries, and delivery objectives.

The distinction between `research/` and `projects/` should follow
the dominant objective rather than the mere presence or absence of code.

The two categories may overlap where appropriate.

### 7.4 Technical Learning

Location:

`rxi-lab/learning/`

Initially planned areas include:

- Google ADK
- LangGraph

Learning activities should support real development and research
needs without automatically becoming independent projects.

Framework selection should follow demonstrated requirements rather
than framework popularity or architectural ambition.

### 7.5 Tools and Miscellaneous Materials

`tools/` should contain utilities when their reuse value is established.

Avoid building a large shared tooling system before real usage
demonstrates the need.

`misc/` is a temporary classification area, not a permanent substitute
for project organization.

## 8. README Responsibilities

### 8.1 Artslink README

Location:

`artslink/README.md`

Responsibilities:

- Explain the overall purpose of the Artslink Workspace.
- Summarize the workspace structure.
- Establish broad working principles.
- Clarify boundaries between work-related materials and personal research.

### 8.2 RXI-Lab README

Location:

`artslink/rxi-lab/README.md`

Responsibilities:

- Explain the RXI-Lab research and development mission.
- Describe the responsibilities of internal work areas.
- State engineering principles.
- Document the Research-to-Practice workflow.
- Establish project, verification, and authorization boundaries.

The two README files should be complementary rather than duplicate
versions of the same document.

## 9. CLI and Scaffolding Preferences

The user prefers straightforward, directly executable CLI commands
for routine filesystem operations.

For basic scaffolding, prefer simple commands such as `mkdir -p`
and `touch` that can be pasted into the VS Code Terminal.

Do not modify `.zshrc` or introduce advanced shell configuration
merely to create a small directory structure.

When initialization requires more substantial file generation,
validation, error handling, or repeated orchestration, a Python script
may be appropriate. Use `subprocess` only when an external command
actually needs to be invoked.

Scaffolding operations should be simple, repeatable, and safe.
Existing file contents should not be overwritten unintentionally.

## 10. Work Boundaries and Governance

Because RXI operates in a real organizational context:

- Handle company materials according to applicable access policies.
- Do not expose confidential information or credentials.
- Keep personal research and work-related deliverables distinguishable.
- Verify authorization before external publication or reuse.
- Preserve the distinction between exploratory notes, hypotheses,
  implementation outputs, and verified conclusions.

These requirements are part of responsible engineering practice,
not optional administrative details.

## 11. Current Status

The following items have been discussed and designed, but their
actual implementation status must be confirmed independently:

- Artslink and RXI-Lab directory structure
- `artslink.code-workspace`
- `artslink/README.md`
- `rxi-lab/README.md`
- `repo-curclm/`
- `research/pro-folio/`
- Project-level Python environments
- Google ADK and LangGraph learning directories

The two README documents have been drafted in Markdown.
The directory structure has been specified, but this baseline alone
does not establish that every item has been created or validated.

Do not infer implementation status from planning discussions.

## 12. Recommended Next Steps

1. Verify the actual local workspace structure.
2. Review the README files after they have been written to disk.
3. Identify the immediate work priorities arising from real RXI tasks.
4. Define the first bounded, verifiable delivery objective.
5. Establish project repositories and environments when needed.
6. Introduce additional automation or agent orchestration only when
   practical requirements justify it.

## 13. Baseline Evolution

This document is an initial baseline, not an immutable specification.

Future changes should distinguish between:

- Confirmed decisions
- Proposed changes
- Open questions
- Verified implementation results

When a new decision supersedes an earlier one, update this baseline
explicitly rather than silently accumulating contradictory guidance.

The goal is to preserve useful shared understanding while allowing
the RXI working model to evolve through real practice and evidence.
