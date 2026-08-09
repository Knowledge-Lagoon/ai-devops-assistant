# Terraform IAM Permission Failure

Symptoms

- AccessDenied
- UnauthorizedOperation

Root Cause

Terraform execution role lacks required permissions.

Resolution

- Review IAM policies
- Grant required permissions
- Re-run terraform apply