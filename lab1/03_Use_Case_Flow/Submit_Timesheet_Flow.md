# Use-Case Flow Specification

## Use Case: Submit Timesheet

**Primary Actor:** Remote Developer
**Secondary Actor:** Engineering Manager (receives the submission for review)
**Related Use Case:** `«include»` Validate Timesheet

---

### Brief Description
This use case describes how a Remote Developer submits a completed timesheet, which the system
automatically validates before routing it to the Engineering Manager for review.

---

### Preconditions
1. The Remote Developer is authenticated and logged into the system.
2. The developer has at least one draft (unsubmitted) timesheet entry with logged hours against a
   valid project task/Jira ticket.
3. The timesheet has not already been submitted, approved, or rejected in this cycle.

---

### Postconditions

**Success Postcondition:**
- The timesheet status changes to "Submitted — Pending Review."
- The Engineering Manager is notified that a timesheet is awaiting review.
- The timesheet entries become locked (read-only) for the developer until reviewed.

**Failure Postcondition:**
- The timesheet remains in "Draft" status.
- The developer is shown a validation error explaining what must be corrected.

---

### Main Success Scenario
1. The Remote Developer navigates to the timesheet dashboard and selects a draft timesheet.
2. The developer reviews the logged entries and selects "Submit Timesheet."
3. The system triggers the included **Validate Timesheet** use case:
   a. Confirms total hours per day do not exceed 24 hours.
   b. Confirms each entry references a valid, open project task/Jira ticket.
   c. Confirms there are no overlapping or duplicate time entries.
4. Validation succeeds; the system changes the timesheet status to "Submitted — Pending Review."
5. The system locks the timesheet entries from further edits by the developer.
6. The system sends a notification to the Engineering Manager that a new timesheet is awaiting
   review.
7. The system displays a confirmation message to the developer.

---

### Alternate Flow: Validation Failure

**Trigger:** At step 3, the Validate Timesheet check fails (e.g., a day's total exceeds 24 hours,
or an entry references a closed/invalid task).

1. The system halts the submission process and does **not** change the timesheet status.
2. The system displays a specific validation error message identifying the problematic entry
   (e.g., "Day exceeds 24-hour limit" or "Task TICKET-123 is closed").
3. The developer is returned to the editable draft timesheet view.
4. The developer corrects the flagged entry (e.g., adjusts hours or reassigns the task).
5. The developer selects "Submit Timesheet" again, re-triggering the Main Success Scenario from
   step 3.

**Resulting Postcondition:** The timesheet remains in "Draft" status until it passes validation and
is successfully submitted.

---

### Special Requirements
- Validation (step 3) must complete and return a result to the developer within 500 ms, per
  NFR-001.
- Rejection/error messages must clearly state which rule was violated and, where possible, which
  specific entry caused it.

### Frequency of Use
Expected daily, at the end of each developer's working day or on a periodic (e.g., weekly) cadence
depending on team policy.
