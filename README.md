## What it does
* Terraform creates VM and ansible vars/inventory, adds public ssh key (~/.ssh/id_rsa.pub) to authorized_keys on VM.
* Ansible role provision provisions Linode node.
* Ansible role webserver install nginx and opens necessary ports. Replaces default site with basic HTML site.
* Ansible role certbot install configures pip env and installs and runs certbot pip package to enable HTTPS with lets encrypt.
* Python script in configureDNS adds linode instance IP to cloudflare. (type A record).
* API keys stored with pass and using .envrc file (enviroment variables).


## Variables to set
* Domain in variables.tf file.
* Linode node label in variables.tf file.
* Domain in configureDNS/var.py(.example).
* Linode node label in configureDNS/var.py(.example).
* Cloudflare API key in .envrc file. Either using pass (preferred) or plain text.
* Linode API key .envrc file. Either using pass (preferred) or plain text.

Linode key needs read access to IP's, read/write to Linodes and read to account.
Cloudflare key needs read access to your domain zone and edit DNS of the zone.

I tried to have as little static variables that needs to be set as possible.





## Links
[Terraform Linode provider](https://registry.terraform.io/providers/linode/linode/latest)

[Certbot pip](https://pypi.org/project/certbot/)

[Python Cloudflare](https://github.com/cloudflare/python-cloudflare)
