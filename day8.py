# 1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

import random

print("Choosing a random num")
rand_number = random.randint(0,100)
print(rand_number)

while True:
  guess_num = int(input("Enter no between 0 to 100: "))
  if guess_num > rand_number:
    print("Your number is greater than number")
  if guess_num < rand_number:
    print("Your number is less than number")
  if guess_num == rand_number:
    print("You got it")
    break

# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.
for c in "Python":
  if c == "o":
    continue
  print(c)
# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.

prime_list = []
for i in range(3, 100):
	for d in range(2,i):
		if i % d == 0:
			break
	else:
	  prime_list.append(i)		

print(",".join(prime_list))


