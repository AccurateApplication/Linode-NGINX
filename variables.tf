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
