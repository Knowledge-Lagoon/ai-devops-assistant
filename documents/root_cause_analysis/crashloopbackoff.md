# Root Cause Analysis - CrashLoopBackOff

Symptoms

- CrashLoopBackOff
- Back-off restarting failed container
- Exit Code 1

Root Cause

The application process exits immediately after startup.

Common Causes

- Invalid startup command
- Missing environment variables
- Configuration errors
- Database connection failures

Resolution

- Check container logs
- Verify startup command
- Review environment variables
- Validate configuration