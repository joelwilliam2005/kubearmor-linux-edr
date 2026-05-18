# Access Activity

## Raw Access Read

- KubeArmor cannot directly monitor Direct disk access if done by bypassing file system controls.

- It can partially cover disk activity using file syscall telemetry and sensitive file access monitoring.

- Audit: `detect-file-operation-in-sensitive-directory.yaml`
- Audit: `detect-operation-on-sensitive-files.yaml`

## Process Access

- It can monitor low level processes. However there is a large number of internal processes interactions happening constantly in Linux, that make suspicious process access detection very hard.

- Partial process access activity can be covered by monitoring execution of related tools.

- Audit: `detect-process-access-and-tampering-tools.yaml`