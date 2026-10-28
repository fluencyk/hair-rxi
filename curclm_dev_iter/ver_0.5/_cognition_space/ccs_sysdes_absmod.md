# CCS — Systems Design and Abstract Modeling

> Candidate Cognition Space (CCS) · v0.1
>
> Course: Systems Design and Abstract Modeling
> Suggested Filename: `ccs_sysdes_absmod.md`
> Status: Initial Draft / Candidate Inventory
> Role: Foundation Core / Advanced Core shared curriculum architecture

---

## 0. Purpose and Scope

### 0.1 Purpose

This document establishes an initial candidate cognition space for
**Systems Design and Abstract Modeling**.

It inventories potentially relevant knowledge, concepts, theories,
methods, processes, tools, artifacts, competencies, and prerequisite
levels that may inform the subsequent development of the course syllabus,
learning activities, assessments, and instructional materials.

The inventory is intended to support:

- Development of systems thinking and abstraction capabilities.
- Identification and representation of system boundaries, components,
  relationships, behaviors, and constraints.
- Construction and interpretation of models for understanding complex
  problems.
- Translation of requirements into structured system representations.
- Evaluation of design alternatives through models and evidence.
- Alignment between models, implementation, testing, and communication.
- Subsequent curriculum construction and AI-assisted content generation.

### 0.2 Working Course Definition

Systems Design and Abstract Modeling introduces learners to the
principles and practices of identifying systems, defining their scope,
abstracting relevant characteristics, representing structure and behavior,
and using these representations to reason about possible solutions.

The course treats a model as a purposeful representation of selected
aspects of a system, rather than as a complete copy of reality.

Its central concerns are:

- What constitutes the system under consideration?
- What belongs inside or outside its boundary?
- Which elements, relationships, and behaviors matter?
- At what level of abstraction should the problem be represented?
- How can a model help reveal dependencies, constraints, and trade-offs?
- How can alternative system designs be compared?
- What assumptions and limitations affect the validity of a model?
- How can a model inform implementation, testing, and decision making?

### 0.3 Candidate Scope

The initial inventory considers the following areas:

1. Systems thinking and system concepts.
2. Problem framing, boundaries, and abstraction.
3. Requirements, stakeholders, and constraints.
4. Structural modeling.
5. Behavioral and process modeling.
6. Relationships, dependencies, and interfaces.
7. System architecture and design alternatives.
8. Quantitative models, simulation, and analysis.
9. Model verification, validation, and refinement.
10. Communication, documentation, and model-based reasoning.

These areas are candidate domains, not a commitment to include every
topic in the final syllabus.

### 0.4 Scope Boundaries

This course focuses on the representation, analysis, and design of
systems at an appropriate level of abstraction.

It should not become a comprehensive substitute for:

- **Fundamentals of Engineering** — broad engineering literacy,
  scientific and mathematical foundations, and introductory
  engineering problem-solving practice.
- **Applied Convergence of Design and Technology** — application-oriented
  integration of design methods, technologies, prototypes, and
  implementation outcomes.
- **Seminar** — focused investigation of engineering best practices,
  computational mathematics, and selected advanced principles.

The course may use examples from software, robotics, products,
infrastructure, information systems, and socio-technical environments.
These examples are contexts for learning systems design, not a mandate
to teach every domain's specialist methods.

---

# 1. Disciplinary Knowledge

This dimension identifies candidate bodies of knowledge that support
the understanding, representation, and design of systems.

## 1.1 Systems Foundations

- Definitions and characteristics of systems.
- Systems as interacting elements organized toward a purpose or outcome.
- Systems, subsystems, and super-systems.
- Components, relationships, interfaces, and environments.
- System inputs, transformations, outputs, and outcomes.
- System boundaries and external dependencies.
- Open and closed systems as conceptual distinctions.
- Static and dynamic systems.
- Physical, computational, informational, organizational, and
  socio-technical systems.
- Engineered systems and naturally occurring systems.
- System behavior arising from interactions among components.

## 1.2 Systems Thinking

- Whole-system and component-level perspectives.
- Interdependence and interaction.
- Feedback and response.
- Emergent behavior.
- Nonlinear effects and indirect consequences.
- Local optimization versus system-level performance.
- Delayed effects and cumulative changes.
- Dependencies across system layers.
- Unintended consequences of design decisions.
- Context sensitivity and environmental influence.

## 1.3 Problem Framing and Abstraction

