# File Manipulation

KubeArmor can detect and block file manipulation activity using file syscall telemetry such as `openat`.

## File Creation

- syscall flags: `O_CREAT`

## File Modification

- syscall flags: `O_WRONLY`, `O_RDWR`, `O_TRUNC`

## File Deletion

- syscalls: `unlink`, `unlinkat`
