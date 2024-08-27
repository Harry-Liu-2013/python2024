'''
https://usaco.org/index.php?page=viewproblem2&cpid=1060

Homework 8/21
1. review diamond_collector
2. review milk_pails
3. read and start coding for daisy_chainsr
4. next class 8/23, Friday, 6:30


Homework 8/23
1. continue working on daisy chains
2. Next class, Monday, 8/25, 6:30

'''

'''
key info
1. N flowers (1 <= N <= 100)
2. flowers labeld 1 .. N
3. flower i has Pi petals
4. takes a photo of all flowers from flower i to flower j, pair(i,j)
5. 1 <= i <= j <= N
5. "average flower", a flower that has P petals, where P is the exact average number of petals among all flowers in the photo

Q: How many of Bessie's photos have an average flower?

1 1 2 3
1: flower 1 has 1 petal 
1: flower 2 has 1 petal
2: flower 3 has 2 petals
3: flower 4 has 3 petals

she takes photos from flower i to flower j (1 <= i <= j <= N)

ans=0
i = 1, j = 1, avg petal = 1, avg flower exist? yes     -> ans+1
i = 1, j = 2, avg petal = 1, avg flower exist? yes     ->ans+1
i = 1, j = 3, avg petal = 4/3, avg flower exist? no     ->ans + 0
i = 1, j = 4, avg petal = 7/4, avg flower exist? no     ->ans + 0

i = 2, j = 2, avg petal = 1, avg flower exist?  yes    ->ans + 1
i = 2, j = 3, avg petal = 1.5, avg flower exist? no    -> ans + 0
i = 2, j = 4, avg petal = 2, avg flower exist?  yes     ->ans + 1

i = 3, j = 3, avg petal = 2, avg flower exist?  yes    ->ans + 1
i = 3, j = 4, avg petal = 2.5, avg flower exist?  no    ->ans + 0

i = 4, j = 4, avg petal = 3, avg flower exist?  yes    ->ans + 1

ans = 6
'''

from os import CLD_CONTINUED


def solution():
  with open("usaco_bronze/complete_search/input_files/daisy.in", "r") as f:
    N = int(f.readline())
    petals = list(map(int, f.readline().strip().split()))
    ans = 0

    # i, j
    # compelete search starting at i, ending at j
    for i in range(1, N + 1):
      for j in range(i, N + 1):
        # calculate total # of patels from i to j, use sum()
        total = sum(petals[i:j+1])
        # calculate avg, and check does avg flower exist?
        # ans + 1 if exists
       
        
    
    
    
    # iflowers = []
    # jflowers = []
    # usedjindex = []
    # usediindex = []
    # ans = 0
    # for i in range(N):
    #   petals.append(int(f.readline())) # need to fix
    #   iflowers.append(int(f.readline()))
    #   jflowers.append(int(f.readline()))
    # for i in range(len(iflowers)):
    #   for j in range(len(jflowers)):
    #     if i not in usediindex and j not in usedjindex:
    #       flowers = []
    #       for k in range(iflowers[i], jflowers[j]):
    #         flowers.append(petals[k])
    #       avg = sum(flowers) / len(flowers)
    #       if avg in flowers:
    #         ans += 1
    #         usediindex.append(i)
    #         usedjindex.append(j)
          
          
          
      
 