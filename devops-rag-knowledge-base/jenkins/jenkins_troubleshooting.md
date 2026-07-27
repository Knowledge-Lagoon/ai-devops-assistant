# Jenkins Troubleshooting Starter

## Common troubleshooting areas

### Build failure
Check:
- Console output
- Source code checkout logs
- Build tool errors
- Dependency restore failures

### Agent offline
Check:
- Agent connectivity
- Agent disk space
- Java/runtime availability
- Network connectivity between controller and agent

### Credentials issue
Check:
- Credential ID referenced by job
- Credential scope
- Expired secrets or tokens
- Permission changes

### Plugin issue
Check:
- Recently updated plugins
- Plugin compatibility
- Jenkins version compatibility
- Error messages in system logs

## RAG metadata

- technology: jenkins
- topic: troubleshooting
- doc_type: runbook
- source_type: curated-starter
