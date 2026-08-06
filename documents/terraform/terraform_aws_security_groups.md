# Terraform Security

- Avoid open security groups
- Restrict SSH access
- Encrypt storage
- Use least privilege IAM roles
- Avoid hardcoded secrets

# AWS Security Groups

High Risk Findings

- cidr_blocks = ["0.0.0.0/0"]
- Public SSH access
- Unrestricted ingress

Risk

Opening ingress to 0.0.0.0/0 exposes resources to the public Internet.

Recommended Actions

- Restrict CIDR ranges
- Use VPN access
- Use Bastion Hosts
- Follow least-privilege network access