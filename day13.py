x,y = 435,55
def add(x,y):
  print(locals(),sep='\n')
  print(x+y)
print(globals(),sep='\n')
add(x,y)

# 1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.
def expo(x,y):
  return x**y

print(expo(2,3))

# 2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.

def process_string(str):
  print(str.lower().strip())

# 3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:

# ("Tom Hardy", "English", 42)  # name, nationality, age
# You can choose whatever key names you like for the dictionary.

def get_details(info):
  actor = {}
  name,nationality,age = info
  actor["name"]=name
  actor["nation"]=nationality
  actor["age"] = age
  print(actor)

info = ("Tom Hardy", "English", 42)
get_details(info)


# 4) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def find_prime(num):
  for i in range(2,num):
    if (num % i == 0):
      print(f"{num} is not prime")
      return True
  return False

print(find_prime(15))
print(find_prime(37))