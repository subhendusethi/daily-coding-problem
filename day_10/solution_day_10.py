import threading
import types
import random
import time
import calendar

random.seed(calendar.timegm(time.gmtime()))

def delay(func:types.FunctionType, delay_in_ms:int, t_id:str):
	print("Scheduled execution of Function: {} after {} ms with thread_id: {}".format(func.__name__, delay_in_ms, t_id))
	time.sleep(delay_in_ms/1000)
	print("Function: {} with {} ms delay with thread_id: {} started execution.".format(func.__name__, delay_in_ms, t_id))
	func(10, 20)
	print("Function: {} with {} ms delay with thread_id: {} completed execution.".format(func.__name__, delay_in_ms, t_id))



def binom_n2(a:float, b:float):
	return a*a + b*b + 2*a*b


def scheduler(func:types.FunctionType, delay_in_ms:int):
	t_id = random.randint(1, 2147483647)
	thread = threading.Thread(target=delay, args=(func, delay_in_ms, t_id)) 
	thread.start()

i = 1
while i<100:
	scheduler(binom_n2, i)
	i+=1

