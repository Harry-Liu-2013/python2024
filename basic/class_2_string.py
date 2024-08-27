def demo():
  ############### string slicing ##########
  ss = "0123456789"
  print(ss[2:7])  # [start:end]
  print(ss)  # the original string won't be changed (string is immutable)

  print(ss[2:])  #[start:] -> slice from start to end of string
  print(ss[:10])  #[:end] -> slice from beginnig of string up to the end index
  print(ss[2:-1])  # -> '2345678', slice from 2 to the -2 index
  print(ss[-5:-1])  # -> '5678'
  print(ss[-1:-5])  # -> empty string, becase start > end (invalid range)
  print(ss[6:2])  # -> empty string, becase start > end (invalid range)

  print(ss[0:11:1])  # -> equals to ss[0:11]
  print(ss[0:11:2])  # -> '02468', left to right
  print(ss[11:0:-2])  # -> '97531', right to left
  print(
      ss[::2]
  )  # -> '02468', slice from beginning to the end, skip every 2 char from left to right
  print(
      ss[::-2]
     # 9 -> 7 -> 5 -> 3 -> 1
  )  # -> '97531', slice from beginning to the end, skip every 2 char from right to left

  #***************** Format with % operator ********************
  # format string with string
  string1 = "I like %s" % "Python"  # %s is a string placeholder
  print(string1)  # 'I like Python'

  temp = "Educative"
  string2 = "I like %s" % temp
  print(string2)  # 'I like Educative'

  string3 = "I like %s and %s" % ("Python", temp)
  print(string3)  # 'I like Python and Educative'

  # format string with integer
  my_string = "%i + %i = %i" % (1, 2, 3)  # %i is a integer placeholder
  print(my_string)  # '1 + 2 = 3'

  # format string with float
  string1 = "%f" % (1.1234567899)
  print(string1)  # '1.110000'

  string2 = "%.2f" % (1.11)
  print(string2)  # '1.11'

  string3 = "%.2f" % (1.117)
  print(string3)  # '1.12'

  string3 = "%.2f" % (1.111)
  print(string3)  # '1.11'

  #***************** Format with format() function ********************
  # format string using format()
  string1 = "I like {}".format("Python")
  print(string1)  #  I like Python

  # format string using format()
  string1 = "I like {} {}".format("Python", 3.12)
  print(string1)  #  I like Python 3.12

  # format string using format()
  string1 = "I like {} {} as well as {} {}".format("Python", 3.12, "Java", 17)
  print(string1)  #  I like Python 3.12 as well as Java 17

  #***************** Format with f"" string ********************
  v1 = "Python"
  v2 = 3.12
  v3 = "Java"
  v4 = 17
  string1 = f"I like {v1} {v2} as well as {v3} {v4}"
  print(string1)  #  I like Python 3.12 as well as Java 17
  '''
  Practice 1
  You are given a string s and two integers start and end. Your task is to extract and return the substring 
  that begins at index start and ends at index end (inclusive). The string is zero-indexed.

  For example, if s = "python" and start = 1, end = 3, the substring from index 1 to 3 is "yth".

  Input:

  A string s (1 ≤ len(s) ≤ 1000)
  Two integers start and end (0 ≤ start ≤ end < len(s))
  
  Output:

  A string representing the substring from start to end.

  e.g. print(practice1("datascience", 4, 7)) --> "scie"
  
  '''
  source = "computer science"
  start = 5
  end = 10
  # your code...
  # orignal code
  # Words = input('Insert word(s)\n')
  # Start = input('Start')
  # End = input('End')
  # Start = int(Start)
  # End = int(End)
  # Words = Words[Start:End]
  # print(Words)
  # output --> "ter sc"

  words = input('Insert word(s): ')  # variable starts with lowercase
  start = input('Start: ')
  end = input('End: ')
  start = int(start)
  end = int(end)
  result = words[
      start:end +
      1]  # end is not inclusive by default, use end + 1 to include end
  print(result)
  '''
  Practice 2
  You are given a name and a time of the day (morning, afternoon, evening). Your task is to 
  create a greeting message using string formatting.    
  The message should be in the format: "Good [time of day], [name]!"

  For example, if the name is "Alex" and the time of the day is "morning", the output should be "Good morning, Alex!".

  Input:

  A string name.
  A string time_of_day, which can be "morning", "afternoon", or "evening".
  Output:

  A string representing the formatted greeting.
  '''
  name = "Alex"
  time_of_day = "afternoon"
  # your code...
  time = 'Afternoon'
  name = 'Alex'
  string1 = 'Good {}, {}!'.format(time, name)  # use format()
  print(string1)

  string2 = f'Good {time}, {name}!'  # use f string
  print(string2)

  # output --> "Good afternoon, Alex!"
