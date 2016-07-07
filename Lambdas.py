my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print my_list[2] # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
print my_list[2](5)

def incrementor(num):
  start = num
  return lambda x: num + x