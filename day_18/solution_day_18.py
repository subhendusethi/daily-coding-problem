from typing import List

VectorInt = List[int]

'''
	Space Complexity: O(K)
	Time Complexity: O(N)
'''

class Day18:
	def execute(self, array:VectorInt, k:int) -> VectorInt:
		dq = []
		res = []
		if not array or k<1 or k>len(array):
			return []

		for i, num in enumerate(array):
			if dq and dq[0] < i-k+1:
				dq.pop(0)
				
			while dq and array[dq[-1]] < num:
				dq.pop()

			dq.append(i)

			if i>=k-1:
				res.append(array[dq[0]])
		return res

day_18 = Day18()

assert day_18.execute([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
