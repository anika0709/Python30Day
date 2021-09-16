#you're going to encounter loops with _ as the loop variable. This is perfectly legal, because _ is a valid variable name, and Python therefore won't complain.
# It serves a specific purpose, which is to indicate to readers that the loop variable is not actually being used in the loop body.

# A good time to use _ as a loop variable is in situations like this:

for _ in range(10):
	print("Hello!")

# 1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
# 2) For the employees above, print out those who are earning an hourly wage above average.
total_emp = len(employees)
print(total_emp) 
avg_wage,total_wage = 0,0
for emp in employees:
  total_wage = total_wage + emp[2]
avg_wage=total_wage/total_emp
for emp in employees:
  if emp[2] > avg_wage:
    print(emp[0]," gets higher wave")

# Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.

#Fizzbuzz

for n in range(15):
	if n%5 == 0 and n%3 == 0:
		print("FizzBuzz")
	if n%3 == 0:
		print("Fizz")
	if n%5 == 0:
		print("Buzz")
	else:
		print (n)


