# 1) Import the fractions module and create a Fraction from the float 2.25. You can find information on how to create fractions in the documentation.
import fractions

f = fractions.Fraction(2.25)
print(f)

# 2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:
from math import fsum

f_list = [2.1,2.8,4.1,5.6,7.9]
print(fsum(f_list))

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))
# 3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function. You can find documentation for this function here.
import random as r
ran_num = r.randint(1,100)
print(ran_num)
