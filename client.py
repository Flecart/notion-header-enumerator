import requests
import os
import json

class NotionClient():
    def __init__(self, version: str ="2021-08-16") -> None:
        token = os.environ['API_KEY']

        self.headers = {
            'Authorization': f"Bearer {token}",
            'Notion-Version': version,
        }

        self.token = token

    # REGION PAGES AND BLOCKS
    def getPage(self, pageId: str):
        response = requests.get(f"https://api.notion.com/v1/pages/{pageId}", headers=self.headers)
        return json.loads(response.text)

    def getBlock(self, blockId: str):
        response = requests.get(f"https://api.notion.com/v1/blocks/{blockId}", headers=self.headers)
        return json.loads(response.text)

    def getBlockChildren(self, blockId: str, start_cursor: str =None, page_size: int=None):
        data = {
            "start_cursor": start_cursor,
            "page_size": page_size
        }
        response = requests.get(f"https://api.notion.com/v1/blocks/{blockId}/children", headers=self.headers, params=data)
        return json.loads(response.text)

    # TODO: if you want to make it more dinamic create a updater class with needed functionalities
    def updateTextBlock(self, blockId: str, text: str, type: str):
        data = {
            type: {
                "text": [{
                    "text": {
                        "content": text
                    }
                }]
            }
        }
        newHeader = self.headers
        newHeader['Content-Type'] = "application/json"
        response = requests.patch(f"https://api.notion.com/v1/blocks/{blockId}", headers=newHeader, data=json.dumps(data))
        return json.loads(response.text)

    # REGION USERS
    def getUsers(self):
        response = requests.get('https://api.notion.com/v1/users', headers=self.headers)
        return json.loads(response.text)

    def getBotUser(self):
        response = requests.get("https://api.notion.com/v1/users/me", headers=self.headers)
        return json.loads(response.text)

    def search(self, query: object, filter: str =None, sort: str =None):
        data = {
            "query": query,
            "sort": sort,
            "filter": filter
        }

        response = requests.post('https://api.notion.com/v1/search', headers=self.headers, data=data)
        return json.loads(response.text)

    # DEPRECATED API
    def getDatabases(self):
        response = requests.get("https://api.notion.com/v1/databases", headers=self.headers)
        return json.loads(response.text)

    def getDatabase(self, databaseId: str):
        response = requests.get(f"https://api.notion.com/v1/databases/{databaseId}", headers=self.headers)
        return json.loads(response.text)

