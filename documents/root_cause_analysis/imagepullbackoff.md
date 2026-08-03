# Root Cause Analysis - ImagePullBackOff

Symptoms

- ImagePullBackOff
- ErrImagePull
- Failed to pull image

Root Cause

Container image cannot be downloaded from the registry.

Common Causes

- Invalid image tag
- Wrong image name
- Registry authentication issues

Resolution

- Verify image name
- Verify image tag
- Verify image exists in registry
- Check image pull secrets