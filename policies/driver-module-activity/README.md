# Driver / Module Activity

KubeArmor cannot directly monitor kernel driver/module activity, it can partially cover it by auditing/blocking related process execution.

- Audit: `detect-kernel-module-tools.yaml`
- Block: `block-kernel-module-tools.yaml`
