class MathDojo(object):
	def __init__(self):
		self.x = 0


	def add(self, *args):
		for i in range(0,len(args)):
			if type(args[i]) is list:
				self.x += sum(args[i])
			elif type(args[i]) is int:
				self.x += args[i]
			elif type(args[i]) is tuple:
				self.x += sum(args[i])
		return self

	def subtract(self, *args):
		for i in range(0,len(args)):
			if type(args[i]) is list:
				self.x -= sum(args[i])
			elif type(args[i]) is int:
				self.x -= args[i]
			elif type(args[i]) is tuple:
				self.x -= sum(args[i])
		return self

	def result(self):
		print self.x

MathDojo().add([2,1],[1,1],4).subtract(2, [2,3], [1.1, 2.3]).result()
MathDojo().add([1],3,4).add((3, 5, 7, 8), [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
