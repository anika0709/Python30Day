# Much like range, zip is lazy, which means it only calculates the next value when we request it. We therefore can't print it directly, but we can convert it to something like a list if we want to see the output:

# One thing you should be aware of when it comes to enumerate and zip is that they are consumed when we iterate over them. 

# 1) Below is some simple data about characters from BoJack Horseman:

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
# The data contains the character name, the voice actor or actress who plays them, and the species of the character.

# Write a for loop that uses destructuring so that you can print each tuple in the following format:

for name,voice,char in main_characters:
  print(f"{name} is a {char.lower()} voiced by {voice}.")


# BoJack Horseman is a horse voiced by Will Arnet.
# Note that you're going to have to change the species information to lowercase when you print it. If you need a reminder on how to do this, we covered it in day 3 of the first week.

# 2) Unpack the following tuple into 4 variables:

tuple_var =  ("John Smith", 11743, ("Computer Science", "Mathematics"))
n,i,(ma,mi) = tuple_var
print(n,i,ma,mi)

# name = tuple_var[0]
# id = tuple_var[1]
# major=tuple_var[2][0]
# minor=tuple_var[2][1]
# The data represents a student's name, their student id number, and their major and minor disciplines in that order.

# 3) Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.

list1 = ["red","green","yellow"]
tuple1 = ["apple","grapes","banana","mango"]
new_one = zip(list1,tuple1)
print(type(new_one))
for i in new_one:
  print (i)


#Project
# The algorithm we're going to use to verify card numbers is called the Luhn algorithm, or Luhn formula. This algorithm is actually used in real-life applications to test credit or debit card numbers as well as SIM card serial numbers.


# The purpose of the algorithm is to identify potentially mistyped numbers, because it can determine whether or not it's possible for a given number to be the number for a valid card.

# The way we're going to use the algorithm is as follows:

# Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
# Reverse the order of the remaining digits.
# For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9, subtract 9 from those numbers.
# Add together all of the results and add the checking digit.
# If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

no = 5893804115457289

# removing the checking digit
temp = str(no)
checking_digit = temp[-1]
print(checking_digit)
temp = temp[:-1]

print(temp)

rev_temp = temp[::-1]
print(rev_temp)

sum = 0
for i,digit in enumerate(rev_temp):
  if (i % 2 == 0):
    j = int(digit)
    j *= 2
    if j > 9:
      j = j-9
    print(digit, j)
    sum += j
  else:
    sum += int(digit)


sum=sum + int(checking_digit)
print(sum)

if sum%10 == 0:
  print("Valid Card Number")
else:
  print("Invalid number")

#OR
card_number = list(input("Please enter a card number: ").strip())

# Remove the last digit from the card number
check_digit = card_number.pop()
check_digit = int(check_digit)

# Reverse the order of the remaining numbers
card_number.reverse()

processed_digits = []

for index, digit in enumerate(card_number):
	if index % 2 == 0:
		doubled_digit = int(digit) * 2

		# Subtract 9 from any results that are greater than 9		
		if doubled_digit > 9:
			doubled_digit = doubled_digit - 9

		processed_digits.append(int(doubled_digit))
	else:
		processed_digits.append(int(digit))

print("processed_digit", processed_digits)
print("sum=",sum(processed_digits) )
sum_digit = sum(processed_digits)
total = check_digit + sum_digit

# Verify that the sum of the digits is divisible by 10
if total % 10 == 0:
	print("Valid!")
else:
	print("Invalid!")
