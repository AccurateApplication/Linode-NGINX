
## General
* API keys stored with pass and using .envrc file
* Terraform creates VM and ansible vars/inventory, adds ~/.ssh/id_rsa.pub to authorized_keys
* Ansible role provision... provisions VM
* Ansible role webserver install nginx and opens necessary ports. Replaces default site with "blank" html

## Todo:
- [ ] Fix python script to configure DNS records
- [ ] Lets encrypt role
- [ ] MySQL/PHP install

## Links
[Terraform Linode provider](https://registry.terraform.io/providers/linode/linode/latest)
[Ansible Lets Encrypt](https://docs.ansible.com/ansible/2.5/modules/letsencrypt_module.html)
[Python Cloudflare](https://github.com/cloudflare/python-cloudflare)