- Problem definition and scope.
- Identification of relevant system characteristics.
- Separation of essential from incidental details.
- Abstraction levels and levels of detail.
- Decomposition and recomposition.
- Assumptions and simplifications.
- Idealization and approximation.
- Boundary conditions.
- Representational choices.
- Model purpose and intended audience.
- Relationships between a model and the reality it represents.

## 1.4 Requirements and Constraints

- Stakeholders and their concerns.
- System purpose and intended outcomes.
- Functional requirements.
- Quality attributes and non-functional requirements.
- Operational scenarios.
- Performance criteria.
- Environmental and operational constraints.
- Resource, cost, and schedule constraints.
- Safety, reliability, and maintainability considerations.
- Requirement conflicts and trade-offs.
- Acceptance criteria.
- Traceability between requirements and design decisions.

## 1.5 Structural System Knowledge

- Components and their responsibilities.
- Composition and decomposition.
- Hierarchical organization.
- Aggregation and association.
- Dependencies and coupling.
- Interfaces and interaction points.
- Information, material, energy, or control flows.
- Functional allocation to components.
- Modular organization.
- Separation of concerns.
- Cohesion and coupling as design considerations.
- Structural constraints and compatibility.

## 1.6 Behavioral and Dynamic System Knowledge

- States and state transitions.
- Events and responses.
- Processes and activities.
- Sequence and ordering.
- Control flow and information flow.
- Feedback loops.
- Inputs, outputs, and transformations.
- Timing and temporal constraints.
- Concurrent and asynchronous behavior.
- Conditions, exceptions, and alternative paths.
- System responses to disturbances.
- Dynamic behavior across operating scenarios.

## 1.7 Architecture and Design Knowledge

- System architecture and architectural viewpoints.
- Functional and physical decomposition.
- Allocation of functions to components.
- Interface definition.
- Architectural alternatives.
- Design constraints and design rationale.
- Modularity and separation of concerns.
- Trade-offs among performance, cost, complexity, and flexibility.
- Scalability and extensibility.
- Reliability and fault containment.
- Maintainability and evolution.
- Integration and interoperability.

Formal architecture frameworks and specialist architecture-description
languages may be introduced selectively rather than treated as
mandatory content.

## 1.8 Quantitative and Computational Modeling

- Variables, parameters, and state.
- Relationships and constraints expressed mathematically.
- Equations and systems of equations.
- Discrete and continuous representations.
- Deterministic and stochastic models.
- Static and dynamic models.
- Graph-based representations.
- Basic optimization models.
- Simulation as a means of exploring system behavior.
- Sensitivity to parameter changes.
- Numerical approximation and computational limitations.
- Interpretation of model outputs.

Formal differential-equation modeling, advanced optimization,
probabilistic modeling, and specialized numerical techniques may be
deferred according to learner readiness.

## 1.9 Model-Based Engineering and Lifecycle

- Models as design and communication artifacts.
- Relationships between requirements, models, and implementation.
- Model refinement across levels of detail.
- Model consistency across representations.
- Model-to-model transformation as an advanced concept.
- Model-based analysis and simulation.
- Design review and model revision.
- Verification and validation.
- Configuration and version management.
- Evolution of models as system understanding changes.

## 1.10 Socio-Technical Systems

- Interaction between people, technology, and organizational processes.
- Stakeholder roles and responsibilities.
- Human-system interfaces.
- Operational context and usage scenarios.
- Organizational constraints and incentives.
- Human error and system-level contributing factors.
- Accessibility and usability considerations.
- Social and environmental consequences.
- Interactions between technical and non-technical requirements.

This area should support systems awareness without turning the course
into a full human-computer interaction or organizational theory course.

---

# 2. Concepts and Theories

This dimension identifies conceptual frameworks used to understand
systems, construct models, and reason about design alternatives.

## 2.1 Core Systems Concepts

- System boundary.
- System environment.
- Component and subsystem.
- Interface and interaction.
- Input, process, output, and outcome.
- State and behavior.
- Dependency and coupling.
- Feedback and control.
- Emergence.
- System hierarchy.
- System lifecycle.
- System-of-systems as an extension concept.

## 2.2 Abstraction and Representation

- Purpose-driven abstraction.
- Essential versus incidental properties.
- Levels of abstraction.
- Decomposition and modularization.
- Idealization and simplification.
- Explicit and implicit assumptions.
- Representation and interpretation.
- Model fidelity and model complexity.
- Representational adequacy for a specific purpose.
- Information loss through abstraction.
- Relationships among multiple models of the same system.
- Limits of a model's explanatory or predictive power.

