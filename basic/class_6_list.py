def demo():
  '''
  Introduction to Lists
  A list in Python is an ordered collection of items which can be of any type. 
  Lists are versatile and can be used to store a sequence of objects.

  **** Creating Lists
  To create a list, you enclose items in square brackets [], 
  separating them with commas
  '''

  # create empty list
  list1 = [] # option 1 using "[]"
  list2 = list() # option 2 using list() function

  # create list with pre-defined values
  my_list = [1, 2, 3]
  names = ["Alice", "Bob", "Charlie"]
  mixed = [1, "Alice", True, 2.5]

  '''
  **** Accessing Elements
  You access elements in a list by their index, starting from 0.
  '''
  print(names[0])  # Output: Alice

  '''
  **** Modifying Lists
  '''
  
  '''
  Adding Elements: You can add elements using append() or extend().
  '''
  my_list.append(4)     # Adds 4 to the end
  my_list.extend([5, 6])  # Adds 5 and 6 to the end


  '''
  Updating elements
  '''
  names[1] = "updated value"
  
  '''
  **** Inserting Elements: Use insert() to add an element at a specific position.
  before [1,2,3,4,5,6,7]
  insert(1, 15)
  after [1,15,2,3,4,5,6,7]
  '''
  my_list.insert(1, 15)  # Inserts 'a' at index 1

  '''
  **** Removing Elements: Use remove() to remove a specific element or pop() to remove an element at a given index.
  '''
  my_list.remove(15)  # Removes the first occurence of 15
  popped = my_list.pop(1)  # Removes and returns the element at index 1

  '''
  **** List Slicing
  Slicing allows you to get a sub-list from the list.
  '''
  sub_list = my_list[1:3]  # Gets elements from index 1 to 2

  '''
  **** Iterating Over Lists
  You can iterate over lists using a for loop.
  '''
  for name in names:
    print(name)

  '''
  **** List Comprehensions
  List comprehensions provide a concise way to create lists.
  '''
  squares = [x**2 for x in range(10)]
  # for each number x in the range [0 - 9]
  # make it as x**2 as the element of the list 
  # squares = [0, 1, 4, 9, 16, 25, 36, 47, 64, 81]


  '''
  Common List Methods
  - len(my_list): Returns the number of items in the list.
  - min(my_list), max(my_list): Returns the minimum or maximum value.
  - my_list.count(x): Counts the number of occurrences of x in the list.
  - my_list.sort(): Sorts the list in place.
  - sorted(my_list): Returns a new sorted list from the elements of my_list.
  '''


# Practice 1
'''
Write a Python function that finds the second largest number in a given list of integers.

Requirements:
1. Input: A list of integers. Example: numbers = [1, 3, 4, 5, 0, 2].
2. Process: Identify the second largest number in the list.
3. Output: The function should return the second largest number.
4. Assume: The list will have at least two distinct numbers.

Example:
Input: numbers = [1, 3, 4, 5, 0, 2]
Output: 4 (5 is the largest number and 4 is the second largest)
'''
def find_second_largest(numbers):
  largest = -100000
  second_largest = -100000
  for number in numbers:
    if number > largest:
      largest = number
      #number = largest # largest = number
  for number in numbers:
    if number > second_largest and number != largest:
      second_largest = number
      #number = second_largest

  print(f"largest {largest}, second_larget {second_largest}")
  return second_largest



# Practice 2
'''
Write a Python function that takes two lists as inputs, merges them into a single list, removes duplicates, and returns a sorted list.

Requirements:
1. Input: Two lists of integers. Example: list1 = [3, 2, 5], list2 = [1, 4, 2].
2. Merge: Combine both lists into one.
3. Remove Duplicates: Ensure that each element is unique in the merged list.
4. Sort: Sort the final list in ascending order.
5. Return: The function should return the processed list.

Example:
Input:
list1 = [3, 2, 5]
list2 = [1, 4, 2]
Output: [1, 2, 3, 4, 5]
'''

list1 = [3, 2, 5]
list2 = [1, 4, 2]
def merge_sort_lists(list1, list2):
  merged_list = list1 + list2
  return print(merged_list)

merge_sort_lists(list1, list2)


  