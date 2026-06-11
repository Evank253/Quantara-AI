Terraform placeholder: IBM Cloud + Cloudflare provider stubs
Fill provider configs and variables before running terraform init / apply.
terraform {
  required_version = ">= 1.0"
}
provider "ibm" {
configure with your IBM Cloud provider block
}
provider "cloudflare" {
configure with your Cloudflare provider block
}
resource "null_resource" "placeholder" {}
