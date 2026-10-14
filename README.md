# HAIR-RXI — Human-AI Resonance Infrastructure

## 1. Overview

`_hair_rxi/` is the Human-AI Resonance infrastructure within the Artslink
Workspace.

It provides a dedicated space for organizing collaboration context,
session baselines, memory, state, and supporting mechanisms that help
maintain continuity across human-AI interactions.

The goal is to establish a structured and maintainable foundation for
contextual consistency, knowledge alignment, and AI-assisted engineering
workflows.

HAIR-RXI is intended to evolve incrementally. Its directory structure
defines logical responsibilities; it does not imply that every component
or capability has already been implemented.

## 2. Architectural Boundary

The Artslink Workspace separates two complementary domains:

- **HAIR-RXI (`_hair_rxi/`)** — Human-AI collaboration infrastructure:
  context organization, session continuity, knowledge alignment, and
  supporting collaboration mechanisms.
- **RXI-Lab (`rxi-lab/`)** — Research and engineering workspace:
  requirements, experiments, implementation, verification, and project
  deliverables.

HAIR-RXI supports the process through which human-AI collaboration is
organized and maintained. RXI-Lab is where concrete research and
engineering work is conducted.

The two domains are logically separated but operationally connected.
Relevant context and decisions may inform engineering work, while
verified findings and project outcomes may contribute to future
collaboration context.

## 3. Directory Structure

| Directory / File | Responsibility |
| --- | --- |
| `sessions/` | Organizes persistent workstreams and their session baselines. |
| `context/` | Intended for contextual materials and alignment inputs. |
| `memory/` | Intended for curated knowledge and reusable information. |
| `state/` | Intended for state-related information required by collaboration workflows. |
| `ccc/` | Reserved for CCC-related materials and mechanisms. |
| `_util/` | Supporting utilities for the infrastructure. |
| `README.md` | Entry point and architectural overview. |

These responsibilities are logical boundaries to guide development.
Detailed schemas, operational rules, and implementation details should
be documented as the corresponding components mature.

## 4. Session and Context Governance

The `sessions/` directory organizes ongoing collaboration by workstream,
rather than treating each individual chat session as an isolated unit.

Its global baseline is maintained in:

- `sessions/BASELINE_GLOBAL.md`

Domain-specific baselines belong in their respective workstream
directories.

The global baseline defines shared governance conventions, including
naming, organization, cross-workstream references, baseline maintenance,
and knowledge continuity.

A baseline is a curated alignment artifact, not an automatic record of
every conversation. Information should be reviewed and structured before
being promoted into reusable context.

## 5. Collaboration Workflow

The intended collaboration workflow is:

1. Identify the relevant workstream and its baseline.
2. Retrieve the necessary context and supporting materials.
3. Align the current session with established decisions and constraints.
4. Conduct analysis, planning, or engineering work.
5. Record meaningful decisions, verified findings, and unresolved issues.
6. Update the appropriate baseline or project documentation when warranted.

Context retrieval may use repository files, explicit URLs, indexes, or
other supported access mechanisms.

Providing a repository URL does not itself guarantee access to private
content or automatically execute a retrieval process. Access permissions,
retrieval procedures, and source references must be handled explicitly.

## 6. Engineering Principles

HAIR-RXI follows these principles:

- **Contextual Consistency** — Preserve relevant decisions and constraints
  across workstreams and sessions.
- **Explicit Boundaries** — Separate collaboration context from project
  implementation and deliverables.
- **Evidence-Based Alignment** — Distinguish established facts, hypotheses,
  decisions, implemented capabilities, and verified results.
- **Incremental Development** — Establish a working minimum before
  introducing additional mechanisms or abstractions.
- **Traceability** — Keep important decisions and claims connected to
  identifiable source materials where practical.
- **Controlled Change** — Prefer reviewable, reversible changes and
  explicit updates to shared baselines.
- **Human Oversight** — Treat AI-generated interpretations and
  recommendations as subject to human review.

## 7. Security and Information Boundaries

HAIR-RXI operates within the Artslink Workspace and must respect
organizational policies, information classifications, and authorization
requirements.

- Do not place credentials, private keys, access tokens, or other secrets
  in tracked files.
- Do not publish company materials or proprietary information without
  appropriate authorization.
- Do not assume that a private repository alone satisfies every
  confidentiality or access-control requirement.
- Keep personal research and organizational work appropriately separated.
- Record and reuse work-related information only within its authorized
  scope.

## 8. Development Status

HAIR-RXI is an evolving collaboration infrastructure.

The current directory structure establishes an initial organizational
foundation. Individual components may remain conceptual, partially
implemented, or subject to further refinement.

Architecture and documentation should evolve according to demonstrated
workflow needs rather than speculative complexity.

## 9. Guiding Principle

> Separate collaboration context from engineering execution, while
> maintaining an explicit, verifiable connection between them.

HAIR-RXI provides the foundation for maintaining human-AI collaboration
continuity. RXI-Lab provides the workspace in which that collaboration
is translated into concrete research and engineering outcomes.
