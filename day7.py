# 1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.
name = input("Enter First and Surname: ")
names = name.split(" ")
First = names[0]
Last = names[1]
print("First = ",First)
print ("last = ", Last)

# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
list1 = [1, 2, 3, 4, 5]
new_str = []  
for i in list1:
  new_str.append(str(i))

print(new_str, type(new_str))
print("|".join(new_str))

# 3) Below you’ll find a short list of quotes:

quotes = [
	"'What a waste my life would be without all the beautiful mistakes I've made.'",
	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
	"'The very essence of romance is uncertainty.'",
	"'We are not here to do what has already been done.'"
]
for quote in quotes:
    print (quote[1:-1])
    print (quote.strip("'"))
# Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

# You may also want to try a solution using strip.

# 4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.
word = input("enter word: ").strip()
print("Length of {} is {}".format(word, len(word)))
print(len(word.split())) # word count

# character_count = len(sample_string)
# word_count = len(sample_string.split())

# print(f"Character count: {character_count}")
# print(f"Word count: {word_count}")

# If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.
from collections import Counter

print(Counter(word))

# Reverse List
friends = ["Rolf", "John", "Mary"]
friends_reversed = friends[::-1]
print(friends_reversed)  # ['Mary', 'John', 'Rolf']

greet = "Hello, World!"
print(greet[::-1])  

# Check for Palindrome
def palindrome_check(word):
    if word == word[::-1]:  # check against full sequence in reverse order
        return True
    return False

print(palindrome_check("kayak"))  # True
print(palindrome_check("lemon"))  # False

#Project

# For this project, your program should do the following:

# Calculate the average budget of all movies in the data set.
# Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
# Print out how many movies spent more than the average you calculated.

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total = 0
for movie in movies:
  total += movie[1]

avg_budget = total/len(movies)
print("Avg budget =", avg_budget )  

for movie in movies:
  if movie[1] > avg_budget:
    print(movie[0], "has higher budget by", movie[1]-avg_budget)
# Ask the user how many movies they want to add to the list.
# Use range and a for loop to perform some option the specified number of times.
# Ask the user for a movie name and budget during each iteration of the loop, and append a tuple to the movies list containing this information.

entry = int(input("no of new entries:"))
try:
  for _ in range(entry):
    name = input("Enter new movie name: ")
    budget = int(input("Enter new movie budget: "))
    movie = (name,budget)
    movies.append(movie)
  print(movies)  
except TypeError as e:
  print (e)  
except Exception as e:
  print (e)  



