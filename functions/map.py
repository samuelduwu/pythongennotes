text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

#use map
map_capitals = list(map(str.upper, text)) #takes function and iterator like string or list. returns iterable as list
print(map_capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

#use map
map_words = list(map(str.upper, text.split(' ')))

for x in map(str.upper, text.split(' ')):
  print(x)

  
