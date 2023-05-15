import logging
import sys
import os

REPLASES_PATH = ""
REPLASES_REPO = ""

class ControlPoint(object):
    def __init__(self, JIRA_USER, JIRA_PASSWORD):
        self.JIRA_USER = JIRA_USER
        self.JIRA_PASSWORD = JIRA_PASSWORD

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

    JIRA_USER = sys.argv[0]
    JIRA_PASSWORD = sys.argv[1]
    RELEASE_CONFIG_PATH = sys.argv[2]

    JSON_ORACLE_DUMP = sys.argv[3]
    JSON_FILE_DUMP = sys.argv[4]
    