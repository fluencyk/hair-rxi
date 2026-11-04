# RXI-210 · Week 01

## Computational Problems, Algorithms, and Abstractions

---

# Slide 01 — Computational Problems, Algorithms, and Abstractions

## Main Content

### Question

**How can a real-world problem become something a computer can solve?**

### Concept

Computational problem solving begins by representing a problem precisely enough that a sequence of computational steps can operate on it.

### Learning Path

Problem  
↓  
Representation  
↓  
Algorithm  
↓  
Implementation  
↓  
Execution  
↓  
Observable Result

---

### References

**Massachusetts Institute of Technology**  
MIT OpenCourseWare — 6.006 Introduction to Algorithms  
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

**Massachusetts Institute of Technology**  
MIT 6.006 — Models of Computation  
https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec02/

---

# Slide 02 — What Is a Computational Problem?

## Main Content

### Concept

A computational problem describes a required transformation from available information to a desired result under defined conditions or constraints.

### Example

**Situation**

A school has electricity-use readings from several classrooms.

**Problem**

Identify the classroom with the highest electricity use.

**Input**

A collection of classroom electricity readings.

**Output**

The classroom associated with the largest reading.

**Constraint**

Every available classroom reading must be considered.

---

### References

**Massachusetts Institute of Technology**  
MIT 6.006 — Introduction to Algorithms  
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

---

# Slide 03 — From Reality to Representation

## Main Content

### Scenario

The real classroom contains students, furniture, lighting, temperature, schedules, electricity meters, and many other details.

### Question

**Which information is actually necessary if our problem is only to identify the classroom with the highest electricity use?**

### Concept

Abstraction preserves information relevant to a computational problem while leaving irrelevant detail outside the representation.

---

### References

**BCS Computing at School / Association for Computing Machinery**  
Computational Thinking guidance and ACM CS2023 Computer Science Foundations  
https://csed.acm.org/computer-science-foundations/

---

# Slide 04 — Input → Process → Output

## Main Content

### Model

#### Input

| Classroom | Electricity Use |
|---|---:|
| Room A | 12 |
| Room B | 7 |
| Room C | 19 |
| Room D | 15 |

#### Process

Compare the electricity-use values.

#### Output

**Room C — 19**

### Concept

Input, process, and output provide a simple structural representation of a computational transformation.

### Question

**The process currently says "compare the values". Is that precise enough for a computer?**

---

### References

**Massachusetts Institute of Technology**  
MIT 6.006 Introduction to Algorithms  
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

**National Institute of Standards and Technology**  
NIST CSRC Glossary — Computer  
https://csrc.nist.gov/glossary/term/computer

---

# Slide 05 — An Algorithm Makes the Process Explicit

## Main Content

### Concept

An algorithm expresses an ordered procedure for transforming a problem state toward a required result.

### Procedure

1. Take the first reading as the current maximum.
2. Inspect the next reading.
3. If it is larger than the current maximum, replace the current maximum.
4. Repeat until all readings have been inspected.
5. Return the classroom associated with the current maximum.

### Question

**What must remain known while this procedure is running?**

---

### References

**National Institute of Standards and Technology / Massachusetts Institute of Technology**  
NIST CSRC Algorithm Glossary; MIT 6.006 Models of Computation  
https://csrc.nist.gov/glossary/term/algorithm

**National Institute of Standards and Technology**  
NIST Dictionary of Algorithms and Data Structures — Algorithm  
https://xlinux.nist.gov/dads/HTML/algorithm.html

---

# Slide 06 — Trace the Algorithm

## Main Content

### Trace

**Input**

12, 7, 19, 15

| Step | Observed Value | Current Maximum |
|---:|---:|---:|
| 1 | 12 | 12 |
| 2 | 7 | 12 |
| 3 | 19 | 19 |
| 4 | 15 | 19 |

**Output**

19

### Reflection

The algorithm does not need to remember every previous comparison. It only needs the current state required by the procedure.

---

### References

**Massachusetts Institute of Technology**  
MIT 6.006 Introduction to Algorithms — Syllabus and algorithm write-up guidance  
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2008/pages/syllabus/

**RXI Instructional Derivation**  
Verified consequence of the displayed algorithm trace.

---

# Slide 07 — Problem ≠ Algorithm ≠ Program

## Main Content

### Comparison

#### Problem

Find the largest electricity-use value.

#### Representation

Represent classroom readings as identifiable numerical values.

#### Algorithm

Inspect values while maintaining the largest value observed so far.

#### Implementation

Express that algorithm using a programming language such as Python.

### Concept

**The computational idea is not identical to the code used to implement it.**

---

### References

**Massachusetts Institute of Technology**  
MIT 6.006 — Lecture 2: Models of Computation  
https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec02/

**Massachusetts Institute of Technology / Association for Computing Machinery**  
MIT 6.006 Models of Computation; ACM Software Development Fundamentals  
https://csed.acm.org/knowledge-areas-software-development-fundamentals-sdf-cs2013-version/

---

# Slide 08 — One Problem, Different Algorithms

## Main Content

### Comparison

#### Approach A

Inspect each value once while maintaining the current maximum.

#### Approach B

Sort all values and then select the largest value.

### Question

**If both approaches return the correct result, what else might matter when comparing them?**

### Concept

Correctness and computational cost are different properties of an algorithm.

---

### References

**Association for Computing Machinery**  
ACM Software Development Fundamentals  
https://csed.acm.org/knowledge-areas-software-development-fundamentals-sdf-cs2013-version/

