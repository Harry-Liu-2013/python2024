'''
https://www.pythontutorial.net/python-basics/python-tuples/

Sometimes, you want to create a list of items that cannot be changed throughout the program. Tuples allow you to do that.

A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.
'''

# create a tuple
rgb = ('red', 'green', 'blue')

# access element in a tuple
rgb = ('red', 'green', 'blue')

print(rgb[0])
print(rgb[1])
print(rgb[2])

# re assign variable to different tuple
# Even though you can’t change a tuple, you can assign a new tuple to a variable that references a tuple. For example:

colors = ('red', 'green', 'blue')
print(colors)

colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)

# practice 1
'''
Find the Longest Consecutive Subsequence in a Tuple

You are given a tuple of integers, which might contain duplicate elements. Your task is to write a Python function that identifies the longest subsequence of consecutive integers present in the tuple. The elements in the subsequence should appear in the same order as they do in the tuple.

For example, in the tuple (4, 5, 1, 2, 3, 4, 6, 7), the longest consecutive subsequence is (1, 2, 3, 4 ) or (4, 5, 6, 7).

input: The input tuple containing integers.
'''

input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
def find_longest_consecutive_subsequence(input_tuple):
    pass