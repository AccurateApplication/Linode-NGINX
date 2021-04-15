variable "API_TOKEN" {
  description = "Api token to do stuff "
  type        = string
  sensitive   = true
}

variable "node_label" {
  description = "Will be name of node created. Will also be used in python script."
  default     = "John_Lennon"
  type        = string
}

variable "hostname" {
  description = "Hostname that is used for local hostname, DNS etc.."
  default     = "Gandalf"
}

variable "location" {
  description = "Which region to deploy"
  default     = "eu-central"
}

#variable "USER_EMAIL" {
#  default = ["${data.linode_profile.me.email}"]
#  #type      = string
#  sensitive = true
#}

