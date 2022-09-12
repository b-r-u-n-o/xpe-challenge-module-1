resource "aws_glue_job" "job-rais-parquet" {
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