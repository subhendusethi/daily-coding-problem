'''
	Higher order functions in Python:
	https://www.hackerearth.com/practice/python/functional-programming/higher-order-functions-and-decorators/tutorial/
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def left(a, b):
		return a
	return pair(left)

def cdr(pair):
    def right(a, b):
        return b
    return pair(right)


assert cdr(cons(1,2)) == 2
assert car(cons(1,2)) == 1
assert cdr(cons(-1,5)) == 5
assert car(cons(-1,5)) == -1
assert car(cons("hello",2)) == "hello"
assert cdr(cons(-1,"world")) == "world"