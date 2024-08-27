'''
Set

1. Set is a data structure in python, samilar as what we have learned like List, Dictionary
2. Elements in Set is unordered (you try to add new element at end the Set, but actually Set may put this element in a different position)
3. Elements in a set are UNIQUE, A Set doesn't allow dupliate elements
'''

def demo():
  # create an empty set
  empty_set = {}
  empty_set = set()

  # create set with some elements
  skills = {'Python programming', 'Databases', 'Software design'}

  # create set from another set
  skills = set({'Python programming', 'Databases', 'Software design'})

  # create set from another iterable elements (e.g. list)
  skills = set([
      'Python programming', 'Databases', 'Software design', "CSS", "English",
      "Chinese", "French"
  ])

  # get length of set
  length = len(skills)

  # check empty set
  if not skills:
    print("Empty set is evaluated as False")


  # check if an element is in the set
  if "Databases" in skills:
    print("Database is in skills set")

  # check if an element is not in the set
  if "HTML" not in skills:
    print("HTML is not in skills set")


  # add element
  skills.add("Java")

  # remove exist element
  skills.remove("Databases")

  # remove non-exist element, will get error and program crash
  # skills.remove("HTML")  # KeyError: 'HTML'

  # Avoid remove error: solution 1
  # a safe way to remove(check before remove), no error throw
  if 'HTML' in skills:
    skills.remove('HTML')

  # Avoid remove error: solution 2
  # a better way of remove
  skills.discard('HTML')


  # remove all elements
  skills.clear()

  
  # frozen a set
  skills = set([
      'Python programming', 'Databases', 'Software design', "CSS", "English",
      "Chinese", "French"
  ])

  # To make a set immutable, you use the built-in function called frozenset(). The frozenset() returns a new immutable set from an existing one. For example:
  frozenSkills = frozenset(skills)


  # Loop set
  for skill in skills:
    print(skill)
    '''
    Output: 
    French
    CSS
    Python programming
    Software design
    Chinese
    English
    Databases
    '''


  # Loop set using enumerate(), enumerate() can give you the index of that element
  for index, skill in enumerate(skills):
    print(f"{index}.{skill}")
    '''
    Output:
    0.French
    1.CSS
    2.Python programming
    3.Software design
    4.Chinese
    5.English
    6.Databases
    '''


  # set comprehension

  # covert tags into lower case
  tags = {'Django', 'Pandas', 'Numpy'}

  lowercase_tags = set()
  for tag in tags:
      lowercase_tags.add(tag.lower())

  print(lowercase_tags)

  # comprehension way
  tags = {'Django', 'Pandas', 'Numpy'}
  lowercase_tags = set(map(lambda tag: tag.lower(), tags))

  print(lowercase_tags)


