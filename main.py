import json
from chapter import Chapter
from client import NotionClient
import argparse
from typing import Union

# TODO: create types for Notion responses
client = NotionClient()

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("pageId", type=str, help="Input the Notion pageId")
	parser.add_argument("-n", "--number", type=int, help="Add the number you want to change the first numbered header to") 
	args = parser.parse_args()
	updateHeaders(args.pageId, args.number)


def updateHeaders(pageId: str, chapterNumber: Union[int, None] = None) -> None:
	supportedTypes = ['heading_1', 'heading_2', 'heading_3']

	startingBlockNumber = getFirstNumberBlock(pageId)
	if startingBlockNumber == False:
		print("There is no heading with the first number in page with ID: " + pageId)
		return 

	if chapterNumber:
		oldChapter = Chapter(first=chapterNumber)
	else:
		oldChapter = Chapter(first=getFirstNumber(startingBlockNumber))

	start_cursor = startingBlockNumber
	while True:
		responseObject = client.getBlockChildren(pageId, start_cursor=start_cursor)
		blockList = responseObject['results']
		# TODO: this is too much indentation
		# should simplify with a new function
		# the problem is how to name the new f
		for block in blockList:
			type = block['type']
			if type in supportedTypes:
				oldChapter = updateBlock(block, oldChapter)

		if not responseObject["has_more"]:
			break
		start_cursor = responseObject['next_cursor']
	return


def updateBlock(block, oldChapter: Chapter) -> Chapter:
	"""
	Updates the current notion block with the chapter,
	returns the new updated chapter to keep track of the progress
	"""
	type = block['type']
	currentChapter = setChapter(oldChapter, type)

	if isSameChapter(currentChapter, block):
		print(f"Heading with chapter {block[type]['text'][0]['plain_text']} is the same")
		return currentChapter
		
	oldHeading = getOldHeadingText(block)

	newHeading = f"{str(currentChapter)} {oldHeading}"
	client.updateTextBlock(block['id'], text=newHeading, type=type)
	print(f"Updating block with old text '{block[type]['text'][0]['plain_text']}' to '{newHeading}'")

	return currentChapter


def isSameChapter(currentChapter, block):
	listOfWords = getListOfWords(block)
	if Chapter(from_string=listOfWords[0]) == currentChapter:
		return True

	return False


def getOldHeadingText(block) -> str:
	listOfWords = getListOfWords(block)

	# filter the first word if it's a header content
	if Chapter.isChapterStr(listOfWords[0], block['type']):
		return " ".join(listOfWords[1::])

	return " ".join(listOfWords)

def getListOfWords(block):
	type = block['type']
	blockText = block[type]['text'][0]['plain_text']
	listOfWords = blockText.split(" ")
	return listOfWords

def setChapter(currentChapter: Chapter, type: str) -> Chapter:
	"""
	type: str 
		heading_1
		heading_2
		heading_3
	"""
	if type == "heading_1":
		currentChapter = Chapter(first=currentChapter.first + 1)
	elif type == "heading_2":
		currentChapter = Chapter(first=currentChapter.first, second=currentChapter.second + 1)
	elif type == "heading_3":
		currentChapter = Chapter(first=currentChapter.first, second=currentChapter.second, third=currentChapter.third + 1)
	else:
		raise TypeError(f"The type identified with { type } does not exist")

	return currentChapter

		
def getFirstNumber(firstNumberBlock: str) -> int:
	block = client.getBlock(firstNumberBlock)
	blockText = block['heading_1']['text'][0]['plain_text']
	return blockText.split(" ")[0]


def getFirstNumberBlock(pageId: str):
	""" Gets the first 10 block and looks for  the header with number """
	responseObject = client.getBlockChildren(pageId, page_size=10)

	if 'code' in responseObject:
		print(json.dumps(responseObject, indent=4, sort_keys=True))
		return False 

	blockList = responseObject['results']

	for block in blockList:
		if hasH1FirstNumber(block):
			return block['id']

	return False


def hasH1FirstNumber(block):
	if not "heading_1" in block:
		return False
		
	content = block['heading_1']['text'][0]['plain_text']
	firstWord = content.split(" ")[0]
	if Chapter.isChapterStr(firstWord, "heading_1"):
		return True

	return False


if __name__ == "__main__":
	main()
