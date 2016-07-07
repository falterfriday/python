class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		print "New Bike!"
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	
	def displayInfo(self):
		print "Bike Price: "+self.price+" Speed: "+self.max_speed+" Current Miles: "+str(self.miles)
	def ride(self):
		print "Riding!"
		self.miles+=10
	def reverse(self):
		print "Reversing"
		if self.miles <=5:
			print "You can't reverse any farther!!"
		else:
			self.miles-=5

bike1 = Bike('$200', '25mph')
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike('$400', '50mph')
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike('$50','5mph')
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()