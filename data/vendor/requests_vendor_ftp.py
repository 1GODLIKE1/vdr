import os
import subprocess
import psycopg2
import numpy as np
import shutil
import zipfile
import re
import logging

SELECT = ""

class RequestsFTP:
    def __init__(self, DB_USER, DB_PASS, DB_PATH, PROXY_URI, FTP_URI, RELEASE_PATH):
        self.DB_USER = DB_USER
        self.DB_PASS = DB_PASS
        self.DB_PATH = DB_PATH

        self.PROXY_URI = PROXY_URI
        self.FTP_URI = FTP_URI

        self.RELEASE_PATH = RELEASE_PATH

    def assembly(self):
        logging.info("Download arhcive from FTP")
        return RequestsFTP.check_archive_in_DB(self, RequestsFTP.get_list_archive(self))
    
    def get_list_archive(self): return subprocess.run(
        f"curl -s -x {self.PROXY_URI} {self.FTP_URI} -p -l",
        shell=True,
        stderr=subprocess.DEVNULL,
        stdout=subprocess.PIPE
    ).stdout.decode().split("\r\n")


    def check_archive_in_DB(self, *args):
        try:
            connect = psycopg2.connect(
                user = self.DB_USER,
                password = self.DB_PASS,
                host = self.DB_PATH,
                port = "5432"
            )
            cursor  = connect.cursor()
            cursor.execute(SELECT)


            not_exists = np.array([])
            for ftp in args[0]:
                if ftp != "":
                    if ftp not in [package[2] for package in cursor.fetchall()]:
                        not_exists = np.append(not_exists, ftp)
            
            if not_exists != ([]):
                if connect:
                    cursor.close()
                    connect.close()
                    logging.info("The connection to the database is closed")
                logging.info("WARNING: No new archives found on ftp")
                return False
            else:
                logging.info(f"Archive: {''.join(not_exists)}")
                for arhcives in not_exists:
                    ftp_archive = RequestsFTP.get_list_archive(self, f"{arhcives}/")
                    for arhcive in ftp_archive:
                        RequestsFTP.create_temp_dirs(self)
                        RequestsFTP.get_archives_on_ftp(self, arhcive)
                
                if connect:
                    cursor.close()
                    connect.close()
                    logging.info("The connection to the database is closed")

                return True
        except:
            logging.info("Err on database")
        

    def get_archives_on_ftp(self, *args):
        os.chdir(fr"{self.RELEASE_PATH}")
        subprocess.run(
            f"curl {self.FTP_URI}/{args[0]} --proxy {self.PROXY_URI} -p -x --output {re.sub(r'rar|RAR|ZIP', 'zip', args[0])}",
            shell=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.PIPE
        ).stdout.decode().split('\r\n')

        logging.info(f"Unpacking archive {args[0]}")
        with zipfile.ZipFile(rf"{self.RELEASE_PATH}/{re.sub(r'rar|RAR|ZIP', 'zip', args[0])}", "r") as zip_arch:
            zip_arch.extractall(fr"{self.RELEASE_PATH}")
        RequestsFTP.remove_arhives(self)

    def remove_arhives(self):
        for list in os.listdir(self.RELEASE_PATH):
            if list.endswith('.zip'):
                os.remove(fr"{self.RELEASE_PATH}/{list}")
        

    def create_temp_dirs(self):
        if not os.path.exists(fr"{self.RELEASE_PATH}"):
            os.makedirs(self.RELEASE_PATH)
        else:
            shutil.rmtree(self.RELEASE_PATH)
            os.makedirs(self.RELEASE_PATH)