A model should be judged by whether it is useful for its intended
purpose, not by whether it contains every detail of the real system.

## 2.3 Structural Concepts

- Hierarchy and composition.
- Part-whole relationships.
- Dependency relationships.
- Functional allocation.
- Interface contracts.
- Modularity.
- Cohesion and coupling.
- Separation of concerns.
- Encapsulation as a structural principle.
- Redundancy and single points of failure.
- Architectural constraints.
- Interoperability and compatibility.

## 2.4 Behavioral Concepts

- State and state transition.
- Events and actions.
- Preconditions and postconditions.
- Process sequence.
- Conditional behavior.
- Feedback and control.
- Concurrency.
- Synchronization.
- Timing and latency.
- Stable and unstable behavior at an introductory level.
- Failure states and recovery paths.
- Interactions between components over time.

## 2.5 Requirements and Design Reasoning

- Stakeholder needs versus system requirements.
- Functional versus quality requirements.
- Requirements versus implementation decisions.
- Constraints versus preferences.
- Completeness and ambiguity.
- Requirement conflicts.
- Traceability and coverage.
- Design rationale.
- Feasibility and trade-off analysis.
- Change impact.
- Design alternatives and decision criteria.

## 2.6 Modeling Theory and Quantitative Reasoning

- Variables, parameters, and assumptions.
- Relationships and constraints.
- Dimensional consistency.
- Model calibration as an introductory concept.
- Sensitivity analysis.
- Parameter uncertainty.
- Deterministic versus probabilistic assumptions.
- Discrete versus continuous representations.
- Simulation and scenario exploration.
- Model validity within a defined domain.
- Verification versus validation.
- Limits of prediction.

## 2.7 Complexity and Emergence

- Complexity arising from interactions.
- Feedback-driven behavior.
- Nonlinear relationships.
- Delays and indirect effects.
- Emergent properties.
- Local behavior versus global behavior.
- Unintended system-level consequences.
- Sensitivity to initial conditions as an extension concept.
- Limits of component-by-component reasoning.
- Trade-offs between model simplicity and explanatory power.

These concepts should be introduced with concrete examples and
without implying that every complex system is inherently unpredictable.

## 2.8 Design Quality and System Evaluation

- Fitness for purpose.
- Functional adequacy.
- Performance and efficiency.
- Reliability and robustness.
- Maintainability and evolvability.
- Usability and accessibility.
- Safety and risk.
- Scalability.
- Resilience.
- Cost and lifecycle implications.
- Trade-offs among quality attributes.
- Evidence supporting design decisions.

---

# 3. Research Methods

This dimension covers methods for investigating existing systems,
constructing models, and evaluating proposed designs.

## 3.1 System Investigation

- Context observation.
- Stakeholder interviews or structured inquiry.
- Review of existing documentation.
- Identification of system purpose and operational context.
- Identification of system actors and external entities.
- Observation of normal and exceptional scenarios.
- Identification of dependencies and constraints.
- Investigation of existing system limitations.
- Comparison between intended and observed behavior.

## 3.2 Problem Framing

- Scope definition.
- Boundary identification.
- Identification of relevant stakeholders.
- Separation of problem statements from proposed solutions.
- Identification of assumptions.
- Identification of unknowns and evidence gaps.
- Definition of the intended modeling purpose.
- Selection of the appropriate level of detail.
- Establishment of success criteria.

## 3.3 Requirements Analysis

- Requirements elicitation.
- Requirements classification.
- Functional decomposition.
- Identification of quality attributes.
- Scenario-based analysis.
- Conflict and ambiguity identification.
- Requirements prioritization.
- Acceptance-criteria definition.
- Traceability mapping.
- Change-impact analysis.

Formal requirements engineering techniques can be selected according
to the complexity of the learning project.

## 3.4 Structural Modeling

- Identification of components and responsibilities.
- Hierarchical decomposition.
- Component relationship mapping.
- Interface identification.
- Dependency mapping.
- Functional allocation.
- Data-flow or material-flow representation.
- Identification of critical coupling points.
- Comparison of alternative decompositions.

## 3.5 Behavioral Modeling

- Scenario analysis.
- Process and activity modeling.
- State identification.
- State-transition modeling.
- Sequence and interaction analysis.
- Event-response modeling.
- Control-flow representation.
- Exception-path analysis.
- Feedback-loop identification.
- Comparison of expected and observed behavior.

