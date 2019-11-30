from typing import List

VectorInt = List[int]


class Day2:
	def execute(self, array: VectorInt) -> VectorInt:
		array_length = len(array)

		left_product = [1 for i in range(array_length)]
		right_product = [1 for i in range(array_length)]

		left_product[0] = array[0]
		right_product[array_length-1] = array[array_length-1]
		
		for i in range(1,array_length):
			left_product[i] = array[i] * left_product[i-1]
			right_product[array_length-1-i] = array[array_length-1-i] * right_product[array_length-i]

		result = [1 for i in range(array_length)]
		result[0] = right_product[1]
		result[array_length-1] = left_product[array_length-2]

		for i in range(1, array_length-1):
			result[i] = left_product[i-1] * right_product[i+1]
		return result

day_2 = Day2()
assert day_2.execute([-3, 10, 5]) == [50, -15, -30]
assert day_2.execute([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert day_2.execute([-11, 5]) == [5, -11]