**Massachusetts Institute of Technology / National Institute of Standards and Technology**  
MIT 6.006 Introduction to Algorithms; NIST Mathematics and Engineering in Computer Science  
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

---

# Slide 09 — Does the Algorithm Always Work?

## Main Content

### Test Cases

| Input | Expected Result |
|---|---:|
| 12, 7, 19, 15 | 19 |
| 4, 4, 4, 4 | 4 |
| -8, -2, -11, -5 | -2 |
| 100 | 100 |

### Question

**Why should we test structurally different inputs rather than only one convenient example?**

### Concept

Correctness reasoning asks whether an algorithm satisfies the required problem behavior across valid inputs, not merely whether one execution happens to work.

---

### References

**Massachusetts Institute of Technology**  
MIT 6.006 Introduction to Algorithms  
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2008/pages/syllabus/

---

# Slide 10 — From Algorithm to Python

## Main Content

### Pseudocode

    current_max ← first value

    FOR each remaining value

        IF value > current_max

            current_max ← value

    RETURN current_max

### Python Implementation

    values = [12, 7, 19, 15]

    current_max = values[0]

    for value in values[1:]:
        if value > current_max:
            current_max = value

    print(current_max)

### Question

**Which parts of the Python program express the algorithm's state, repetition, and decision?**

---

### References

**Association for Computing Machinery**  
ACM Software Development Fundamentals  
https://csed.acm.org/knowledge-areas-software-development-fundamentals-sdf-cs2013-version/

**Python Software Foundation**  
Python Documentation — More Control Flow Tools  
https://docs.python.org/3/tutorial/controlflow.html

---

# Slide 11 — The Code Is Not the Computational Idea

## Main Content

### Comparison

| Computational Reasoning | Python Mechanisms |
|---|---|
| Maintain a current candidate. | variable |
| Inspect remaining values. | list / iteration |
| Replace the candidate when a better value is observed. | if statement / assignment |
| Return the final candidate. | resulting variable |

### Question

**Could the same algorithm be implemented in JavaScript, Java, C++, or another language?**

### Concept

Programming languages provide mechanisms for expressing computation; they do not define the computational problem itself.

---

### References

**Massachusetts Institute of Technology / Association for Computing Machinery**  
MIT 6.006 Models of Computation; ACM CS2023  
https://csed.acm.org/computer-science-foundations/

**Massachusetts Institute of Technology**  
MIT 6.006 — Models of Computation  
https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec02/

---

# Slide 12 — Run a Small Computational Experiment

## Main Content

### Experiment

**Task**

Run the maximum-value algorithm using several different input collections.

**Procedure**

1. Predict the expected output before execution.
2. Run the Python implementation.
3. Record the observed output.
4. Compare prediction and observation.
5. Explain whether the observed behavior is consistent with the algorithm.

**Suggested Inputs**

- 12, 7, 19, 15
- 4, 4, 4, 4
- -8, -2, -11, -5
- 100

### Evidence

Record the following for each experiment:

| Input | Predicted Result | Observed Result | Explanation |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

### References

**Association for Computing Machinery**  
ACM Software Development Fundamentals  
https://csed.acm.org/knowledge-areas-software-development-fundamentals-sdf-cs2013-version/

---

# Slide 13 — Construct Your Own Computational Solution

## Main Content

### Assignment

**Task**

Choose a small bounded problem and construct a computational solution using structured reasoning and a guided Python-based experiment.

**Required Elements**

1. Define the problem.
2. Identify inputs, outputs, and relevant constraints.
3. Explain what information is abstracted from the original situation.
4. Describe or trace an algorithm.
5. Implement a small computational artifact.
6. Run the artifact and record observable behavior.
7. Explain how the implementation expresses the underlying computational reasoning.

### Learning Evidence

Your work should provide:

- Structured representation of a bounded computational problem.
- Explanation or trace of a simple algorithm.
- Short computational artifact connecting abstraction with observable execution.

---

### References

No external reference is required for this assignment.

---

# Slide 14 — Week 01: Computational Reasoning Chain

## Main Content

### Knowledge Chain

Real-world Situation  
↓  
Bounded Problem  
↓  
Abstraction  
↓  
Computational Representation  
↓  
Algorithm  
↓  
Implementation  
↓  
Execution  
↓  
Observable Evidence

### Reflection

**Which stages describe the problem, which describe computational reasoning, and which describe implementation?**

### Transition

Once problems can be represented computationally, we can ask how intelligent systems represent states, search possible solutions, and reason about what to do next.

---

### References

**RXI Synthesis grounded in Massachusetts Institute of Technology / Association for Computing Machinery**  
MIT 6.006 and ACM Computer Science curricular foundations  
https://csed.acm.org/computer-science-foundations/

**Massachusetts Institute of Technology**  
MIT OpenCourseWare — Algorithmic Problem Solving and Computation  
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

---

# Week 01 — End

## Computational Reasoning Foundation

By the end of Week 01, learners should be able to distinguish and connect:

- Real-world situations and bounded computational problems.
- Relevant information and abstraction.
- Computational representations and algorithms.
- Algorithms and programming-language implementations.
- Execution results and evidence.
- Observed successful cases and general correctness reasoning.

The central reasoning chain for this week is:

**Problem → Representation → Algorithm → Implementation → Execution → Observable Evidence**

This chain serves as a Week 01 instructional scaffold for understanding computational reasoning and prepares the transition into representation, search, and intelligent reasoning in Week 02.