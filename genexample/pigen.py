#this generates all odd numbers without requiring a limit to be set
def oddnumbers(num):
  start = 1
  while True:
    yield start
    start += 2

# this performs the infinite series approximation for pi    
def pi_series():
  odds = oddnumbers()
  approximation = 0
  while True:
    approximation += (4 / next(odds))
    yield approximation
    approximation -= (4 / next(odds))
    yield approxmiation
    
approx_pi = pi_series()

#the greater the range is, the more accurate
for x in range(10):
  print(next(approx_pi))