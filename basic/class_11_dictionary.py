'''
Dictionary
- dictionary is a collection of key-value pairs where each key is associated with a value
'''
'''
list: ['a','b','c','d']
list[0] ==> 'a'
list[1] ==> 'b'
...

'''
'''
Dictionary -> key-value pair
dict: {}, use curly braces to declare 

dict: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
'''


def demo():
  # Empyt dictionary
  empty_dict = {}

  # dictionary with entries (key-value pair)
  person = {
      'first_name': 'John',
      'last_name': 'Doe',
      'age': 25,
      'favorite_colors': ['blue', 'green'],
      'active': True
  }

  # *********************** Access Key **********************
  print(person['first_name'])

  # access non-exist key
  ssn = person['ssn']  # get KeyError, due to key 'ssn' not found
  # output: Traceback (most recent call last):
  #  File "dictionary.py", line 15, in <module>
  #    ssn = person['ssn']
  #  KeyError: 'ssn'

  # access non-exist key and avoid KeyError
  ssn = person.get('ssn')  # get None, if the key not exist
  # output: None

  # access non-exist key and use default value instead of None
  ssn = person.get('ssn', '000-00-0000')  # get None, if the key not exist
  # output: 000-00-0000

  # *********************** Add / Modify Key-value paires**********************
  person['gender'] = 'Famale'
  # 1. if the key 'gender' not exsits, new key-value will be added into the dict
  # 2. if the key 'gender' already exsits, value will be modified as 'Female'

  # *********************** Remove Key-value paires**********************
  del person['age']

  # *********************** Loop dictionary**********************
  person = {
      'first_name': 'John',
      'last_name': 'Doe',
      'age': 25,
      'favorite_colors': ['blue', 'green'],
      'active': True
  }

  # loop key-value
  print(person.items())
  # items() returns an object which contains a list of key-value pairs as tuples in a list
  # output: dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 25), ('favorite_colors', ['blue', 'green']), ('active', True)])

  for k, v in person.items():
    print(f"{k}: {v}")

  # loop keys only
  for key in person.keys():
    print(key)
  # output:
  #    first_name
  #    last_name
  #    age
  #    favorite_colors
  #    active

  # loop values only
  for value in person.values():
    print(value)
  # output:
  #  John
  #  Doe
  #  25
  #  ['blue', 'green']
  #  True

  # Dictionary comprehension

  stocks = {
      'AAPL': 121,
      'AMZN': 3380,
      'MSFT': 219,
      'BIIB': 280,
      'QDEL': 266,
      'LVGO': 144
  }

  # for loop (traditional style)
  new_stocks = {}
  for symbol, price in stocks.items():
    new_stocks[symbol] = price * 1.02

  # comprehension style
  new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

  # with filter
  # for loop
  selected_stocks = {}
  for symbol, price in stocks.items():
    if price > 200:
      selected_stocks[symbol] = price

  # comprehension style
  selected_stocks = {
      symbol: price
      for (symbol, price) in stocks.items() if price > 200
  }


'''
Practice 1

Word Pattern
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

'''


def wordPattern(pattern, s):
  # 1. split string into words by white space
  words = s.split()
  # build the dictionary and check if both word and pattern are good
  pattern_to_word = {}  # {'a': 'dog', 'b':'cat'}
  word_to_pattern = {}  # {'dog': 'a', 'cat': 'b'}

  # 1. get the length of pattern and the length of words
  size_pattern = len(pattern)
  size_words = len(words)
  if size_pattern != size_words:
    return False
  # if not same --> return false

  # 2. use for loop to go through pattern and words
  i = 0
  for i in range(size_pattern):
    char_in_pattern = pattern[i]
    word = words[i]

    # if the mapping existing in one but not the other one: --> false
    if (char_in_pattern in pattern_to_word and pattern_to_word[char_in_pattern] != word) \
        or (word in word_to_pattern and word_to_pattern[word] != char_in_pattern):
      # case 1
      # pattern_to_word = {'a': 'dog'}
      # char = 'a'
      # word = 'cat'

      # case 2
      # word_to_pattern = {'dog': 'a'}
      # word = 'dog'
      # char = 'b'

      return False

    # otherwise, 1st seen, add mapping to both dict
    pattern_to_word[char_in_pattern] = word
    word_to_pattern[word] = char_in_pattern

  return True


'''
Practice 2
Keyboard stroks

Given an list of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []

Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


'''


def findWordsUsingDict(words):
  row_letters = {1: 'qwertyuiop', 2: 'asdfghjkl', 3: 'zxcvbnm'}
  row_1 = row_letters.get(1)
  row_2 = row_letters.get(2)
  row_3 = row_letters.get(3)
  ans = []
  for word in words:
    print(word)
    prev_letter_row = 0
    isGood = True
    for l in word:
      l = l.lower()  # convert letters to lower case before comparing
      curr_letter_row = 0
      # if l in row_1 ...
      if l in row_1:
        curr_letter_row = 1
      # elif l in row_2 ...
      elif l in row_2:
        curr_letter_row = 2
      # elif l in row_3 ...
      else:
        curr_letter_row = 3

      # compare prev_letter_row with curr_letter_row
      # if prev_letter_row is 0 --> current letter is the first letter
      # if prev_letter_row is NOT 0 --> can compare current letter with prev letter
      if prev_letter_row != 0 and prev_letter_row != curr_letter_row:
        # red flag --> letters are not from the same row
        isGood = False
        break
        # stop checking further for this word, because I know it's a "bad" word

      else:
        # so far all good -> update -> keep going to check the next letter
        prev_letter_row = curr_letter_row

    # will add this word into final answer if it a "good" word
    print(isGood)
    if isGood:
      ans.append(word)

  return ans


