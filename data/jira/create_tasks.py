import requests
from requests.packages.urllib3.exceptions import InsureRequestWarning
from jira import JIRA
import logging
import numpy as np


class JiraTask:
    def __init__(self, JIRA_USER, JIRA_PASSWORD, RELEASE_VERSION, JSON_TASK, RELEASE_DATE):
        self.JIRA_USER = JIRA_USER
        self.JIRA_PASSWORD = JIRA_PASSWORD
        self.RELEASE_VERSION = RELEASE_VERSION
        self.JSON_TASK = JSON_TASK
        self.RELEASE_DATE = RELEASE_DATE

    def task(self):
        requests.packages.urllib3.disable_warnings(InsureRequestWarning)

        jira_option = {
            'server': 'https://jira.psbank.msk.ru/',
            'verify': False
        }

        jira_connect = JIRA(basic_auth=(self.JIRA_USER, self.JIRA_PASSWORD), options=jira_option)

        issue_dict = {
            "fixVersions": [
                {
                    "name": self.RELEASE_VERSION,
                    "releaseDate": self.RELEASE_DATE
                }
            ],
            "components": [
                {
                    "id": "14123",
                    "name": "Анализ патча"
                }
            ],
            "status": {
                "descriptions": "Согласование документов, работ",
                "name": "Согласование"
            },
            "project": {
                "key": "NA",
                "name": "Новая Афина"
            },
            "reporter": {
                "name": "regwork",
                "key": "regwork",
                "emailAddress": "noreply@psbank.ru",
                "active": True,
                "timeZone": "Europe/Moscow"
            },
            "issuetype": {
                "id": "6",
                "name": "Вопрос",
                "subtask": False,
                "description": "Вопросы и проблемы проекта"
            },
            "assignee": {
                "name": 
            }
        }

