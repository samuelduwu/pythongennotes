# Normal implementation
print(__file__)

numbers = [1,2,3,4,5,6]

number = int(input("Please enter a number, and I'll tell you its square: "))

squares = []
for number in numbers:
  squares.append(number**2)
  
index_pos = numbers.index(number)
print(squares[index_pos]))

#since number is used as input and index for for loop, it always outputs 36

# Using comprehensions
numbers = [1,2,3,4,5,6]

#squares = [number ** 2 for number in numbers] #using {} creates a set comprehension
number = int(input("Please enter a number, and I'll tell you its square: "))

squares = [number ** 2 for number in numbers]

print(squares[index_pos]))

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

