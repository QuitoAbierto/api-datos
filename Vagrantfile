# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = 'ubuntu/trusty64'
  config.vm.network'forwarded_port', guest: 5000, host: 5000
  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'provision/playbook.yml'
  end
end
