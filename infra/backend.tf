# Configura o backend para o S3
terraform {
  backend "s3" {
    bucket = "terraform-dl-edc-2022" # arn:aws:s3:::terraform-dl-edc-2022
    key = "state/igti/mod1/terraform.tfstate" # objeto do s3 "camada/divisão"
    region = "us-east-1"
  }
}