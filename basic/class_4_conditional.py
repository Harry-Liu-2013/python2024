def demo():
  print("***************** Simple if statement *******************")
  num = 5

  if num == 5:  # The condition is true
    # In Python, use indentation to define the block of code, usually by typing the 'Tab' key
    print("The number is equal to 5")  # The code is executed
    print("The number is equal to 5")  # The code is executed
  if num > 5:  # The condtion is false
    print("The number is greater than 5")  # The code is not executed

  print(
      "***************** if statement with Logical Operators *******************"
  )

  num = 12
  '''
  Logical Operator
  precedence: Not > And > Or
  '''

  if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    # Only print when num is a multiple of 2, 3, and 4
    print("The number is a multiple of 2, 3, and 4")

  # evaluation stops at num % 3 == 1, because it's False, and not need to check further
  # code inside the if won't be executed because the if statement is evaluated as False
  if num % 2 == 0 and num % 3 == 1 and num % 4 == 0:
    print("Version 2")

  if (num % 5 == 0 or num % 6 == 0):
    # Only works when num is either a multiple of 5 or 6
    print("The number is a multiple of 5 and/or 6")

  if num % 5 != 0:  # this is same as "if not num % 5 == 0:"
    print("The number is not a multiple of 5")

  print("***************** Nested if *******************")
  num = 63

  # Note: Each nest if statement requires further indentation.
  if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
      if num >= 60 and num <= 70:
        print("The number is in the 60-70 range")

  print("***************** Creating and Editing Values *****************")
  num = 10
  new_num = None  # to be safe, initialize a variable as None to avoid local variable not found error
  if num > 5:
    num = 20  # Assigning a new value to num
    new_num = num * 5  # Creating a new value called newNum

  # The if condition ends, but the changes made inside it remain
  print(num)
  print(new_num)  # new_num created only the above if statement is true

  print("***************** if-else statement *******************")

  num = 60

  if num <= 50:
    print("The number is less than or equal to 50")
  else:
    print(
        "The number is greater than 50")  # this line printed because if fails

  print("***************** Conditional Expressions *******************")
  '''
  output_value1 if condition else output_value2
  '''

  result = "pass" if num > 50 else "fail"
  # the result can have either "pass" or "fail"
  print(f"result = {result}")

  num = 60

  # Please note that the backslash \ in the above code is only a
  # line continuation character
  # that can be used to split a single line into multiple lines.
  output = "The number is less than or equal to 50" \
      if num <= 50 else "The number is greater than 50"

  print(output)

  print("***************** if-elif-else statement *******************")

  light = "Red"

  if light == "Green":
    print("Go")

  elif light == "Yellow":
    print("Caution")

  elif light == "Red":
    print("Stop")

  else:
    print("Incorrect light signal")

  print("***************** if-elif-else vs multiple if *******************")

  print("***************** if-elif-else shopping store *******************")
  costco_open = True
  walmart_open = True
  target_open = True
  shopping_store_count = 0
  if costco_open == True:
    shopping_store_count += 1
  elif walmart_open == True:
    shopping_store_count += 1
  elif target_open == True:
    shopping_store_count += 1
  else:
    print("None of the shopping stores are open")

  print("if-elif-else case: shopping_store_count = ",
        shopping_store_count)  # shopping_store_count =  1

  print("***************** multiple if shopping store *******************")
  costco_open = True
  walmart_open = True
  target_open = True
  shopping_store_count = 0
  if costco_open == True:
    shopping_store_count += 1
  if walmart_open == True:
    shopping_store_count += 1
  if target_open == True:
    shopping_store_count += 1

  print("multiple if: shopping_store_count = ",
        shopping_store_count)  # shopping_store_count = 3

  # **************************** Practice1 ******************************
  '''
  In this challenge, you must discount a price according to its value.

  If the price is 300 or above, there will be a 30% discount.

  If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.

  If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.

  If the price is less than 100, there will be a 5% discount.

  If the price is negative, there will be no discount.
  '''


def practice1():
  price = input("Input a price \n")
  price = float(price)
  if price >= 300:
    price = price * 0.7
    print("30% discount")
    print(price)
  elif price >= 200:
    price = price * 0.8
    print("20% discount")
    print(price)
  elif price >= 100:
    price = price * 0.9
    print("10% discount")
    print(price)
  elif price < 100 and price > 0:
    price = price * 0.95
    print("5% discount")
    print(price)
  else:
    print("No discount")
    print(price)

  # **************************** Practice2 ******************************
  '''
  Write a program that asks the user to enter a number.
  If the number is even, print "The number is even"
  If the number is odd, print "The number is odd"
  If the number is a multiple of 5, print "The number is a multiple of 5"
  If the number is a multiple of 7, print "The number is a multiple of 7"
  If the number is a multiple of 5 and 7, print "The number is a multiple of 5 and 7"
  If the number is a multiple of 5 or 7, print "The number is a multiple of 5 or 7"
  If the number is not a multiple of 5 or 7, print "The number is not a multiple of 5 or 7"
  '''


def practice2():
  number = input("Input a number \n")
  number = int(number)
  if number % 2 == 0:
    print("Even")
    if number % 5 == 0 and number % 7 == 0:
      print("Multiple of 5 and 7")
    elif number % 7 == 0:
      print("Multiple of 7")
    elif number % 5 == 0:
      print("Multiple of 5")
    else:
      print("Neither multiple of 5 or 7")
  elif number % 2 > 0:
    print('Odd')
    if number % 5 == 0 and number % 7 == 0:
      print("Multiple of 5 and 7")
    elif number % 7 == 0:
      print("Multiple of 7")
    elif number % 5 == 0:
      print("Multiple of 5")
    else:
      print("Neither multiple of 5 or 7")


def practice2_v2():
  number = input("Input a number \n")
  number = int(number)
  # 1st if block to check even or odd
  if number % 2 == 0:
    print("Even")
  else:
    print("Odd")

  # 2nd if block to check multiple of 5, 7
  if number % 5 == 0 and number % 7 == 0:
    print("Multiple of 5 and 7")
  elif number % 7 == 0:
    print("Multiple of 7")
  elif number % 5 == 0:
    print("Multiple of 5")
  else:
    print("Neither multiple of 5 or 7")
