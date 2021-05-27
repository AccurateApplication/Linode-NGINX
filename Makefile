##
# Linode-NGINX
#
# @file
# @version 0.1


help: ## help
	@grep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: build
build: ## terraform apply
	terraform apply -auto-approve
	python ./configureDNS/main.py
	ansible-playbook -i ./Ansible/inventory.yml ./Ansible/provision.yml
	ansible-playbook -i ./Ansible/inventory.yml ./Ansible/webserver.yml
	ansible-playbook -i ./Ansible/inventory.yml ./Ansible/certbot.yml

.PHONY: destroy
destroy: ## terraform destroy
	terraform destroy -auto-approve
	./configureDNS/remove_a_records.py


# end
