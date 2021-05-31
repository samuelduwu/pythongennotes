# Normal implementation
print(__file__)

numbers = [1,2,3,4,5,6]

squares = []
for number in numbers:
  squares.append(number**2)
  
print(squares)

# Using comprehensions
numbers = [1,2,3,4,5,6]

squares = [number ** 2 for number in numbers] #using {} creates a set comprehension

print(squares)

# A list comprehension's first segment (number ** 2) is expression we want to return
# second is iteration over a sequence. Identical to for part in for loop

# A string or generator could also work 
squares = [number ** 2 for number in range(1, 7)] #replace line 15 with this

#another example
text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words) # doing something like this wouldn't require comprehension
#lc_words = [word for word in text.split(' ')]  - this is pointless

