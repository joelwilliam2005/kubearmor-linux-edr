# Script Activity

- KubeArmor cannot directly inspect script contents and selectively block malicious scripts.
- It can detect and block script execution using process execution telemetry from specified directories.

- Audit: `detect-script-exec-in-directory.yaml`
- Block: `block-script-exec-in-directory.yaml`
