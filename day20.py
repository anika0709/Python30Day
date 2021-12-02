#https://www.teclado.com/30-days-of-python/python-30-day-20-map-filter
#map is a function that allows us to call some other function on every item in an iterable.

def cube(n):
  return n*n*n

nos = [1,3,5,7]
cubed_no = map(cube,nos)
print(cubed_no) #lazyobject, passes the mem location. Better than comprehension

print(*cubed_no,sep=",") #Important
#OR
numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(lambda number: number ** 3, numbers)

#####################

def add(a, b):
	return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19


# Operator Module
from operator import add,methodcaller

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

names = ["tom", "richard", "harold"]
title_names = map(methodcaller("title"), names)

# Much like map is a functional analogue for "normal" comprehensions, filter performs the same role as a conditional comprehension.

# Much like map, filter calls a function (known as a predicate) for every item in an iterable, and it discards any values for which that function returns a falsy value.

# A predicate is a function that accepts some value as an argument and returns either True or False.

def is_even(num):
  if num % 2 == 0:
    return True

nums = [2,4,5,7,9,8]
print(list(filter(is_even,nums)))

#Print Truthy value

values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ") 

####### Exercise ############

# 1) Use map to call the strip method on each string in the following list:

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]
stripped_poem = map(lambda x: x.strip(),humpty_dumpty)
print(*stripped_poem, sep='\n')
# Print the lines of the nursery rhyme on different lines in the console.

# Remember that you can use the operator module and the methodcaller function instead of a lambda expression if you want to.
from operator import methodcaller
str_hd = filter(methodcaller("strip"),humpty_dumpty)
print(*str_hd, sep='\n')
# 2) Below you'll find a tuple containing several names:

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

filter_names = [n.title() for n in names if len(n) < 8]
print(filter_names)
# Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list. Make sure that every name in the new list is in title case.

# 3) Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to the console.
ans = filter(None, [n for n in range(-5,11) if n >= 0] )
print(*ans, sep=",")







