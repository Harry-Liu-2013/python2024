'''
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

def isAnagram(s, t):
  if len(s) != len(t):
    return False
  s_dict = {}
  t_dict = {}
  # {'a': 3, 'n': 1, 'g' : 1, 'r': 1, 'm' : 1}
  for i in range(len(s)):
    s_dict[s[i]] = s_dict.get(s[i], 0) + 1
    t_dict[t[i]] = t_dict.get(t[i], 0) + 1
    # if s_dict[s[i]] != t_dict[t[i]]:
    #   return False

  # compare two dictionaries once loop is completed
  if s_dict != t_dict:
    return False
  return True
    
  """
  :type s: str
  :type t: str
  :return type: bool
  """
  pass





'''
Roman Converter
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


def romanToInt(s):
  # make a mapping from roman value to integer value
  mapping = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
  total = 0
  prev_value = 0;

  # loop in reversed order, which means loop from the smallest digit
  for char in reversed(s):
    # get the integer value for the current roman value
    value = mapping[char]

    # if the current value is less than the previouse value, we subtract it from the total
    # this is for cases like IV(4), IX(9)
    if value < prev_value:
      total -= value
    else:
      total += value

    prev_value = value

  return total
