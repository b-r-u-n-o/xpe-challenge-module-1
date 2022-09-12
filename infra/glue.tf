# cria database
# resource "aws_glue_catalog_database" "rais_db" {
#   name = "rais"

#   create_table_default_permission {
#     permissions = ["SELECT"]

#     principal {
#       data_lake_principal_identifier = "IAM_ALLOWED_PRINCIPALS"
#     }
#   }
# }

# # cria crawler para a tabela rais
# resource "aws_glue_crawler" "rais_crawler" {
#   database_name = aws_glue_catalog_database.rais.name
#   name          = "rais_crawler"
#   role          = aws_iam_role.rais_crawler.arn

#   s3_target {
#     path = "s3://${aws_s3_bucket.rais_crawler.bucket}"
#   }
# }

resource "aws_glue_job" "name" {
  name = "glue_job_rais"
  role_arn = ""
  description = "Job Glue para realizar pequenos ajustes na RAIS e salvar no formato parquet"
  max_retries = "1"
  timeout = 2880

  command {
    script_location = aws_s3_bucket_object.upload-python-file.key
    python_version = "3"
  }

  execution_property {
    max_concurrent_runs = 2
  }

  glue_version = "3.0"
}