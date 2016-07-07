class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		print "New Bike!"
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	
	def displayInfo(self):
		print "Bike Price: "+self.price+" Speed: "+self.max_speed+" Current Miles: "+str(self.miles)
		return self
	def ride(self):
		print "Riding!"
		self.miles+=10
		return self
	def reverse(self):
		print "Reversing"
		if self.miles <=5:
			print "You can't reverse any farther!!"
		else:
			self.miles-=5
		return self

bike1 = Bike('$200', '25mph')
bike1.ride().ride().ride().reverse().displayInfo()
bike2 = Bike('$400', '50mph')
bike2.ride().ride().reverse().reverse().displayInfo()
bike3 = Bike('$50','5mph').reverse().reverse().reverse().displayInfo()