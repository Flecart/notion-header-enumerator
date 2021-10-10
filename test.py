import unittest
from client import NotionClient

class Test(unittest.TestCase):
	# These are not usefull, just to see if i cant change
	client = NotionClient()

	block = client.getBlock("d6396981d13b40f48adaafcfd734bfb0")
	print(block.text)
	user = client.getUsers()
	print(user.text)
	botUser = client.getBotUser()
	print(botUser.text)
	search = client.search("b")
	print(search.text)
	page = client.getPage("d6396981d13b40f48adaafcfd734bfb0")
	print(page.text)
	database = client.getDatabases()
	print(database.text)

	getDatabase = client.getDatabase("206c30e4fb4f476f8d0b1f39c8064f26")
	print(getDatabase.text)