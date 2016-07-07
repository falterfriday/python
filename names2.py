users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

 # iterate through through the dictionary with a for loop - drink a beer
 # print iteration (x) - first_name last_name - len(first_name) + len(last_name) - coffee!!!!!!!
for key, data in users.items():
	print key
	count = 0
	for x in data:
		count += 1
		print count, '-', x['first_name'], x['last_name'], '-',  len(x['first_name'])+len(x['last_name'])