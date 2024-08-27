def input_one():
  '''
  Summary: input format 1
  Each line contains multiple values
  split() is needed to separate the line into multiple tokens
  '''

  '''
  input data
  3 3
  40 75
  50 35
  10 45
  40 76
  20 30
  40 40
  '''
  # read from file (this is same as read from input())
  with open("usaco_bronze/input_reuse_data.txt", "r") as f:
    # 1. read the first line "3 3"
    
    # f.readline() - read the next SINGLE line of the file
    # strip() - trim beginning and ending whitespace, e.g. "       hello world      "
    #           "       hello world      ".strip() ===> "hello world"
    # split() - split the string into smaller piece of string by given special delimiter, the default delimiter is whitespace " "
    #           "hello world this is from python".split() ===> ["hello", "world", "this", "is", "from", "python"]
    tokens = f.readline().strip().split()
  
    # create variable to store the value
    M = int(tokens[0])
    N = int(tokens[1])
    print(f"M is {M}, N is {N}")
  
    # 2. read the next M lines from file, store the 1st value into segments[], store the 2nd value into speeds[], remember convert to int
    segments = []
    speeds = []
    for i in range(M):
      # f is the file object, it's holding the file data as well as what's the current line you are reading
      tokens = f.readline().strip().split()
      segments.append(int(tokens[0]))
      speeds.append(int(tokens[1]))
    print(f"segments[]: {segments}")
    print(f"speeds[]: {speeds}")

    # 3. read the next N line from the file, store the 1st value into travels[], store the 2nd value into travel_speeds[]. remember convert to int
    travels = []
    travel_speeds = []
    for i in range(N):
      tokens = f.readline().strip().split()
      travels.append(int(tokens[0]))
      travel_speeds.append(int(tokens[1]))
    print(f'travels[]: {travels}')
    print(f'travel_speeds[]: {travel_speeds}')
    

def input_two():
  '''
  Summary: input format 2
  Each line contains SINGLE value
  split() is NOT needed to separate the line into multiple tokens
  '''

  '''
  3 4
  hello
  world
  I think
  python
  is
  very
  easy
  
  1. read file usaco_bronze/input_reuse_data2.txt
  2. read the 1st line and store the value into variable M, N
  3. read the next M lines, and store each line as an element into the my_words1[]
  4. read the next N lines, and store each line as an element into the my_words2[]
  5. print from 2 lists as a single sentence "hello world I think python is very easy"
  '''
  my_words1 = []
  my_words2 = []
  with open("usaco_bronze/input_reuse_data2.txt", "r") as f:
    tokens = f.readline().strip().split()
    M = int(tokens[0])
    N = int(tokens[1])
    for i in range(M):
      line = f.readline().strip()
      my_words1.append(line)
    for i in range(N):
      line = f.readline().strip()
      my_words2.append(line)
    print(f'my_words1[]: {my_words1}')
    print(f'my_words2[]: {my_words2}')
    merge_list = my_words1 + my_words2
    print(f'merge_list[]: {merge_list}')
    simple_sentence = ' '.join(merge_list) # use ' '.join(list), can take out every element and join them with whitespace
    print(f"simple_sentence: {simple_sentence}")
    
  
      
  
  
