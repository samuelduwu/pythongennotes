#both variables are iterators. big_range is a generator, special type of iterator
import sys

#defining my own generator
def my_range(n: int):
  print("my_range starts")
  start = 0
  while start < n:
      pritn("my_range is returning {}.format(start))
      yield start
      start += 1
      
#yield returns the value but keeps track of prev values and position
      
pause = input("line 14")
#big_range = range(1000) # occupies 48 bytes
big_range = my_range(10000) # occupies 88 bytes 
pause = input("line 17") # here we see that my_range hasn't been executed

print(next(big_range)) #next gets next val of generator. Shows 0 initially. The next call to the function would yield 1
print("big_range is {} bytes".format(sys.getsizeof(big_range))) 

pause = input("line 21") #right after this pause, my_range runs
#create a list containing a ll the values in big_range
big_list = []
for val in big_range:
    pause = input("line 25 (in loop)") #after this point, that start message doesn't occur. the code picks up where yield ended
    big_list.append(val)
  
print("big_list is {} bytes".format(sys.getsizeof(big_list))) # occupies 9024 bytes
print(big_range) # this is a generator object
print(big_list) # this is a list

print("looping again... or not")
for i in big_range: #big_range generator is exhausted so nothing runs here. To make it run, change big_range to my_range(5)
    #if big_range = range(5), we've stored the generator so it can be called multiple times
    print("i is {}".format(i))
