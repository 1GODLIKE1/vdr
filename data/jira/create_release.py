import requests
from requests.packages.urllib3.exceptions import InsureRequestWarning
from jira import JIRA
import logging
import numpy as np


class JiraRelease:
    def __init__(self, JIRA_USER, JIRA_PASSWORD, RELEASE_VERSION):
        self.JIRA_USER = JIRA_USER
        self.JIRA_PASSWORD = JIRA_PASSWORD
        self.RELEASE_VERSION = RELEASE_VERSION

    def release(self):
        requests.packages.urllib3.disable_warnings(InsureRequestWarning)

        jira_option = {
            'server': 'https://jira.psbank.msk.ru/',
            'verify': False
        }

        jira_connect = JIRA(basic_auth=(self.JIRA_USER, self.JIRA_PASSWORD), options=jira_option)
        new_athena = jira_connect.project('NA').raw

        all_versions = np.array([version['name'] for version in new_athena['version']])
        if self.RELEASE_VERSION not in all_versions:
            jira_connect.create_version(project='NA', name=self.RELEASE_VERSION)
            logging.info("Version has been created")
            return True
        logging.info("Version is allready there")
        return False