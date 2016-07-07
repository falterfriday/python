class car(object):
	def __init__(self, price, speed, fuel, mileage, tax=0):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = tax

		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()

	def display_all(self):
		print "Price: $"+str(self.price)+"\nSpeed: "+self.speed+ "\nFuel Level: "+self.fuel+ "\nMileage: "+self.mileage+ "\nTax Rate: "+str(self.tax)

car1 = car(9999,'120 mph','Full','35mpg')
car2 = car(142987,'80 mph','Meh','25mpg')
car3 = car(2373,'110 mph','Full','56mpg')
car4 = car(5,'5 mph','Empty','5mpg')
car5 = car(9811,'80 mph','Half','35mpg')