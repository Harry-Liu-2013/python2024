def demo():
  '''
  try except
  https://www.pythontutorial.net/python-basics/python-try-except/
  
  
  In Python, there’re two main kinds of errors: syntax errors and exceptions
  
  - syntax errors: invalid Python code, happens before code running
  
  - exceptions: In Python, errors that occur during the execution(runtime) are called exceptions. The causes of exceptions mainly come from the environment where the code executes. 
  For example:
  
    Reading a file that doesn’t exist.
    Connecting to a remote server that is offline.
    Bad user inputs.
  
  '''
  '''
  Handling exception
  
  try:
    # code that may cause error
  except:
    # handle errors
  '''
  try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
      result = f'Sales increase {abs(change)}%'
    else:
      result = f'Sales decrease {abs(change)}%'

    print(result)
  except:
    print('Error! Please enter a number for net sales.')
  '''
  multiple except
  '''
  try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
      result = f'Sales increase {abs(change)}%'
    else:
      result = f'Sales decrease {abs(change)}%'

    print(result)
  except ValueError:
    print('Error! Please enter a number for net sales.')
  except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
  # It’s a good practice to catch other general errors by placing the catch Exception block at the end of the list:
  except Exception as error:
    print(error)
  '''
  finally clause
  
  try:
    # code that may cause exceptions
  except:
    # code that handle exceptions
  finally:
    # code that clean up
  
  The finally clause always executes whether an exception occurs or not. And it executes after the try clause and any except clause.
'''
  a = 10
  b = 0

  try:
    c = a / b
    print(c)
  except ZeroDivisionError as error:
    print(error)
  finally:
    print('Finishing up.')
  '''
  try...except...else

  If an exception occurs in the try clause, Python skips the rest of the statements in the try clause and the except statement execute.
  
  In case no exception occurs in the try clause, the else clause will execute.


  When you include the finally clause, the else clause executes after the try clause and before the finally clause.
  '''


'''
Practice 1

Baseball Game

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.


Return the sum of all the scores on the record after applying all the operations.

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
'''


def baseball_game(ops):
  for op in ops:
    pass
  pass


'''
Practice 2

Defanging IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''


def defangIPaddr(address: str):
  pass
