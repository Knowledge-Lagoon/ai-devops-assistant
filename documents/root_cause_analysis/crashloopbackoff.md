# Root Cause Analysis - CrashLoopBackOff

## Symptoms

- Pod status shows CrashLoopBackOff
- Container repeatedly restarts
- Kubernetes events show Back-off restarting failed container
- Container may terminate with Exit Code 1

## Common Root Causes

- Application startup failure
- Invalid container command
- Missing environment variables
- Configuration errors
- Database connection failure
- Application dependency unavailable

## Recommended Checks

- Run kubectl describe pod
- Run kubectl logs --previous
- Check container command and arguments
- Check environment variables
- Check ConfigMaps and Secrets
- Check application dependencies

## Recommended Resolution

- Fix the application startup error
- Correct missing or invalid configuration
- Validate dependency connectivity
- Redeploy the workload