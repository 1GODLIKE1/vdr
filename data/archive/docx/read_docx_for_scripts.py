import docx
import numpy as np
import re
import os


class VendorDocx:
    def __init__(self, RELEASE_PATH, VERSION, SCRIPTS_PATH):
        self.RELEASE_PATH = RELEASE_PATH
        self.VERSION = VERSION
        self.SCRIPTS_PATH = SCRIPTS_PATH

    def docx(self):
        VendorDocx.rename_all_file_in_doc_path(self)
        doc = docx.Document(fr"{self.RELEASE_PATH}/{self.VERSION}/docs/Инструкция_по_установке_{self.VERSION}.docx")
        all_txt = np.array([])
        for paragrapg in doc.paragraphs:
            all_txt = np.append(all_txt, paragrapg)

        json_obj = {
            "scripts_path": self.SCRIPTS_PATH
        }

        ignore = []
        ignore_elem = []
        count = 0
        for text in all_txt:
            if re.findall('Установка скриптов для банков', text) != []:
                vendor_scripts = VendorDocx.docx_scripts(self, all_txt, text, ignore)
                ignore.append(text)
                json_obj[count] = {
                    "install": text,
                    "scripts": vendor_scripts[sum(ignore_elem):]
                }
                ignore_elem.append(len(vendor_scripts))
                count += 1
        return json_obj        

    def docx_scripts(self, *args):
        all_scripts = []
        for script in args[0]:
            if str(script).endswith('.sql'):
                all_scripts.append(script)
            elif re.findall('Установка скриптов для банков', script):
                if script not in args[2]:
                    if script != args[1]:
                        break
        return all_scripts

    def rename_all_file_in_doc_path(self):
        for file in os.listdir(fr"{self.RELEASE_PATH}/{self.VERSION}/docs"):
            os.rename(
                fr"{self.RELEASE_PATH}/{self.VERSION}/docs/{file}", 
                fr"{self.RELEASE_PATH}/{self.VERSION}/docs/{file.replace('', '_')}"
            )
            