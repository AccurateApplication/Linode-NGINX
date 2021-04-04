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

resource "local_file" "private_key" {
  content         = tls_private_key.ssh.private_key_pem
  filename        = "PrivateLinode.pem"
  file_permission = "0600"
}

output "nanode_ip" {
  value = linode_instance.LucasLinodeInstance.ip_address
}

#resource "Public_SSH_Key" "LucasLinodeInstance" {
#  label   = "LucasLinodeInstance"
#  ssh_key = chomp(file("~/.ssh/id_rsa.pub"))
#}
provider "tls" {}

resource "tls_private_key" "ssh" {
  algorithm = "RSA"
  rsa_bits  = "4096"
}

resource "linode_instance" "LucasLinodeInstance" {
  label           = "example_instance"
  region          = "eu-central"
  authorized_keys = [chomp(tls_private_key.ssh.public_key_openssh)]
  image           = "linode/centos8"
  type            = "g6-standard-1"

}

