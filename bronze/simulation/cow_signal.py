'''
https://usaco.org/index.php?page=viewproblem2&cpid=665

Bessie and her cow friends are playing as their favorite cow superheroes. Of course, everyone knows that any self-respecting superhero needs a signal to call them to action. Bessie has drawn a special signal on a sheet of M×N paper (1≤M≤10,1≤N≤10 ), but this is too small, much too small! Bessie wants to amplify the signal so it is exactly K times bigger (1≤K≤10) in each direction.
The signal will consist only of the '.' and 'X' characters.

INPUT FORMAT (file cowsignal.in):
The first line of input contains M, N, and K, separated by spaces.
The next M lines each contain a length-N string, collectively describing the picture of the signal.

OUTPUT FORMAT (file cowsignal.out):
You should output KM lines, each with KN characters, giving a picture of the enlarged signal.

SAMPLE INPUT:
5 4 2
XXX.
X..X
XXX.
X..X
XXX.
SAMPLE OUTPUT:
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..

1st approach
1. 
XXX. -> XXXXXX..   // double column
2. 
XXXXXX.. -> XXXXXX.. * 2 // double row

2nd approach
1. 
XXX.  -> XXX. * 2  // double row
2.  
XXX. * 2 -> XXXXXX.. * 2 // double column

'''


# use input() to read input data
# use print() to print the output data

#get dimensions
# m = rows n = columns k = amplification
def solution():
  # m = int(input())
  # n = int(input())
  # k = int(input())
  # "5 4 2" MAP TO m n k
  m, n, k = map(int, input().strip().split())
  print(m, n, k)
  #loop through rows
  amplified_rows = []
  for i in range(m): # 0, 1,2,3,4
    row = input()
  #make rows k times larger  
    for char in row:
      amplified_rows.append(char*k)
  #print new row k times  
    for j in range(k):
      # print(amplified_rows) # Don't print the list directly
      amplified_rows_str = ''.join(amplified_rows)
      print(amplified_rows_str)
  #reset amplified_rows for next loop 
    amplified_rows.clear()
    


'''
Previous Solution
'''
def solucction1():
  '''
  input data can be read from input()
  No data need to store in list
  1. loop rows
    2. loop of K to duplicate the row
      3. loop each char in the current row
        4. duplicate each char K time
          5. print what you have
  '''

  # read first line to get M, N, K and covert to int
  M, N, K = map(int, input().strip().split())
  ##print(f"{M}, {N}, {K}")

  # for M, read each row and store the value in the variable "row"
  for i in range(M):
    # step 1 as above
    row = input().strip()

    # next, how to use the row var to start enlarging the image

    for j in range(K): # enlarge K times for each row
      enlarged_row = ''.join(char * K for char in row)
      print(enlarged_row)

solution()
    # enlarged_row = ""
    # for char in row:
    #   char * K
    #   enlarged_row += char * K
    # for j in range K:
    #   print(enlarged_row)


    # 2. generate the same row K times



    # 3. loop over each character for each generated row...

    # 4. print character k times (enlarge)

# this is to read / write data through file
def solution2():
  '''
  input data can be read from input()
  No data need to store in list
  1. loop rows
    2. loop of K to duplicate the row
      3. loop each char in the current row
        4. duplicate each char K time
          5. print what you have
  '''

  with open("cowsignal.in", "r") as f:
  # read first line to get M, N, K and covert to int
    M, N, K = map(int, f.readline().strip().split())
    ##print(f"{M}, {N}, {K}")

    with open("cowsignal.out", "w") as out:
      # for M, read each row and store the value in the variable "row"
      for i in range(M):
        # step 1 as above
        row = f.readline().strip()

        # next, how to use the row var to start enlarging the image

        for j in range(K): # enlarge K times for each row
          enlarged_row = ''.join(char * K for char in row)
          out.write(enlarged_row)
          out.write("\n") # new line
    
    
