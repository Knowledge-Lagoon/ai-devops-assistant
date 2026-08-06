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
- Security group exposure
- Open ingress rule
- Unrestricted access
- Public internet access

Risk Level

High

Recommendations

- Restrict CIDR ranges
- Use VPN access
- Use Bastion Hosts