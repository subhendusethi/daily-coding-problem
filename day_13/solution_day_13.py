class Day13:
	'''
		Time Complexity: O(LENGTH(S))
		Space Complexity: O(SYMBOL[S]))
		S : Given string
	'''
	def __calc_dist_chars(self, window_map):
		res = 0
		for key in window_map:
			if window_map[key] > 0:
				res+=1
		return res

	def execute(self, string:str, k:int) -> int:
		if len(string) < k:
			return len(string)
		start,end = 0,0
		if k <= 0:
			print("Invalid k. k should be > 0.")
			exit(0)
		window_map = {}
		string_len = len(string)
		max_chars = 0
		window_map[string[0]] = 1
		while start < string_len and end < string_len:
			number_of_distinct_chars = self.__calc_dist_chars(window_map)
			if number_of_distinct_chars <= k:
				max_chars = max(max_chars, end-start+1)
				end+=1
				if end < string_len:
					char = string[end]
					if char not in window_map:
						window_map[char] = 0
					window_map[char] += 1
			else:
				char = string[start]
				window_map[char]-=1
				if window_map[char] == 0:
					del window_map[char]
				start+=1
		return max_chars

day_13 = Day13()

assert day_13.execute("abcbaaaaaaaaaaaacbbbbbbbbbbbbbbbbbbbbb", 2) == 22
assert day_13.execute("abcba", 2) == 3
assert day_13.execute("abcbaaaaaaaaaaaacbbbbbbbbbbbbbbbbbbbbb", 4) == 38
assert day_13.execute("dbcbaaaaaaaaaaaacbbbbbbbbbbbbbbbbbbbbb", 3) == 37
assert day_13.execute("qwerty", 3) == 3
assert day_13.execute("", 1) == 0
assert day_13.execute("poilkjqwerty", 12) == 12
assert day_13.execute("poilkjqwerty", 100) == 12