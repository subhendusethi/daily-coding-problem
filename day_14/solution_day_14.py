import random

'''
	Monte carlo approximation of PI:
	PI ~ (4 * number of random points in a circle) / total points considered in a square
'''

class Day14:
	def execute(self, number_of_iterations:int) -> float:
		radius = 2
		count = 0
		for _ in range(number_of_iterations):
			x_cur = random.uniform(-1*radius, radius)
			y_cur = random.uniform(-1*radius, radius)
			if x_cur*x_cur + y_cur*y_cur <= radius*radius:
				count+=1
		return (4*count)/number_of_iterations

day_14 = Day14()
assert round(day_14.execute(10000000),3) == 3.141
