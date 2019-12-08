class Day16:
	'''
		Time Complexity: 
			record(order_id): O(1)
			get_last(i) : O(1)

		Space Complexity: O(N)
		N: Initial log size
	'''
	def __init__(self):
		self.arr = []
	def execute(self, N):
		self.arr = [None for i in range(N)]
		self.start = -1
		self.end = -1
		self.capacity = 0
		self.N = N
	def record(self, order_id):
		if self.capacity == 0:
			self.start = self.end = 0
			self.capacity+=1
		elif self.capacity == self.N:
			self.start = (self.start + 1) % self.N
		else:
			self.capacity+=1
		self.end = (self.end + 1) % self.N
		self.arr[self.end] = order_id

	def get_last(self, i):
		if self.capacity == 0:
			return None
		return self.arr[(self.N + self.end - i + 1) % self.N]

day_16 = Day16()
day_16.execute(5)

day_16.record(1)
day_16.record(2)
day_16.record(3)
day_16.record(4)
day_16.record(5)

'''
	     state
	[1, 2, 3, 4, 5]
	 s           e
'''

assert day_16.get_last(5) == 1
assert day_16.get_last(4) == 2
assert day_16.get_last(3) == 3
assert day_16.get_last(2) == 4
assert day_16.get_last(1) == 5

day_16.record(10)
day_16.record(11)
day_16.record(12)

'''
	       state
	[10, 11, 12, 4, 5]
	          e  s
'''
assert day_16.get_last(5) == 4
assert day_16.get_last(4) == 5
assert day_16.get_last(3) == 10
assert day_16.get_last(2) == 11
assert day_16.get_last(1) == 12


day_16.record(100)
day_16.record(101)

'''
	       state
	[10, 11, 12, 100, 101]
	  s                 e
'''

assert day_16.get_last(5) == 10
assert day_16.get_last(4) == 11
assert day_16.get_last(3) == 12
assert day_16.get_last(2) == 100
assert day_16.get_last(1) == 101

day_16.execute(1)
day_16.record(1)
assert day_16.get_last(1) == 1
day_16.record(100)
assert day_16.get_last(1) == 100

'''
# interactive mode

print("Enter N")
N = input()
day_16.execute(int(N))

while True:
	print("Enter 1 for record(order_id) or 2 for get_last(i)")
	option = int(input())
	if option == 1:
		print("Enter order_id to enter into record")
		order_id = int(input())
		day_16.record(order_id)
	elif option == 2:
		print("Enter i for get_last")
		order_id = int(input())
		print(day_16.get_last(order_id))
'''