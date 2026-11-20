# Lab 3: Component Modelling & Architectural Pattern Selection

**Problem Statement #46: Remote Team Time-Tracking & Project Approver**  
**Department of Computer Science and Engineering, PES University**  
**Student:** Rahul Vivek Shenoy | **SRN:** PES2UG24AM129 | **Section:** B  

---

## 1. Overview

This laboratory exercise involves designing a structural component model and selecting an appropriate architectural pattern for the **Remote Team Time-Tracking & Project Approver** system, justified against non-functional and domain requirements.

## 2. Key Deliverables & Artifacts

- **Full Report (PDF):** [`PES2UG24AM129_SE_LAB3.pdf`](./PES2UG24AM129_SE_LAB3.pdf)
- **Component Diagram:** Illustrating service boundaries, external adapters, and API interfaces.
- **Architectural Selection:** **Microservices Architecture**

## 3. Microservices Architecture Breakdown

The system is decomposed into five independently deployable and scalable microservices:

1. **Time Entry Service:** Handles daily timesheet inputs, revisions, and persistence.
2. **Approval Workflow Service:** Manages manager review cycles, approval status transitions, and audit trails.
3. **Budget Analytics Service:** Computes real-time project budget burn rates, financial forecasts, and alert thresholds.
4. **Jira Integration Service:** Dedicated integration adapter interfacing with external Jira REST APIs for ticket validation and synchronization.
5. **Notification Service:** Dispatches asynchronous email/in-app notifications for pending approvals, rejections, and budget alerts.

### Interfaces & APIs
- `JiraValidationAPI`
- `TimesheetDataAPI`
- `RecordedHoursAPI`
- `NotificationAPI`
- `ApprovalAPI`
- `BudgetDashboardAPI`

## 4. Architectural Justification Summary

- **Domain-Driven Modularity:** Mirrors the clear business domain boundaries defined in Lab 2. Modifications to approval workflows or business rules do not require redeploying time-entry or analytics modules.
- **Resilient Third-Party Integration:** Encapsulating Jira integration within an isolated service ensures network latency, Jira API rate limits, or downtime never block internal user time logging workflows.
- **Security Advantages:** Strict least-privilege boundary gating; manager-only approval actions (NFR-002) are protected at the Approval Workflow Service, preventing compromised entry-level services from exposing payroll or managerial data.
- **Performance Benefits:** Enables targeted horizontal scaling for the Budget Analytics Service to compute and render metrics within 500 ms (NFR-001) while handling submission peak traffic at week-end cutoffs.
