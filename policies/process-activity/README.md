# Process Activity

## Process Creation

- KubeArmor provides process execution telemetry using `execve` syscall telemetry.
- It can detect and block suspicious process execution.

## Process Termination

- It cannot directly monitor process termination events.
- It can partially cover process termination activity by detecting or blocking commonly used process and service termination tools.
