FILE_TYPE = "file"
DIR_TYPE = "dir"

class Token:
	def __init__(self, string:str, level:int, ttype:int):
		self.string = string
		self.level = level
		self.ttype = ttype

class Day17:
	def execute(self, string:str) -> int:
		stack = []
		curr_index = 0
		max_len = 0
		while curr_index < len(string):
			curr_token, return_index = self.__parser(string, curr_index)
			curr_ttype = curr_token.ttype
			curr_level = curr_token.level
			curr_str = curr_token.string
			if curr_ttype == DIR_TYPE:
				while len(stack):
					top = stack[-1]
					if top[0] >= curr_level:
						stack.pop(-1)
					else:
						break
				if len(stack):
					top = stack[-1]
					stack.append((curr_level, top[1] + len(curr_str) + 1))
				else:
					stack.append((curr_level, len(curr_str) + 1))
			elif curr_ttype == FILE_TYPE:
				max_len = max(max_len, stack[-1][1] + len(curr_str))
			curr_index = return_index
		return max_len

	def __parser(self, string:str, index:int) -> ((str,str),int):
		res = ""
		ttype = None
		level = 0
		curr_index = index
		while curr_index < len(string) and string[curr_index] == '\t':
			level+=1
			curr_index+=1

		while curr_index < len(string) and string[curr_index] != '\n':
			res+=string[curr_index]
			curr_index+=1

		if res.find('.') != -1:
			ttype = FILE_TYPE
		else:
			ttype = DIR_TYPE

		return (Token(res, level, ttype), curr_index + 1)

day_17 = Day17()

assert day_17.execute("dir\n\ttemp.txt") == 12
assert day_17.execute("dir\n\tsubdir1\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n") == 0
assert day_17.execute("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
assert day_17.execute("dir\n\tsubdir1\n\t\tfile1tfile1tfile1tfile111.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 41
