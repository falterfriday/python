# import random
# a = random.random()
# print a
heads_count = 0
tails_count = 0
for x in range (1,5001):
	import random
	a = random.random()
	if round(a) == 1:
		heads_count+=1
		print 'Attempt #{}: Throwing a coin... Its heads! ... Got {} head(s) so far and {} tail(s) so far'.format(x,heads_count,tails_count)
	elif round(a) == 0:
		tails_count+=1
		print 'Attempt #{}: Throwing a coin... Its tails! ... Got {} heads(s) so far and {} tail(s) so far'.format(x,heads_count,tails_count)
print 'Ending the program, thank you!'