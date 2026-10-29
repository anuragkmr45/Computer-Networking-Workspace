# Platform lab backlog — specifications, not completed runnable deployments

## Docker: trace a request across a user-defined network
Prerequisites: M07 basics and an approved disposable runtime. Later create two minimal services, inspect addresses/routes, predict bridge/namespace behavior, test permitted connectivity, then remove only lab resources. Confirm the actual runtime platform; desktop VMs change the host view. Images, downloads, and version-specific commands must be approved and verified before use.

## Kubernetes: diagnose Service-to-Pod connectivity
Prerequisites: container model, routing, DNS, and policy. Use a disposable local cluster after checking version, CNI, and service implementation. Predict DNS -> Service -> endpoint -> Pod and return path. Introduce one controlled fault, collect evidence, repair it, and verify cleanup. Do not assume all clusters use the same packet path or NetworkPolicy behavior. Source entry point: K8S-NETWORK.

## AWS: hybrid path review before deployment
Start design-only: synthetic VPC/on-premises CIDRs, route tables, security boundaries, DNS, return path, failure domain, and cost assumptions. Later paid execution needs account approval, region, budgets, tags, resource inventory, and teardown verification. No cloud credentials or Terraform apply are included. Sources: AWS-VPC and AWS-ANS.

## Routing: small multi-router experiment
Choose an approved emulator or isolated routing-container environment after fundamentals. Pin platform/version, trace route advertisements versus forwarding, apply one fault, and compare predicted/observed convergence. Vendor configurations must be checked against the actual image and license.
