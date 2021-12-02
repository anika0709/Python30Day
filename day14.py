# Rewrite the following piece of code using a context manager:

#  f = open("hello_world.txt", "w")
#  f.write("Hello, World!")
#  f.close()

with open("hello_world.txt", "w") as f:
  f.write("Hello, World! ")
# Use append mode to write "How are you?" on the second line of the hello_world.txt file above.
with open("hello_world.txt", "a") as f:
  f.write("How are you?")
with open("hello_world.txt", "r") as f:
  print(f.readlines())

# Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.

with open ("iris.csv", "r") as i_file:
  #key_csv = ir.readlines(1)
  data = i_file.readlines()
  #print(key_csv)
  irises = []
  header=data[0].strip().split(",")
  print(header)
  for i in data[1:]:
    ir_row = i.strip().split(",")
    i_dict = dict(zip(header, ir_row))
    irises.append(i_dict)
print(irises)

with open("new_csv","w") as new_file:

    for row in irises:
        #print(row)
        #print('\n')
        # for v in row.values():
        #     new_file.write(v)
        ls = (",".join(row.values())+ "\n")
        new_file.write(ls)
        # header=data=[]
        # row = tup(row)
        # print()
        # for k,v in row.keys():
        #     data.append(k)
        # print(data)

#############
# Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.

# The program should store information about all of these books in a file called books.csv, and this data should be stored in CSV format.
# Users should be able to retrieve the books in their reading list, and these books should be printed out in a user-friendly format.

# Users should be able to search for a specific book by providing a book title.


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
  title = input("Enter the title: ").title().strip()
  author = input ("Author: ").title().strip()
  year = (input("year: ")).strip()
  
  book = (title,author, year)
  read_list.append(book)
  print(read_list)
  with open("read_list", "a") as r_file:
    # r_file.write(",".join(book)+ '\n') or
    r_file.write(f"{title},{author},{year}\n")

def list_book():
  for b in read_list:
    #print(a,t,y)
    print(b)

def read_books():
  with open("read_list") as r_list:
    line = r_list.readlines()
    for l in line:
      t,a,y = l.split(",")
      print(f"{t} is written by {a} in {y}")

def find_book(search):
  with open("read_list") as r_list:
    line = r_list.readlines()
    for l in line:
      t,a,y = l.split(",")
      if t == search:
        print("book found")
        break
    else:
      print("Not Found")

def enter_choice():
  while True:
    choice = input("enter a or l, r , s or q: ")
  
    if choice == "a":
      add_book()
    if choice == "l":
      list_book()
    if choice == "r":
      read_books()
    if choice == "s":
      search = input("enter book title to be found")
      find_book(search)
    if choice == 'q':
      sys.exit("Quitting. Bye!")

enter_choice()


#lst1, lst2 = zip(*zipped_list)
# should give you the unzipped list.

# *zipped_list unpacks the zipped_list object. it then passes all the tuples from the zipped_list object to zip, which just packs them back up as they were when you passed them in.

# so if:

# a = [1,2,3]
# b = [4,5,6]
# then zipped_list = zip(a,b) gives you:

# [(1,4), (2,5), (3,6)]
# and *zipped_list gives you back

# (1,4), (2,5), (3,6)
# zipping that with zip(*zipped_list) gives you back the two collections:

# [(1, 2, 3), (4, 5, 6)]


        

