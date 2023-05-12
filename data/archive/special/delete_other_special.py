import os
import shutil


class VendorSpecial:
    def __init__(self, RELEASE_PATH, VERSION):
        self.RELEASE_PATH = RELEASE_PATH
        self.VERSION = VERSION

    def special(self):
        for list in os.listdir(fr"{self.RELEASE_PATH}/{self.VERSION}/special"):
            if list != 'psv':
                shutil.rmtree(fr"{self.RELEASE_PATH}/{self.VERSION}/special/{list}")