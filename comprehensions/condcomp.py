menu = [
  ["egg", "spam", "bacon"],
  ["egg", "sausage", "bacon"],
  ["egg", "spam"],
  ["egg", "bacon", "spam"],
  ...
  
meals = []
for meal in menu:
  if "spam" not in meal:
    meals.append(meal)
  else:
    meals.append("a meal was skipped")
print(meals)

#meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal] #cannot just add else into this, but we can have multiple "if" filters
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal] # this works the same as above
print(meals)
  
# this third section is a filter added onto a comprehension
  
fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)]
  
fussy_meals = [meal for meal in menu if ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
  
  
-----------------------------
menu = [
  ["egg", "spam", "bacon"],
  ["egg", "sausage", "bacon"],
  ["egg", "spam"],
  ["egg", "bacon", "spam"],
  ...
]
  
meals = []
for meal in menu:
  if "spam" not in meal:
    meals.append(meal)
  else:
    meals.append("a meal was skipped")
print(meals)

meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu] # this is how we can include an else statement
  #this is like our first list comprehension but the expression is a bit more complex

x = 12
expression = "Twelve" if x == 12 else "unknown" # this is a conditional expression
print(expression)
  
for meal in menu:
  print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")
  
#making a set of all items that can be in a meal
print()
items = set()
for meal in menu:
  for item in meal:
    items.add(item)
  
print(items)
print()
  
#prints first matching item list contains
for meal in menu:
  for item in items:
    if item in meal:
      print("{} contains {}".format(meal, item))
      break
  
#checking for division
for x in range(1, 31):
  fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
  print(fizzbuzz)
