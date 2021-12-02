nums = [1,2,3,4,5]
num_iter = iter(nums)

# print(num_iter)
# print (num_iter is iter(num_iter))
# print(next(num_iter))

while True:
	try: 
		n = next(num_iter)
	except StopIteration:
		break
	else:
		print(n)

# generator
#What yield actually does is create a pause in the execution of the function body. When we call next and pass in our generator iterator, 
#the code in the function body is going to run until we hit that yield keyword.

def first_hundred():
	for number in range(1, 11):
		yield number
gen = first_hundred()
print(next(gen))

# Generator Expression

print ([x for x in range(1,5)])
print({x:x**x for x in range(1,5)})

#print (x**2 for x in range(1,5) ) #<generator object <genexpr> at 0x10d1caf20>
sq = (x**2 for x in range(1,5)) 
while True:
	try:
		s = next(sq)
	except StopIteration:
		break
	else:
		print(s)

squares = (number ** 2 for number in range(1, 11))

print(*squares, sep=", ")

Exercises

# 1) Write a generator that generates prime numbers in a specified range. You can make use of your solution to exercise 3 from day 8 as a starting point.

def get_prime(n):
  #print(n)
  for i in range(2,n):
    if n % i == 0:
    #  print(f'{n} is divisible by {i}')
      break
  else:
    return (n)

prime_numbers = [get_prime(n) for n in range(2,20)  if get_prime(n) != None ]
print(prime_numbers)

p_m = (get_prime(n) for n in range(2,20)  if get_prime(n) != None)
print(p_m)
for p in p_m:
  print (p,end=",")

#OR
def gen_prime(limit):
  for dividend in range(2,limit+1):
    for divisor in range(2,dividend):
      if dividend % divisor == 0:
        break
    else:
      yield (dividend)

primes = gen_prime(21)
#print ("printing p")
print(next(primes)) 

# 2) Below we have an example where map is being used to process names in a list. Rewrite this code using a generator expression.

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = (name.strip().title() for name in names)
print(names)
for n in names:
  print (n)
# 3) Write a small program to deal cards for a game of Texas Hold'em. The order of the deal is as follows:

# The deck is shuffled.
# One card is handed to each player in order.
# A second card is handed to each player order.
# Then comes the more complicated part of the deal.

import random
ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")
cards = []
for rank in ranks:
  for suit in suits:
    cards.append((rank,suit))
print(len(cards))

def shuf_cards(cards):
  deck = list(cards)
  random.shuffle(deck)
  return iter(deck)
  

#OR
import itertools


# How many players are there? 2

# Player 1 was dealt: (4, hearts), (4, clubs)
# Player 2 was dealt: (9, clubs), (jack, diamonds)

# The flop: (jack, clubs), (4, diamonds), (king, spades)
# The turn: (8, hearts)
# The river: (ace, hearts)
# As the example would indicate, the program should accept a variable number of players. There must be at least 2 players, and no more than 10.




