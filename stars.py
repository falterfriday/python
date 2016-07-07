def draw_stars(list):
	for x in list:
		if type(x) is int:
			print x * '*'
		elif type(x) is str:
			print x[0].lower() * len(x)


draw_stars([4, "Tom", 1, "Bro", 5, 7, "Jimmy Smith"])