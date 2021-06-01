burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# these 3 do similar things
meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

for burger in burgers:
  for topping in toppings:
    print((burger, topping))
    
for meals in [(burger, topping) for burger in burgers for topping in toppings]:
  print(meals)

# nested list containing tuples (list of 4 lists) - prints out nicely but ordering is changed
for meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
  print(meals)
 

### CHALLENGE ##
for i in range(1, 11):
  for j in range(1, 11):
    print(i, i * j)

#Answer:
times = [(i, i * j) for i in range(1, 11) for j in range(1, 11)] 
print(times)

#or
for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
  print(x, y)
  
#or
times2 = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)] 
print(times2)

#using generator function
for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):
  print(x, y)