## 3.6 Quantitative Model Construction

- Selection of variables and parameters.
- Formulation of assumptions.
- Translation of relationships into equations or rules.
- Identification of boundary and initial conditions.
- Selection of a suitable mathematical representation.
- Parameter estimation using available evidence.
- Basic sensitivity checks.
- Interpretation of model output.
- Recognition of numerical and representational limitations.

## 3.7 Model Evaluation

- Internal consistency checking.
- Completeness checking against intended scope.
- Dimensional and logical checks.
- Comparison with requirements.
- Comparison with observed system behavior.
- Scenario-based testing.
- Sensitivity analysis.
- Simulation-based exploration.
- Expert or stakeholder review.
- Identification of unsupported assumptions.
- Revision in response to discrepancies.

## 3.8 Design Alternative Evaluation

- Generation of alternative architectures.
- Comparison against requirements.
- Evaluation of quality attributes.
- Trade-off analysis.
- Feasibility assessment.
- Basic decision matrices.
- Scenario-based comparison.
- Risk and dependency assessment.
- Design rationale documentation.
- Revision of decisions when evidence changes.

## 3.9 Research Quality and Model Transparency

- Clear statement of modeling purpose.
- Explicit assumptions and simplifications.
- Traceability from evidence to representation.
- Reproducible calculations where appropriate.
- Documentation of model versions.
- Distinction between observations and inferences.
- Recognition of uncertainty.
- Honest reporting of model limitations.
- Appropriate use of simulation and computational tools.

---

# 4. Processes and Methods

This dimension identifies candidate workflows for systems design and
abstract modeling.

## 4.1 General Systems Modeling Cycle

A candidate working cycle is:

1. Identify the problem, purpose, and intended stakeholders.
2. Investigate the operating context.
3. Define system scope and boundaries.
4. Identify assumptions, requirements, and constraints.
5. Select an appropriate level of abstraction.
6. Identify system elements and relationships.
7. Construct structural and behavioral representations.
8. Analyze interactions, dependencies, and potential failure points.
9. Compare candidate system designs.
10. Evaluate models against evidence and requirements.
11. Refine the models and design decisions.
12. Communicate the result, assumptions, and limitations.

The cycle is iterative. New evidence or a change in requirements may
require revisiting earlier decisions.

## 4.2 Boundary and Scope Definition

- Identify the system of interest.
- Identify external actors and neighboring systems.
- Distinguish system responsibilities from environmental influences.
- Identify relevant inputs and outputs.
- Define the operating context.
- State explicit inclusions and exclusions.
- Record assumptions that affect the boundary.
- Review whether the boundary supports the modeling purpose.

## 4.3 Abstraction and Decomposition

- Identify the questions the model must answer.
- Select the relevant system properties.
- Remove details that do not serve the current purpose.
- Decompose the system into manageable elements.
- Define responsibilities and relationships.
- Establish consistent levels of detail.
- Identify dependencies that cross decomposition boundaries.
- Recompose the parts to check overall coherence.
- Revise the abstraction when it hides important behavior.

## 4.4 Requirements-to-Model Workflow

- Gather and classify requirements.
- Identify conflicting or ambiguous requirements.
- Convert relevant requirements into observable conditions.
- Map requirements to system functions or components.
- Identify interfaces and dependencies.
- Check whether each important requirement is represented.
- Identify requirements without a plausible implementation path.
- Record design decisions and unresolved questions.

## 4.5 Structural and Behavioral Modeling Workflow

- Identify major system elements.
- Establish relationships and interfaces.
- Determine the important system states or activities.
- Represent interactions under selected scenarios.
- Check consistency between structure and behavior.
- Identify missing states, paths, or dependencies.
- Revise the model to resolve contradictions.

## 4.6 Alternative Architecture Development

- Establish the primary design problem.
- Identify non-negotiable constraints.
- Generate alternative structures or allocations.
- Compare modularity, complexity, performance, and cost.
- Identify trade-offs and failure dependencies.
- Evaluate alternatives against representative scenarios.
- Select and justify a candidate design.
- Record assumptions and reasons for rejecting alternatives.

## 4.7 Model-Based Analysis and Simulation

- Define the question the model should investigate.
- Select a representation suitable for that question.
- Establish model assumptions and parameters.
- Define scenarios or test conditions.
- Run calculations or simulations where appropriate.
- Compare outputs across alternatives.
- Examine sensitivity to important assumptions.
- Interpret results within the model's valid scope.
- Avoid treating simulated results as direct proof of real-world behavior.

