def demo():
  print("Hello World")

  # snake_case - Python uses this way
  hello_this_is_snake_case_variable = "hello"

  # camelCase - Java uses this way
  helloThisIsCamelCaseVariable = "hello"

  # String
  print("Harry Potter!")  # Double quotation marks

  got = 'Game of Thrones...'  # Single quotation marks
  print(got)
  print("$")  # Single character

  empty = ""
  print(empty)  # Just prints an empty line

  multiple_lines = '''
  Triple quotes allows - line 1
  multi-line string. - line 2
  this is line 3
  '''
  print(multiple_lines)

  # length of string len()
  random_string = "I am Batman"  # 11 characters
  print(len(random_string))

  # indexing
  batman = "Bruce Wayne"

  first = batman[0]  # Accessing the first character
  print(first)

  space = batman[5]  # Accessing the empty space in the string
  print(space)

  last = batman[len(batman) - 1]
  print(last)
  # The following will produce an error since the index is out of bounds
  # err = batman[len(batman)]

  # Reversing index
  batman = "Bruce Wayne"
  print(batman[-1])  # Corresponds to batman[10]
  print(batman[-5])  # Corresponds to batman[6]

  # String Immutability
  # String is not allowed to be updated after creation
  string = "Immutability"
  # string[0] = 'O' # Will give error

  ################## Practice #################
  '''
  1. create a number variable to store an integer
  2. create a number variable to store a decimal number
  3. create a boolean variable to store either True / False
  4. create a string variabble to store the sum of #1 and #2 as string type
  '''

  #1

  num = 1
  print(num)

  #2

  float = 1.1
  print(float)
  #3

  T_F = True
  print(T_F)

  #4

  strng = (num + float)  # sum = num + float
  str(strng)  # strng = str(sum)
  print(strng)  # print(string)
  '''
  Question 2: String Reversal: Write a Python program to reverse a given string.
  Example: Input: "Hello", Output: "olleH".
  1. might need to create string to store the result
  2. might need to use a loop 
  sample of loop
  for i in range(start, end):
      logic in loop...
  '''
  # get string input
  # s = "Hello"
  # get the length of string
  # l = len(s)
  # hint: loop s from end char by char (most difficult)
  # hint: add each char into a new string variable
  # hint: finally print the result string
  # print(s)

  # Option 1: use for loop
  s = "Hello"
  output = ""
  length = len(s)  # get the size of string
  for idx in range(length - 1, -1, -1):
    # the range is how many elements need loop through (length-1 elements)
    # it starts at poistion -1 (last position in the string)
    # everytime the idx will (-1), which means will go to the left position in the string
    # H e l l o
    #         |
    #       |
    #     |
    #   |
    # |

    output += s[idx]  # += append the char(s[idx]) at the end of output string
    # output = "o"
    # output = "ol"
    # output = "oll"
    # output = "olle"
    # output = "olleH"
  print(output)

  # Option 2: use reverse string slicing
  ss = "Hello"
  output = ss[::-1]
  print(output)
