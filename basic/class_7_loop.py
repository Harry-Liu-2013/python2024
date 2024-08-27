def demo():
  '''
  Loops in Python are used to execute a block of code repeatedly. Python primarily uses two types of loops: for loops and while loops.
  1. for Loops
  A for loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string).

  for element in sequence:
    # do something with element
  '''
  for number in [1, 2, 3, 4, 5]:
    print(number)
  '''
  Range Function:
  The range() function is often used with for loops to generate sequences of numbers.
  '''
  for i in range(5):  # Generates numbers from 0 to 4
    print(i)
  
  '''
  Range Function in List
  Useful when you want to get both value and index in a list
  '''
  list = ['a', 'b', 'c', 'd', 'e', 'f']
  for index in range(len(list)): # Generate numbers from 0 to len(list) - 1
    print(f"{list[index]} at index {index}")
    
    

  '''
  2. while Loops
  A while loop repeats as long as a certain boolean condition is met.

  while condition:
    # do something
  '''
  
  i = 1
  while i <= 5:
    print(i)
    i += 1 # if missing i+=1 will result in infinite loop
  '''
  Loop Control Statements
  - break: Exits the loop.
  - continue: Skips the rest of the code inside the loop for the current iteration and goes to the next iteration.
  '''
  for num in range(1, 10): # 5
    if num == 5:
      break  # Stops the loop when num equals 5
    if num % 2 == 0:
      continue  # Skips the current iteration if num is even
    print(num)
    
  # output: 1 3
  # all even numbers less than 5 will trigger continue and skip print()
  # all odd numbers less than 5 will NOT trigger continue and hit print()
  # 5 will trigger the break and exit the for loop
  '''
  Nested Loops
  You can use one loop inside another loop.
  '''
  for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
      print(f"i: {i}, j: {j}")
  '''
  Conclusion
  Loops are fundamental in Python and are used to execute repetitive tasks efficiently. The for loop is typically used when the number of iterations is known in advance, whereas the while loop is used when the iterations depend on a condition being true. Understanding how to control the flow of loops using break, continue, and else can lead to more efficient and readable code.
  '''


# Practice 1
'''
Write a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Requirements:
1. Input: A string. Example: text = "A man, a plan, a canal: Panama".
2. Process: Check if the string is a palindrome.
3. Output: The function should return True if the string is a palindrome and False otherwise.
4. Assume: The string can contain spaces, punctuation, and mixed case letters.

Example:
Input: text = "A man, a plan, a canal: Panama"
Output: True (This string is a palindrome when punctuation and spaces are ignored and letters are considered in a case-insensitive manner)

Tips:
1. Consider preprocessing the string to remove spaces and punctuation, and to standardize the case.

2. A loop can be used to compare characters from the beginning and end of the string, moving towards the middle.
'''


def is_palindrome(text):
  # 1. get rid of spaces, punctuations, and Caplitalization
  clean_string = ''.join(char.lower() for char in text if char.isalnum())
  # if char.isalnum() -> check if the char is alphabet or number
  # for char in text -> loop through every char in the text string
  # char.lower() -> convert letter to lowercase
  # ''.join(..) -> combine every eligible char, connect with '' (empty space)
  ## "A man, a plan, a canal: Panama" -> "amanaplanacanalpanama"
  
  # 2. have a way to comapre the string forward and backward
  # example 1 - not a palindrome
  # clean_string = abcd
  # clean_string[::-1] = dcba

  # example 2 - is a palindrome
  # clean_string = level
  # clean_string[::-1] = level
  is_good_palindrome = clean_string == clean_string[::-1]
  return is_good_palindrome


# Practice 2
'''
Write a Python function to rotate a list by a given number of steps to the right.

Requirements:
1. Input: A list of integers and an integer k, indicating the number of steps to rotate the list. Example: nums = [1, 2, 3, 4, 5], k = 2.
2. Process:
Rotate the list to the right by k steps.
For each step, the last element of the list should become the first.
3. Output: The rotated list.
4. Assume: k is non-negative.

Example:

Input:
nums = [1, 2, 3, 4, 5]
k = 2
step 1 -> [5,1,2,3,4]
step 2 -> [4,5,1,2,3]

Output: [4, 5, 1, 2, 3] (The list is rotated two steps to the right)

Things to Consider:
What happens if k is larger than the length of the list?
Try to find an efficient way to rotate the list without using extra space.
You may need to use modulo operation (%) to handle cases where k is greater than the list length.

'''


def rotate_list(nums, k):
  # step 1: understand the k, for small value or large value
  # nums = [1, 2, 3, 4, 5], k = 5
  # step 1 -> [5,1,2,3,4]
  # step 2 -> [4,5,1,2,3]
  # step 3 -> [3,4,5,1,2]
  # step 4 -> [2,3,4,5,1]
  # step 5 -> [1,2,3,4,5]
  # 5 or 10 or 15 ...
  # calculate the effective rotation by takeing the modulo of k with the list length
  real_k = k % len(nums) # --> get the raminder
  # 5 % 5 = 0
  # 10 % 5 = 0
  # 15 % 5 = 0
  # to use the remainder, we can get rid of repeating process, and only focus on the effective rotation

  # step 2 -> make the result after rotation
  answer = nums[-k: ] + nums[ : -k]
  # nums = [1, 2, 3, 4, 5], k = 2
  # nums[-2 : ] = [4, 5]
  # nums[ : -2] = begining to position -2 [1,2,3,4] but not include the last -2 element
  # nums[ : -2] -> [1,2,3]
  # combine -> nums[-k: ] + nums[ : -k] -> [4,5, 1,2,3]
  return answer
  


# Practice 3
'''
Write a Python function that finds the missing number in a given list of consecutive integers. The integers are in random order, and one number from the sequence is missing.

Requirements:
1. Input: A list of integers. Example: numbers = [3, 7, 1, 2, 8, 4, 5].
2. Process: Find the missing number in the sequence.
3. Output: The missing number.
4. Assume: There is exactly one number missing in the sequence, and the sequence starts from 1.

Example:
Input: numbers = [3, 7, 1, 2, 8, 4, 5]
current sum = 1+2+3+4+5+7+8
expected sum = 1+2+3...+ 8  #(len(list)+1)
(1+2+3+4+5+6+7+8) - (1+2+3+4+5+7+8) = missing number -> 6
Output: 6 (Since 6 is the missing number in the sequence from 1 to 8)

Tips:
- Consider how the sum of consecutive integers from 1 to n can be used to find the missing number.
- Try to solve this in a way that is both efficient in terms of space and time complexity.
'''


def find_missing_number(numbers):
  #expected_sum = (len(numbers)+1) # this should be 1+2+3+4+...+(len(numbers)+1)
  # an = a1 + (n – 1)d
  # Sn = n/2 (first term + last term)
  
  expected_size = (len(numbers) + 1)
  expected_sum = (1 + expected_size) * expected_size / 2

  current_sum = sum(numbers)
  missing_number = expected_sum - current_sum
  return missing_number