## 4.8 Verification and Validation Workflow

- Check that the representation is internally consistent.
- Check that it covers the intended scope.
- Check relationships and constraints.
- Compare model behavior with specified expectations.
- Compare predictions with observations when available.
- Identify discrepancies and their possible causes.
- Revise the model or revise unsupported assumptions.
- Record what has and has not been demonstrated.

Verification asks whether the model or design conforms to specified
requirements. Validation asks whether it is an adequate representation
or solution for the intended purpose and context.

## 4.9 Model Evolution and Change Management

- Maintain clear model versions.
- Record significant assumptions and design decisions.
- Identify changes in requirements or context.
- Assess the impact of changes on dependent representations.
- Update affected models and documentation.
- Check consistency after revision.
- Preserve traceability between revisions and their rationale.

---

# 5. Tools and Technologies

This dimension identifies candidate tools for representing and
analyzing systems. Tool selection should follow the modeling purpose.

## 5.1 Visual and Diagrammatic Modeling

- Whiteboards and collaborative sketching.
- Flowcharts.
- Block diagrams.
- Context diagrams.
- Hierarchical decomposition diagrams.
- Relationship and dependency diagrams.
- Process and activity diagrams.
- State-transition diagrams.
- Sequence diagrams.
- Data-flow diagrams.
- System maps and causal-loop diagrams.

Not every diagram type needs to be taught. The final syllabus should
select a small, coherent set based on the intended learning outcomes.

## 5.2 Formal Modeling Notations

- UML as a family of modeling notations.
- SysML as a systems modeling language.
- BPMN for business process modeling.
- Entity-relationship diagrams for data structure.
- Finite-state representations.
- Mathematical notation for variables, relationships, and constraints.
- Interface and contract representations.

Formal notations are candidate tools rather than prerequisites for
understanding systems. Their selection should reflect the students'
readiness and the needs of the projects.

## 5.3 Quantitative and Computational Tools

- Spreadsheets for parameter tables and calculations.
- Graphing and plotting tools.
- Basic programming environments.
- Numerical calculation tools.
- Simulation environments.
- Discrete-event or agent-based simulation tools, where appropriate.
- Simple optimization tools.
- Data visualization tools.

## 5.4 System and Architecture Documentation

- Requirements tables.
- Interface specifications.
- Component inventories.
- Traceability matrices.
- Architecture decision records.
- Model repositories.
- Version control systems.
- Collaborative technical documentation.
- Review and annotation tools.

## 5.5 Tool Selection Principles

Tools should be selected according to:

- The question the model is intended to answer.
- The complexity of the system.
- The required level of precision.
- The learners' current competencies.
- The cost and availability of the tool.
- The ease of reviewing and communicating the model.
- The need for reproducibility and revision.
- The risk of introducing tool complexity unrelated to learning goals.

A visually sophisticated model is not necessarily a good model.
Clarity, consistency, fitness for purpose, and defensible assumptions
matter more than decorative complexity.

---

# 6. Artifacts and Deliverables

This dimension identifies observable outputs through which learners
may demonstrate systems modeling and design competence.

## 6.1 Problem and Context Artifacts

- Problem statement.
- System purpose statement.
- Stakeholder and actor inventory.
- Operational context description.
- Scope and boundary definition.
- Assumptions register.
- Constraints inventory.
- Initial requirements list.

## 6.2 Structural Modeling Artifacts

- System context diagram.
- System decomposition diagram.
- Component diagram.
- Functional decomposition.
- Interface map.
- Dependency graph.
- Data-flow or material-flow representation.
- Component responsibility table.
- Alternative structural models.

## 6.3 Behavioral Modeling Artifacts

- Process or activity diagram.
- State-transition diagram.
- Sequence or interaction diagram.
- Operational scenario descriptions.
- Input-output behavior table.
- Exception and recovery paths.
- Feedback-loop representation.
- Behavioral assumptions and constraints.

## 6.4 Quantitative and Analytical Artifacts

- Parameter and variable definitions.
- Mathematical model.
- Constraint or relationship equations.
- Spreadsheet model.
- Simulation configuration.
- Scenario comparison.
- Sensitivity analysis.
- Model output interpretation.
- Model limitations statement.

## 6.5 Design Artifacts

- Candidate system architecture.
- Alternative architecture comparison.
- Functional allocation table.
- Interface specification.
- Requirements-to-design traceability matrix.
- Design decision record.
- Trade-off analysis.
- Preliminary verification plan.

