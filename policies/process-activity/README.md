# Process Activity

## Process Creation

- KubeArmor provides process execution telemetry using `execve` events.
- It can detect and block suspicious process execution.

## Process Termination

- KubeArmor cannot directly monitor process termination events.
- It can partially cover process termination activity by detecting or blocking commonly used process and service termination tools.