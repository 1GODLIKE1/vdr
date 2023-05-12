import pandas as pd


class VendorXls:
    def __init__(self, RELEASE_PATH, VERSION):
        self.RELEASE_PATH = RELEASE_PATH
        self.VERSION = VERSION

    def xls(self):
        df = pd.read_excel(
            fr"{self.RELEASE_PATH}/{self.VERSION}/docs/Перечень_изменений_{self.VERSION}.xls",
            skiprows=7
        ).to_numpy()
        
        xls_obj = {}

        count = 0
        for data in df:
            xls_obj[count] = {
                "№": data[0],
                "type": data[1],
                "Direction": data[2],
                "Description": data[5],
                "Scripts": data[6],
                "BBR": data[7],
                "Configure": data[8],
                "Modules": data[9],
                "DDL": data[10],
                "Documents": data[11]
            }

            count += 1

        return xls_obj