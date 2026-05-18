# Process Tampering Activity

## Process Tampering

- KubeArmor cannot directly monitor low-level process tampering events.
- It can partially cover it by monitoring execution of related tools such as `gdb`, `strace`, and `ptrace`-related utilities.
- Audit: `detect-process-access-and-tampering-tools.yaml`
