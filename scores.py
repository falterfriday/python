arr = []
for x in range(0,10):
	arr.append(raw_input('Score: '))
print 'Scores and Grades'
for y in arr:
	if int(y) >=90:
		print 'Score: ' +y+ '; Your grade is A'
	elif int(y) >=80:
		print 'Score: ' +y+ '; Your grade is B'
	elif int(y) >=70:
		print 'Score: ' +y+ '; Your grade is C'
	elif int(y) >=60:
		print 'Score: ' +y+ '; Your grade is D'
print 'End of the program, Bye!'