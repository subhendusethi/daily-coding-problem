import random
'''
	Time Complexity: O(N)
	Space Complexity: O(1)
	N: Size of stream.

	Idea is to go over the stream and uniformly random weights to each number,
	then pick the number with largest/smallest weight.
'''
class Day15:
	def execute(self, stream)->int:
		res = None
		max_prob_so_far = -1
		for element in stream:
			curr_weight = random.random()
			if curr_weight > max_prob_so_far:
				res = element
				max_prob_so_far = curr_weight
		return res

day_15 = Day15()

assert day_15.execute([1]) == 1
assert day_15.execute([]) == None

print(day_15.execute([1,2,3,4,5,6,7,8,"po po po"]))



