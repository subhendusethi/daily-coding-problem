from typing import List
VectorInt = List[int]

'''
	Time Complexity: O(N*LEN(k_arr))
	Space Complexity: O(N)
'''
class Day12:
	def __init__(self):
		self.dp = None
	def execute(self, N:int, k_arr:VectorInt=[1,2]) -> int:
		self.dp = []
		for i in range(N+1):
			self.dp.append(0)
		for i in range(1, N+1):
			for k in k_arr:
				if i == k:
					self.dp[i]+= 1
				if i > k:
					self.dp[i] += self.dp[i-k]
		return self.dp[N]

day_12 = Day12()
assert day_12.execute(4, [1,2,3]) == 7
assert day_12.execute(4) == 5
assert day_12.execute(4, [1]) == 1
assert day_12.execute(6, [2,3]) == 2