## 6.6 Evaluation Artifacts

- Model consistency checklist.
- Requirements coverage assessment.
- Scenario-based evaluation.
- Model verification record.
- Model validation report.
- Comparison between model predictions and observations.
- Risk and dependency analysis.
- Revision history.
- Unresolved issues register.

## 6.7 Communication Artifacts

- Model explanation.
- Annotated system diagrams.
- Technical modeling report.
- Architecture or design presentation.
- Model walkthrough.
- Design rationale.
- Peer-review comments and revisions.
- Reflection on abstraction choices and model limitations.

A project should produce a coherent subset of these artifacts.
The purpose is to make reasoning inspectable, not to maximize document
count or diagram quantity.

---

# 7. Competencies and Performance

This dimension identifies what learners may be expected to understand,
construct, analyze, justify, and communicate.

## 7.1 Systems Thinking

Learners may be expected to:

- Explain how system elements interact to produce overall behavior.
- Identify relevant subsystems and external dependencies.
- Recognize the effects of interfaces and feedback.
- Distinguish component-level performance from system-level outcomes.
- Identify possible indirect or unintended consequences.
- Explain why system boundaries affect analysis and decisions.

## 7.2 Problem Framing and Abstraction

Learners may be expected to:

- Define the system of interest and its purpose.
- Establish an explicit scope and boundary.
- Select an appropriate level of abstraction.
- Identify relevant assumptions and simplifications.
- Explain why particular details were included or excluded.
- Recognize when a model omits information necessary for its purpose.
- Revise an abstraction when evidence exposes a limitation.

## 7.3 Requirements and Constraints

Learners may be expected to:

- Identify relevant stakeholders and operational conditions.
- Distinguish functional requirements from quality attributes.
- Identify constraints and conflicting objectives.
- Express selected requirements in observable terms.
- Connect requirements to system functions or components.
- Explain how requirements influence design choices.
- Identify unresolved requirements and missing evidence.

## 7.4 Structural Modeling

Learners may be expected to:

- Identify system components and responsibilities.
- Represent component relationships and interfaces.
- Decompose a system into manageable elements.
- Recognize dependencies and coupling.
- Compare alternative structural organizations.
- Check whether the representation is consistent with the stated scope.
- Explain important architectural decisions.

## 7.5 Behavioral Modeling

Learners may be expected to:

- Represent important system processes or states.
- Explain interactions over time.
- Identify conditional and exceptional behavior.
- Trace a scenario through a model.
- Identify missing states or interaction paths.
- Compare expected behavior with observed behavior.
- Explain how structural choices affect behavior.

## 7.6 Quantitative and Computational Reasoning

Learners may be expected to:

- Define variables, parameters, and assumptions.
- Express simple system relationships quantitatively.
- Interpret model outputs and visualizations.
- Explore the effects of parameter changes.
- Recognize uncertainty and limitations in a model.
- Compare alternative scenarios using evidence.
- Avoid claims that exceed what the model supports.

## 7.7 System Design and Trade-Offs

Learners may be expected to:

- Generate multiple candidate system structures.
- Compare alternatives against stated requirements.
- Identify trade-offs among important quality attributes.
- Explain dependencies and potential failure points.
- Justify a design choice with explicit criteria.
- Recognize when additional analysis is necessary.
- Revise design decisions when evidence changes.

## 7.8 Verification and Validation

Learners may be expected to:

- Check internal consistency in a model.
- Evaluate whether a model covers its intended scope.
- Compare a representation with requirements.
- Design simple scenario-based checks.
- Distinguish verification from validation.
- Identify evidence needed to support a model's validity.
- State limitations and unresolved uncertainties.

## 7.9 Communication and Collaboration

Learners may be expected to:

- Construct readable and interpretable models.
- Select a representation appropriate to the audience and purpose.
- Explain model assumptions and boundaries.
- Communicate structural and behavioral relationships.
- Maintain consistent terminology across artifacts.
- Review and critique another person's model.
- Incorporate feedback without losing traceability.

---

# 8. Levels and Prerequisites

This dimension identifies potential entry requirements and progression
levels. It does not prescribe the final course sequence.

## 8.1 Entry-Level Assumptions

Potential prerequisites or readiness indicators:

- Basic logical and analytical reasoning.
- Ability to interpret simple diagrams and tables.
- Familiarity with elementary variables and relationships.
- Basic quantitative reasoning.
- Ability to describe a process or practical problem.
- Basic digital literacy.
- Willingness to make assumptions explicit and revise them.

