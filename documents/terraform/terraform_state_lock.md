# Terraform State Lock Failure

Symptoms

- Failed to lock state
- ConditionalCheckFailedException

Root Cause

Another Terraform process currently owns the lock.

Resolution

- Wait for lock release
- Verify no active Terraform jobs
- Remove stale lock if appropriate