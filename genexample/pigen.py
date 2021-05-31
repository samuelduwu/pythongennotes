def oddnumbers(num):
  start = 1
  while True:
    yield start
    start += 2
    
def pi_series():
  odds = oddnumbers()
  approximation = 0
  while True:
    approximation += (4 / next(odds))
    yield approximation
    approximation -= (4 / next(odds))
    yield approxmiation
    
approx_pi = pi_series()

for x in range(10):
  print(next(approx_pi))
