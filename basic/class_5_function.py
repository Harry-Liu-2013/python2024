# *************** Create a Function without parameters ***************
# put "()" at end of function name
# don't forget ":" to declare a new block for this function
def my_print_function():  # No parameters
  print("This")
  print("is")
  print("A")
  print("function")


# *************** Create a Function with parameters ***************
def my_print_function_param(p1, p2, p3, p4):  # No parameters
  print(p1)
  print(p2)
  print(p3)
  print(p4)


# *************** Create a Function with optional parameters ****************
# for each parameter
# if the value is given by caller, then the given value will take effective
# it the value is NOT given by caller, then the default value will take effective
# e.g. at caller, can do:
# class_5_function.my_print_function_param_optional()
# class_5_function.my_print_function_param_optional(p3="optional", p1="It", p2="is" )
def my_print_function_param_optional(p1=None, p2=None, p3=None, p4=None):
  print(p1)
  print(p2)
  print(p3)
  print(p4)


# *************** Create a Function with parameters and return value ***************
# must have a return statement to return a value
# Caller will receive the return value and use it in a different way
def my_function_return(in1, in2, in3, in4):
  combined = f"{in1} {in2} {in3} {in4}"
  return combined
  # Any code below return statement will be ignored
  # which means return statement will terminate the function immediately
  print("hello")


# *************** Function without return ***************
'''
Function without return will return a None object
'''


def my_function_without_return():
  inner_var = "a"


# for conditional statement
# you need to have a return statement for each condition
def my_minimum(first, second):
  if (first < second):
    return first
  else:
    return second


def is_even(number):
  print(f" Will return {number % 2 == 0} for input number {number}")
  return number % 2 == 0


'''
Let's take your skill of converting miles to kilometers to the next level! Define a function that accepts the number of miles and returns this distance in kilometers.

Assume that one mile is approximately equal to 1.609 kilometers.
'''


def mi_to_km(miles):
  km = miles * 1.609
  return km


#****************** Practice 1*********************
'''
Write a Python function named convert_temperature that converts a given temperature from Fahrenheit to Celsius, or from Celsius to Fahrenheit, based on the user's choice.

Requirements:
Function Name: convert_temperature
Parameters:
temp: A numeric value representing the temperature to convert.
from_scale: A string, either "F" for Fahrenheit or "C" for Celsius, indicating the scale of the input temperature.
Returns: The function should return the converted temperature.
Conversion Formulas:
Celsius to Fahrenheit: (Celsius * 9/5) + 32
Fahrenheit to Celsius: (Fahrenheit - 32) * 5/9
Error Handling: If from_scale is not "F" or "C", the function should return None.

print(convert_temperature(32, 'F'))  # Should output 0 (Celsius)
print(convert_temperature(100, 'C')) # Should output 212 (Fahrenheit)
print(convert_temperature(78, 'X'))  # Should output None
'''


def convert_temperature(temp, letter):
  if letter == "F" or 'f':
    return print((temp - 32) * 5 / 9)
  elif letter == "C" or 'c':
    return print((temp * 9 / 5) + 32)
  else:
    return None


#****************** Practice 2 **********************
'''
Create a Python function named count_vowels that counts the number of vowels in a given string.
1. The function should take a single string argument.
2. It should return the count of vowels ('a', 'e', 'i', 'o', 'u') in the string.
3. The function should be case-insensitive (it should count both upper case and lower case vowels).

Sample Input and Output:

count_vowels("Hello World") should return 3 (due to 'e', 'o', 'o').
count_vowels("Python Programming") should return 4 (due to 'o', 'o', 'a', 'i').
'''


def count_vowels(string):  # string = "Hello World"
  vowels = "aeiouAEIOU"
  vowels_count = 0
  for _letter in string:
    if _letter in vowels:
      vowels_count += 1
  return print(vowels_count)
  # for _letter in string:
  #   if ('a' or 'A' in string) or \
  #   ('e' or 'E' in string) or \
  #   ('i' or 'I' in string) or \
  #   ('o' or 'O' in string) or \
  #   ('u' or 'U' in string):
  #     vowels = vowels + 1
  # return print(vowels)


#***************** Practice 3 ***********************
'''
Create a Python function named compress_string that implements a basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string is not smaller than the original string, your function should return the original string. You can assume the string only has uppercase and lowercase letters (a-z).

1. The function should take a single string as an argument.
2. It should return the compressed string if the compressed version is shorter, otherwise, it should return the original string.
3. You need to count consecutive characters and append the count after the character.

Sample Input and Output:

compress_string("aabcccccaaa") should return "a2b1c5a3".
compress_string("abcdef") should return "abcdef" (since compression does not shorten the string).
'''


def compress_string(string):
  # if the string is empty, no need to go further
  if string == "":
    return ""

  # initialization
  compressed_str = ""
  current_char = string[0]
  current_char_count = 1

  # loop over the string starting from the second character
  for next_char in string[1:]:
    if next_char == current_char:
      # increament the count if the same
      current_char_count += 1
    else:
      # 1. add the current char and count to the compressed_str
      compressed_str += current_char + str(current_char_count)
      # 2. reset the current char and count
      current_char = next_char
      current_char_count = 1

  # append the last char and count, because there is not next char to compare
  compressed_str += current_char + str(current_char_count)

  # return
  if len(compressed_str) < len(string):
    return compressed_str
  else:
    return string
