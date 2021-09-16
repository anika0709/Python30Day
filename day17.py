#https://www.teclado.com/30-days-of-python/python-30-day-17-args-kwargs

def multigreet(*args):
	for name in args:
		print(f"Hello, {name}!")

multigreet("Rolf", "Bob", "Anne", "Annie", "Garry", "Mira")

#If we define both *args and **kwargs for a given function, **kwargs has to come second. If the order is reversed, Python considers it invalid syntax.

def print_movie(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

movie = {
	"title": "The Matrix",
	"director": "Wachowski",
	"year": 1999
}

print_movie(studio="Warner Bros", **movie)

# 1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.
def get_sum(*num):
  print(sum(num))

get_sum(1,2,3,4,5)


# 2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.
def get_arg(*args,**kwargs):
  print(f"Positional arguments are: {args}")
  print(f"Keyword arguments are: {kwargs}")
  
movie = {
"title": "The Matrix",
"director": "Wachowski",
"year": 1999
}

get_arg("Rolf", "Bob", "Anne", **movie)
get_arg(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)

# 3) Print the following dictionary using the format method and ** unpacking.

country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
 }
def get_country(**c):
   for k,v in c.items():
     print(k,'=', v)

get_country(**country)
# 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for print function's sep parameter for this exercise.

nums = [i for i in range(1,20)]
print(*nums,sep=",")
#or
print(*range(1, 21), sep=", ")

#5) Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.

print(*nums,sep="\n")

#destructuring values
head, *tail = [1, 2, 3, 4, 5] #remaining values to tail

print(head)  # 1
print(tail)  # [2, 3, 4, 5]

first, second, third, *rest = [1, 2, 3, 4, 5, 6, 7]
print(rest)





