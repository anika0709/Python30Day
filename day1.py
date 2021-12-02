# Print your age to the console.

age = 38
print("My age is",age)
# Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!

year_mon = 12
year_week = 52
year_days = 365

print("Number of months in 27 years", year_mon*27)
print("Number of months in 27 years", year_week*27)
print("Number of months in 27 years", year_days*27)
# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.

import math

def circle_area(radius):
	area = math.pi*radius**2
	return area

print("The area is", circle_area(5))



