import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

# @params:['JOB_NAME']
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args['JOB_NAME'], args)

enem = (
    spark
    .read
    .format('csv')
    .option('header', True)
    .option('inferSchema', True)
    .option('delimiter', ';')
    .load('s3//...')
)

(
    enem
    .write
    .mode('overwrite')
    .format('parquet')
    .partitionBy('NU_ANO')
    .save('s3//...')
)

# acrescentar na policy a role de deleção de objeto para o glue no S3
