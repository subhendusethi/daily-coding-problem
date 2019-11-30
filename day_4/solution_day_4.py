from typing import List

VectorInt = List[int]

class Day4():
	def execute(self, array:VectorInt) -> int:
		array_length = len(array)
		for i in range(array_length):
			current_item = array[i]
			if current_item == i+1:
				continue
			elif current_item < 0 or current_item >= array_length:
				continue
			else:
				array[i], array[current_item-1] = array[current_item-1], array[i]
				i-=1
		for i in range(array_length):
			if array[i] != i+1:
				return i+1
		return array_length+1

day_4 = Day4()

assert day_4.execute([3, 4, -1, 1]) == 2
assert day_4.execute([1, 2, 0]) == 3
assert day_4.execute([-1,-1,-5,-7,-10,4,1,2,2,5]) == 3
assert day_4.execute([-1,-1,-5,-7]) == 1
assert day_4.execute([-1]) == 1


