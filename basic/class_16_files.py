def demo():
  '''
  Reade txt file
  1. First, open a text file for reading by using the open() function.
  2. Second, read text from the text file using the file read(), readline(), or readlines() method of the file object.
  3. Third, close the file using the file close() method.
  '''
  '''
  Open()
  
  open(path_to_file, mode)

  The path_to_file parameter specifies the path to the text file.

  If the program and file are in the same folder, you need to specify only the filename of the file. Otherwise, you need to include the path to the file as well as the filename.

  To specify the path to the file, you use the forward-slash ('/') even if you’re working on Windows.

  For example, if the file readme.txt is stored in the sample folder as the program, you need to specify the path to the file as c:/sample/readme.txt

  Mode
  'r'	Open for text file for reading text
  'w'	Open a text file for writing text (overwrite previous data)
  'a'	Open a text file for appending text(doesn't overwrite, just apped at the end of the previous data)
  
  '''
  '''
  2) Reading text methods
  The file object provides you with three methods for reading text from a text file:

  read(size) – read some contents of a file based on the optional size and return the contents as a string. If you omit the size, the read() method reads from where it left off till the end of the file. If the end of a file has been reached, the read() method returns an empty string.
  readline() – read a single line from a text file and return the line as a string. If the end of a file has been reached, the readline() returns an empty string.
  readlines() – read all the lines of the text file into a list of strings. This method is useful if you have a small file and you want to manipulate the whole text of that file.
  '''
  '''
  3) close() method
  The file that you open will remain open until you close it using the close() method.

  It’s important to close the file that is no longer in use for the following reasons:

  First, when you open a file in your script, the file system usually locks it down so no other programs or scripts can use it until you close it.
  Second, your file system has a limited number of file descriptors that you can create before it runs out of them. Although this number might be high, it’s possible to open a lot of files and deplete your file system resources.
  Third, leaving many files open may lead to race conditions which occur when multiple processes attempt to modify one file at the same time and can cause all kinds of unexpected behaviors.
  '''


'''
Homework 1:

Defuse the Bomb
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!



Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

'''


def defuse_bomb(code, k):
  result = []
  if k == 0:
    decrypt = [0] * len(code)
    return decrypt

  for i in range(len(code)):
    if k > 0:  #replace the ith number with the sum of the next k numbers
      sum = 0
      next_index = i + i
      temp_count = k
      while (temp_count > 0):
        # divide by len of code and get the ramainder
        # the remainder is the next number position
        next_num = code[next_index % len(code)]
        # [5,7,1,4]
        #  0 1 2 3
        #  4 5 6 7 -> formula = index % len(code)
        #  4 % 4 = 0, 5 % 4 = 1, 6 % 4 = 2, 7 % 4 = 3
        #  8 9 10 11 ->
        #  8 % 4 = 0, 9 % 4 = 1, 10 % 4 = 2, 11 % 4 = 3
        sum += next_num
        temp_count -= 1
        next_index += 1
      result.append(sum)

    elif k < 0:  #replace the ith number with the sum of the previous k numbers.
      sum = 0
      next_index = i - 1
      temp_count = abs(
          k)  # k is negative number, so use abs() get the absolute value
      while (temp_count > 0):
        next_num = code[next_index % len(code)]
        sum += next_num
        temp_count -= 1
        next_index -= 1
      result.append(sum)

  return result


'''
Homework 2

Day of the Year
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
'''
def dayOfYear(date):
  # get year, month, day
  parsed_date = date.split('-')
  year, month, day = int(parsed_date[0]), int(parsed_date[1]), int(parsed_date[2])

  months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  day_number = 0

  curr_mon = 0
  while curr_mon < month - 1:
      day_number += months[curr_mon]
      curr_mon+=1

      # leap year
      if year % 4 == 0 and curr_mon >= 2:
          day_number += 1

  # plus day to the last month
  day_number += day
  return day_number
  
