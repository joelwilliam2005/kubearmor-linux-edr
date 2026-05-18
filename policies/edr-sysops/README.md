# EDR SysOps Activity

## Agent Start
KubeArmor cannot directly monitor agent startup events. We'll have to use other commands like systemctl for it.

## Agent Stop

- It can partially cover agent stop and tampering activity by auditing/blocking modifications to KubeArmor binary and service files.

- Audit: `detect-kubearmor-binary-tamper.yaml`
- Audit: `detect-kubearmor-service-tamper.yaml`

- Block: `block-kubearmor-binary-tamper.yaml`
- Block: `block-kubearmor-service-tamper.yaml`
