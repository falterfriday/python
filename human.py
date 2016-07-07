class Human(object):
	def __init__(self, clan=None):
		print "New Human!"

		self.clan = clan
		self.health = 100
		self.strength = 3
		self.intelligence = 3
		self.stealth = 3
	def taunt(self):
		print "You wanna go?!"
michael = Human('Ninjas')
jimmy = Human('Ninjas')
tom = Human('Samurai')

print michael.clan
print jimmy.clan
print tom.clan

class Test(object):
	def __init__(self, phrase='Nothing was passed'):
		print "This string was passed in:" + phrase
		self.phrase = phrase
test1 = Test("Hello, World!")
test2 = Test()
print "Test1 has phrase: '" + test1.phrase + "'"
print "Test2 has phrase: '" + test2.phrase + "'"
