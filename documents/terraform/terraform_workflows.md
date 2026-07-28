# Terraform Common Workflows

## Initial setup

```bash
git clone <repo-url>
cd <repo>/terraform
terraform init
terraform validate
terraform fmt -recursive
```

## Preview infrastructure changes

```bash
terraform plan
```

## Apply changes

```bash
terraform apply
```

## Inspect state

```bash
terraform state list
terraform state show <resource-address>
terraform output
```

## Troubleshooting checklist

- Run `terraform validate` to check configuration syntax.
- Run `terraform fmt -check -recursive` to check formatting.
- Confirm provider authentication.
- Confirm backend configuration.
- Review state locking errors.
- Compare Terraform state with actual cloud resources.

## RAG metadata

- technology: terraform
- topic: workflows
- doc_type: runbook
- source_type: curated-starter
