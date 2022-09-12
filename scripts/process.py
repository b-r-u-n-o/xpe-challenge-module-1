#!/usr/bin/env python3
import logging
import os
from pathlib import Path
import boto3
from botocore.exceptions import ClientError

# from ftplib import FTP


# def extract_file_ftp(url: str, file: str):
#     ftp = FTP(url)
#     ftp.login()
#     ftp.retrlines("LIST")

#     file_name = file

#     with open(f"{file_name}", mode="wb") as archive:
#         ftp.retrbinary(f"RETR {file_name}", archive.write)

#     ftp.quit()

import zipfile

z = zipfile.ZipFile("final.zip", "w", zipfile.ZIP_DEFLATED)
z.write("file1.txt")
z.write("file2.txt")
z.close()


def upload_file_s3(name_file: str, bucket: str, obj_name=None) -> bool:
    """_summary_

    Args:
        name_file (str): nome do arquivo
        bucket (str): nome do bucket
        obj_name (str, optional): destino do dado no bucket. Caso não seja
            fornecido o nome do arquivo será utilizado.Padrão None.

    Returns:
        bool: True em caso de sucesso e False para caso de falha.
    """
    if obj_name is None:
        obj_name = os.path.basename(name_file)

    s3 = boto3.client("s3")

    try:
        s3.upload_file(name_file, bucket, obj_name)

    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    # Configura a saída dos logs
    logging.basicConfig(format="%(asctime)s - %(message)s:", level=logging.INFO)
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)

    # define as constantes utilizadas nas funções
    # URL = "ftp://ftp.mtps.gov.br/pdet/microdados/"
    PREFIX_PATH = "./data/"
    FILE_NAME = "RAIS_ESTAB_PUB.txt"
    PATH_FILE_NAME = f"{PREFIX_PATH}{FILE_NAME}"
    # TARGET_PATH = f"{PREFIX_PATH}{SUFIX_PATH}"
    BUCKET = ""
    OBJ_NAME = ""
    logger.info("Constantes criadas")

    # faz o upload para do arquivo para o bucket
    upload_file_s3(name_file=PATH_FILE_NAME, bucket=BUCKET, obj_name=OBJ_NAME)
    logger.info(f"Upload realizado com sucesso: {BUCKET}-{OBJ_NAME}")
    logger.info("Processo de EL finalizado com sucesso!")


if __name__ == "__main__":
    main()
