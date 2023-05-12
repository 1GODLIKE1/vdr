import os

class VendorScripts:
    def __init__(self, RELEASE_PATH, VERSION):
        self.RELEASE_PATH = RELEASE_PATH
        self.VERSION = VERSION

    def script(self):
        full_scipts_path_list = [list for list in os.listdir(fr"{self.RELEASE_PATH}/{self.VERSION}/scripts")]
        oracle_scripts_path_list = [list for list in full_scipts_path_list if list.startswith("Oracle11")]
        if oracle_scripts_path_list != []:
            return [True, full_scipts_path_list]
        return [False, full_scipts_path_list]