# User Activity

KubeArmor cannot directly monitor user activity, but it can partially cover it using process execution telemetry.

## User Logon

- Audit: `detect-user-login.yaml`
- Audit: `detect-user-session-activity.yaml`

## User Logoff

- Audit: `detect-user-session-activity.yaml`

## Logon Failed

- KubeArmor cannot directly monitor failed authentication events.
