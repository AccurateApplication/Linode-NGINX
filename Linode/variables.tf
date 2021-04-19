variable "API_TOKEN" {
  description = "Api token to do stuff "
  type        = string
  sensitive   = true
}

variable "node_label" {
  description = "Will be name of node created. Will also be used in python script."
  # default     = "John_Lennon" # Change here, and in var.py file in configuredns dir
  type = string
}

variable "domain" {
  description = "Used in variable for certbot playbook"
  type        = string
  # default = "domain.org" # Change
}

variable "hostname" {
  description = "Hostname that is used for local hostname, DNS etc.."
  default     = "Gandalf"
}

variable "location" {
  description = "Which region to deploy"
  default     = "eu-central"
}
