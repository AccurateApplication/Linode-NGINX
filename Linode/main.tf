terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "1.16.0"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "3.0.0"
    }
  }
}

data "linode_profile" "me" {}

provider "linode" {
  token = var.API_TOKEN

}

output "nanode_ip" {
  value = linode_instance.Node.ip_address
}

resource "linode_sshkey" "ssh_key" {
  label   = "john"
  ssh_key = chomp(file("~/.ssh/id_rsa.pub"))
}

resource "linode_instance" "Node" {
  label           = var.node_label
  region          = var.location
  authorized_keys = ["${linode_sshkey.ssh_key.ssh_key}"]
  image           = "linode/centos8"
  type            = "g6-standard-1"


  connection {
    type = "ssh"
    user        = "root"
    host = linode_instance.Node.ip_address
    private_key = "${file("~/.ssh/id_rsa")}"
  }

  provisioner "remote-exec" {
    inline = [
      "echo ssh_up"
    ]
}
}
