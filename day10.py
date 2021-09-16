####1) Below is a tuple describing an album:
tup = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
 )
# Inside the tuple we have the album name, the artist (in this case, the band), the year of release, and then another tuple containing the track list.

album = {}
album.update({"name": tup[0], "artist": tup[1], "year": tup[2], "song_list": tup[3]})
print(album)

# Convert this outer tuple to a dictionary with four keys.

# 2) Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.
for k,v in album.items():
  print(f"{k}: {v}")

# 3) Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.

del album["song_list"], album["year"]
album["date_year"] = "March 1st, 1973"
print(album)

# If you use a different album for the exercises, update the date accordingly.

# 4) Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.

#print(album["year"]) #KeyError: 'year'
print(album.get("year")) #None
print(album.get("year","Unknown")) #Unknown

