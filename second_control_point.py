import logging
import sys
import os
import json

REPLASES_PATH = ""
REPLASES_REPO = ""
 
class ControlPoint(object):
    def __init__(self, JIRA_USER, JIRA_PASSWORD, JSON_DUMP, DB_USER, DB_PASS, DB_PATH):
        self.JIRA_USER = JIRA_USER
        self.JIRA_PASSWORD = JIRA_PASSWORD
        self.JSON_DUMP = json.loads(JSON_DUMP)

        self.DB_USER = DB_USER
        self.DB_PASS = DB_PASS
        self.DB_PATH = DB_PATH


        self.RELEASE_PATH = os.getcwd().replace(REPLASES_PATH, "").replace(REPLASES_REPO, "tmp")

    def point(self):
        pass


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s %(message)s",
        datefmt="%d/%b/%Y %H:%M:%S",
        stream=sys.stdout
    )

    JIRA_USER = sys.argv[1]
    JIRA_PASSWORD = sys.argv[2]
    JSON_DUMP = sys.argv[3]

    DB_USER = sys.argv[4]
    DB_PASS = sys.argv[5]
    DB_PATH = sys.argv[6]

    ControlPoint(JIRA_USER, JIRA_PASSWORD, JSON_DUMP, DB_USER, DB_PASS, DB_PATH)