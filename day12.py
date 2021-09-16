
##1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

def add (a,b):
  print(a+b)
def subtract(a,b):
  print(a-b)  
def multiply(a,b):
  print(a*b)  
def divide(a,b):
  if b == 0:
    print("f{b} can't be zero")
  else:
    print(a/b)  
#When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand. For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.

# You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you should print a warning instead of calculating their division.

# 2) Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:

tv_show = {
	"title": "Breaking Bad",
	"seasons": 5,
	"initial_release": 2008
}

def print_show_info(tv_show):
  # print (f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} ")
   # for k,v in tv_show.items():
   #  print ()
   print (f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} ")

print_show_info(tv_show)
# The print_show_info function should print the information stored in the dictionary, in a nice way. For example:

#  Breaking Bad (2008) - 5 seasons
# Remember you must define your function before calling it!

# 3) Below you’ll find a list containing details about multiple TV series.

series = [
	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
]
for tv in series:
    print_show_info(tv)
# Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary. You should end up with each series printed in the appropriate format.

# 4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.

sample = "was it a car or a cat I saw".strip(" ").lower().split()
sample = "".join(sample)
print(sample)
rev_sam = reversed(sample)
new_sam = ""
for i in rev_sam:
  new_sam = new_sam+i
print(new_sam)

if new_sam == sample:
  print("It's a Palindrome")
else:
  print("Not one")

  # OR

import re

def check_if_palindrome(test_string):
  letters_only = re.sub("[^a-z]+", "", test_string.casefold())
  if letters_only == letters_only[::-1]:
    print(f"'{test_string}' is a palindrome.")
  else:
    print(f"'{test_string}' is not a palindrome.")


check_if_palindrome("Never odd or even.")
# 'Never odd or even.' is a palindrome.

check_if_palindrome("Python is awesome!")
# 'Python is awesome!' is not a palindrome.

#####
# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# The program should store information about all of these books in a Python list.
# Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting the program. You can see an example of a working menu in the post on while loops (day 8).
import sys
menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """
print(menu_prompt)
read_list = []
def add_book():
  title = input("Enter the title: ")
  author = input ("Author: ")
  year = int(input("year: "))

  book = [(title,author, year )]
  read_list.append(book)

  print(read_list)

def list_book():
  for b in read_list:
    #print(a,t,y)
    print(b)

def enter_choice():
  while True:
    choice = input("enter a or l or q: ")
  
    if choice == "a":
      add_book()
    if choice == "l":
      list_book()
    if choice == 'q':
      sys.exit(1)

enter_choice()


