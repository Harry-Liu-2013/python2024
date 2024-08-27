'''
Iterables

Definition: An iterable has the ability to return its elements one at a time.

A easy understand case of this feature, you can use a for loop to iterate over an iterable
Because List is an iterable

          iterable
     /    |    |     \           \
string  list  tuple  dictionary   ....



What is an iterator

An iterable can be iterated over. And an iterator is the agent that performs the iteration
To get an iterator from an iterable, you use the iter() function
'''
def demo():
  colors = ['red', 'green', 'blue']
  colors_iter = iter(colors)  # get the iterator object
  
  # Once you have the iterator, you can get the next element from the iterable using the next() function
  next_color = next(colors_iter)  # next()
  print(next_color)
  '''
  If there isn’t any more element and you call the next() function, you’ll get an exception
  '''
  '''
  The iterator is stateful. It means that once you consume an element from the iterator, it’s gone.
  
  In other words, once you complete looping over an iterator, the iterator becomes empty. If you iterate over it again, it’ll return nothing.
  
  Since you can iterate over an iterator, the iterator is also an iterable object. This is quite confusing. For example:
  '''
  
  colors = ['red', 'green', 'blue']
  iterator = iter(colors)
  
  for color in iterator:
    print(color)
  '''
  Output:
  
  red
  green
  blue
  '''
  '''
  **************************************************************************
  '''
  # map()
  '''
  The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.
  
  The following shows the basic syntax of the map() function:
  iterator = map(fn, list)
  In this syntax, fn is the name of the function that will call on each element of the list.
  '''
  
  
  # double value in the list using map
  def double(bonus):
    return bonus * 2
  
  
  bonuses = [100, 200, 300]
  
  iterator = map(double, bonuses)
  # Once you have an iterator, you can iterate over the new elements using a for loop.
  # Or you can convert an iterator to a list by using the the list() function :
  print(list(iterator))
  # output: [200, 400, 600]
  
  # filter()
  '''
  The filter() function iterates over the elements of the list and applies the fn() function to each element. It returns an iterator for the elements where the fn() returns True.
  '''
  
  
  def great_than_70(score):
    return score >= 70
  
  
  scores = [70, 60, 80, 90, 50]
  filtered = filter(great_than_70, scores)
  
  print(list(filtered))  # output [70, 80, 90]

# reduce()
'''
The reduce() function applies the fn function of two arguments cumulatively to the items of the list, from left to right, to reduce the list into a single value.

Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python. In fact, the reduce() function belongs to the functools module.

To use the reduce() function, you need to import it from the functools module using the following statement at the top of the file:
'''
from functools import reduce


def sum(a, b):
  print(f"a={a}, b={b}, {a} + {b} ={a+b}")
  return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)  #output 365
'''
List Comprehension

The following shows how to use list comprehension to make a list of squares from the numbers list:

numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

print(squares)
Code language: Python (python)
And here’s the list comprehension part:

squares = [number**2 for number in numbers]
Code language: Python (python)
A list comprehension consists of the following parts:


The following shows the basic syntax of the Python list comprehension:

[output_expression for element in list]

It’s equivalent to the following:

output_list = []
for element in list:
    output_list.append(output_expression)
'''

# Practice 1 - map() / filter()
'''
Write a Python program that takes a list of numeric strings (e.g., ['1', '5', '3', '8', '2']) and uses the map() function to perform the following transformations and operations:

1. Convert the list of strings to a list of integers.
2. Square each number in the newly converted list of integers.
3. Finally, filter out all squared numbers that are odd, leaving only the squared numbers that are even.
Your program should define a function transform_and_filter_list(input_list) that takes one argument, input_list, which is a list of numeric strings. The function should return a new list containing the squared, even numbers resulting from the transformations described above.

For instance, given the input list ['1', '5', '3', '8', '2'], the function should first convert it to [1, 5, 3, 8, 2], then square each number to get [1, 25, 9, 64, 4], and finally filter out the odd squares to return [64, 4].

Tips:
Use the map() function to convert the list of strings to integers and to square each number.
Use the filter() function or a list comprehension to filter out the odd squares.
Remember, the map() function returns a map object, which is an iterator. You will need to convert it to a list before performing further operations or returning it.
'''


def transform_and_filter_list(input_list):
  def convert_to_int(x):
    return int(x)**2
  def odd(square):
    return 
    
  input_list = map(convert_to_int, input_list)
  input_list = filter(odd, input_list)
  return print(input_list)

  pass


# Practice 2 - reduce()
'''
You are given a list of integers. Write a Python function that uses reduce() to compute the sum of the squares of these integers. For example, given the list [1, 2, 3], the function should compute 
1^2+2^2+3^=14

Requirements:

The function should take a single argument, a list of integers.
Use the reduce() function from the functools module to perform the computation.
You should also use a lambda function or a named function for the operation inside reduce().
If the list is empty, the function should return 0.

print(sum_of_powers([1, 2, 3])) # Should return 14 for squares
print(sum_of_powers([1, 2, 3], 3)) # Should return 36 for cubes
'''
from functools import reduce


def sum_of_powers(numbers, power=2):
  pass
