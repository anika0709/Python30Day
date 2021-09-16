#1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.

list1 = [4,5,6]
list2 = [4,5,6]

print(list1  == list2) #True
print(list1 is list2)
print("mem location of list1",id(list1))
print("mem location of list2",id(list2))
print(id(list1) == id(list2)) #False

list3 = list1
print("mem location of list2",id(list3))
print(list1  == list3) #True
print(list1 is list3) #True

# 2) Try to use the is operator or the id function to investigate the difference between this:

# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]
# And this:

# numbers = [1, 2, 3, 4]
# numbers.append(5)

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print (id(numbers), id(new_numbers)) #same id
numbers = [1, 2, 3, 4]
print (id(numbers))
numbers.append(5)
print (id(numbers))

# Are new_numbers and numbers the same thing? YES
#What about numbers before and after we append 5? YES

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
num = int(input("Enter no: "))
if num > 0:
  print("positive")
elif num <0:
  print("negative")
elif num==0:
  print("Zero")
else:
  print("Not a valid number")

# 4) Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
hours_worked = int(input("Hours worked: "))
hourly_wage = int(input("Hourly wage: "))
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.
add_pay = 0
if hours_worked > 40:
  print("overtime")
  regular_pay = 40*hourly_wage
  add_pay = (hours_worked-40)* 110/100*hourly_wage

else:
  regular_pay = hours_worked * hourly_wage

  print("new pay is ",regular_pay+ add_pay)

