# Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.

movies = [
	("Eternal Sunshine of the Spotless Mind", "Michel Gondry", "2004", "30000000")
	]
# Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
title = input("Enter movie title: ")
director = input("Enter directory: ")
yr = input("Enter Release year: ")
budget = input("Enter budget: ")
# Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
new_movie = (title,director,yr,budget)

# Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{new_movie[0]} {new_movie[2]}")

# Add the new movie tuple to the movies collection using append.
movies.append(new_movie)


# Print both movies in the movies collection.
print(movies[0][0], movies[1][0])
# Remove the first movie from movies. Use any method you like.
del movies[0]