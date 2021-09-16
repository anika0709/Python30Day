name = "John"
age = 24

print(f"{name} is {age} years old!")

# print("Hello, World!".lower() )      # "hello, world!"
# print("Hello, World!".upper() )      # "HELLO, WORLD!"
# print("Hello, World!".capitalize() ) # "Hello, world!"
# print("hello, world!".title() )      # "Hello, World!"

print("  Hello, World!  ".strip())

# Using the variable below, print "Hello, world!".
# greeting = "Hello, world"
# You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours.

greeting = "Hello, world"
print ("{}!".format(greeting))
# Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.
# For example, if the user enters "lewis ", your output should be something like this:
# Hello, Lewis!
greeting = "Hello"
name = " lewis "
print(greeting + ", " + name.strip().title())

# Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
first = "I am "
age = 29

print(first + str(age))
# Remember that we can only concatenate strings to other strings, so you will have to convert the integer to a string before you can perform the concatenation.

# Format and print the information below using string interpolation:
# title = "Joker"
# director = "Todd Phillips"
# release_year = 2019
# The output should look like this:

# Joker (2019), directed by Todd Phillips

title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(f"{title} ({release_year}) directed by {director}")


# Our application should work as follows:

# The user should be given three prompts where they'll be asked to provide different information about an employee. One prompt should ask for the employee's name, another should ask for their hourly wage, and the final one should ask how many hours the employee worked this week.
# The employee name should be processed to ensure that it's in a particular format. All employee names should be stripped of any excess white space, and should be in title case. This means that each word is capitalised with all other letters being lowercase. For example, if the employer accidentally has caps lock on and they write "rEGINA gEORGE", the name will still be correctly stored as "Regina George".
# The employee's total earnings for the week should be calculated by multiplying the hours worked by their hourly wage.
# Remember that any user input we receive is going to be a string. While we can multiply strings, it won't quite do what you want in this case. It's also worth keeping in mind that the employee's wage, or the numbers of hours they worked, might not be a whole number.
# After processing the employee's name and calculating their earnings for the week, the program should output this information as a single string. For example, output like this would be appropriate:
# Regina George earned $800 this week.

name = input("Enter name: ").strip().title()
hours_worked = input ("Enter hours worked: ")
hourly_wage = input ("Enter hourly wage: ")

total_sal = float(hours_worked)*float(hourly_wage)
print("total_sal: ", total_sal)
print ("{} earned ${} this week.".format(name,int(total_sal)))







