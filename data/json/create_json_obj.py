import json


class JsonObj:
    def __init__(self, RELEASE_PATH, RELEASE_VERSION, OBJECTS, NAME):
        self.RELEASE_PATH = RELEASE_PATH
        self.RELEASE_VERSION = RELEASE_VERSION
        self.OBJECTS = OBJECTS
        self.NAME = NAME

    def obj(self):
        with open(fr'{self.RELEASE_PATH}/{self.RELEASE_VERSION}/devops/{self.NAME}.json', 'w', encoding='utf-8') as f:
            json.dump(self.OBJECTS, f, ensure_ascii=False, sort_keys=False, indent=4)