from typing import List
VectorInt = List[int]
min_neg = -999999999999999
'''
	Time Complexity: O(N)
	Space Complexity: O(1)
	N : Number of elements in the array.
	To Test submission: https://leetcode.com/problems/house-robber/
'''
class Day9:
	def execute(self, array:VectorInt) -> int:
		array_length = len(array)
		if array_length == 0:
			return 0
		elif array_length == 1:
			return array[0]
		elif array_length == 2:
			return max(array[0], array[1])
		else:
			prev_without = array[0]
			prev_with = array[1]
			prev_prev_without = min_neg
			prev_prev_with = array[0]
			curr_without = min_neg
			curr_with = min_neg
			for i in range(2, array_length):
				curr_without = max(prev_with, prev_without)
				curr_with = max(prev_prev_with, prev_prev_without) + array[i]
				prev_prev_without = prev_without
				prev_prev_with = prev_with
				prev_without = curr_without
				prev_with = curr_with
			return max(curr_without, curr_with)

day_9 = Day9()
assert day_9.execute([]) == 0
assert day_9.execute([2, 4, 6, 2, 5]) == 13
assert day_9.execute([2, 4, 5, 2, 5]) == 12
assert day_9.execute([2, 4, 5, 2, 5]) == 12
assert day_9.execute([9, 1, 1, 1, 1, 9]) == 19
assert day_9.execute([-1, -2]) == -1
assert day_9.execute([-2, 4, -6, 2, -5]) == 6
assert day_9.execute([2, 4, 6, 2, 5,-2, 4, -6, 2, -5]) == 19