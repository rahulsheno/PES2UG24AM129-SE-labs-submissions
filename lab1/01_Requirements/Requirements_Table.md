# Requirements Table — Remote Team Time-Tracking & Project Approver

## Functional Requirements

### FR-001 [Priority: High]
**Description:** The system shall allow developers to log time against specific project tasks
(Jira tickets) and prevent timesheet submissions exceeding 24 hours in a single calendar day.

**Acceptance Criteria:**
- Pass: A valid timesheet entry (≤ 24 hrs/day, linked to a valid Jira ticket) is submitted for
  manager approval.
- Fail: A timesheet entry logging 30 hours in one day is accepted by the system.

**Rationale:** Prevents fraudulent or erroneous time entries and ensures logged hours remain
physically plausible for accurate billing and budget tracking.

---

### FR-002 [Priority: Medium]
**Description:** The system shall allow developers to edit or delete previously logged, unsubmitted
timesheet entries before they are submitted for manager review.

**Acceptance Criteria:**
- Pass: A developer successfully updates the hours/task on a draft (unsubmitted) entry.
- Fail: A developer is able to edit an entry that has already been approved by the manager.

**Rationale:** Developers need flexibility to correct mistakes (wrong task, wrong hours) before
entries are locked for approval, without compromising the integrity of finalized records.

---

### FR-003 [Priority: High]
**Description:** The system shall validate a timesheet (`«include»` Validate Timesheet) — checking
task/ticket validity, daily hour limits, and absence of overlapping entries — before allowing a
developer to submit it for manager review.

**Acceptance Criteria:**
- Pass: A timesheet with valid tasks and no overlapping/duplicate entries is submitted
  successfully.
- Fail: A timesheet referencing a closed or non-existent Jira ticket is submitted without error.

**Rationale:** Guarantees only well-formed timesheets reach the approval queue, reducing manager
workload and preventing invalid data from affecting budget reports.

---

### FR-004 [Priority: High]
**Description:** The system shall allow the Engineering Manager to review a submitted timesheet
and either approve it or reject it with a mandatory comment (`«extend»` Reject Timesheet →
Review Timesheet).

**Acceptance Criteria:**
- Pass: A manager rejects a timesheet and is required to enter a reason before the rejection is
  recorded; the developer is notified.
- Fail: A rejection is recorded without a reason, or the developer is not notified.

**Rationale:** Ensures accountability in the approval workflow and gives developers actionable
feedback when a timesheet is not accepted.

---

### FR-005 [Priority: Medium]
**Description:** The system shall allow the Engineering Manager to view real-time project budget
burn (approved hours converted to cost, plotted against allocated budget) for each project.

**Acceptance Criteria:**
- Pass: The budget burn dashboard reflects newly approved timesheet hours within the defined
  refresh window.
- Fail: Approved hours are not reflected in the budget burn view, or unapproved hours are
  incorrectly included.

**Rationale:** Enables managers to proactively track project spend and take corrective action
before budget overruns occur.

---

## Non-Functional Requirements

### NFR-001 [Type: Performance & Security]
**Description:** Timesheet approval status transitions and project budget burn charts must update
across dashboards within 500 ms, and all timesheet/budget data must be transmitted and stored
using industry-standard encryption.

**Acceptance Criteria:**
- Pass: Benchmarking tests confirm the 500 ms latency target and security standards (e.g.,
  TLS in transit, encryption at rest) under simulated peak load.
- Fail: Dashboard updates exceed 500 ms latency, or data is found to be transmitted/stored
  unencrypted.

**Rationale:** Remote managers rely on near real-time visibility into approvals and budget burn to
make timely decisions; sensitive timesheet/salary-adjacent data must be protected in a distributed,
remote-access environment.

---

### NFR-002 [Type: Availability & Usability]
**Description:** The system shall be accessible via web and mobile clients across time zones with
99.5% monthly uptime, and core actions (log time, submit, approve/reject) shall be completable in
no more than 3 user interactions from the dashboard.

**Acceptance Criteria:**
- Pass: Uptime monitoring logs confirm ≥ 99.5% availability over a rolling 30-day period, and
  usability testing confirms core actions complete within 3 clicks/taps.
- Fail: Monthly uptime falls below 99.5%, or a core action requires more than 3 interactions to
  complete.

**Rationale:** Since the platform serves a distributed remote team working across time zones, high
availability and low-friction interactions are essential to consistent daily adoption.