Prior knowledge of UML, SysML, programming, or formal systems engineering
should not be assumed universally.

## 8.2 Foundational Level

Possible learning expectations:

- Recognize systems, components, boundaries, and interactions.
- Define a simple system's purpose and scope.
- Construct context and decomposition diagrams.
- Represent a basic process or sequence of interactions.
- Identify assumptions and constraints.
- Explain the purpose and limitations of a model.
- Compare simple alternative representations.

## 8.3 Developing Level

Possible learning expectations:

- Analyze a bounded problem with multiple interacting components.
- Define requirements and connect them to system elements.
- Construct consistent structural and behavioral models.
- Identify interface dependencies and possible failure points.
- Compare alternative system designs.
- Use simple quantitative analysis or simulation where appropriate.
- Evaluate models against requirements and scenarios.
- Justify abstraction choices and design trade-offs.

## 8.4 Extension Level

Possible enrichment for learners with stronger preparation:

- Model systems with multiple interacting subsystems.
- Explore feedback, delays, and emergent behavior.
- Use formal modeling notations selectively.
- Develop a quantitative or computational model.
- Perform sensitivity or scenario analysis.
- Compare architectural alternatives against several quality attributes.
- Maintain traceability across multiple representations.
- Investigate model-based engineering workflows.

Extension should deepen model quality and reasoning rather than merely
introduce more diagram types or more sophisticated software.

## 8.5 Progression Considerations

The course may support progression toward:

- Applied Convergence of Design and Technology.
- Modern Software Development.
- Applied AI and Intelligent Systems.
- Robotics.
- Industrial Design and Technologies.
- Business Intelligence and Analytics.
- More advanced systems engineering or model-based engineering study.

The specific progression depends on the final curriculum architecture.
The same systems concepts may be reused in different concentrations
with different domain-specific representations and applications.

---

# 9. Cross-Dimensional Relationships

The eight dimensions are observational perspectives rather than
mutually exclusive categories. A single modeling activity may involve
several dimensions simultaneously.

| Modeling Activity | Relevant Dimensions |
|---|---|
| Defining the boundary of a smart-room system | Disciplinary Knowledge; Concepts and Theories; Processes and Methods |
| Decomposing a device into components and interfaces | Structural Modeling; Tools and Technologies; Competencies |
| Representing a user interaction as a sequence of states | Behavioral Modeling; Research Methods; Artifacts and Deliverables |
| Translating stakeholder needs into system requirements | Requirements Knowledge; Processes and Methods; Competencies |
| Comparing alternative architectures | Architecture Knowledge; Design Reasoning; Evaluation Artifacts |
| Simulating changes in system parameters | Quantitative Modeling; Computational Tools; Research Methods |
| Checking a model against observed behavior | Model Evaluation; Verification and Validation; Evidence Quality |
| Revising a model after discovering a missing dependency | Abstraction; System Structure; Model Evolution |

These relationships may inform subsequent curriculum modeling.
They are not yet a formal ontology, dependency graph, or required teaching
sequence.

---

# 10. Candidate Learning-Activity Patterns

The following patterns may be used to investigate the candidate
cognition space during subsequent syllabus development.

They are illustrative patterns rather than finalized course modules.

## 10.1 From Real-World Situation to System Boundary

Learners examine a practical situation, identify the system of interest,
and justify what belongs inside or outside the boundary.

Potential coverage:

- Problem framing.
- Stakeholders and operational context.
- System boundary and environment.
- Assumptions and scope.
- Abstraction choices.

## 10.2 One System, Multiple Representations

Learners represent the same bounded system through complementary
structural and behavioral models.

Potential coverage:

- System components and relationships.
- Process and state representations.
- Different modeling viewpoints.
- Cross-model consistency.
- Representation limitations.

## 10.3 Decompose, Then Recompose

Learners decompose a system into elements, assign responsibilities,
identify interfaces, and check whether the elements collectively
support the system's purpose.

Potential coverage:

- Hierarchy and decomposition.
- Component responsibilities.
- Dependencies and coupling.
- Interfaces.
- System-level coherence.

## 10.4 Requirements-to-Architecture Challenge

Learners receive a small set of requirements and constraints, develop
alternative system structures, and compare them against explicit
criteria.

Potential coverage:

- Requirements analysis.
- Functional allocation.
- Architectural alternatives.
- Trade-off reasoning.
- Design rationale.

