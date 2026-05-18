# Scheduled Task Activity

KubeArmor cannot directly monitor scheduled task activity events, but it can partially cover it using file telemetry.

- By auditing file operations in `cron` related dirs.
- policy: `detect-file-operation-in-sensitive-directory.yaml`