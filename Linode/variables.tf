variable "ACCOUNT_USERNAME" {
  description = "Account username for Linode"
  type        = string
  sensitive   = true
}

variable "ACCOUNT_PASSWORD" {
  description = "Account password for Linode"
  type        = string
  sensitive   = true
}

variable "API_TOKEN" {
  description = "Api token to do stuff "
  type        = string
  sensitive   = true
}

variable "hostname" {
  description = "Hostname that is used for local hostname, DNS etc.."
  default     = "Gandalf"
}

variable "location" {
  description = "Which region to deploy"
  default     = "eu-central"
}

variable "ssh_key" {
  description = "SSH-key that is generated"
  default     = "PrivateLinode.pem"
}

variable "ssh_key_path" {
  description = "Path to SSH key that is used"
  default     = "./PrivateLinode.pem"
}
