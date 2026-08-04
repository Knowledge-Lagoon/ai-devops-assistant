# Root Cause Analysis - ImagePullBackOff

## Symptoms

- Pod status shows ImagePullBackOff
- Events show ErrImagePull
- Events show failed to pull image
- Events show image not found or unauthorized

## Common Root Causes

- Invalid image name
- Invalid image tag
- Image does not exist in registry
- Missing image pull secret
- Registry authentication failure

## Recommended Checks

- Verify image name
- Verify image tag
- Confirm image exists in the registry
- Check imagePullSecrets
- Check registry permissions

## Recommended Resolution

- Update deployment with a valid image reference
- Push the missing image to the registry
- Configure imagePullSecrets if using a private registry
- Redeploy the workload