from typing import List

VectorInt = List[int]

class Day1:
	def execute(self, array: VectorInt, k: int) -> bool:
		visited_set = set()
		for item in array:
			if k-item in visited_set:
				return True
			else:
				visited_set.add(item)
		return False

day_1 = Day1()

assert day_1.execute([1,2,3,4,5], 10) == False
assert day_1.execute([1,2,3,5,5], 10) == True
assert day_1.execute([1,2,3,4,5], 2) == False
assert day_1.execute([0,2,3,4,5], 2) == True
assert day_1.execute([3,4,5,0], 0) == False
assert day_1.execute([3,4,5,0,0], 0) == True
assert day_1.execute([3,-14], -11) == True
