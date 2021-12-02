#Iterator - any time we call zip, enumerate, map, or filter, what we get back is an iterator.
#all iterators are iterables.
#1. Iterators are often lazy - Being lazy comes with some significant memory benefits, because we only have to keep the most recent value in memory. Once we're done using it for whatever it is we're doing, we can throw it away, potentially freeing up that memory.
#2. Iterator values are consumed - once it reaches the end of iterator, it throws StopIteration Exception

#3. Changes to mutable collections can affect an iterator

from operator import methodcaller
words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

words.append("apple")  # Added apple to the filter input as it is lazy

#next function
print(next(a_words)) #anaconda
print(next(a_words)) #anime

for word in a_words:
	print(word)

# a_words = list(a_words)

# print(a_words)  # []











