#!/usr/bin/env bash
while true; do
    read -p "Want to build terraform managed infra and add DNS A records? (y/n) " yn
    case $yn in
        [Yy]* ) \
            terraform apply -auto-approve; \
            python ./configureDNS/main.py; \
            ansible-playbook -i ./Ansible/inventory.yml ./Ansible/provision.yml; \
            ansible-playbook -i ./Ansible/inventory.yml ./Ansible/webserver.yml; \
            ansible-playbook -i ./Ansible/inventory.yml ./Ansible/certbot.yml \
            ; break;;

        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
