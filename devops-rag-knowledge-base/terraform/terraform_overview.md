# Terraform Overview

## Purpose
Terraform is an Infrastructure as Code tool. It is used to define, provision, modify, and manage infrastructure using configuration files.

## Core concepts

### Provider
A provider allows Terraform to interact with a platform or service such as Azure, AWS, Kubernetes, or GitHub.

### Resource
A resource represents infrastructure managed by Terraform, such as a virtual machine, storage account, network, or Kubernetes cluster.

### Module
A module is a reusable package of Terraform configuration.

### State
Terraform state tracks the real infrastructure that Terraform manages.

### Plan
`terraform plan` previews the changes Terraform will make.

### Apply
`terraform apply` applies the planned changes.

## Common commands

```bash
terraform init
terraform validate
terraform fmt -recursive
terraform plan
terraform apply
terraform output
terraform state list
```

## RAG metadata

- technology: terraform
- topic: overview
- doc_type: concept
- source_type: curated-starter
