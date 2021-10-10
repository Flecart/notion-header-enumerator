from client import NotionClient


def main():
	client = NotionClient()

	# block = client.getBlock("d6396981d13b40f48adaafcfd734bfb0")
	# print(block.text)
	# user = client.getUsers()
	# print(user.text)
	# botUser = client.getBotUser()
	# print(botUser.text)
	# search = client.search("b")
	# print(search.text)
	# page = client.getPage("d6396981d13b40f48adaafcfd734bfb0")
	# print(page.text)
	# database = client.getDatabases()
	# print(database.text)

# [Note Uni](https://www.notion.so/206c30e4fb4f476f8d0b1f39c8064f26)
	getDatabase = client.getDatabase("206c30e4fb4f476f8d0b1f39c8064f26")
	print(getDatabase.text)

if __name__ == "__main__":
	main()