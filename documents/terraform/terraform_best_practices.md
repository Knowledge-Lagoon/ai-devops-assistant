# Terraform Best Practices Starter

## Recommended practices

- Use remote state for team collaboration.
- Protect state files because they can contain sensitive information.
- Use modules for reusable infrastructure patterns.
- Run `terraform plan` before `terraform apply`.
- Use variables and outputs clearly.
- Keep environment-specific values separate from reusable modules.
- Use version constraints for providers and modules.

## Suggested metadata for internal Terraform documents

- application_name
- environment
- cloud_provider
- module_name
- owner_team
- last_reviewed_date
- support_contact

## RAG metadata

- technology: terraform
- topic: best-practices
- doc_type: guidance
- source_type: curated-starter
