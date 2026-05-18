# Enable BPF LSM
sudo sed -i 's/GRUB_CMDLINE_LINUX=""/GRUB_CMDLINE_LINUX="lsm=lockdown,capability,landlock,yama,apparmor,bpf"/' /etc/default/grub
sudo update-grub

echo "BPF LSM enabled. Reboot to activate."
