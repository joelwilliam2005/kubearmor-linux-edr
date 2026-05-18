# User Activity

KubeArmor cannot directly monitor user activity, but it can partially cover it using process execution telemetry.

## User Logon

- by auditing `/usr/bin/login` -> policy: `detect-user-login.yaml`
- by auditing `/run/systemd/sessions/` -> policy: `detect-user-session-activity.yaml`

## User Logoff

- by auditing `.bash_logout` -> policy: `detect-user-session-activity.yaml`

## Logon Failed

- KubeArmor cannot directly monitor failed authentication events.
