# KEDR
## KubeArmor based Linux EDR (Endpoint Detection and Response) Solution

### Support Table -
| Telemetry Feature Category | Sub-Category | KubeArmor Support Status |
|---|---|---|
| [Process Activity](./policies/process-activity/README.md)| Process Creation | Full |
|  | Process Termination | Partial |
| [File Manipulation](./policies/file-manipulation/README.md) | File Creation | Full |
|  | File Modification | Full |
|  | File Deletion | Full |
|  | File Rename | Partial |
| [User Activity](./policies/user-activity/README.md) | User Logon | Partial |
|  | User Logoff | Partial |
|  | Logon Failed | No |
| [Script Activity](./policies/script-activity/README.md) | Script Content | Partial |
| [Network Activity](./policies/network-activity/README.md) | Network Connection | Full |
|  | Network Socket Listen | Partial |
|  | DNS Query | Partial | 
| [Scheduled Task Activity](./policies/scheduled-task-activity/README.md) | Scheduled Task | Partial |
| [User Account Activity](./policies/user-account-activity/README.md) | User Account Created | Partial |
|  | User Account Modified | Partial |
|  | User Account Deleted | Partial |
| [Driver/Module Activity](./policies/driver-module-activity/README.md) | Driver Load | Partial |
| [Access Activity](./policies/access-activity/README.md) | Raw Access Read | Partial |
|  | Process Access | Partial |
| [Process Tampering Activity](./policies/process-tampering-activity/README.md) | Process Tampering | Partial |
| [Service Activity](./policies/service-activity/README.md) | Service Creation | Full |
|  | Service Modification | Full |
|  | Service Deletion | Full |
| [EDR SysOps](./policies/edr-sysops/README.md) | Agent Start | No |
|  | Agent Stop | Partial |
| Hash Algorithms | MD5 | No |
|  | SHA | No |
|  | Fuzzy Hash | No |

### Benchmark Tests using ttp-bench
Tested KEDR against multiple Linux attack simulations from the MITRE ATT&CK framework using [ttp-bench](https://github.com/tstromberg/ttp-bench):
- [evade-shell-history](./ttp-bench-results/evade-shell-history.md)
- [evade-tools-in-var-tmp](./ttp-bench-results/evade-tools-in-var-tmp-hidden.md)
- [exec-bash-reverse-shell](./ttp-bench-results/exec-bash-reverse-shell.md)
- [exec-curl-to-hidden-url](./ttp-bench-results/exec-curl-to-hidden-url.md)
- [exec-linpeas](./ttp-bench-results/exec-linpeas.md)
- [exec-netcat-listen](./ttp-bench-results/exec-netcat-listen.md)
- [exec-python-reverse-shell](./ttp-bench-results/exec-python-reverse-shell.md)

## Installation

- Tested on Ubuntu 22.04 VM
- BPF-LSM enabled.
- Script installs: KubeArmor(systemd mode) + karmor CLI + KEDR
  
`curl -sfL https://raw.githubusercontent.com/joelwilliam2005/kubearmor-linux-edr/main/install.sh | sudo sh`

## Activate BPF-LSM
- Edit: `/etc/default/grub`
- Find line: `GRUB_CMDLINE_LINUX=""`
- Change to: `GRUB_CMDLINE_LINUX="lsm=lockdown,capability,landlock,yama,apparmor,bpf"`
- `sudo update-grub`
- `sudo reboot`
- Verify: `cat /sys/kernel/security/lsm` and `sudo karmor probe`
      
