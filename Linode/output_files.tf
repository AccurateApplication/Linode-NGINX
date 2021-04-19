# Ansible inventory file
#data "linode_profile" "profile" {}
data "linode_account" "account" {}
resource "local_file" "AnsibleInventory" {
  content = templatefile("inventory.tmpl",
    {
      server-ip = linode_instance.Node.ip_address
    }
  )
  filename = "Ansible/inventory.yml"
}

# Ansible inventory file
resource "local_file" "AnsibleVariables" {
  content = templatefile("variables.tmpl",
    {
      email = data.linode_profile.me.email
      domain = var.domain

    }
  )
  filename = "Ansible/group_vars/all/vars.yml"
}
