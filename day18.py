# 1) Import the fractions module and create a Fraction from the float 2.25. You can find information on how to create fractions in the documentation.
import fractions

f = fractions.Fraction(2.25)
print(f)

# 2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:
from math import fsum

f_list = [2.1,2.8,4.1,5.6,7.9]
print(fsum(f_list))

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))
# 3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function. You can find documentation for this function here.
import random as r
ran_num = r.randint(1,100)
print(ran_num)


############Project: Json Reading_list ##############
#There are two important functions we need to be aware of in the json module.
# The first of these functions is json.load, which is going to allow us to take JSON data from a file and convert it to standard Python types, like dictionaries, lists, integers, strings, etc.
# The second of the functions we need to learn about is json.dump. This function expects a dictionary or list, as well as a file to write to.

#The dumps and loads ("s" in the function names refers to strings), because these functions either take in JSON as a string, or give us a string representation of the code we've converted to JSON.

import json

def add_book():
	books = get_all_books()

	title = input("Title: ").strip().title()
	author = input("Author: ").strip().title()
	year = input("Year of publication: ").strip()

	books.append({
		"title": title,
		"author": author,
		"year": year,
		"read": "Not read"
	})

	with open("books.json", "w") as reading_list:
		json.dump(books, reading_list)

def create_book_file():
	try:
		with open("books.json", "x") as reading_list:
			json.dump([], reading_list)
	except FileExistsError:
		pass

def delete_book(books, book_to_delete):
	books.remove(book_to_delete)

def find_books():
	reading_list = get_all_books()
	matching_books = []

	search_term = input("Please enter a book title: ").strip().lower()

	for book in reading_list:
		if search_term in book["title"].lower():
			matching_books.append(book)

	return matching_books

# Helper function for retrieving data from the csv file
def get_all_books():
	with open("books.json", "r") as reading_list:
		return json.load(reading_list)

def mark_book_as_read(books, book_to_update):
	index = books.index(book_to_update)
	books[index]['read'] = "Read"

def update_reading_list(operation):
	books = get_all_books()
	matching_books = find_books()

	if matching_books:
		operation(books, matching_books[0])

		with open("books.json", "w") as reading_list:
			json.dump(books, reading_list)
	else:
		print("Sorry, we didn't find any books matching that title.")

def show_books(books):
	# Adds an empty line before the output
	print()

	for book in books:
		print("{title}, by {author} ({year}) - {read}".format(**book))

	print()

create_book_file()

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

# Get a selection from the user
selected_option = input(menu_prompt).strip().lower()

# Run the loop until the user selected 'q'
while selected_option != "q":
	if selected_option == "a":
		add_book()
	elif selected_option == "d":
		update_reading_list(delete_book)
	elif selected_option == "l":
		# Retrieves the whole reading list for printing
		reading_list = get_all_books()

		# Check that reading_list contains at least one book
		if reading_list:
			show_books(reading_list)
		else:
			print("Your reading list is empty.")
	elif selected_option == "r":
		update_reading_list(mark_book_as_read)
	elif selected_option == "s":
		matching_books = find_books()

		# Checks that the seach returned at least one book
		if matching_books:
			show_books(matching_books)
		else:
			print("Sorry, we didn't find any books for that search term")
	else:
		print(f"Sorry, '{selected_option}' isn't a valid option.")

	# Allow the user to change their selection at the end of each iteration
	selected_option = input(menu_prompt).strip().lower()


