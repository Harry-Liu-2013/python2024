def sort_key(company):  # company is a tuple (name, year, revenue)
  return company[2]


def demo():
  '''
  list.sort() - sort the list in-place
  sort the list in-place (it will change the original list)
  in-place change 
  pros:
    1. more efficient, as you don't need to change the copy of the list one by one 

  cons
    1. more risky, original list change will impact all downsteam users
  '''
  list = []
  list.sort()  # sort the list from small to large
  list.sort(reverse=True)  # sort the list in reverse order (large to small)

  guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
  # string sort is by alphabet order
  # alphabet order checking will apply to string letter by letter until the order can be determined
  guests.sort()  # ['James', 'Jennifer', 'John', 'Mary', 'Patricia', 'Robert']

  # List sort() method to sort a list of tuples
  companies = [('Google', 2019, 134.81), ('Apple', 2019, 260.2),
               ('Facebook', 2019, 70.7)]

  companies.sort(key=sort_key, reverse=True)
  # output
  # [('Apple', 2019, 260.2), ('Google', 2019, 134.81), ('Facebook', 2019, 70.7)]

  # lambda expression
  # sort the companies by revenue
  companies.sort(key=lambda company: company[2], reverse=True)

  # More on lambda function
  '''
  https://www.pythontutorial.net/python-basics/python-lambda-expressions/
  '''
  '''
  sorted() function - sort the list in copy
  
  The list.sort() function sorts a list in place. In other words, it changes the order of elements in the original list.

  To return the new sorted list from the original list, you use the sorted() function
  '''
  list = []
  sorted(
      list)  # return a copy of sorted list without changing the orignal list
  sorted(
      list, reverse=True
  )  # return a copy of reverse sorted list without changing the orignal list
  '''
  List Slice
  sub_list = list[begin: end: step]
  The slice will start from the begin up to the end in the step of step.
  The begin, end, and step can be positive or negative. Positive values slice the list from the first element to the last element while negative values slice the list from the last element to the first element.
  '''

  # basic usage of list slice
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  sub_colors = colors[
      1:
      4]  # slice colors from index 1 to index 3, 4 is not included -> ['oriange', 'yellow', 'green']

  # basic usage with step
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  sub_colors = colors[
      1:5:
      2]  # slice colors from index 1 to index 5, 5 is not included, in step 2 (slice every 2 elements) -> ['orange', 'green']

  # to get the n-first (not include n) elements from a list
  # list[ : n]
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  sub_colors = colors[:
                      3]  # equivlent to colors[0:3] -> ['red', 'orange', 'yellow']

  # slice to get the n-last elements from a list
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  sub_colors = colors[
      -3:]  # equivlent to colors[-3 : len(colors)] -> ['blue', 'indigo', 'violet']

  # slice to get every nth element from a list
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  sub_colors = colors[::
                      2]  # slice every 2 elements -> ['red', 'yellow', 'blue', 'violet']

  # List slice to reverse a list
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  reverse_colors = colors[::
                          -1]  # slice list in reverse order -> ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

  # List slice to substitute part of a list
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  colors[0:2] = [
      'black', 'white'
  ]  # replace element at index 0, 1 -> ['black', 'white', 'yellow', 'green', 'blue', 'indigo', 'violet']

  # List slice to partially replace and resize a list
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  colors[0:2] = [
      'black', 'white', 'gray'
  ]  # take out 2 elements, put back with 3 elements -> ['black', 'white', 'gray', 'yellow', 'green', 'blue', 'indigo', 'violet']

  # List slice to delete elements
  colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
  del colors[
      2:
      5]  # del is keyword means delete -> ['red', 'orange', , , , 'indigo', 'violet']
  '''
  unpack list usually refer to assign list elements into variables
  there are different ways to do so and they can make your code clean code concise
  '''

  # basic unpack
  colors = ['red', 'blue', 'green']
  red = colors[0]
  blue = colors[1]
  green = colors[2]

  # sequence unpacking
  red, blue, green = colors

  # mistake in sequence unpacking
  # If you use a fewer number of variables on the left side, you’ll get an error. For example:
  colors = ['red', 'blue', 'green']
  red, blue = colors  # ValueError: too many values to unpack (expected 2)

  # sometimes, we only care about first few element, and don't care about the remaining

  # If you want to unpack the first few elements of a list and don’t care about the other elements, you can:
  # First, unpack the needed elements to variables.
  # Second, pack the leftover elements into a new list and assign it to another variable.
  # By putting the asterisk (*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable. For example:
  colors = ['orange', 'red', 'yellow', 'black', 'blue', 'purple']
  orange, red, *other = colors
  # output:
  # orange -> 'orange'
  # red -> 'red'
  # other -> ['yellow', 'black', 'blue', 'purple']


'''
You are given two lists, list1 and list2, that are sorted in non-decreasing order. Write a function that merges these two lists into one new sorted list in non-decreasing order. The new list should be made by splicing together the nodes of the first two lists. You may assume the lists are simple lists of integers

Examples:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Explanation: The merged list is [1,1,2,3,4,4] which is sorted in non-decreasing order.

Input: list1 = [0,3,4], list2 = [0,2,5]
Output: [0,0,2,3,4,5]
Explanation: The merged list is [0,0,2,3,4,5] which is sorted in non-decreasing order.

Input: list1 = [], list2 = [0,2,3]
Output: [0,2,3]
Explanation: Since list1 is empty, the merged list is the same as list2.
'''


def merge_sorted_lists(list1, list2):
  mergelists = []
  i = 0
  j = 0
  # keep looping when both i and j are not ended yet
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      mergelists.append(list1[i])
      i += 1
    else:
      mergelists.append(list2[j])
      j += 1

  while i < len(list1):
    mergelists.append(list1[i])
    i += 1

  while j < len(list2):
    mergelists.append(list2[j])
    j += 1
  # step 5 goes here..

  # 5. If there are remaining elements in list1, add them to merged list

  # 6. If there are remaining elements in list2, add them to merged list

  # 7. return the merged list
  return mergelists


#           i
# list1 = [ 1,  3,  5, 7, 8, 9, 10, 12, 14, 15, 20],

#           j
# list2 = [ 2,  2,  4]

# [1, 2, 2, 3, 4, 5]

# 1. create a new empty list which will store the result

# 2. create a variable i which will be the index of list 1
# 3. create a variable j which will be the index of list 2

# compare elements from both lists and add the smaller one to the merged list
# 4. while i < len(list1) and j < len(list2)
# if list1[i] < list2[j]:
# ...
# else:
# ...