def demo_2():
  '''
  Union
  The union of two sets returns a new set that contains distinct elements from both sets.

  Link: https://www.pythontutorial.net/python-basics/python-set-union/
  '''

  s1 = {'Python', 'Java'}
  s2 = {'C#', 'Java'}

  # union() function
  new_set = s1.union(s2)

  print(s1)
  print(s2)
  print(new_set)  # union of set

  # union operator:  use '|' to union set
  new_set = s1 | s2
  print(new_set)

  # NOTE: In fact, the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.
  # However, the union operator (|) only allows sets, not iterables like the union() method.

  rates = {1, 2, 3}
  ranks = [2, 3, 4]

  ratings = rates.union(ranks)  # okay
  # ratings = rates | ranks # error: TypeError: unsupported operand type(s) for |: 'set' and 'list'


  s1 = {'Python', 'Java'}
  s2 = {'C#', 'Java'}
  s3 = {"JS", "Ruby"}
  s4 = {"Lua"}

  # union() allows multiple sets
  new_set = s1.union(s2, s3).union(s4)
  print(new_set)

  # union operator only allows set one by one
  new_set = s1 | s2 | s3 | s4
  print(new_set)


  '''
  intersection (the common elements in all sets)
  When intersecting two or more sets, you’ll get a new set consisting of elements that exist in all sets.

  Link: https://www.pythontutorial.net/python-basics/python-set-intersection/


  Use case of intersection:
  The set intersection has many useful applications. For example, you can use set intersections to find the common favorites of two friends on a social networking
  '''

  s1 = {'Python', 'Java'}
  s2 = {'C#', 'Java'}
  s3 = {"JS", "Ruby"}
  s4 = {"Lua"}

  # intersection function
  new_set = s1.intersection(s2, s3)

  # intersection operator '&'
  new_set = s1 & s2 & s3


  '''
  difference

  The difference between the two sets results in a new set that has elements from the first set which aren’t present in the second set.

  Link: https://www.pythontutorial.net/python-basics/python-set-difference/
  '''

  s1 = {'Python', 'Java', 'C++'}
  s2 = {'C#', 'Java', 'C++'}

  # difference function
  s1_diff = s1.difference(s2) # -> 'Python'
  s2_diff = s2.difference(s1) # -> "C#s"
  print(s1_diff)
  print(s2_diff)

  # difference operator
  s1_diff = s1 - s2  # result in the left elements in s1 only
  s2_diff = s2 - s1  # result in the left elements in s2 only
  print(s1_diff)
  print(s2_diff)


  '''
  symmetric difference (the union of difference)
  The symmetric difference between two sets is a set of elements that are in either set, but not in their intersection.

  Link: https://www.pythontutorial.net/python-basics/python-symmetric-difference/
  '''
  s1 = {'Python', 'Java', 'C++'}
  s2 = {'C#', 'Java', 'C++'}

  # symmetric difference function
  s = s1.symmetric_difference(s2)

  # symmetric difference operator
  s = s1 ^ s2

  '''
  Subset vs Superset
  Suppose that you have two sets A and B. Set A is a subset of set B if all elements of A are also elements of B. Then, set B is a superset of set A.

  Link: https://www.pythontutorial.net/python-basics/python-issubset/
  Link: https://www.pythontutorial.net/python-basics/python-issuperset/
  '''
  numbers = {1, 2, 3, 4, 5}
  scores = {1, 2, 3}

  # issubset function
  print(scores.issubset(numbers))

  # issubset operator
  print(scores <= numbers)

  # issuperset function
  print(numbers.issuperset(scores))

  # issuperset operator
  print(numbers >= scores)


  '''
  disjoint set
  Two sets are disjoint when they have no elements in common. In other words, two disjoint sets are sets whose intersection is an empty set.

  For example, the {1,3,5} and {2,4,6} sets are disjoint because they have no common elements.

  Link: https://www.pythontutorial.net/python-basics/python-disjoint-sets/
  '''

  odd_numbers = {1, 3, 5}
  even_numbers = {2, 4, 6}

  result = odd_numbers.isdisjoint(even_numbers)

  print(result)

  # No disjoin operator



# Practice 1
'''
Unique Number of Occurrences

Given a list of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Tips:
  1. consider which data strcuture is proper one to use
  2. get occurence cout for each value
  3. verify if all occurences are unique or not

  Set only allows unquie value
  1. from the nums dictionary, you get 3 entries
  2. add occurences into a set
  3. compare the size, if the set size still 3 --> all are unique occurences
      else --> some duplicated occurences exist
'''

def uniqueOccurrences(arr):
  nums = {} # dict
  for i in range(len(arr)):
    if arr[i] in nums:
      nums[arr[i]] += 1
    else:
      nums[arr[i]] = 1
  # nums: {1: 3, 2: 2, 3 : 1}
  unique_set = set()
  for value in nums.values():
    unique_set.add(value)
  
  return len(unique_set) == len(nums.values())

  

# Practice 2
'''
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
def two_sum(nums, target):
  pass



# Practice 3
'''
Common Word

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.



Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
'''
def common_word(paragraph, banned):
  '''
  dict:
  {
    key: "word"
    value: count of the word
  }
  {
    "hit" : 3
    "ball": 2
    "bob": 1 
  }
  '''
  word_counts = {}
  # 1. normalize the paragraph
  # isalnum(): https://www.w3schools.com/python/ref_string_isalnum.asp
  normalized_paragraph = ''.join(c.lower() if c.isalnum() else ' ' for c in paragraph)
  # normalized_paragraph = "bob hit a ball  the hit ball flew far after it was hit "
  # 2. parse words by whitespace
  # split(): https://www.w3schools.com/python/ref_string_split.asp
  words = normalized_paragraph.split() # split() by default splits string by whitespace
  # words = ["bob", "hit", "a", "ball", "the", "hit", "ball", "flew", "far", "after", "it", "was", "hit"]

  # 3. loop the words list and update word_counts dictionary
  for word in words:
    if word not in banned:
      if word in word_counts: # word exists in word_counts
        word_counts[word] = word_counts[word] + 1
      else: # word not exists in word_counts
        word_counts[word] = 1
  # 4. find out the most frequent non banned word
  maxfrequency =  max(word_counts.values())
  for word in word_counts:
    if word_counts[word] == maxfrequency:
      return word

