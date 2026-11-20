# Software Engineering Lab Submissions

**PES University — Department of Computer Science and Engineering**  
**Course:** Software Engineering (SE) Lab  
**Student:** Rahul Vivek Shenoy  
**SRN:** PES2UG24AM129  
**Section:** B  

---

## 📌 Repository Overview

This repository consolidates all seven Software Engineering laboratory submissions into a unified, structured monorepo. It encompasses requirements engineering, agile project planning, component-level architectural modeling, AI-assisted development ("vibe coding"), static code quality analysis, code coverage measurement, and automated property-based fuzz testing.

---

## 📂 Laboratory Submissions Summary

| Lab | Topic / Title | Problem Statement / Scope | Key Deliverables & Artifacts | Folder |
|:---:|:---|:---|:---|:---:|
| **Lab 1** | **Requirements Engineering & UML Use-Case Modelling** | Remote Team Time-Tracking & Project Approver (#46) | Functional (5 FRs) & Non-Functional (2 NFRs) table, UML use-case diagram with `<<include>>` and `<<extend>>`, detailed use-case flow | [`lab1/`](./lab1/) |
| **Lab 2** | **Agile Backlog Creation & Sprint Simulation in Jira** | Remote Team Time-Tracking & Project Approver | 3 Epics, 5 User Stories with Fibonacci story points (23 total), Active Sprint Board, Burndown chart & reflection | [`lab2/`](./lab2/) |
| **Lab 3** | **Component Modelling & Architectural Pattern Selection** | Remote Team Time-Tracking & Project Approver | Component diagram, Microservices Architecture selection (5 services, 6 APIs), security & performance justifications | [`lab3/`](./lab3/) |
| **Lab 4** | **AI-Assisted Pair Programming ("Vibe Coding")** | Space Invaders Game (Pygame) | Collision detection enhancement, score/audio fixes, before & after gameplay demo videos | [`lab4/`](./lab4/) |
| **Lab 5** | **Static Code Analysis** | Hospital Patient System (`hospital_patient_system.py`) | Pylint score raised from 5.19 to 10.00/10, Bandit issues eliminated (5 → 0), Flake8 warnings fixed (11 → 0), before/after reports | [`lab5/`](./lab5/) |
| **Lab 6** | **Code and Branch Coverage Analysis** | Photo Print Order Processing (`photo_print_order.py`) | Unit tests achieving 100% statement coverage and 100% branch coverage, analysis report (PDF & DOCX), terminal screenshots | [`lab6/`](./lab6/) |
| **Lab 7** | **Fuzz Testing for Input Validation Bugs** | Photo Print Order Processing (`photo_print_order.py`) | Hypothesis property-based fuzz testing suite, bug reproduction, validation hardening, verification report & screenshots | [`lab7/`](./lab7/) |

---

## 🔍 Detailed Lab Descriptions

### [Lab 1: Requirements Engineering & UML Use-Case Modelling](./lab1/)
- **Domain:** Developer Tools & IT Operations (Remote Team Time-Tracking & Project Approver)
- **Key Artifacts:**
  - `01_Requirements/Requirements_Table.md`: 5 Functional Requirements (FR-001 to FR-005) and 2 Non-Functional Requirements (NFR-001, NFR-002) with priority, acceptance criteria, and rationale.
  - `02_UML/Use_Case_Diagram.png`: UML diagram illustrating actors (Remote Developer, Engineering Manager), include relationships (Validate Timesheet), and extend relationships (Reject Timesheet).
  - `03_Use_Case_Flow/Submit_Timesheet_Flow.md`: Detailed end-to-end flow specification for timesheet submission.

### [Lab 2: Agile Backlog Creation & Sprint Simulation in Jira](./lab2/)
- **Focus:** Agile project management, sprint simulation, and capacity estimation using Atlassian Jira.
- **Key Artifacts:**
  - `PES2UG24AM129_SE_LAB2.pdf`: Complete lab submission document with screenshots and analytical reflection.
  - Breakdown of 3 Epics (Time Logging & Submission, Approval Workflow, Budget Visibility).
  - 5 User Stories estimated using the Fibonacci scale (3, 5, 2, 5, 8 story points).
  - Active Sprint Board progression and Sprint Burndown analysis examining mid-sprint scope creep.

### [Lab 3: Component Modelling & Architectural Pattern Selection](./lab3/)
- **Focus:** Structural decomposition and architectural pattern justification.
- **Key Artifacts:**
  - `PES2UG24AM129_SE_LAB3.pdf`: Complete component design and architectural selection report.
  - Architecture: **Microservices Architecture** composed of Time Entry Service, Approval Workflow Service, Budget Analytics Service, Jira Integration Service, and Notification Service.
  - Justifications covering domain-driven boundary isolation, external API resilience, security least-privilege enforcement, and horizontal scaling.

### [Lab 4: AI-Assisted Pair Programming ("Vibe Coding")](./lab4/)
- **Focus:** Collaborative debugging and game feature enhancement with an LLM partner.
- **Game:** Space Invaders clone built in Python with Pygame.
- **Key Artifacts:**
  - `main.py` & `game/`: Cleaned and functional object-oriented game engine.
  - `before.mp4` & `after.mp4`: Side-by-side gameplay recordings showcasing the bug reproduction and resolved collision detection.
  - `requirements.txt`: Project dependencies (`pygame`).

### [Lab 5: Static Code Analysis](./lab5/)
- **Focus:** Automated static analysis, security vulnerability scanning, and code refactoring.
- **System:** Hospital Patient Records and Admission Manager (`hospital_patient_system.py`).
- **Results Achieved:**
  - **Pylint:** Score increased from **5.19/10** to **10.00/10**.
  - **Bandit:** High/medium/low security vulnerabilities reduced from **5 to 0**.
  - **Flake8:** Style, formatting, and linting violations reduced from **11 to 0**.
- **Key Artifacts:**
  - `reports/before/` & `reports/after/`: Raw command-line audit reports.
  - `issues.md`: Detailed issue register mapping line numbers, issue categories, and applied remedies.
  - `reflection.md`: Reflection questions addressing security and code hygiene.

### [Lab 6: Code and Branch Coverage Analysis](./lab6/)
- **Focus:** Systematic testing, statement coverage, and branch coverage measurement using `coverage.py`.
- **Module Under Test:** `photo_print_order.py`
- **Key Artifacts:**
  - `CodeCoverageTest_photo_print_order.py`: Unit tests achieving **100% Line/Statement Coverage**.
  - `BranchCoverageTest_photo_print_order.py`: Additional test cases satisfying all condition branches for **100% Branch Coverage**.
  - `Lab_6_Coverage_Analysis_Report.pdf` / `.docx`: Formal analytical report.
  - `screenshots/`: Verifiable terminal run screenshots.

### [Lab 7: Fuzz Testing for Input Validation Bugs](./lab7/)
- **Focus:** Property-based automated testing and robust input boundary validation using `Hypothesis`.
- **Module Under Test:** `photo_print_order.py`
- **Key Artifacts:**
  - `test_photo_print_order.py`: Hypothesis property-based fuzz tests discovering edge-case inputs (negative values, infinite floats, zero-division hazards).
  - Hardened `photo_print_order.py` incorporating input guards and exception handling.
  - `Lab_7_Fuzz_Testing_Report.pdf` / `.docx`: Formal vulnerability report and remediation verification.
  - `screenshots/`: Terminal output demonstrating bug discovery and test pass verification.

---

## 🛠️ Repository Structure

```
PES2UG24AM129-SE-labs-submissions/
├── .gitignore
├── README.md
├── lab1/
│   ├── README.md
│   ├── 01_Requirements/
│   │   └── Requirements_Table.md
│   ├── 02_UML/
│   │   └── Use_Case_Diagram.png
│   └── 03_Use_Case_Flow/
│       └── Submit_Timesheet_Flow.md
├── lab2/
│   ├── README.md
│   └── PES2UG24AM129_SE_LAB2.pdf
├── lab3/
│   ├── README.md
│   └── PES2UG24AM129_SE_LAB3.pdf
├── lab4/
│   ├── README.md
│   ├── requirements.txt
│   ├── main.py
│   ├── before.mp4
│   ├── after.mp4
│   └── game/
│       ├── bullet.py
│       ├── enemy.py
│       ├── game_engine.py
│       ├── player.py
│       └── sound.py
├── lab5/
│   ├── README.md
│   ├── hospital_patient_system.py
│   ├── issues.md
│   ├── reflection.md
│   └── reports/
│       ├── before/
│       │   ├── bandit_report.txt
│       │   ├── flake8_report.txt
│       │   └── pylint_report.txt
│       └── after/
│           ├── bandit_report.txt
│           ├── flake8_report.txt
│           └── pylint_report.txt
├── lab6/
│   ├── README.md
│   ├── photo_print_order.py
│   ├── test_photo_print_order.py
│   ├── CodeCoverageTest_photo_print_order.py
│   ├── BranchCoverageTest_photo_print_order.py
│   ├── Lab_6_Coverage_Analysis_Report.pdf
│   ├── Lab_6_Coverage_Analysis_Report.docx
│   └── screenshots/
│       ├── lab6_step4_initial_line_coverage.png
│       ├── lab6_step4_initial_branch_coverage.png
│       ├── lab6_step5_code_coverage_100.png
│       └── lab6_step7_branch_coverage_100.png
└── lab7/
    ├── README.md
    ├── photo_print_order.py
    ├── test_photo_print_order.py
    ├── Lab_7_Fuzz_Testing_Report.pdf
    ├── Lab_7_Fuzz_Testing_Report.docx
    └── screenshots/
        ├── lab7_step2_buggy_app_run.png
        ├── lab7_step4_hypothesis_fuzz_failures.png
        ├── lab7_step5_fixed_app_run.png
        └── lab7_step6_hypothesis_fuzz_passing.png
```

---

## 🔗 Original Source Repositories

| Lab | Original GitHub Repository |
|:---:|:---|
| Lab 1 | [Remote-Team-Time-Tracking-Project-Approver-SE-Lab-1](https://github.com/rahulsheno/Remote-Team-Time-Tracking-Project-Approver-SE-Lab-1) |
| Lab 2 | [LAB_02_RAHUL_VIVEK_SHENOY_PES2UG2UG24AM129](https://github.com/rahulsheno/LAB_02_RAHUL_VIVEK_SHENOY_PES2UG2UG24AM129) |
| Lab 3 | [LAB_03_RAHUL_VIVEK_SHENOY_PES2UG2UG24AM129](https://github.com/rahulsheno/LAB_03_RAHUL_VIVEK_SHENOY_PES2UG2UG24AM129) |
| Lab 4 | [LAB_04_RAHUL_VIVEK_SHENOY_PES2UG2UG24AM129](https://github.com/rahulsheno/LAB_04_RAHUL_VIVEK_SHENOY_PES2UG2UG24AM129) |
| Lab 5 | [L5_46_RAHUL_VIVEK_SHENOY_PES2UG24AM129](https://github.com/rahulsheno/L5_46_RAHUL_VIVEK_SHENOY_PES2UG24AM129) |
| Lab 6 | [L6_L7_46_photo_print_order](https://github.com/rahulsheno/L6_L7_46_photo_print_order) |
| Lab 7 | [L6_L7_46_photo_print_order](https://github.com/rahulsheno/L6_L7_46_photo_print_order) |
