# Ansible inventory file
resource "local_file" "AnsibleInventory" {
  content = templatefile("inventory.tmpl",
    {
      server-ip = linode_instance.Node.ip_address
    }
  )
  filename = "Ansible/inventory.yml"
}
