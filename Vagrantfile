# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below.
# The "2" in Vagrant.configure configures the configuration version.
Vagrant.configure("2") do |config|

  # Every Vagrant development environment requires a box.
  # You can search for boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/impish64"

  # Define the VM.
  config.vm.define "ubuntu"

  # Create a private network with static IP address.
  config.vm.network "private_network", ip: "10.10.10.20"

  # VirtualBox specific configurations.
  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 1
    vb.memory = 1024
    vb.name = "Ubuntu"
    vb.customize ["modifyvm", :id, "--cpuexecutioncap", 100]
  end

  # Enable provisioning with Ansible playbook.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.groups = {
      "virtualbox" => ["ubuntu"]
    }
  end
end