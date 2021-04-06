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

provider "linode" {
  #token = "$LINODE_TOKEN"
  token = var.API_TOKEN
}

provider "tls" {}

resource "local_file" "private_key" {
  content         = tls_private_key.ssh.private_key_pem
  filename        = var.ssh_key
  file_permission = "0600"
}

output "nanode_ip" {
  value = linode_instance.Node.ip_address
}


resource "tls_private_key" "ssh" {
  algorithm = "RSA"
  rsa_bits  = "4096"
}


resource "linode_instance" "Node" {
  label           = "John_Lennon"
  region          = var.location
  authorized_keys = ["${chomp(file("~/.ssh/id_rsa.pub"))}"]
  image           = "linode/centos8"
  type            = "g6-standard-1"
}
