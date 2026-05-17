# exec-linpeas

Downloads and launches LinPEAS



Policies that can be used to protect against this attack:

- Audit: `detect-shell-execution.yaml`
- Audit: `detect-script-exec-in-directory.yaml`

- Block: `block-script-exec-in-directory.yaml`

Shell Execution Detected:

```

joelw@jw-ubuntu-server-vm:~/ttp-bench$ sudo go run . 
Building 1 selected simulations ...
2026/05/17 07:39:26 #0: build failed: exit status 1
error obtaining VCS status: fork/exec /usr/bin/git: permission denied
	Use -buildvcs=false to disable VCS stamping.
Executing 1 selected simulations ...
                                                                                                      
    [1 of 1] exec-linpeas at 2026-05-17 07:39:26.923                                                  
    Downloads and launches LinPEAS                                                                    
2026/05/17 07:39:26 executing [./exec-linpeas]
2026/05/17 07:39:26 Downloading https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh to /tmp ...
2026/05/17 07:40:44 running ./linpeas.sh -s ... (timeout=1m30s)



                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |
    |---------------------------------------------------------------------------------|
    |         Linux PE & Hardening    :     https://hacktricks-training.com/courses/lhe/ |
    |         Learn Cloud Hacking       :     https://training.hacktricks.xyz         |
    |         Follow on Twitter         :     @hacktricks_live                        |
    |         Respect on HTB            :     SirBroccoli                             |
    |---------------------------------------------------------------------------------|
    |                                 Thank you!                                      |
    \---------------------------------------------------------------------------------/
          LinPEAS-ng by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.wiki/en/linux-hardening/linux-privilege-escalation-checklist.html
Best Linux PE & Hardening course: https://hacktricks-training.com/courses/lhe/
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You should take a look into it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

  YOU ARE ALREADY ROOT!!! (it could take longer to complete execution)

 Starting LinPEAS. Caching Writable Folders...
                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════
                               ╚═══════════════════╝
OS: Linux version 5.15.0-177-generic (buildd@lcy02-amd64-099) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #187-Ubuntu SMP Sat Apr 11 22:54:33 UTC 2026
User & Groups: uid=0(root) gid=0(root) groups=0(root)
Hostname: jw-ubuntu-server-vm

[+] /usr/bin/ping is available for network discovery (LinPEAS can discover hosts, learn more with -h)
[+] /usr/bin/bash is available for network discovery, port scanning and port forwarding (LinPEAS can discover hosts, scan ports, and forward ports. Learn more with -h)
[+] /usr/bin/nc is available for network discovery & port scanning (LinPEAS can discover hosts and scan ports, learn more with -h)


Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE

                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════
                              ╚════════════════════╝
╔══════════╣ Operative system (T1082)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#kernel-exploits
Linux version 5.15.0-177-generic (buildd@lcy02-amd64-099) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #187-Ubuntu SMP Sat Apr 11 22:54:33 UTC 2026
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.5 LTS
Release:	22.04
Codename:	jammy

╔══════════╣ Sudo version (T1548.003,T1068)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-version
Sudo version 1.9.9


╔══════════╣ PATH (T1574.007)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#writable-path-abuses

╔══════════╣ Date & uptime (T1082)
Sun May 17 07:40:55 UTC 2026
 07:40:55 up 22:29,  5 users,  load average: 0.31, 0.07, 0.07

╔══════════╣ Unmounted file-system? (T1082,T1120)
╚ Check if you can mount umounted devices
/dev/disk/by-uuid/dae80da8-6fc9-499f-a5c3-5cd87f022162 / ext4 defaults 0 1
/swap.img	none	swap	sw	0	0

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20) (T1082)
disk

╔══════════╣ Environment (T1082,T1552.007)
╚ Any private information inside environment variables?
SUDO_GID=1000
MAIL=/var/mail/root
USER=root
HOME=/root
SUDO_UID=1000
LOGNAME=root
TERM=xterm-256color
LANG=C.UTF-8
SUDO_COMMAND=/usr/bin/go run .
SHELL=/bin/bash
SUDO_USER=joelw
PWD=/tmp

╔══════════╣ Searching Signature verification failed in dmesg (T1082)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#dmesg-signature-verification-failed
dmesg Not Found

╔══════════╣ Protections (T1518.001)
═╣ AppArmor enabled? .............. apparmor module is loaded.
27 profiles are loaded.
27 profiles are in enforce mode.
   /snap/snapd/26865/usr/lib/snapd/snap-confine
   /usr/lib/NetworkManager/nm-dhcp-client.action
   /usr/lib/NetworkManager/nm-dhcp-helper
   /usr/lib/connman/scripts/dhclient-script
   /usr/lib/snapd/snap-confine
   /usr/lib/snapd/snap-confine//mount-namespace-capture-helper
   /{,usr/}sbin/dhclient
   lsb_release
   nvidia_modprobe
   nvidia_modprobe//kmod
   snap-update-ns.lxd
   snap.lxd.activate
   snap.lxd.buginfo
   snap.lxd.check-kernel
   snap.lxd.daemon
   snap.lxd.hook.configure
   snap.lxd.hook.connect-plug-ceph-conf
   snap.lxd.hook.connect-plug-ovn-certificates
   snap.lxd.hook.connect-plug-ovn-chassis
   snap.lxd.hook.disconnect-plug-ceph-conf
   snap.lxd.hook.disconnect-plug-ovn-certificates
   snap.lxd.hook.disconnect-plug-ovn-chassis
   snap.lxd.hook.install
   snap.lxd.hook.remove
   snap.lxd.lxc
   snap.lxd.lxd
   snap.lxd.user-daemon
0 profiles are in complain mode.
0 profiles are in kill mode.
0 profiles are in unconfined mode.
0 processes have profiles defined.
0 processes are in enforce mode.
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
0 processes are in mixed mode.
0 processes are in kill mode.
═╣ AppArmor profile? .............. unconfined
═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found
═╣ Execshield enabled? ............ Execshield Not Found
═╣ SELinux enabled? ............... sestatus Not Found
═╣ Seccomp enabled? ............... disabled
═╣ User namespace? ................ enabled
═╣ unpriv_userns_clone? ........... 1
═╣ unpriv_bpf_disabled? ........... 2
═╣ Cgroup2 enabled? ............... enabled
═╣ kptr_restrict? ................. 1
═╣ dmesg_restrict? ................ 1
═╣ ptrace_scope? .................. 1
═╣ protected_symlinks? ............ 1
═╣ protected_hardlinks? ........... 1
═╣ perf_event_paranoid? ........... 4
═╣ mmap_min_addr? ................. 65536
═╣ lockdown mode? ................. [none] integrity confidentiality
═╣ Kernel hardening flags? ........ CONFIG_SLAB_FREELIST_RANDOM=y
CONFIG_SLAB_FREELIST_HARDENED=y
CONFIG_RANDOMIZE_BASE=y
CONFIG_STACKPROTECTOR=y
CONFIG_STACKPROTECTOR_STRONG=y
# CONFIG_KASAN is not set
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (kvm)

╔══════════╣ Kernel Modules Information (T1547.006)
══╣ Kernel modules with weak perms? (T1547.006)

══╣ Kernel modules loadable?  (T1547.006)
Modules can be loaded
══╣ Module signature enforcement?  (T1547.006)
Not enforced

╔══════════╣ Checking for Copy Fail (CVE-2026-31431) (T1068)
╚ https://copy.fail/
╚ https://www.cve.org/CVERecord?id=CVE-2026-31431
NOT VULNERABLE: AF_ALG/authencesn is not reachable from this context (No such file or directory)

╔══════════╣ Kernel Exploit Registry (T1068)
═╣ Operating system ............. Linux
═╣ Kernel release ............... 5.15.0-177-generic
═╣ Comparable version ........... 5.15.0.177
═╣ Data chunk limit ............. max 25 rows per KERNEL_CVE_DATA_* variable (1..21)
═╣ Kernel config source ......... /boot/config-5.15.0-177-generic
CVE: CVE-2022-0847 | Name: DirtyPipe | Match data: pkg=linux-kernel,ver>=5.8,ver<=5.16.11 | Tags: ubuntu=(20.04|21.04),debian=11 | Rank: 1
CVE: CVE-2022-0995 | Name: watch_queue | Match data: pkg=linux-kernel,ver>=5.8,ver<5.16.5,x86_64 | Tags: ubuntu=21.10{kernel:5.13.0.37-generic} | Rank: 1 | Details: Not 100% reliable, may need to be run a couple of times. It rare cases it may panic the kernel.
CVE: CVE-2022-2586 | Name: nft_object UAF | Match data: pkg=linux-kernel,ver>=5.12,ver<5.19,CONFIG_USER_NS=y,sysctl:kernel.unprivileged_userns_clone==1 | Tags: ubuntu=(20.04){kernel:5.12.13} | Rank: 1 | Details: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)
CVE: CVE-2022-32250 | Name: nft_object UAF (NFT_MSG_NEWSET) | Match data: pkg=linux-kernel,ver<5.18.1,CONFIG_USER_NS=y,sysctl:kernel.unprivileged_userns_clone==1 | Tags: ubuntu=(22.04){kernel:5.15.0-27-generic} | Rank: 1 | Details: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)
CVE: CVE-2023-0386 | Name: OverlayFS suid smuggle | Match data: pkg=linux-kernel,ver>=5.11,ver<=6.2,CONFIG_USER_NS=y,sysctl:kernel.unprivileged_userns_clone==1 | Tags: ubuntu=22.04.1{kernel:5.15.0-57-generic} | Rank: 1 | Details: CONFIG_USER_NS needs to be enabled && kernel.unprivileged_userns_clone=1 required
═╣ Kernel vulns found: 5

╔══════════╣ Checking for Dirty Frag (CVE-2026-43284 / CVE-2026-43500) (T1068)
╚ https://ubuntu.com/blog/dirty-frag-linux-vulnerability-fixes-available
╚ https://www.cve.org/CVERecord?id=CVE-2026-43284
╚ https://www.cve.org/CVERecord?id=CVE-2026-43500
CVE-2026-43284 (xfrm-ESP): autoloadable: esp4 esp6 xfrm_user ipcomp6
CVE-2026-43500 (rxrpc): autoloadable: rxrpc
modprobe mitigation (xfrm-ESP): not found
modprobe mitigation (rxrpc): not found
Unprivileged user namespaces: enabled
Current process: CAP_NET_ADMIN present (matches public PoC requirement)
Kernel build predates upstream fix (2026-05-08): likely unpatched unless distro backport.
LIKELY VULNERABLE to CVE-2026-43284 (xfrm-ESP).
LIKELY VULNERABLE to CVE-2026-43500 (rxrpc).
Mitigation: 'install esp4/esp6/rxrpc /bin/false' in /etc/modprobe.d/, then rmmod;
or sysctl kernel.unprivileged_userns_clone=0; or apply distro patches.



                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════
                                   ╚═══════════╝
╔══════════╣ Container related tools present (if any): (T1613)
/usr/sbin/lxc
/usr/sbin/apparmor_parser
/usr/bin/nsenter
/usr/bin/unshare
/usr/sbin/chroot
/usr/sbin/capsh
/usr/sbin/setcap
/usr/sbin/getcap

╔══════════╣ Container details (T1613,T1611)
═╣ Is this a container? ........... No
═╣ LXC version ................ Client version: 5.21.4 LTS
Server version: 5.21.4 LTS
═╣ LXC info ................... config: {}
api_extensions:
- storage_zfs_remove_snapshots
- container_host_shutdown_timeout
- container_stop_priority
- container_syscall_filtering
- auth_pki
- container_last_used_at
- etag
- patch
- usb_devices
- https_allowed_credentials
- image_compression_algorithm
- directory_manipulation
- container_cpu_time
- storage_zfs_use_refquota
- storage_lvm_mount_options
- network
- profile_usedby
- container_push
- container_exec_recording
- certificate_update
- container_exec_signal_handling
- gpu_devices
- container_image_properties
- migration_progress
- id_map
- network_firewall_filtering
- network_routes
- storage
- file_delete
- file_append
- network_dhcp_expiry
- storage_lvm_vg_rename
- storage_lvm_thinpool_rename
- network_vlan
- image_create_aliases
- container_stateless_copy
- container_only_migration
- storage_zfs_clone_copy
- unix_device_rename
- storage_lvm_use_thinpool
- storage_rsync_bwlimit
- network_vxlan_interface
- storage_btrfs_mount_options
- entity_description
- image_force_refresh
- storage_lvm_lv_resizing
- id_map_base
- file_symlinks
- container_push_target
- network_vlan_physical
- storage_images_delete
- container_edit_metadata
- container_snapshot_stateful_migration
- storage_driver_ceph
- storage_ceph_user_name
- resource_limits
- storage_volatile_initial_source
- storage_ceph_force_osd_reuse
- storage_block_filesystem_btrfs
- resources
- kernel_limits
- storage_api_volume_rename
- network_sriov
- console
- restrict_devlxd
- migration_pre_copy
- infiniband
- maas_network
- devlxd_events
- proxy
- network_dhcp_gateway
- file_get_symlink
- network_leases
- unix_device_hotplug
- storage_api_local_volume_handling
- operation_description
- clustering
- event_lifecycle
- storage_api_remote_volume_handling
- nvidia_runtime
- container_mount_propagation
- container_backup
- devlxd_images
- container_local_cross_pool_handling
- proxy_unix
- proxy_udp
- clustering_join
- proxy_tcp_udp_multi_port_handling
- network_state
- proxy_unix_dac_properties
- container_protection_delete
- unix_priv_drop
- pprof_http
- proxy_haproxy_protocol
- network_hwaddr
- proxy_nat
- network_nat_order
- container_full
- backup_compression
- nvidia_runtime_config
- storage_api_volume_snapshots
- storage_unmapped
- projects
- network_vxlan_ttl
- container_incremental_copy
- usb_optional_vendorid
- snapshot_scheduling
- snapshot_schedule_aliases
- container_copy_project
- clustering_server_address
- clustering_image_replication
- container_protection_shift
- snapshot_expiry
- container_backup_override_pool
- snapshot_expiry_creation
- network_leases_location
- resources_cpu_socket
- resources_gpu
- resources_numa
- kernel_features
- id_map_current
- event_location
- storage_api_remote_volume_snapshots
- network_nat_address
- container_nic_routes
- cluster_internal_copy
- seccomp_notify
- lxc_features
- container_nic_ipvlan
- network_vlan_sriov
- storage_cephfs
- container_nic_ipfilter
- resources_v2
- container_exec_user_group_cwd
- container_syscall_intercept
- container_disk_shift
- storage_shifted
- resources_infiniband
- daemon_storage
- instances
- image_types
- resources_disk_sata
- clustering_roles
- images_expiry
- resources_network_firmware
- backup_compression_algorithm
- ceph_data_pool_name
- container_syscall_intercept_mount
- compression_squashfs
- container_raw_mount
- container_nic_routed
- container_syscall_intercept_mount_fuse
- container_disk_ceph
- virtual-machines
- image_profiles
- clustering_architecture
- resources_disk_id
- storage_lvm_stripes
- vm_boot_priority
- unix_hotplug_devices
- api_filtering
- instance_nic_network
- clustering_sizing
- firewall_driver
- projects_limits
- container_syscall_intercept_hugetlbfs
- limits_hugepages
- container_nic_routed_gateway
- projects_restrictions
- custom_volume_snapshot_expiry
- volume_snapshot_scheduling
- trust_ca_certificates
- snapshot_disk_usage
- clustering_edit_roles
- container_nic_routed_host_address
- container_nic_ipvlan_gateway
- resources_usb_pci
- resources_cpu_threads_numa
- resources_cpu_core_die
- api_os
- container_nic_routed_host_table
- container_nic_ipvlan_host_table
- container_nic_ipvlan_mode
- resources_system
- images_push_relay
- network_dns_search
- container_nic_routed_limits
- instance_nic_bridged_vlan
- network_state_bond_bridge
- usedby_consistency
- custom_block_volumes
- clustering_failure_domains
- resources_gpu_mdev
- console_vga_type
- projects_limits_disk
- network_type_macvlan
- network_type_sriov
- container_syscall_intercept_bpf_devices
- network_type_ovn
- projects_networks
- projects_networks_restricted_uplinks
- custom_volume_backup
- backup_override_name
- storage_rsync_compression
- network_type_physical
- network_ovn_external_subnets
- network_ovn_nat
- network_ovn_external_routes_remove
- tpm_device_type
- storage_zfs_clone_copy_rebase
- gpu_mdev
- resources_pci_iommu
- resources_network_usb
- resources_disk_address
- network_physical_ovn_ingress_mode
- network_ovn_dhcp
- network_physical_routes_anycast
- projects_limits_instances
- network_state_vlan
- instance_nic_bridged_port_isolation
- instance_bulk_state_change
- network_gvrp
- instance_pool_move
- gpu_sriov
- pci_device_type
- storage_volume_state
- network_acl
- migration_stateful
- disk_state_quota
- storage_ceph_features
- projects_compression
- projects_images_remote_cache_expiry
- certificate_project
- network_ovn_acl
- projects_images_auto_update
- projects_restricted_cluster_target
- images_default_architecture
- network_ovn_acl_defaults
- gpu_mig
- project_usage
- network_bridge_acl
- warnings
- projects_restricted_backups_and_snapshots
- clustering_join_token
- clustering_description
- server_trusted_proxy
- clustering_update_cert
- storage_api_project
- server_instance_driver_operational
- server_supported_storage_drivers
- event_lifecycle_requestor_address
- resources_gpu_usb
- clustering_evacuation
- network_ovn_nat_address
- network_bgp
- network_forward
- custom_volume_refresh
- network_counters_errors_dropped
- metrics
- image_source_project
- clustering_config
- network_peer
- linux_sysctl
- network_dns
- ovn_nic_acceleration
- certificate_self_renewal
- instance_project_move
- storage_volume_project_move
- cloud_init
- network_dns_nat
- database_leader
- instance_all_projects
- clustering_groups
- ceph_rbd_du
- instance_get_full
- qemu_metrics
- gpu_mig_uuid
- event_project
- clustering_evacuation_live
- instance_allow_inconsistent_copy
- network_state_ovn
- storage_volume_api_filtering
- image_restrictions
- storage_zfs_export
- network_dns_records
- storage_zfs_reserve_space
- network_acl_log
- storage_zfs_blocksize
- metrics_cpu_seconds
- instance_snapshot_never
- certificate_token
- instance_nic_routed_neighbor_probe
- event_hub
- agent_nic_config
- projects_restricted_intercept
- metrics_authentication
- images_target_project
- cluster_migration_inconsistent_copy
- cluster_ovn_chassis
- container_syscall_intercept_sched_setscheduler
- storage_lvm_thinpool_metadata_size
- storage_volume_state_total
- instance_file_head
- instances_nic_host_name
- image_copy_profile
- container_syscall_intercept_sysinfo
- clustering_evacuation_mode
- resources_pci_vpd
- qemu_raw_conf
- storage_cephfs_fscache
- network_load_balancer
- vsock_api
- instance_ready_state
- network_bgp_holdtime
- storage_volumes_all_projects
- metrics_memory_oom_total
- storage_buckets
- storage_buckets_create_credentials
- metrics_cpu_effective_total
- projects_networks_restricted_access
- storage_buckets_local
- loki
- acme
- internal_metrics
- cluster_join_token_expiry
- remote_token_expiry
- init_preseed
- storage_volumes_created_at
- cpu_hotplug
- projects_networks_zones
- network_txqueuelen
- cluster_member_state
- instances_placement_scriptlet
- storage_pool_source_wipe
- zfs_block_mode
- instance_generation_id
- disk_io_cache
- amd_sev
- storage_pool_loop_resize
- migration_vm_live
- ovn_nic_nesting
- oidc
- network_ovn_l3only
- ovn_nic_acceleration_vdpa
- cluster_healing
- instances_state_total
- auth_user
- security_csm
- instances_rebuild
- numa_cpu_placement
- custom_volume_iso
- network_allocations
- storage_api_remote_volume_snapshot_copy
- zfs_delegate
- operations_get_query_all_projects
- metadata_configuration
- syslog_socket
- event_lifecycle_name_and_project
- instances_nic_limits_priority
- disk_initial_volume_configuration
- operation_wait
- cluster_internal_custom_volume_copy
- disk_io_bus
- storage_cephfs_create_missing
- instance_move_config
- ovn_ssl_config
- init_preseed_storage_volumes
- metrics_instances_count
- server_instance_type_info
- resources_disk_mounted
- server_version_lts
- oidc_groups_claim
- loki_config_instance
- storage_volatile_uuid
- import_instance_devices
- instances_uefi_vars
- instances_migration_stateful
- container_syscall_filtering_allow_deny_syntax
- access_management
- vm_disk_io_limits
- storage_volumes_all
- instances_files_modify_permissions
- image_restriction_nesting
- container_syscall_intercept_finit_module
- device_usb_serial
- network_allocate_external_ips
- explicit_trust_token
- instance_import_conversion
- instance_create_start
- devlxd_images_vm
- instance_protection_start
- disk_io_bus_virtio_blk
- metadata_configuration_entity_types
- network_allocations_ovn_uplink
- network_ovn_uplink_vlan
- shared_custom_block_volumes
- metrics_api_requests
- projects_limits_disk_pool
- access_management_tls
- state_logical_cpus
- vm_limits_cpu_pin_strategy
- gpu_cdi
- metadata_configuration_scope
- unix_device_hotplug_ownership_inherit
- unix_device_hotplug_subsystem_device_option
- storage_ceph_osd_pool_size
- network_get_target
- network_zones_all_projects
- vm_root_volume_attachment
- projects_limits_uplink_ips
- entities_with_entitlements
- profiles_all_projects
- storage_driver_powerflex
- storage_driver_pure
- cloud_init_ssh_keys
- oidc_scopes
- project_default_network_and_storage
- ubuntu_pro_guest_attach
- images_all_projects
- client_cert_presence
- resources_device_fs_uuid
- clustering_groups_used_by
- container_bpf_delegation
- override_snapshot_profiles_on_copy
- backup_metadata_version
- storage_buckets_all_projects
- network_acls_all_projects
- networks_all_projects
- clustering_restore_skip_mode
- disk_io_threads_virtiofsd
- oidc_client_secret
- pci_hotplug
- device_patch_removal
api_status: stable
api_version: "1.0"
auth: trusted
public: false
auth_methods:
- tls
client_certificate: false
auth_user_name: root
auth_user_method: unix
environment:
  addresses: []
  architectures:
  - x86_64
  - i686
  backup_metadata_version_range:
  - 1
  - 2
  certificate: |
    -----BEGIN CERTIFICATE-----
    MIICCjCCAZGgAwIBAgIRAOdmMQ9Ho9lRxSFuKjBuTw8wCgYIKoZIzj0EAwMwMTEM
    MAoGA1UEChMDTFhEMSEwHwYDVQQDDBhyb290QGp3LXVidW50dS1zZXJ2ZXItdm0w
    HhcNMjYwNTE3MDY1MjI2WhcNMzYwNTE0MDY1MjI2WjAxMQwwCgYDVQQKEwNMWEQx
    ITAfBgNVBAMMGHJvb3RAanctdWJ1bnR1LXNlcnZlci12bTB2MBAGByqGSM49AgEG
    BSuBBAAiA2IABPhIOnCuX7/f9CkjQJ2O4YNcIpqro/+jJIzLLj474jg+WwLxOMFO
    4+4tedo8K1xtLP9kUhlpJDOb/dEvOP3jDw6r62enQZdz7Gs2rHojBm3CkON2KljP
    0ld/9Ipy5JQRz6NtMGswDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUF
    BwMBMAwGA1UdEwEB/wQCMAAwNgYDVR0RBC8wLYITanctdWJ1bnR1LXNlcnZlci12
    bYcEfwAAAYcQAAAAAAAAAAAAAAAAAAAAATAKBggqhkjOPQQDAwNnADBkAjAnGUye
    ACV03HG/8oGu5aD+BhTg1LsLjTq3JHx7+pD4H+ZqIWO1byKQMbnl2S7Nn0MCMB4X
    kAzF1JPmkelPvwqQRigAcFuJ6761R9t+o/Bk/DkIZAcB/6Ru4oJIFeIUudMQVA==
    -----END CERTIFICATE-----
  certificate_fingerprint: 5d3b0425cc9182daddf4bf43cef8fb96607257f6b4f179451ee8caa3ad36fb1d
  driver: lxc | qemu
  driver_version: 6.0.4 | 8.2.2
  instance_types:
  - container
  - virtual-machine
  firewall: nftables
  kernel: Linux
  kernel_architecture: x86_64
  kernel_features:
    bpf_token: "false"
    idmapped_mounts: "true"
    netnsid_getifaddrs: "true"
    seccomp_listener: "true"
    seccomp_listener_continue: "true"
    uevent_injection: "true"
    unpriv_binfmt: "false"
    unpriv_fscaps: "true"
  kernel_version: 5.15.0-177-generic
  lxc_features:
    cgroup2: "true"
    core_scheduling: "true"
    devpts_fd: "true"
    idmapped_mounts_v2: "true"
    mount_injection_file: "true"
    network_gateway_device_route: "true"
    network_ipvlan: "true"
    network_l2proxy: "true"
    network_phys_macvlan_mtu: "true"
    network_veth_router: "true"
    pidfd: "true"
    seccomp_allow_deny_syntax: "true"
    seccomp_notify: "true"
    seccomp_proxy_send_notify_fd: "true"
  os_name: Ubuntu
  os_version: "22.04"
  project: default
  server: lxd
  server_clustered: false
  server_event_mode: full-mesh
  server_name: jw-ubuntu-server-vm
  server_pid: 74933
  server_version: 5.21.4
  server_lts: true
  storage: ""
  storage_version: ""
  storage_supported_drivers:
  - name: btrfs
    version: 5.16.2
    remote: false
  - name: ceph
    version: 17.2.9
    remote: true
  - name: cephfs
    version: 17.2.9
    remote: true
  - name: cephobject
    version: 17.2.9
    remote: true
  - name: dir
    version: "1"
    remote: false
  - name: lvm
    version: 2.03.11(2) (2021-01-08) / 1.02.175 (2021-01-08) / 4.45.0
    remote: false
  - name: powerflex
    version: 1.16 (nvme-cli)
    remote: true
  - name: pure
    version: 2.1.5 (iscsiadm) / 1.16 (nvme-cli)
    remote: true
  - name: zfs
    version: 2.1.5-1ubuntu6~22.04.6
    remote: false
═╣ Interesting runtime sockets ... ═╣ Any running containers? ........ No



                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════
                                     ╚═══════╝
./linpeas.sh: 2962: curl: Permission denied
Learn and practice cloud hacking techniques in https://training.hacktricks.xyz

═╣ GCP Virtual Machine? ................. No
═╣ GCP Cloud Funtion? ................... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. No
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ AWS Codebuild? ....................... No
═╣ DO Droplet? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM or Az metadata? ............. No
═╣ Azure APP or IDENTITY_ENDPOINT? ...... No
═╣ Azure Automation Account? ............ No
═╣ Aliyun ECS? .......................... No
═╣ Tencent CVM? ......................... No



                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════
                ╚════════════════════════════════════════════════╝
╔══════════╣ Running processes (cleaned) (T1057)
╚ Check weird & unexpected processes run by root: https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#processes
root           1  0.0  0.3 167356 12768 ?        Ss   May16   0:17 /sbin/init
root         407  0.0  0.5  56012 23732 ?        S<s  May16   0:01 /lib/systemd/systemd-journald
root         446  0.0  0.6 289316 27100 ?        SLsl May16   0:07 /sbin/multipathd -d -s
root         450  0.0  0.1  25684  6536 ?        Ss   May16   0:00 /lib/systemd/systemd-udevd
systemd+     504  0.0  0.1  89364  6604 ?        Ssl  May16   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
systemd+     605  0.0  0.2  16256  8264 ?        Ss   May16   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
systemd+     607  0.0  0.3  26336 13256 ?        Ss   May16   0:00 /lib/systemd/systemd-resolved
  └─(Caps) 0x0000000000002000=cap_net_raw
message+     619  0.0  0.1   8656  5024 ?        Ss   May16   0:00 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root         626  0.0  0.4  30136 18772 ?        Ss   May16   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         631  0.0  0.1  31920  7564 ?        Ss   May16   0:00 /lib/systemd/systemd-logind
joelw       4565  0.0  0.2  17320  8072 ?        S    May16   0:02  |   _ sshd: joelw@pts/0
joelw       4566  0.0  0.1   5168  4112 pts/0    Ss   May16   0:00  |       _ -bash
root      300867  0.0  0.1   8916  5520 pts/0    S+   07:38   0:00  |           _ sudo go run .
root      300869  0.0  0.0   8916   884 pts/3    Ss   07:38   0:00  |               _ sudo go run .
root      300870  0.0  0.5 1275228 23632 pts/3   Sl+  07:38   0:00  |                   _ go run .
root      300902  0.7  0.2 1970432 11228 pts/3   Sl+  07:38   0:00  |                       _ /root/.cache/go-build/3f/3f28c274b7ec0adeb9d0842f30b9a229a92e4225c1edb98b66703d2e6bea223c-d/ttp-bench
root      301858  0.2  0.3 1784356 12664 pts/3   Sl+  07:39   0:00  |                           _ ./exec-linpeas
root      301867  2.9  0.0   4136  3060 pts/3    S+   07:40   0:00  |                               _ /bin/sh ./linpeas.sh -s
root      317697  0.0  0.0   4136  1436 pts/3    S+   07:41   0:00  |                                   _ /bin/sh ./linpeas.sh -s
root      317699  0.0  0.0   7820  3608 pts/3    R+   07:41   0:00  |                                   |   _ ps fauxwww
root      317701  0.0  0.0   4136  1436 pts/3    S+   07:41   0:00  |                                   _ /bin/sh ./linpeas.sh -s
joelw       4598  0.0  0.1  17324  7952 ?        S    May16   0:02      _ sshd: joelw@pts/1
joelw       4599  0.0  0.1   5168  4244 pts/1    Ss   May16   0:01          _ -bash
joelw     301837  0.0  0.0   4784  3188 pts/1    S+   07:39   0:00              _ /bin/bash /usr/local/bin/kedr
root      301838  0.0  0.1   8916  5260 pts/1    S+   07:39   0:00                  _ sudo karmor logs --gRPC=localhost:32767 --logFilter=policy
root      301840  0.0  0.0   8916   888 pts/2    Ss+  07:39   0:00                  |   _ sudo karmor logs --gRPC=localhost:32767 --logFilter=policy
root      301841  0.7  1.1 1293872 45884 pts/2   Sl   07:39   0:00                  |       _ karmor logs --gRPC=localhost:32767 --logFilter=policy
joelw     301839  0.0  0.2  13704  8236 pts/1    S+   07:39   0:00                  _ python3 /home/joelw/kubearmor-linux-edr/kedr.py
root         666  0.0  0.5 107260 21144 ?        Ssl  May16   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root         668  0.0  0.1   7816  4796 tty1     Ss   May16   0:00 /bin/login -p --
joelw        865  0.0  0.1   5172  4096 tty1     S    May16   0:00  _ -bash
joelw       4269  0.0  0.1   5048  4068 tty1     S    May16   0:00      _ bash
joelw       4289  0.0  0.0   5048  4000 tty1     S    May16   0:00          _ bash
joelw       4310  0.0  0.1   5048  4088 tty1     S    May16   0:00              _ bash
joelw       4333  0.0  0.1   5048  4036 tty1     S    May16   0:00                  _ bash
joelw       4344  0.0  0.1   5048  4048 tty1     S    May16   0:00                      _ bash
joelw       4377  0.0  0.1   5048  4056 tty1     S+   May16   0:00                          _ bash
root         670  0.0  0.2 235476  8204 ?        Ssl  May16   0:00 /usr/libexec/polkitd --no-debug
joelw        782  0.0  0.2  17076  9720 ?        Ss   May16   0:00 /lib/systemd/systemd --user
joelw        783  0.0  0.0 168896  3472 ?        S    May16   0:00  _ (sd-pam)
root         993  0.2  4.6 1513140 185988 ?      Ssl  May16   2:54 /opt/kubearmor/kubearmor
root        1349  0.0  0.5 293032 20236 ?        Ssl  May16   0:00 /usr/libexec/packagekitd
root       73503  0.6  0.9 2072352 39880 ?       Ssl  06:50   0:19 /snap/snapd/current/usr/lib/snapd/snapd
root       74718  0.0  0.0   2892  1772 ?        Ss   06:53   0:00 /bin/sh /snap/lxd/38767/commands/daemon.start
root       74933  0.1  1.9 6354232 78948 ?       Sl   06:53   0:03  _ lxd --logfile /var/snap/lxd/common/lxd/logs/lxd.log --group lxd
root       74923  0.0  0.0 153184  2172 ?        Sl   06:53   0:00 lxcfs /var/snap/lxd/common/var/lib/lxcfs -p /var/snap/lxd/common/lxcfs.pid
root      119063  0.0  0.0  78828   920 ?        Ss   06:57   0:00 gpg-agent --homedir /root/.gnupg --use-standard-socket --daemon[0m

╔══════════╣ Processes with unusual configurations (T1057)
Process 993 (root) - /opt/kubearmor/kubearmor 
Unusual number of FDs: 363


╔══════════╣ Processes with credentials in memory (root req) (T1003.007)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd Not Found
apache2 Not Found
sshd: process found (dump creds from memory as root)
mysql Not Found
postgres Not Found
redis-server Not Found
mongod Not Found
memcached Not Found
elasticsearch Not Found
jenkins Not Found
tomcat Not Found
nginx Not Found
php-fpm Not Found
supervisord Not Found
vncserver Not Found
xrdp Not Found
teamviewer Not Found

╔══════════╣ Opened Files by processes (T1003.007)
Process 1 (root) - /sbin/init 
  └─ Has open files:
    └─ /proc/1/mountinfo
    └─ pipe:[18942]
    └─ /run/cloud-init/share/hook-hotplug-cmd
    └─ /proc/swaps
    └─ /dev/autofs
    └─ /dev/kmsg
    └─ /run/dmeventd-server
    └─ /run/dmeventd-client
    └─ /run/initctl
    └─ /sys/fs/cgroup
    └─ /dev/rfkill
Process 407 (root) - /lib/systemd/systemd-journald 
  └─ Has open files:
    └─ /proc/sys/kernel/hostname
    └─ /var/log/journal/48f58895114e4c1a903d2a3243114796/system.journal
    └─ /var/log/journal/48f58895114e4c1a903d2a3243114796/user-1000.journal
    └─ /dev/kmsg
Process 446 (root) - /sbin/multipathd -d -s 
  └─ Has open files:
    └─ /run/multipathd.pid
    └─ /dev/mapper/control
Process 450 (root) - /lib/systemd/systemd-udevd 
  └─ Has open files:
    └─ /usr/lib/udev/hwdb.bin
Process 607 (systemd-resolve) - /lib/systemd/systemd-resolved 
  └─ Has open files:
    └─ /proc/sys/kernel/hostname
Process 631 (root) - /lib/systemd/systemd-logind 
  └─ Has open files:
    └─ /run/systemd/inhibit/1.ref
    └─ /dev/input/event0
    └─ /dev/tty6
    └─ /run/systemd/sessions/7.ref
    └─ /run/systemd/sessions/3.ref
    └─ /run/systemd/sessions/8.ref
    └─ /dev/input/event1
    └─ /sys/devices/virtual/tty/tty0/active
Process 666 (root) - /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal 
  └─ Has open files:
    └─ /var/log/unattended-upgrades/unattended-upgrades-shutdown.log
    └─ /run/systemd/inhibit/1.ref
Process 668 (root) - /bin/login -p --       
  └─ Has open files:
    └─ /dev/tty1
    └─ /run/systemd/sessions/3.ref
Process 782 (joelw) - /lib/systemd/systemd --user 
  └─ Has open files:
    └─ /proc/782/mountinfo
    └─ /proc/swaps
    └─ /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service
Process 783 (joelw) - (sd-pam) 
  └─ Has open files:
    └─ pipe:[18334]
Process 865 (joelw) - -bash 
  └─ Has open files:
    └─ /dev/tty1
Process 1349 (root) - /usr/libexec/packagekitd 
  └─ Has open files:
    └─ /var/lib/PackageKit/transactionsdb.db
Process 4269 (joelw) - bash 
  └─ Has open files:
    └─ /dev/tty1
Process 4289 (joelw) - bash 
  └─ Has open files:
    └─ /dev/tty1
Process 4310 (joelw) - bash 
  └─ Has open files:
    └─ /dev/tty1
Process 4333 (joelw) - bash 
  └─ Has open files:
    └─ /dev/tty1
Process 4344 (joelw) - bash 
  └─ Has open files:
    └─ /dev/tty1
Process 4377 (joelw) - bash 
  └─ Has open files:
    └─ /dev/tty1
Process 4544 (root) - sshd: joelw [priv]   
  └─ Has open files:
    └─ /dev/ptmx
    └─ /run/systemd/sessions/7.ref
Process 4565 (joelw) - sshd: joelw@pts/0    
  └─ Has open files:
    └─ /dev/ptmx
    └─ /run/systemd/sessions/7.ref
Process 4566 (joelw) - -bash 
  └─ Has open files:
    └─ /dev/pts/0
Process 4577 (root) - sshd: joelw [priv]   
  └─ Has open files:
    └─ /dev/ptmx
    └─ /run/systemd/sessions/8.ref
Process 4598 (joelw) - sshd: joelw@pts/1    
  └─ Has open files:
    └─ /dev/ptmx
    └─ /run/systemd/sessions/8.ref
Process 4599 (joelw) - -bash 
  └─ Has open files:
    └─ /dev/pts/1
Process 73503 (root) - /snap/snapd/current/usr/lib/snapd/snapd 
  └─ Has open files:
    └─ pipe:[148568]
    └─ /var/lib/snapd/state.lock
Process 74718 (root) - /bin/sh /snap/lxd/38767/commands/daemon.start 
  └─ Has open files:
    └─ /snap/lxd/38767/commands/daemon.start
Process 74923 (root) - lxcfs /var/snap/lxd/common/var/lib/lxcfs -p /var/snap/lxd/common/lxcfs.pid 
  └─ Has open files:
    └─ /var/snap/lxd/common/lxcfs.pid
    └─ /dev/fuse
    └─ /sys/fs/cgroup
    └─ mnt:[4026532558]
    └─ /
Process 74933 (root) - lxd --logfile /var/snap/lxd/common/lxd/logs/lxd.log --group lxd 
  └─ Has open files:
    └─ pipe:[151633]
    └─ pipe:[151634]
    └─ /var/snap/lxd/common/lxd/database/global/dqlite-lock
    └─ /var/snap/lxd/common/lxd/database/global/open-1
    └─ /var/snap/lxd/common/lxd/database/global/open-2
    └─ /var/snap/lxd/common/lxd/database/global/open-3
    └─ /dev
    └─ /var/snap/lxd/common/lxd/logs/lxd.log
    └─ /var/snap/lxd/common/lxd/database/localdb.db
Process 300867 (root) - sudo go run . 
  └─ Has open files:
    └─ /dev/pts/0
    └─ pipe:[618955]
    └─ /etc/sudoers
    └─ /dev/tty
    └─ /dev/ptmx
Process 300869 (root) - sudo go run . 
  └─ Has open files:
    └─ /dev/pts/0
    └─ /dev/pts/3
    └─ pipe:[617128]
    └─ pipe:[618955]
    └─ /etc/sudoers
    └─ /dev/tty
Process 300870 (root) - go run . 
  └─ Has open files:
    └─ /dev/pts/3
    └─ /root/.config/go/telemetry/local/go@go1.26.3-go1.26.3-linux-amd64-2026-05-17.v1.count
Process 300902 (root) - /root/.cache/go-build/3f/3f28c274b7ec0adeb9d0842f30b9a229a92e4225c1edb98b66703d2e6bea223c-d/ttp-benc
  └─ Has open files:
    └─ /dev/pts/3
Process 301837 (joelw) - /bin/bash /usr/local/bin/kedr 
  └─ Has open files:
    └─ /dev/pts/1
    └─ /usr/local/bin/kedr
Process 301838 (root) - sudo karmor logs --gRPC=localhost:32767 --logFilter=policy 
  └─ Has open files:
    └─ /dev/pts/1
    └─ pipe:[619189]
    └─ pipe:[620615]
    └─ /etc/sudoers
    └─ /dev/tty
    └─ /dev/ptmx
Process 301839 (joelw) - python3 /home/joelw/kubearmor-linux-edr/kedr.py 
  └─ Has open files:
    └─ pipe:[619189]
    └─ /dev/pts/1
Process 301840 (root) - sudo karmor logs --gRPC=localhost:32767 --logFilter=policy 
  └─ Has open files:
    └─ /dev/pts/1
    └─ pipe:[619189]
    └─ /dev/pts/2
    └─ pipe:[618241]
    └─ pipe:[620615]
    └─ /etc/sudoers
    └─ /dev/tty
Process 301841 (root) - karmor logs --gRPC=localhost:32767 --logFilter=policy 
  └─ Has open files:
    └─ /dev/pts/2
    └─ pipe:[619189]
Process 301858 (root) - ./exec-linpeas 
  └─ Has open files:
    └─ /dev/pts/3

╔══════════╣ Processes with memory-mapped credential files (T1003.007)

╔══════════╣ Processes whose PPID belongs to a different user (not root) (T1134.004)
╚ You will know if a user can somehow spawn processes as a different user
Proc 300870 with ppid 300869 is run by user root but the ppid user is joelw
Proc 301841 with ppid 301840 is run by user root but the ppid user is joelw

╔══════════╣ Check for vulnerable cron jobs (T1053.003)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#scheduledcron-jobs
══╣ Cron jobs list (T1053.003)
crontab Not Found
incrontab Not Found
/etc/cron.d:
total 12
drwxr-xr-x  2 root root 4096 Sep 11  2024 .
drwxr-xr-x 80 root root 4096 May 17 06:53 ..
-rw-r--r--  1 root root  201 Jan  8  2022 e2scrub_all

/etc/cron.daily:
total 20
drwxr-xr-x  2 root root 4096 May  9 19:53 .
drwxr-xr-x 80 root root 4096 May 17 06:53 ..
-rwxr-xr-x  1 root root  376 Jul 24  2023 apport
-rwxr-xr-x  1 root root 1478 Apr  8  2022 apt-compat
-rwxr-xr-x  1 root root  123 Dec  5  2021 dpkg

══╣ Cron files with hidden carriage returns (T1053.003)

══╣ Checking for specific cron jobs vulnerabilities (T1053.003)
Checking cron directories...
Writable cron directory: /etc/cron.d
Writable cron directory: /etc/cron.daily
══╣ run-parts executable entries (T1053.003)
[/etc/cron.daily]
/etc/cron.daily/apport
/etc/cron.daily/apt-compat
/etc/cron.daily/dpkg


╔══════════╣ System timers (T1053.003)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#timers
══╣ Active timers: (T1053.003)
NEXT                        LEFT          LAST                        PASSED       UNIT                         ACTIVATES
Sun 2026-05-17 09:26:15 UTC 1h 44min left Mon 2026-05-11 15:20:44 UTC 5 days ago   systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Sun 2026-05-17 12:22:57 UTC 4h 41min left Sun 2026-05-17 05:29:41 UTC 2h 11min ago motd-news.timer              motd-news.service
Sun 2026-05-17 20:46:32 UTC 13h left      Sun 2026-05-17 06:53:16 UTC 48min ago    apt-daily.timer              apt-daily.service
Mon 2026-05-18 00:00:00 UTC 16h left      Sun 2026-05-17 05:28:50 UTC 2h 12min ago dpkg-db-backup.timer         dpkg-db-backup.service
Mon 2026-05-18 00:37:49 UTC 16h left      Mon 2026-05-11 13:34:42 UTC 5 days ago   fstrim.timer                 fstrim.service
Mon 2026-05-18 06:52:26 UTC 23h left      Sun 2026-05-17 06:43:17 UTC 57min ago    apt-daily-upgrade.timer      apt-daily-upgrade.service
Sun 2026-05-24 03:10:41 UTC 6 days left   Sun 2026-05-17 05:28:50 UTC 2h 12min ago e2scrub_all.timer            e2scrub_all.service
n/a                         n/a           n/a                         n/a          apport-autoreport.timer      apport-autoreport.service
n/a                         n/a           n/a                         n/a          snapd.snap-repair.timer      snapd.snap-repair.service
══╣ Disabled timers: (T1053.003)
Potential privilege escalation in timer file: /lib/systemd/system/xfs_scrub_all.timer
  └─ WRITABLE_FILE: Timer file is writable
══╣ Additional timer files: (T1053.003)
Potential privilege escalation in timer file: /etc/systemd/system/mdmonitor.service.wants/mdcheck_continue.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/mdcheck_continue.timer
Potential privilege escalation in timer file: /etc/systemd/system/mdmonitor.service.wants/mdcheck_start.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/mdcheck_start.timer
Potential privilege escalation in timer file: /etc/systemd/system/mdmonitor.service.wants/mdmonitor-oneshot.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/mdmonitor-oneshot.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/apport-autoreport.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/apport-autoreport.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/apt-daily-upgrade.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/apt-daily-upgrade.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/apt-daily.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/apt-daily.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/dpkg-db-backup.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/dpkg-db-backup.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/e2scrub_all.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/e2scrub_all.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/fstrim.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/fstrim.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/motd-news.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/motd-news.timer
Potential privilege escalation in timer file: /etc/systemd/system/timers.target.wants/snapd.snap-repair.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/snapd.snap-repair.timer
Potential privilege escalation in timer file: /snap/core22/2411/usr/lib/systemd/system/timers.target.wants/apt-daily-upgrade.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/apt-daily-upgrade.timer
Potential privilege escalation in timer file: /snap/core22/2411/usr/lib/systemd/system/timers.target.wants/apt-daily.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/apt-daily.timer
Potential privilege escalation in timer file: /snap/core22/2411/usr/lib/systemd/system/timers.target.wants/e2scrub_all.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/e2scrub_all.timer
Potential privilege escalation in timer file: /snap/core22/2411/usr/lib/systemd/system/timers.target.wants/fstrim.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/fstrim.timer
Potential privilege escalation in timer file: /usr/lib/systemd/system/apport-autoreport.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/apt-daily-upgrade.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/apt-daily.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/dpkg-db-backup.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/e2scrub_all.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/fstrim.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/mdadm-last-resort@.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/mdcheck_continue.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/mdcheck_start.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/mdmonitor-oneshot.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/motd-news.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/snapd.snap-repair.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/systemd-tmpfiles-clean.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/system/timers.target.wants/systemd-tmpfiles-clean.timer
  └─ WRITABLE_FILE: Timer target file is writable: /usr/lib/systemd/system/systemd-tmpfiles-clean.timer
Potential privilege escalation in timer file: /usr/lib/systemd/system/xfs_scrub_all.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /usr/lib/systemd/user/systemd-tmpfiles-clean.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/mdmonitor.service.wants/mdcheck_continue.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/mdmonitor.service.wants/mdcheck_start.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/mdmonitor.service.wants/mdmonitor-oneshot.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/apport-autoreport.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/apt-daily-upgrade.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/apt-daily.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/dpkg-db-backup.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/e2scrub_all.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/fstrim.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/motd-news.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/deb-systemd-helper-enabled/timers.target.wants/snapd.snap-repair.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/timers/stamp-apt-daily-upgrade.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/timers/stamp-apt-daily.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/timers/stamp-e2scrub_all.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/timers/stamp-fstrim.timer
  └─ WRITABLE_FILE: Timer file is writable
Potential privilege escalation in timer file: /var/lib/systemd/timers/stamp-motd-news.timer
  └─ WRITABLE_FILE: Timer file is writable

╔══════════╣ Services and Service Files (T1543.002,T1007)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#services

══╣ Active services: (T1543.002,T1007)
apparmor.service                     loaded active exited  Load AppArmor profiles
apport.service                       loaded active exited  LSB: automatic crash report generation
binfmt-support.service               loaded active exited  Enable support for additional executable binary formats
blk-availability.service             loaded active exited  Availability of block devices
cloud-config.service                 loaded active exited  Cloud-init: Config Stage
cloud-final.service                  loaded active exited  Cloud-init: Final Stage
cloud-init-local.service             loaded active exited  Cloud-init: Local Stage (pre-network)
  Potential issue in service file: /lib/systemd/system/cloud-init-local.service
  └─ RELATIVE_PATH: Could be executing some relative path
cloud-init.service                   loaded active exited  Cloud-init: Network Stage
console-setup.service                loaded active exited  Set console font and keymap
dbus.service                         loaded active running D-Bus System Message Bus
  Potential issue in service file: /lib/systemd/system/dbus.service
  └─ RELATIVE_PATH: Could be executing some relative path
finalrd.service                      loaded active exited  Create final runtime dir for shutdown pivot root
getty@tty1.service                   loaded active running Getty on tty1
keyboard-setup.service               loaded active exited  Set the console keyboard layout
kmod-static-nodes.service            loaded active exited  Create List of Static Device Nodes
kubearmor.service                    loaded active running KubeArmor
  Potential issue in service: kubearmor.service
  └─ RUNS_AS_ROOT: Service runs as root
lvm2-monitor.service                 loaded active exited  Monitoring of LVM2 mirrors, snapshots etc. using dmeventd or progress polling
multipathd.service                   loaded active running Device-Mapper Multipath Device Controller
networkd-dispatcher.service          loaded active running Dispatcher daemon for systemd-networkd
packagekit.service                   loaded active running PackageKit Daemon
  Potential issue in service: packagekit.service
  └─ RUNS_AS_ROOT: Service runs as root
plymouth-quit-wait.service           loaded active exited  Hold until boot process finishes up
plymouth-quit.service                loaded active exited  Terminate Plymouth Boot Screen
plymouth-read-write.service          loaded active exited  Tell Plymouth To Write Out Runtime Data
polkit.service                       loaded active running Authorization Manager
setvtrgb.service                     loaded active exited  Set console scheme
snap.lxd.daemon.service              loaded active running Service for snap application lxd.daemon
snap.lxd.workaround.service          loaded active exited  /bin/true
  Potential issue in service file: /run/systemd/transient/snap.lxd.workaround.service
  └─ RELATIVE_PATH: Could be executing some relative path
snapd.apparmor.service               loaded active exited  Load AppArmor profiles managed internally by snapd
snapd.seeded.service                 loaded active exited  Wait until snapd is fully seeded
snapd.service                        loaded active running Snap Daemon
ssh.service                          loaded active running OpenBSD Secure Shell server
systemd-binfmt.service               loaded active exited  Set Up Additional Binary Formats
systemd-journal-flush.service        loaded active exited  Flush Journal to Persistent Storage
  Potential issue in service file: /lib/systemd/system/systemd-journal-flush.service
  └─ RELATIVE_PATH: Could be executing some relative path
systemd-journald.service             loaded active running Journal Service
systemd-logind.service               loaded active running User Login Management
systemd-modules-load.service         loaded active exited  Load Kernel Modules
systemd-networkd-wait-online.service loaded active exited  Wait for Network to be Configured
systemd-networkd.service             loaded active running Network Configuration
  Potential issue in service file: /lib/systemd/system/systemd-networkd.service
  └─ RELATIVE_PATH: Could be executing some relative path
systemd-random-seed.service          loaded active exited  Load/Save Random Seed
systemd-remount-fs.service           loaded active exited  Remount Root and Kernel File Systems
  Potential issue in service: systemd-remount-fs.service
  └─ UNSAFE_CMD: Uses potentially dangerous commands
systemd-resolved.service             loaded active running Network Name Resolution
systemd-sysctl.service               loaded active exited  Apply Kernel Variables
systemd-sysusers.service             loaded active exited  Create System Users
  Potential issue in service file: /lib/systemd/system/systemd-sysusers.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service: systemd-sysusers.service
  └─ UNSAFE_CMD: Uses potentially dangerous commands
systemd-timesyncd.service            loaded active running Network Time Synchronization
systemd-tmpfiles-setup-dev.service   loaded active exited  Create Static Device Nodes in /dev
systemd-tmpfiles-setup.service       loaded active exited  Create Volatile Files and Directories
systemd-udev-trigger.service         loaded active exited  Coldplug All udev Devices
  Potential issue in service file: /lib/systemd/system/systemd-udev-trigger.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service: systemd-udev-trigger.service
  └─ UNSAFE_CMD: Uses potentially dangerous commands
systemd-udevd.service                loaded active running Rule-based Manager for Device Events and Files
  Potential issue in service file: /lib/systemd/system/systemd-udevd.service
  └─ RELATIVE_PATH: Could be executing some relative path
systemd-update-utmp.service          loaded active exited  Record System Boot/Shutdown in UTMP
systemd-user-sessions.service        loaded active exited  Permit User Sessions
unattended-upgrades.service          loaded active running Unattended Upgrades Shutdown
user-runtime-dir@1000.service        loaded active exited  User Runtime Directory /run/user/1000
user@1000.service                    loaded active running User Manager for UID 1000
LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.
52 loaded units listed.

══╣ Disabled services: (T1543.002,T1007)
console-getty.service                  disabled disabled
debug-shell.service                    disabled disabled
iscsid.service                         disabled enabled
nftables.service                       disabled enabled
serial-getty@.service                  disabled enabled
systemd-boot-check-no-failures.service disabled disabled
systemd-network-generator.service      disabled enabled
systemd-sysext.service                 disabled enabled
  Potential issue in service file: /lib/systemd/system/systemd-sysext.service
  └─ RELATIVE_PATH: Could be executing some relative path
systemd-time-wait-sync.service         disabled disabled
upower.service                         disabled enabled
10 unit files listed.

══╣ Additional service files: (T1543.002,T1007)
  Potential issue in service file: /etc/systemd/system/cloud-init.target.wants/cloud-init-local.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /etc/systemd/system/multi-user.target.wants/grub-common.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /etc/systemd/system/multi-user.target.wants/systemd-networkd.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /etc/systemd/system/sleep.target.wants/grub-common.service
  └─ RELATIVE_PATH: Could be executing some relative path
  Potential issue in service file: /opt/kubearmor/BPF/libbpf/travis-ci/rootfs/s390x-self-hosted-builder/actions-runner-libbpf.service
  └─ RELATIVE_PATH: Could be executing some relative path
You can't write on systemd PATH

╔══════════╣ Systemd Information (T1543.002)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#systemd-path---relative-paths
═╣ Systemd version and vulnerabilities? .............. 249.11
3.20
═╣ Services running as root? ..... 
═╣ Running services with dangerous capabilities? ... 
═╣ Services with writable paths? . dbus.service: /usr/bin/dbus-daemon (from ExecStart=@/usr/bin/dbus-daemon @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only)
kubearmor.service: /opt/kubearmor/kubearmor (from ExecStart=/opt/kubearmor/kubearmor)
multipathd.service: /sbin/modprobe (from ExecStartPre=-/sbin/modprobe -a scsi_dh_alua scsi_dh_emc scsi_dh_rdac dm-multipath)
multipathd.service: /sbin/multipathd (from ExecStart=/sbin/multipathd -d -s)
networkd-dispatcher.service: /usr/bin/networkd-dispatcher (from ExecStart=/usr/bin/networkd-dispatcher $networkd_dispatcher_args)
packagekit.service: /usr/libexec/packagekitd (from ExecStart=/usr/libexec/packagekitd)
polkit.service: /usr/libexec/polkitd (from ExecStart=/usr/libexec/polkitd --no-debug)
snap.lxd.daemon.service: /usr/bin/snap (from ExecStart=/usr/bin/snap run lxd.daemon)
snapd.service: /usr/lib/snapd/snapd (from ExecStart=/usr/lib/snapd/snapd)
ssh.service: /usr/sbin/sshd (from ExecStartPre=/usr/sbin/sshd -t)
ssh.service: /usr/sbin/sshd (from ExecStart=/usr/sbin/sshd -D $SSHD_OPTS)
systemd-journald.service: /lib/systemd/systemd-journald (from ExecStart=/lib/systemd/systemd-journald)
systemd-logind.service: /lib/systemd/systemd-logind (from ExecStart=/lib/systemd/systemd-logind)
systemd-networkd.service: /lib/systemd/systemd-networkd (from ExecStart=!!/lib/systemd/systemd-networkd)
systemd-resolved.service: /lib/systemd/systemd-resolved (from ExecStart=!!/lib/systemd/systemd-resolved)
systemd-timesyncd.service: /lib/systemd/systemd-timesyncd (from ExecStart=!!/lib/systemd/systemd-timesyncd)
systemd-udevd.service: /lib/systemd/systemd-udevd (from ExecStart=/lib/systemd/systemd-udevd)
unattended-upgrades.service: /usr/share/unattended-upgrades/unattended-upgrade-shutdown (from ExecStart=/usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal)

╔══════════╣ Systemd PATH (T1543.002)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#systemd-path---relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

╔══════════╣ D-Bus Analysis (T1559.001)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#d-bus
NAME                             PID PROCESS         USER             CONNECTION    UNIT                        SESSION DESCRIPTION
:1.0                             607 systemd-resolve systemd-resolve  :1.0          systemd-resolved.service    -       -
:1.1                             504 systemd-timesyn systemd-timesync :1.1          systemd-timesyncd.service   -       -
:1.111                        342444 busctl          root             :1.111        session-7.scope             7       -
:1.15                            782 systemd         joelw            :1.15         user@1000.service           -       -
:1.2                             605 systemd-network systemd-network  :1.2          systemd-networkd.service    -       -
:1.26                           1349 packagekitd     root             :1.26         packagekit.service          -       -
:1.3                               1 systemd         root             :1.3          init.scope                  -       -
:1.4                             631 systemd-logind  root             :1.4          systemd-logind.service      -       -
:1.7                             626 networkd-dispat root             :1.7          networkd-dispatcher.service -       -
:1.79                          73503 snapd           root             :1.79         snapd.service               -       -
:1.8                             670 polkitd         root             :1.8          polkit.service              -       -
:1.9                             666 unattended-upgr root             :1.9          unattended-upgrades.service -       -
com.ubuntu.SoftwareProperties      - -               -                (activatable) -                           -       -
io.netplan.Netplan                 - -               -                (activatable) -                           -       -
org.freedesktop.DBus               1 systemd         root             -             init.scope                  -       -
org.freedesktop.PackageKit      1349 packagekitd     root             :1.26         packagekit.service          -       -
org.freedesktop.PolicyKit1       670 polkitd         root             :1.8          polkit.service              -       -
org.freedesktop.UPower             - -               -                (activatable) -                           -       -
org.freedesktop.hostname1          - -               -                (activatable) -                           -       -
org.freedesktop.locale1            - -               -                (activatable) -                           -       -
org.freedesktop.login1           631 systemd-logind  root             :1.4          systemd-logind.service      -       -
org.freedesktop.network1         605 systemd-network systemd-network  :1.2          systemd-networkd.service    -       -
org.freedesktop.resolve1         607 systemd-resolve systemd-resolve  :1.0          systemd-resolved.service    -       -
org.freedesktop.systemd1           1 systemd         root             :1.3          init.scope                  -       -
org.freedesktop.thermald           - -               -                (activatable) -                           -       -
org.freedesktop.timedate1          - -               -                (activatable) -                           -       -
org.freedesktop.timesync1        504 systemd-timesyn systemd-timesync :1.1          systemd-timesyncd.service   -       -

╔══════════╣ D-Bus Configuration Files (T1559.001)
Analyzing /etc/dbus-1/system.d/com.ubuntu.SoftwareProperties.conf:
  └─(Allow rules in default context)
             └─     <allow send_destination="com.ubuntu.SoftwareProperties"
            <allow send_destination="com.ubuntu.SoftwareProperties"
            <allow send_destination="com.ubuntu.DeviceDriver"
Analyzing /etc/dbus-1/system.d/org.freedesktop.PackageKit.conf:
  └─(Allow rules in default context)
             └─     <allow send_destination="org.freedesktop.PackageKit"
            <allow send_destination="org.freedesktop.PackageKit"
            <allow send_destination="org.freedesktop.PackageKit"
Analyzing /etc/dbus-1/system.d/org.freedesktop.thermald.conf:
  └─(Weak group policy found)
     └─         <policy group="power">
  └─(Allow rules in default context)
             └─                 <allow receive_sender="org.freedesktop.thermald"/>
                        <allow send_destination="org.freedesktop.thermald"/>
Activation definitions in /usr/share/dbus-1/services:
/usr/share/dbus-1/services/io.snapcraft.SessionAgent.service:2:Name=io.snapcraft.SessionAgent
/usr/share/dbus-1/services/io.snapcraft.SessionAgent.service:4:Exec=Exec=/bin/false
/usr/share/dbus-1/services/io.snapcraft.Launcher.service:2:Name=io.snapcraft.Launcher
/usr/share/dbus-1/services/io.snapcraft.Launcher.service:3:Exec=Exec=/usr/bin/snap userd
/usr/share/dbus-1/services/io.snapcraft.Settings.service:2:Name=io.snapcraft.Settings
/usr/share/dbus-1/services/io.snapcraft.Settings.service:3:Exec=Exec=/usr/bin/snap userd
/usr/share/dbus-1/services/org.freedesktop.systemd1.service:11:Name=org.freedesktop.systemd1
/usr/share/dbus-1/services/org.freedesktop.systemd1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/services/org.freedesktop.systemd1.service:13:User=User=root
Analyzing /usr/share/dbus-1/session.d/snapd.session-services.conf:
  └─(Multiple weak policies found)
Activation definitions in /usr/share/dbus-1/system-services:
/usr/share/dbus-1/system-services/org.freedesktop.network1.service:11:Name=org.freedesktop.network1
/usr/share/dbus-1/system-services/org.freedesktop.network1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.network1.service:13:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.thermald.service:2:Name=org.freedesktop.thermald
/usr/share/dbus-1/system-services/org.freedesktop.thermald.service:3:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.thermald.service:4:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.resolve1.service:11:Name=org.freedesktop.resolve1
/usr/share/dbus-1/system-services/org.freedesktop.resolve1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.resolve1.service:13:User=User=root
/usr/share/dbus-1/system-services/com.ubuntu.SoftwareProperties.service:2:Name=com.ubuntu.SoftwareProperties
/usr/share/dbus-1/system-services/com.ubuntu.SoftwareProperties.service:3:Exec=Exec=/usr/lib/software-properties/software-properties-dbus
/usr/share/dbus-1/system-services/com.ubuntu.SoftwareProperties.service:4:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.timedate1.service:11:Name=org.freedesktop.timedate1
/usr/share/dbus-1/system-services/org.freedesktop.timedate1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.timedate1.service:13:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.UPower.service:2:Name=org.freedesktop.UPower
/usr/share/dbus-1/system-services/org.freedesktop.UPower.service:3:Exec=Exec=/usr/libexec/upowerd
/usr/share/dbus-1/system-services/org.freedesktop.UPower.service:4:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.PackageKit.service:2:Name=org.freedesktop.PackageKit
/usr/share/dbus-1/system-services/org.freedesktop.PackageKit.service:3:Exec=Exec=/usr/libexec/packagekitd
/usr/share/dbus-1/system-services/org.freedesktop.PackageKit.service:4:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.login1.service:11:Name=org.freedesktop.login1
/usr/share/dbus-1/system-services/org.freedesktop.login1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.login1.service:13:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.locale1.service:11:Name=org.freedesktop.locale1
/usr/share/dbus-1/system-services/org.freedesktop.locale1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.locale1.service:13:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.timesync1.service:11:Name=org.freedesktop.timesync1
/usr/share/dbus-1/system-services/org.freedesktop.timesync1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.timesync1.service:13:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.PolicyKit1.service:2:Name=org.freedesktop.PolicyKit1
/usr/share/dbus-1/system-services/org.freedesktop.PolicyKit1.service:3:Exec=Exec=/usr/libexec/polkitd --no-debug
/usr/share/dbus-1/system-services/org.freedesktop.PolicyKit1.service:4:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.hostname1.service:9:Name=org.freedesktop.hostname1
/usr/share/dbus-1/system-services/org.freedesktop.hostname1.service:10:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.hostname1.service:11:User=User=root
/usr/share/dbus-1/system-services/org.freedesktop.systemd1.service:11:Name=org.freedesktop.systemd1
/usr/share/dbus-1/system-services/org.freedesktop.systemd1.service:12:Exec=Exec=/bin/false
/usr/share/dbus-1/system-services/org.freedesktop.systemd1.service:13:User=User=root
/usr/share/dbus-1/system-services/io.netplan.Netplan.service:2:Name=io.netplan.Netplan
/usr/share/dbus-1/system-services/io.netplan.Netplan.service:3:Exec=Exec=/usr/libexec/netplan/netplan-dbus
/usr/share/dbus-1/system-services/io.netplan.Netplan.service:4:User=User=root

══╣ D-Bus Session Bus Analysis (T1559.001)
(Access to session bus available)


╔══════════╣ Legacy r-commands (rsh/rlogin/rexec) and host-based trust (T1021.004)

══╣ Listening r-services (TCP 512-514) (T1021.004)

══╣ systemd units exposing r-services (T1021.004)
rlogin|rsh|rexec units Not Found

══╣ inetd/xinetd configuration for r-services (T1021.004)
/etc/inetd.conf Not Found
/etc/xinetd.d Not Found

══╣ Installed r-service server packages (T1021.004)
  No related packages found via dpkg

══╣ /etc/hosts.equiv and /etc/shosts.equiv (T1021.004)

══╣ Per-user .rhosts files (T1021.004)
.rhosts Not Found

══╣ PAM rhosts authentication (T1021.004)
/etc/pam.d/rlogin|rsh Not Found

══╣ SSH HostbasedAuthentication (T1021.004)
  HostbasedAuthentication no or not set

══╣ Potential DNS control indicators (local) (T1021.004)
  Not detected

╔══════════╣ Crontab UI (root) misconfiguration checks (T1053.003)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#scheduledcron-jobs
crontab-ui Not Found


                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════
                              ╚═════════════════════╝
╔══════════╣ Interfaces (T1016)
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
══╣ Routing & policy quick view (T1016)

══╣ Virtual/overlay interfaces quick view (T1016)
══╣ Network namespaces quick view (T1016)
total 0
drwxr-xr-x  2 root root  40 May 17 06:53 .
drwxr-xr-x 24 root root 740 May 17 06:53 ..
══╣ Forwarding status (T1016)
net.ipv4.ip_forward = 0
net.ipv6.conf.all.forwarding = 0

╔══════════╣ Hostname, hosts and DNS (T1016,T1018)
══╣ Hostname Information (T1016,T1018)
System hostname: jw-ubuntu-server-vm
FQDN: jw-ubuntu-server-vm

══╣ Hosts File Information (T1016,T1018)
Contents of /etc/hosts:
  127.0.0.1 localhost
  127.0.1.1 jw-ubuntu-server-vm
  ::1     ip6-localhost ip6-loopback
  fe00::0 ip6-localnet
  ff00::0 ip6-mcastprefix
  ff02::1 ip6-allnodes
  ff02::2 ip6-allrouters

══╣ DNS Configuration (T1016,T1018)
DNS Servers (resolv.conf):
  127.0.0.53
  search .
-e 
Systemd-resolved configuration:
  [Resolve]
-e 
DNS Domain Information:
(none)

╔══════════╣ Active Ports (T1049)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#open-ports
══╣ Active Ports (ss) (T1049)
══╣ Local-only listeners (loopback) (T1049)
══╣ Unique listener bind addresses (T1049)
══╣ Potential local forwarders/relays (T1049)
root      342972  0.0  0.0   4108  1092 pts/3    S+   07:41   0:00 sed -E s,socat|ssh|-L|-R|-D|ncat|nc,?[1;31;103m&?[0m,g

╔══════════╣ Network Traffic Analysis Capabilities (T1040)

══╣ Available Sniffing Tools (T1040)
No sniffing tools found

══╣ Network Interfaces Sniffing Capabilities (T1040)
./linpeas.sh: 7720: ip: Permission denied
No sniffable interfaces found

══╣ Running sniffing/traffic reconstruction processes (T1040)

╔══════════╣ Firewall Rules Analysis (T1016)

══╣ Iptables Rules (T1016)
iptables Not Found

══╣ Nftables Rules (T1016)
nftables v1.0.2 (Lester Gooch)
-e 
Nftables Ruleset:
table ip kubearmor {
	chain INPUT {
		type filter hook input priority filter; policy accept;
		iifname "lo" accept
		ct state { established, related } accept
		log prefix "Host INPUT Allow" group 0 accept
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		oifname "lo" accept
		ct state { established, related } accept
		log prefix "Host OUTPUT Allow" group 0 accept
	}
}
table ip6 kubearmor {
	chain INPUT {
		type filter hook input priority filter; policy accept;
		iifname "lo" accept
		ct state { established, related } accept
		log prefix "Host INPUT Allow" group 0 accept
	}

	chain OUTPUT {
		type filter hook output priority filter; policy accept;
		oifname "lo" accept
		ct state { established, related } accept
		log prefix "Host OUTPUT Allow" group 0 accept
	}
}
-e 
Nftables Ruleset with handles (-a):
table ip kubearmor { # handle 13
	chain INPUT { # handle 1
		type filter hook input priority filter; policy accept;
		iifname "lo" accept # handle 5
		ct state { established, related } accept # handle 6
		log prefix "Host INPUT Allow" group 0 accept # handle 7
	}

	chain OUTPUT { # handle 2
		type filter hook output priority filter; policy accept;
		oifname "lo" accept # handle 8
		ct state { established, related } accept # handle 9
		log prefix "Host OUTPUT Allow" group 0 accept # handle 10
	}
}
table ip6 kubearmor { # handle 14
	chain INPUT { # handle 1
		type filter hook input priority filter; policy accept;
		iifname "lo" accept # handle 5
		ct state { established, related } accept # handle 6
		log prefix "Host INPUT Allow" group 0 accept # handle 7
	}

	chain OUTPUT { # handle 2
		type filter hook output priority filter; policy accept;
		oifname "lo" accept # handle 8
		ct state { established, related } accept # handle 9
		log prefix "Host OUTPUT Allow" group 0 accept # handle 10
	}
}
-e 
Saved Rules:
Found rules in /etc/nftables.conf:

flush ruleset

table inet filter {
	chain input {
		type filter hook input priority 0;
	}
	chain forward {
		type filter hook forward priority 0;
	}
	chain output {
		type filter hook output priority 0;
	}
}

══╣ Firewalld Rules (T1016)
firewalld Not Found

══╣ UFW Rules (T1016)
ufw Not Found

══╣ Forwarding and rp_filter (T1016)
net.ipv4.ip_forward = 0
net.ipv6.conf.all.forwarding = 0
net.ipv4.conf.all.rp_filter = 2

╔══════════╣ Inetd/Xinetd Services Analysis (T1049)

══╣ Inetd Services (T1049)
inetd Not Found

══╣ Xinetd Services (T1049)
xinetd Not Found

══╣ Running Inetd/Xinetd Services (T1049)
-e 
Active Services (from ss):
-e 
Running Service Processes:

╔══════════╣ Internet Access? (T1016,T1590)
Port 443 is not accessible with curl
ICMP is not accessible
Port 443 is accessible
Port 80 is accessible
DNS accessible
2026/05/17 07:41:26 exec-linpeas timed out as expected: signal: killed

══╣ Proxy discovery (T1016,T1590)
╚ Checking common proxy env vars and apt proxy config



                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ My user (T1033)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#users
uid=0(root) gid=0(root) groups=0(root)

╔══════════╣ PGP Keys and Related Files (T1552.004)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#pgp-keys
GPG:
GPG is installed, listing keys:
-e 
NetPGP:
netpgpkeys Not Found
-e 
PGP Related Files:
Found: /root/.gnupg
total 20
drwx------  3 root root 4096 May 17 07:41 .
drwx------ 10 root root 4096 May 17 06:57 ..
srwx------  1 root root    0 May 17 06:57 S.gpg-agent
srwx------  1 root root    0 May 17 06:57 S.gpg-agent.browser
srwx------  1 root root    0 May 17 06:57 S.gpg-agent.extra
srwx------  1 root root    0 May 17 06:57 S.gpg-agent.ssh
drwx------  2 root root 4096 May 17 06:57 private-keys-v1.d
-rw-------  1 root root   32 May 17 06:57 pubring.kbx
-rw-------  1 root root 1200 May 17 06:57 trustdb.gpg

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d (T1548.003)
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-and-suid
Matching Defaults entries for root on jw-ubuntu-server-vm:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User root may run the following commands on jw-ubuntu-server-vm:
    (ALL : ALL) ALL
Matching Defaults entries for root on jw-ubuntu-server-vm:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User root may run the following commands on jw-ubuntu-server-vm:
    (ALL : ALL) ALL
Writable secure_path entry: /snap/bin
/etc/sudoers:Defaults	env_reset
/etc/sudoers:Defaults	mail_badpass
/etc/sudoers:Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
/etc/sudoers:Defaults	use_pty
/etc/sudoers:root	ALL=(ALL:ALL) ALL
/etc/sudoers:%admin ALL=(ALL) ALL
/etc/sudoers:%sudo	ALL=(ALL:ALL) ALL
/etc/sudoers:@includedir /etc/sudoers.d
Sudoers file: /etc/sudoers.d/README is writable and may allow privilege escalation
Sudoers file: /etc/sudoers.d/README is readable

                                                                                                      
    CHECKS COMPLETE - 0 of 1 checks failed                                                            
exec-linpeas                  : SUCCESS

```

