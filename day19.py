#Exception Handling

#https://www.teclado.com/30-days-of-python/python-30-day-19-exception-handling
while True:
  try:
    num = input("enter number: ")
    num = int(num)
    break
  except ValueError as e:
    print("Not a valid number",e)

import math
def avg_nums(nums):
  try:
    avg = math.fsum(nums)/ len(nums)
  except (ValueError, ZeroDivisionError, TypeError ):
    print("this is not valid")
  else:
    print(avg)


try:
  nums = [1,e, 3,4]
  avg_nums(nums)
except NameError as e:
    print(e)


######Exercise#########
# 1) Create a short program that prompts the user for a list of grades separated by commas. Split the string into individual grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the user when the values they entered cannot be converted.
try: 
  nums = input("enter grades separated by ,: ")
  nums = nums.split(',')
  print(nums)
  num_list = [int(num) for num in nums ]
  print((num_list))
except ValueError as e:
  print("Not valid entries", e)
# 2) Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.
def test_return():
  try:
    a,b=5,2
    return a/b
  except ZeroDivisionError:
    print("Can't divide by 0")
  finally:
    return (a) # this gets printed

print(test_return())

# 3) Imagine you have a file named data.txt with this content:

# There is some data here!
# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.

try:
  with open("data.txt","r") as dFile:
    read_file = dFile.read()
    print(read_file)
except FileNotFoundError as e:
  print("File is not available. The error is ", e)

# When files don't exist when you try to open them, the exception raised is FileNotFoundError.


