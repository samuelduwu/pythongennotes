import os
import fnmatch

def find_albums(root, artist_name):
  
  for path, directories, files in os.walk(root):
    for artist in fnmatch.filter(directories, artist_name): #filter used to only look to folder of artist name
      subdir = os.path.join(path, artist)
      for album_path, albums, _ in os.walk(subdir):
        for album in albums:
          yield os.path.join(album_path, album), album

def find_songs(albums):
  for album in albums:
    for song in os.listdir(album[0]):# we want the path not the name of the album
      yield song
      
album_list = find_albums("music", "BLACK*") #fnmatch can search for terms (not case sensitive if proper installation/drive)
song_list = find_songs(album_list) 

for s in song_list:
  print(s)