## 10.5 Model, Predict, and Compare

Learners construct a simple quantitative or rule-based model, predict
behavior under selected conditions, and compare predictions with
observations or a reference scenario.

Potential coverage:

- Variables and assumptions.
- Model construction.
- Scenario analysis.
- Verification and validation.
- Model limitations.

## 10.6 Find the Missing Relationship

Learners review an incomplete or inconsistent system model, identify
missing dependencies or interactions, and revise the representation.

Potential coverage:

- Structural consistency.
- Behavioral reasoning.
- Model critique.
- Evidence and assumptions.
- Iterative refinement.

## 10.7 Design for Change

Learners examine how a change in one requirement affects system
components, interfaces, and dependent representations.

Potential coverage:

- Dependency analysis.
- Traceability.
- Change impact.
- Architecture evolution.
- Model maintenance.

The final syllabus should select a small number of activities that
integrate multiple objectives while remaining feasible for the
intended learners and teaching environment.

---

# 11. Candidate Inclusion and Exclusion Rules

## 11.1 Inclusion Criteria

A candidate topic should receive stronger consideration when it:

- Supports a clearly stated learning outcome.
- Helps learners understand systems, abstraction, or design.
- Can be represented through an interpretable model or analysis.
- Encourages explicit assumptions and defensible decisions.
- Supports comparison, testing, or evaluation.
- Transfers across multiple engineering or technology domains.
- Can be taught and assessed with available resources.
- Provides a foundation for subsequent coursework.

## 11.2 Deferral or Exclusion Criteria

A topic may be deferred or excluded when it:

- Requires advanced mathematical or domain-specific prerequisites.
- Is primarily a specialist technique unrelated to the course's core aims.
- Duplicates another course's intended depth and primary responsibility.
- Requires formal notation whose complexity exceeds the learning benefit.
- Introduces a tool without a clear modeling purpose.
- Cannot be meaningfully assessed within the available course scope.
- Adds diagrammatic complexity without improving understanding.
- Is included merely because it appears in a systems engineering
  textbook or modeling standard.

The presence of a topic in this inventory does not establish its priority.

---

# 12. Open Questions for Subsequent Curriculum Modeling

The following questions remain unresolved and should be addressed
during curriculum construction.

1. What learner age, prior knowledge, and mathematical readiness
   should this course assume?

2. Should the course emphasize general systems thinking, formal
   modeling, system design decisions, or a balanced combination?

3. Which modeling representations should all learners be able to
   interpret and construct?

4. How much formal notation is appropriate before it begins to obscure
   rather than clarify the underlying system?

5. Should the primary examples come from physical products, software,
   robotics, information systems, or a deliberately mixed set?

6. Which quantitative and computational modeling methods are feasible
   within the intended teaching environment?

7. How should Foundation Core and Advanced Core differ in model
   complexity, independence, evidence requirements, and design scope?

8. Which learning outcomes should be shared across both Core versions?

9. What is the minimum set of models and artifacts needed to demonstrate
   the intended learning outcomes?

10. How should consistency be checked when a system is represented
    through multiple diagrams or modeling viewpoints?

11. What evidence is sufficient to validate a model for its intended
    purpose?

12. Which concepts should be delegated to Fundamentals of Engineering,
    Applied Convergence of Design and Technology, or Seminar?

13. How can the course teach abstraction as a reasoning skill rather
    than simply teach students to use diagramming software?

14. What balance between qualitative models, quantitative models,
    and implementation-oriented examples best serves the target learners?

---

# 13. Current Status and Next Step

**Status:** Initial candidate inventory; not a final syllabus.

This document maps potential knowledge and practice areas for
Systems Design and Abstract Modeling. It does not establish final
topic priorities, weekly sequence, course duration, assessment weights,
or Core-specific variants.

The next modeling stage should:

1. Compare the inventory against the intended learner profile and
   curriculum requirements.
2. Select a manageable set of foundational learning outcomes.
3. Define the minimum structural and behavioral modeling capabilities
   learners should acquire.
4. Select a coherent set of modeling activities and assessment artifacts.
5. Check overlap and progression with the other Core courses.
6. Define differences between Foundation Core and Advanced Core.
7. Record unresolved design decisions rather than silently assuming them.

The objective is not to maximize the number of models, diagrams,
notations, or tools introduced.

It is to help learners construct useful abstractions, reason about
interacting elements, evaluate design alternatives, and communicate
system-level decisions with clarity and evidence.
