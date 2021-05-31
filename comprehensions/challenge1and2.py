#question 1, change this to be a list comp
text = input("Please enter your text: ")

output = []
for x in text.split():
  output.append(len(x))
print(output)

#solution
print([len(x) for x in text.split()])

#question 2 change this so tuples are returned in list 
output = []
for x in text.split():
  output.append((x, len(x)))
print(output)

#solution 
print({(x, len(x)) for x in text.split()}) # we use a set to avoid dupes


-----------------------------
# question 3 return tuple of comprehension converting inches to cm
inch_measurement = (3, 8, 20)

cm_measurement = [inch * 2.54 for inch in inch_measurement]
print(cm_measurement)
#if we wanted a tuple, 
cm_measurement = tuple([inch * 2.54 for inch in inch_measurement])
#attempting to do (inch * 2.54 for inch in inch_measurement) would create a generator since () is reserved for that
