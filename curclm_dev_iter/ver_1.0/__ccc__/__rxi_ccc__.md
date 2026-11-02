# RXI-CCC

## RXI Contextual Consistency Collaboration Profile

RXI-CCC is the domain-specific Contextual Consistency Collaboration (CCC)
command profile for the RXI Curriculum Engineering System.

It provides a lightweight command interface for human-AI collaborative
reasoning across the RXI curriculum transformation pipeline.

RXI-CCC does not replace the underlying curriculum Flow specifications.
Commands select and invoke transformations, while the corresponding Flow
specification defines the authoritative reasoning boundary, input state,
transformation semantics, validation requirements, and output state.

The primary curriculum transformation chain is:

BSD
→ Field
→ Stem
→ Syllabus
→ Agenda
→ Slide

Each transformation consumes an existing semantic state and materializes
a new structured semantic state for downstream use.

RXI-CCC follows the CCC hierarchical command principle:

rxi <intent> -<primary_attribute> --<secondary_constraint>

Where:

- `rxi` designates the RXI Curriculum reasoning context.
- `<intent>` identifies the requested curriculum transformation or operation.
- `-<primary_attribute>` specifies the primary mandatory execution target.
- `--<secondary_constraint>` optionally supplies additional execution scope
  or alignment constraints.

The corresponding RXI Flow specification remains authoritative over the
semantics of every transformation.

---

## Core Transformation Commands

### `rxi bsd2field -<bsd>`

Executes the BSD-to-Field transformation for the selected Business Strategy
Domain and produces the corresponding academically qualified Field state
according to the BSD2FIELD Flow.

---

### `rxi field2stem -<field>`

Executes Field-to-Stem reasoning for the selected academically qualified
Field and produces its structured Stem state according to the FIELD2STEM Flow.

The selected Field acts as the primary reasoning and alignment target.

---

### `rxi field2stem -<field> --<bsd>`

Executes Field-to-Stem reasoning for the selected Field within the explicit
generation scope of the specified Business Strategy Domain.

The Field defines the fine-grained academic alignment focus while the BSD
defines the broader curriculum generation boundary.

The selected Field must already be qualified within the selected BSD scope.

---

### `rxi stem2syllabi -<domain>`

Transforms the resolved and reconciled Stem state of the selected curriculum
Domain into a structured syllabus state according to the STEM2SYLLABI Flow.

The generated syllabus must preserve traceability to its contributing Stems
and upstream Field and BSD lineage.

---

### `rxi syllabi2agenda -<domain>`

Transforms the selected syllabus state into a lecturable agenda state
according to the SYLLABI2AGENDA Flow.

Agenda represents instructional runtime structure, including the sequencing
and organization of teachable sessions or weeks, rather than a meeting agenda.

---

### `rxi agenda2slide -<domain>`

Transforms the selected agenda state into structured instructional Slide
state according to the AGENDA2SLIDE Flow.

The resulting Slide state represents the final curriculum materialization
layer while preserving upstream semantic lineage.

---

## State Inspection Commands

### `rxi inspect -bsd`

Returns the currently available Business Strategy Domain state without
performing a curriculum transformation.

---

### `rxi inspect -field`

Returns the currently available academically qualified Field state without
performing a curriculum transformation.

---

### `rxi inspect -stem`

Returns the currently available Stem state without performing a curriculum
transformation.

---

### `rxi inspect -syllabi`

Returns the currently available syllabus state without performing a curriculum
transformation.

---

### `rxi inspect -agenda`

Returns the currently available agenda state without performing a curriculum
transformation.

---

### `rxi inspect -slide`

Returns the currently available Slide state without performing a curriculum
transformation.

---

## Traceability Command

### `rxi trace -<node>`

Retrieves the available semantic lineage of the selected curriculum node.

The trace should resolve upstream relationships where available, following
the general lineage:

Slide
← Agenda
← Syllabus
← Stem
← Field
← BSD

The command performs lineage inspection only and must not modify existing
semantic state.

---

## Validation Command

### `rxi validate -<node>`

Validates the selected semantic node or generated state against the
constraints declared by its authoritative Flow specification.

Validation does not independently redefine curriculum semantics and must not
silently repair, reinterpret, or replace invalid state.

---

## Holding-State Command

### `rxi hold -<node>`

Designates an existing curriculum node or semantic state as the current
working context for subsequent RXI-CCC operations.

Holding state provides contextual continuity but does not override explicit
selectors, Flow constraints, provenance requirements, or validation rules.

---

## Holding-State Inspection

### `rxi holding -current`

Returns the currently designated holding state and its available semantic
identity without executing a transformation.

---

## Execution Semantics

An RXI-CCC transformation is interpreted through the following execution
model:

Command
→ Selector Resolution
→ Holding-State Resolution
→ Flow Resolution
→ RAG / Evidence Context
→ Reasoning
→ Validation
→ Structured State
→ Materialization

Commands do not themselves contain curriculum-generation knowledge.

Curriculum transformation semantics are defined by the authoritative
RXI Curriculum Flow Specification.

---

## Selector Semantics

### BSD Selector

The BSD selector defines the primary business and curriculum generation scope.

It controls the semantic boundary within which downstream curriculum
generation occurs.

---

### Field Selector

The Field selector defines a finer-grained academic reasoning and alignment
focus within the active BSD scope.

It does not independently redefine BSD boundaries or establish Field
qualification.

Where both selectors are present:

BSD Selector = Generation Boundary

Field Selector = Academic Alignment Focus

The Field selector must resolve to an academically qualified Field within
the selected BSD scope.

---

## RAG Semantics

RAG materials supplied with an RXI-CCC command provide external grounding
for the requested transformation.

RAG material must be interpreted within the constraints of the authoritative
Flow and must not independently override:

- upstream semantic state,
- selector boundaries,
- provenance-qualified identities,
- transformation rules,
- validation constraints,
- or required output structure.

---

## Output Semantics

Transformation commands should return a minimal structured semantic state
suitable for materialization as JSON.

The default execution response should contain:

1. a concise RXI-CCC runtime header;
2. the generated structured JSON state.

Explanatory prose should remain minimal unless explicitly requested.

---

## Annotation Rules

Content wrapped in:

`// ...`

or:

`/* ... */`

is treated as human-only annotation.

Annotated content must not be interpreted as executable RXI-CCC instruction,
selector, constraint, transformation rule, or semantic state.

---

## Runtime Principle

RXI-CCC separates command semantics from curriculum reasoning semantics.

The command determines:

WHAT transformation is requested.

The selector determines:

WHICH semantic state is targeted.

The Flow determines:

HOW the transformation is permitted to occur.

RAG provides:

WHAT external knowledge may ground the reasoning.

The generated JSON provides:

WHAT semantic state has been materialized.

Therefore:

Command ≠ Flow

Flow ≠ State

State ≠ Artifact Presentation

RXI-CCC coordinates these layers without collapsing their responsibilities.