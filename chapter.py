import re
class Chapter():
	def __init__(self, first: int, second: int=0, third: int =0, from_string: str="") -> None:
		if from_string == "":
			self.first = int(first)
			self.second = int(second)
			self.third = int(third)
		else:
			if len(from_string.split(" ")) > 1:
				raise Exception("Enter a single word, not a phrase (not supported)")
			if not self.isChapterStr(from_string):
				raise TypeError("Format of the string is not correct")

			numbers = [int(number) for number in from_string.split(".")]
			# fill  numbers with None in case not 3
			if len(numbers) < 3:
				numbers += [-1] * (3 - len(numbers))

			self.first = int(numbers[0])
			self.second = int(numbers[1])
			self.third = int(numbers[2])
				

	def __add__(self, other):
		self.first += other.first
		self.second += other.second
		self.third += other.third
		return self  
	
	def __eq__(self, other) -> bool:
		if self.first == other.first and self.second == other.second and self.third == other.third:
			return True

		return False

	def __str__(self) -> str:
		current = str(self.first)
		if self.second and not self.third:
			current += f".{self.second}"
		elif self.second and self.third:
			current += f".{self.second}.{self.third}"

		return current

	@staticmethod
	def isChapterStr(string: str, type: str = "heading") -> bool:
		"""
		type: str 
			heading = 1 or 2 or 3
			heading_1
			heading_2
			heading_3
		"""
		if type == "heading":
			# matches any integer number in those form
			# single number: 1  10  10000
			# double n: 1.2 10.1234 12.1
			# triple number: 1.2.1  30.122.34 34.34.132
			chapterRegex = re.compile(r"\d+\.\d+\.\d+|\d+\.\d+|\d+")
			searchResult = chapterRegex.search(string)
			return bool(searchResult)
			
		elif type == "heading_1":
			chapterRegex = re.compile(r"\d+")
			searchResult = chapterRegex.search(string)
			return bool(searchResult)
		
		elif type == "heading_2":
			chapterRegex = re.compile(r"\d+\.\d+")
			searchResult = chapterRegex.search(string)
			return bool(searchResult)

		elif type == "heading_3":
			chapterRegex = re.compile(r"\d+\.\d+\.\d+")
			searchResult = chapterRegex.search(string)
			return bool(searchResult)

		else:
			raise TypeError(f"Cannot parse type {type}")