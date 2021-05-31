import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
  #just to parse path directory
  if files: #this would only run if files exist in folder
    print(path) #string
    first_split = os.path.split(path) #list of ["folder/artist, album name"]
    print(first_split)
    second_split = os.path.split(first_split[0]) #list of ["folder", "artist"]
    print(second_split)
    for f in files:
      song_details = f[:-5].split(' - ') #take off .emp3 extension. split on song number character
      print(song_detials)
    print("*"*40)
  #
  print(directories) # list
  print(files) # list
  input()
  #for f in files:
  #  print("\t{}".format(f))
    
