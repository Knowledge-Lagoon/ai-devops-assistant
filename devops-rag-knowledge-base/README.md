# AI DevOps Assistant POC - RAG Knowledge Base

This starter knowledge base is structured for a DevOps Assistant proof of concept. It contains curated Markdown documents for Kubernetes, Terraform, and Jenkins, plus configuration files you can use when ingesting content into a vector database.

## Recommended ingestion flow

1. Load all `.md` files from this package.
2. Split files into chunks using the settings in `config/rag_chunking_config.json`.
3. Store chunks in your vector database with metadata from `ingestion_manifest.csv`.
4. Use the `source_url`, `topic`, `technology`, and `doc_type` fields as metadata filters.
5. Add your internal runbooks, SOPs, architecture notes, and troubleshooting guides under `company-specific/`.

## Folder structure

```text
knowledge-base/
├── kubernetes/
├── terraform/
├── jenkins/
├── company-specific/
├── config/
└── sources/
```

## Important note

For production use, replace or extend these starter files with your approved internal documentation and latest official vendor documentation. This package is designed as a clean POC seed dataset, not a complete production knowledge base.
