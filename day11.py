#If we try to remove an item which doesn't exist, we get a KeyError. If we don't want this KeyError to be raised, we can use another method called discard.

# 1) Create an empty set and assign it to a variable.

my_set = set()
# 2) Add three items to your empty set using either several add calls, or a single call to update.
my_set.add("Ankit")
my_set.update(["Anika", "Monika", "Tanu"])
print(my_set)

# 3) Create a second set which includes at least one common element with the first set.
new_set = ("Gaurav","Miraya", "Anika")

# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
print(my_set.union(new_set))
print(my_set.intersection(new_set))
print(my_set.symmetric_difference(new_set))

# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.

numbers = range(27, 54)
user_number = int(input("Enter a number: "))

if user_number in numbers:
	print("Your number is in the valid range.")
else:
	if user_number < numbers[0]:
		print("Your number is too low.")
	else:
		print("Your number is too high.")
# If you want an extra challenge, also tell the user if their number was too high or too low.


