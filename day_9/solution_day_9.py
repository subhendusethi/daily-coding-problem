from typing import List
VectorInt = List[int]
min_neg = -999999999999999
'''
	Time Complexity: O(N)
	Space Complexity: O(N) [Can be reduced to O(1) by tracking dp[i-1](0,1) and dp[i-2](0,1) for i]
	N : Number of elements in the array.
	To Test submission: https://leetcode.com/problems/house-robber/
'''
class Day9:
	def __init__(self):
		self.dp = {}
	def execute(self, array:VectorInt) -> int:
		array_length = len(array)
		if array_length == 0:
			return 0
		elif array_length == 1:
			return array[0]
		elif array_length == 2:
			return max(array[0], array[1])
		else:
			for i in range(array_length):
				self.dp[i] = [0 for j in range(0,2)]
			self.dp[0][0] = min_neg
			self.dp[0][1] = array[0]
			self.dp[1][0] = array[0]
			self.dp[1][1] = array[1]
			for i in range(2, array_length):
				self.dp[i][0] = max(self.dp[i-1][0], self.dp[i-1][1])
				self.dp[i][1] = max(self.dp[i-2][0], self.dp[i-2][1]) + array[i]
			return max(self.dp[array_length-1][0], self.dp[array_length-1][1])

day_9 = Day9()
assert day_9.execute([]) == 0
assert day_9.execute([2, 4, 6, 2, 5]) == 13
assert day_9.execute([2, 4, 5, 2, 5]) == 12
assert day_9.execute([2, 4, 5, 2, 5]) == 12
assert day_9.execute([9, 1, 1, 1, 1, 9]) == 19
assert day_9.execute([-1, -2]) == -1
assert day_9.execute([-2, 4, -6, 2, -5]) == 6
assert day_9.execute([2, 4, 6, 2, 5,-2, 4, -6, 2, -5]) == 19