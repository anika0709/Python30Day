
# Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("Please enter name: ")
age = int(input("Please enter age: "))
print("{} is {} years old". format(name, age))

# Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.

age = 37
print("Age = ",age)
age = 45
print("Age now =", age)
# Below you’ll find some code with a number of errors. 
#Try to go through the program line by line and fix the issues in the code. 
#I’d encourage you to try running the program while you’re working on it, as reading the error messages is great practice for debugging your own programs.
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)




