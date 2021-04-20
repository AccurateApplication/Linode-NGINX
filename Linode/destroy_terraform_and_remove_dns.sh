#!/usr/bin/env bash
while true; do
    read -p "Want to destroy terraform managed infra and remove type A DNS records? (y/n) " yn
    case $yn in
        [Yy]* ) \
            terraform destroy ; \
            ./configureDNS/remove_a_records.py \
            ; break;;

        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
