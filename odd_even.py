for x in range(1,2001):
	if x%2 > 0:
		y = 'This number is odd.'
		z = 'This number is even.'
		print "Number is {}. {}".format(x,y)
	else:
		print "Number is {}. {}".format(x,z)
