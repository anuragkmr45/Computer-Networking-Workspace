# Capstones — design briefs, not completed deployments

## C1. Follow a request across a hybrid platform
Design a synthetic system with a browser/client, DNS, TLS termination, a load balancer, a service in Kubernetes, and an on-premises dependency. Draw addressing, routing, trust boundaries, and return paths. State unknowns and choose an implementation rather than mixing incompatible packet paths.

**Deliver:** a request trace, routing/policy tables, failure hypotheses, required measurements, and recovery plan. **Evaluate:** correctness, assumptions, observability, least privilege, capacity, cost, and clarity. No paid deployment is required.

## C2. Diagnose an intermittent service incident
The tutor supplies synthetic logs/counters and a topology, with one controlled fault in an isolated lab or paper scenario. Form competing hypotheses before requesting more evidence. Avoid changing several variables at once.

**Deliver:** timeline, test plan, evidence, corrected diagnosis, verification, prevention, and unresolved uncertainty. A guessed correct root cause without evidence is not a successful investigation.

## C3. Automate a safe network change
Create an offline address/configuration validator. Add tests for overlaps, missing routes, overly broad permissions, and rollback metadata. Then design an approval and staged deployment workflow without connecting to production.

**Deliver:** tested code, expected inputs, failure behavior, dry-run diff, invariants, pre/post checks, and rollback procedure. Real device/API access is a separate authorization.

## C4. Principal architecture review
Compare two designs for a hypothetical multi-region or on-premises/cloud service. Include correlated failure risks, capacity assumptions, data movement, operational ownership, security, and a migration plan.

**Deliver:** requirements, alternatives, a decision record, measurable acceptance criteria, and questions you cannot yet answer. This evaluates judgment, not memorization of a preferred vendor architecture.
