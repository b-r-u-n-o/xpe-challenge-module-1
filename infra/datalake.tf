# Iniciar o desenvolvimento de novos recursos na AWS com IaC 

# Cria bucket para o nosso datalake
resource "aws_s3_bucket" "teste-datalake" {
    bucket = "${var.bucket_name}-${var.enviroment}"
    acl = "private"

    server_side_encryption_configuration {
      rule {
        apply_server_side_encryption_by_default {
          sse_algorithm = "AES256"
        }
      }
    }

    tags = {
        bootcamp = "xpe",
        curso = "edc"
    }
}

