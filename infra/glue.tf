# cria database
resource "aws_glue_catalog_database" "rais_db" {
  name = "rais"

  create_table_default_permission {
    permissions = ["SELECT"]

    principal {
      data_lake_principal_identifier = "IAM_ALLOWED_PRINCIPALS"
    }
  }
}

# cria crawler para a tabela rais
resource "aws_glue_crawler" "rais_crawler" {
  database_name = aws_glue_catalog_database.rais.name
  name          = "rais_crawler"
  role          = aws_iam_role.rais_crawler.arn

  s3_target {
    path = "s3://${aws_s3_bucket.rais_crawler.bucket}"
  }
}