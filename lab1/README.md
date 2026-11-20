# Remote Team Time-Tracking & Project Approver

**Problem Statement #46 | Developer Tools & IT Operations**
PES University — Dept. of CSE | Lab 1: Requirements Engineering & UML Use-Case Modelling

## 1. Overview

An engineering productivity platform that tracks developer hours against Jira tickets, monitors
project budget burn rates, and facilitates managerial timesheet approval workflows.

## 2. Stakeholders / Actors

| Actor | Description |
|---|---|
| **Remote Developer** | Logs, edits, views, and submits daily timesheets against project tasks. |
| **Engineering Manager** | Reviews, approves, or rejects submitted timesheets and monitors project budget burn. |

## 3. Repository Structure

```
Remote-Team-Time-Tracking/
│
├── README.md
│
├── 01_Requirements/
│   └── Requirements_Table.md      # 5 FRs + 2 NFRs
│
├── 02_UML/
│   └── Use_Case_Diagram.png       # Use-case diagram with <<include>> and <<extend>>
│
└── 03_Use_Case_Flow/
    └── Submit_Timesheet_Flow.md   # Detailed flow spec for core use case
```

## 4. Deliverables Summary

- **Requirements Table** — `01_Requirements/Requirements_Table.md`
  Contains FR-001 to FR-005 and NFR-001 to NFR-002, each with ID, Type, Description, Priority,
  Acceptance Criteria, and Rationale.

- **UML Use-Case Diagram** — `02_UML/Use_Case_Diagram.png`
  Models both actors (Remote Developer, Engineering Manager), all primary use cases, one
  `<<include>>` relationship (Submit Timesheet → Validate Timesheet), and one `<<extend>>`
  relationship (Reject Timesheet → Review Timesheet).

- **Use-Case Flow Specification** — `03_Use_Case_Flow/Submit_Timesheet_Flow.md`
  A detailed flow document for the core use case **"Submit Timesheet"**, covering Preconditions,
  Postconditions, Main Success Scenario, and an Alternate Flow.

## 5. How to Use This Repo

1. Read `01_Requirements/Requirements_Table.md` for the full requirements baseline.
2. Refer to `02_UML/Use_Case_Diagram.png` for the system-level use-case model.
3. Refer to `03_Use_Case_Flow/Submit_Timesheet_Flow.md` for the detailed step-by-step flow of the
   core use case.
