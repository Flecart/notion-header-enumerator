from configparser import ConfigParser
import requests
from requests.api import head
from requests.models import Response

class NotionClient():
	def __init__(self, version: str ="2021-08-16") -> None:
		config = ConfigParser()
		config.read("config.ini")
		token = config['NOTION']['key']

		self.headers = {
			'Authorization': f"Bearer {token}",
			'Notion-Version': version,
		}

		self.token = token

	def getPage(self, pageId: str):
		response = requests.get(f"https://api.notion.com/v1/pages/{pageId}", headers=self.headers)
		return response

	def getBlock(self, blockId: str):
		response = requests.get(f"https://api.notion.com/v1/blocks/{blockId}", headers=self.headers)
		return response

	def getUsers(self):
		response = requests.get('https://api.notion.com/v1/users', headers=self.headers)
		return response

	def getBotUser(self):
		response = requests.get("https://api.notion.com/v1/users/me", headers=self.headers)
		return response

	def search(self, query, filter=None, sort=None):
		data = {
			"query": query,
			"sort": sort,
			"filter": filter
		}

		response = requests.post('https://api.notion.com/v1/search', headers=self.headers, data=data)
		return response

	# DEPRECATED API
	def getDatabases(self):
		response = requests.get("https://api.notion.com/v1/databases", headers=self.headers)
		return response

	def getDatabase(self, databaseId: str):
		response = requests.get(f"https://api.notion.com/v1/databases/{databaseId}", headers=self.headers)
		return response