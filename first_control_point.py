import logging
import sys
import os

from data.vendor.requests_vendor_ftp import RequestsFTP
from data.archive.version.release_version import Release
from data.archive.docx.read_docx_for_scripts import VendorDocx
from data.archive.script.read_scripts import VendorScripts
from data.archive.special.delete_other_special import VendorSpecial
from data.archive.xls.read_xls import VendorXls
from data.json.create_json_obj import JsonObj
from data.archive.tree.tree import Tree

REPLASES_PATH = ""
REPLASES_REPO = ""


class ControlPoint(object):
    def __init__(self, DB_USER, DB_PASS, DB_PATH, FTP_URI, PROXY_URI) -> None:
        self.DB_USER = DB_USER
        self.DB_PASS = DB_PASS
        self.DB_PATH = DB_PATH
        self.FTP_URI = FTP_URI
        self.PROXY_URI = PROXY_URI

        self.RELEASE_PATH = os.getcwd().replace(REPLASES_PATH, "").replace(REPLASES_REPO, "tmp")
        
    def point(self):
        logging.info("Start build vendor release")
        
        if RequestsFTP(self.DB_USER, self.DB_PASS, self.DB_PATH, self.PROXY_URI, self.FTP_URI, self.RELEASE_PATH).assembly():
            ALL_ARCHIVES = os.listdir(self.RELEASE_PATH)
            RELEASE_VERSION = Release(self.RELEASE_PATH).release()

            logging.info(f"Release version is 5.06.{RELEASE_VERSION}.000")
            os.makedirs(fr"{self.RELEASE_PATH}/5.06.{RELEASE_VERSION}.000/devops")
            

            oracle_exists_obj = {
                "RELEASE_VERSION": RELEASE_VERSION,
                "ALL_ARCHIVES": ALL_ARCHIVES
            }

            tree_extend_obj = {}
            
            for archive in ALL_ARCHIVES:
                VendorSpecial(self.RELEASE_PATH, archive)        
                scripts_path = VendorScripts(self.RELEASE_PATH, archive).script() 
                if scripts_path[0]:
                    logging.info(f"Oracle11 files found in the archive {archive}")
                docx_obj = VendorDocx(self.RELEASE_PATH, archive, scripts_path[1]).docx()
                xls_obj = VendorXls(self.RELEASE_PATH, archive).xls()
                tree_obj = Tree(self.RELEASE_PATH, archive)

                oracle_exists_obj[archive] = [
                    docx_obj,
                    xls_obj 
                ]

                tree_extend_obj[archive] = tree_obj

            JsonObj(self.RELEASE_PATH, f"5.06.{RELEASE_VERSION}.000", oracle_exists_obj, 'data').obj()
            JsonObj(self.RELEASE_PATH, )
            logging.info("The json object has been pumped out, please consider it !")
        else: logging.info('WARNING: No new archives were found on the FTP server')

            
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
        stream=sys.stdout
    )

    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_PATH = sys.argv[3]
    FTP_URI = sys.argv[4]
    PROXY_URI = sys.argv[5]

    ControlPoint(DB_USER, DB_PASS, DB_PATH, FTP_URI, PROXY_URI).point()