```

[#1] 07:39:26 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
     go ─▶ git
     Resource: /usr/bin/git status --porcelain
     

[#2] 07:39:30 Alert: File operation detected on sensitive files                      [Audit][Passed]
     systemd ─▶ kubearmor
     Resource: /etc/passwd
     Source: /opt/kubearmor/kubearmor
     Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#3] 07:39:59 Alert: File operation detected on sensitive files                      [Audit][Passed]
     systemd ─▶ kubearmor
     Resource: /etc/passwd
     Source: /opt/kubearmor/kubearmor
     Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#4] 07:39:59 Alert: File operation detected on sensitive files                      [Audit][Passed]
     systemd ─▶ kubearmor
     Resource: /etc/passwd
     Source: /opt/kubearmor/kubearmor
     Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#5] 07:40:44 Alert: Suspicious Process Created - System Information discovery       [Audit][Passed]
     dash ─▶ uname
     Resource: /usr/bin/uname
     

[#6] 07:40:44 Alert: Suspicious Process Created - System Information discovery       [Audit][Passed]
     dash ─▶ uname
     Resource: /usr/bin/uname
     

[#7] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
     dash ─▶ id
     Resource: /etc/passwd
     Source: /usr/bin/id
     Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#8] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
     dash ─▶ id
     Resource: /etc/group
     Source: /usr/bin/id
     Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#9] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
     dash ─▶ id
     Resource: /etc/group
     Source: /usr/bin/id
     Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#10] 07:40:47 Alert: Suspicious Process Created - System Information discovery       [Audit][Passed]
      dash ─▶ hostname
      Resource: /usr/bin/hostname
      

[#11] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
      dash ─▶ groups
      Resource: /etc/group
      Source: /usr/bin/groups root
      Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#12] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
      dash ─▶ groups
      Resource: /etc/passwd
      Source: /usr/bin/groups root
      Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#13] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
      dash ─▶ groups
      Resource: /etc/group
      Source: /usr/bin/groups root
      Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#14] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
      dash ─▶ groups
      Resource: /etc/passwd
      Source: /usr/bin/groups root
      Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#15] 07:40:47 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ find
      Resource: /usr/bin/find / -maxdepth 3 -type d ! -path /proc/* ( ( -user root ) -or ( -perm -o=w ) -or ...
      

[#16] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
      dash ─▶ find
      Resource: /etc/passwd
      Source: /usr/bin/find / -maxdepth 3 -type d ! -path /proc/* ( ( -user root ) -or ( -perm -o=w ) -or ...
      Syscall: SYS_OPENAT  Flags: O_RDONLY  

[#17] 07:40:47 Alert: File operation detected on sensitive files                      [Audit][Passed]
      dash ─▶ find
      Resource: /etc/group
      

[#18] 07:40:56 Alert: Kernel module tools detected                                    [Block][Permission denied]
       ─▶ kmod
      Resource: /usr/bin/kmod
      

[#19] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ curl
      Resource: /usr/bin/curl --connect-timeout 2 metadata.google.internal
      

[#20] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ curl
      Resource: /snap/bin/curl --connect-timeout 2 metadata.google.internal
      

[#21] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ wget
      Resource: /usr/bin/wget
      

[#22] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ wget
      Resource: /usr/bin/wget --timeout 2 --tries 1 metadata.google.internal
      

[#23] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ curl
      Resource: /usr/bin/curl --connect-timeout 2 -X PUT http://169.254.169.254/latest/api/token -H X-aws-ec2-metadata-token-ttl-seconds: 21600
      

[#24] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ curl
      Resource: /usr/bin/curl --connect-timeout 2 -X PUT http://169.254.169.254/latest/api/token -H X-aws-ec2-metadata-token-ttl-seconds: 21600
      

[#25] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ wget
      Resource: /sbin/wget --timeout 2 --tries 1 -q -O - --method PUT http://169.254.169.254/latest/api/token --header X-aws-ec2-metadata-token-ttl-seconds: 21600
      

[#26] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ wget
      Resource: /bin/wget --timeout 2 --tries 1 -q -O - --method PUT http://169.254.169.254/latest/api/token --header X-aws-ec2-metadata-token-ttl-seconds: 21600
      

[#27] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ curl
      Resource: /usr/bin/curl -s --max-time 2 http://169.254.169.254/metadata/identity/oauth2/token
      

[#28] 07:41:04 Alert: Download and Transfer Tools Blocked                             [Block][Permission denied]
      dash ─▶ curl
      Resource: /usr/bin/curl -s --max-time 2 http://169.254.169.254/metadata/identity/oauth2/token
      

[#29] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /lib/systemd/system/xfs_scrub_all.timer
      

[#30] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/mdmonitor.service.wants/mdcheck_continue.timer
      

[#31] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/mdmonitor.service.wants/mdcheck_start.timer
      

[#32] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/mdmonitor.service.wants/mdmonitor-oneshot.timer
      

[#33] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/timers.target.wants/apport-autoreport.timer
      

[#34] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/timers.target.wants/apt-daily.timer
      

[#35] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/timers.target.wants/dpkg-db-backup.timer
      

[#36] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/timers.target.wants/e2scrub_all.timer
      

[#37] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/timers.target.wants/fstrim.timer
      

[#38] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/timers.target.wants/motd-news.timer
      

[#39] 07:41:17 Alert: Suspicious Process Created - File/Directory Discovery           [Audit][Passed]
      dash ─▶ stat
      Resource: /usr/bin/stat -L -c %a /etc/systemd/system/timers.target.wants/snapd.snap-repair.timer
      

[#40] 07:41:22 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ss
      Resource: /usr/bin/ss -ltnp
      

[#41] 07:41:22 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ss
      Resource: /usr/bin/ss -ltnp
      

[#42] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /sbin/ip a
      

[#43] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /sbin/ip a
      

[#44] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /sbin/ip a
      

[#45] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /snap/bin/ip a
      

[#46] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /usr/sbin/ip route
      

[#47] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /snap/bin/ip route
      

[#48] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /snap/bin/ip route
      

[#49] 07:41:23 Alert: Network Discovery Tools Blocked                                 [Block][Permission denied]
      dash ─▶ ip
      Resource: /snap/bin/ip route


```