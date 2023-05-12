import json


class JsonObj:
    def __init__(self, RELEASE_PATH, RELEASE_VERSION, OBJECTS):
        self.RELEASE_PATH = RELEASE_PATH
        self.RELEASE_VERSION = RELEASE_VERSION
        self.OBJECTS = OBJECTS
        

    def obj(self):
        with open(fr'{self.RELEASE_PATH}/{self.RELEASE_VERSION}/devops/data.json', 'w', encoding='utf-8') as f:
            json.dump(self.OBJECTS, f, ensure_ascii=False, indent=4)