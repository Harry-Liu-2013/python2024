'''
https://usaco.org/index.php?page=viewproblem2&cpid=615

Farmer John has received an order for exactly M
 units of milk (1≤M≤1,000
) that he needs to fill right away. Unfortunately, his fancy milking machine has just become broken, and all he has are three milk pails of integer sizes X
, Y
, and M
 (1≤X<Y<M
). All three pails are initially empty. Using these three pails, he can perform any number of the following two types of operations:
- He can fill the smallest pail (of size X
) completely to the top with X
 units of milk and pour it into the size-M
 pail, as long as this will not cause the size-M
 pail to overflow.

- He can fill the medium-sized pail (of size Y
) completely to the top with Y
 units of milk and pour it into the size-M
 pail, as long as this will not cause the size-M
 pail to overflow.

Although FJ realizes he may not be able to completely fill the size-M
 pail, please help him determine the maximum amount of milk he can possibly add to this pail.

INPUT FORMAT (file pails.in):
The first, and only line of input, contains X
, Y
, and M
, separated by spaces.
OUTPUT FORMAT (file pails.out):
Output the maximum amount of milk FJ can possibly add to the size-M
 pail.
SAMPLE INPUT:
17 25 77
SAMPLE OUTPUT:
76
In this example, FJ fills the pail of size 17 three times and the pail of size 25 once, accumulating a total of 76 units of milk.
'''

'''
X = 17
Y = 25
M = 77

max amount = 76

1. try to fill with X only, with xTimes, get xAmount
2. try to fill with Y only, with yTimes, get yAmount
3. try to fill with some X xTimes and some Y yTimes, get xAmount + yAmount
   - X 1 time  and no overflow,  Y ? times and no overflow -> xAmount + yAmount
   - X 2 times and no overflow,  Y ? times and no overflow -> xAmount + yAmount
   - X 3 times and no overflow,  Y ? times and no overflow -> xAmount + yAmount
   - X i times and no overflow,  Y j times and no overflow -> xAmount + yAmount
   - Compare your current answer with prev max amount -> take the larger one
'''

def solution():
  with open("usaco_bronze/complete_search/input_files/pails.in", "r") as f:
    #Read input
    X, Y, M = map(int, f.readline().split())
    max_amount = 0
    #Get xTimes and yTimes
    xTimes = M // X
    yTimes = M // Y
    if X * xTimes > max_amount:
      max_amount = X * xTimes
    if Y * yTimes > max_amount:
      max_amount = Y * yTimes

    # compelete search the best xTimes and yTimes
    for i in range(1, xTimes +1):
      for j in range(1, yTimes +1): # j = 4
        cur_total = X * i + Y * j
        if cur_total > M:
          break # if cur_total > M, break j loop and start with next value i
        if cur_total > max_amount and cur_total <= M:
          max_amount = cur_total

    return max_amount
          
    
    

  
  