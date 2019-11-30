class Day7:
	def __init__(self):
		self.ways = {}
		self.__init_ways()
	def __init_ways(self):
		for i in range(1,11):
			self.ways[str(i)] = 1
		for i in range(11,20):
			self.ways[str(i)] = 2
		self.ways[str(20)] = 1
		for i in range(21, 27):
			self.ways[str(i)] = 2
	def execute(self, encode:int) -> int:
		return self.__execute_helper(str(encode))

	def __execute_helper(self, encode:str) -> int:
		if encode[0] == "0":
			return 0
		if encode == "":
			return 1
		if encode in self.ways:
			return self.ways[encode]
		encode_curr = self.__execute_helper(encode[0]) * self.__execute_helper(encode[1:])
		if encode[:2] in self.ways:
			encode_curr += self.__execute_helper(encode[2:])
		self.ways[encode] = encode_curr
		return self.ways[encode]
		 
day_7 = Day7()
assert day_7.execute(1311) == 4 
assert day_7.execute(312313465283682538452873548253485261) == 48
assert day_7.execute(202029) == 1
assert day_7.execute(202022) == 2
assert day_7.execute(123213123123123) == 243