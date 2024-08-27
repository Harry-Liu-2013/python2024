'''
https://usaco.org/index.php?page=viewproblem2&cpid=760
The Bovine Shuffle

1. review the solution of circular barn
2. re-write solutoin for speeding ticket
3. read and try to understand The Bovine Shuffle
'''

'''
Key info:
1. N cows (1≤ N ≤ 100) lining up in a row in some order
2. performing three "shuffles" in a row
3. after 3 shuffles, they will be lined up in some possibly different order
4. position 1…N, so the first cow in the lineup will be in position 1, the next in position 2, and so on, up to position N
5. Every cow moves to its new location during the shuffle, so no two cows try to move to the same position during a shuffle

Task: If you are given the ordering of the cows after three shuffles, please determine their initial order.
'''

'''
5 --- the number of cows
1 3 4 5 2 --- the N integers a1…aN, the shuffle rule
      the cow in position i moves to position ai
      cow#1 -> pos#1
      cow#2 -> pos#3
      cow#3 -> pos#4
      cow#4 -> pos#5
      cow#5 -> pos#2
    
1234567 2222222 3333333 4444444 5555555 --- the order of the N cows after three shuffles

output - the initial order
1234567
5555555
2222222
3333333
4444444
'''

'''
123    555    222    333     444
1st shuffle
123    444    555    222     333
2nd shuffle
123    333    444    555     222
3rd shuffle
123    222    333    444     555

'''


'''
Homework 8/05
1. review circular barn, draw something on paper to help understand
2. review speeding ticket solution
3. reivew the notes for bovine shuffle, think about how we could reverse the shuffle to get initial positions

'''

'''
8/07 Notes 
Normally, the shuffle is from initial position to final position
But this question is about reverse shuffle, because we are given the final position and we are asked to figure out the initial position

Normally, if we define a move[], it would be
move[pos_before] = pos_after
move [] = [1, 3, 4, 5, 2]
move [1] = 1
move [2] = 3
move [3] = 4
move [4] = 5
move [5] = 2

But for this question, we need to define a rever_move[], it would be
reverse_move[pos_after] = pos_before
reverse_move [] = [1, 5, 2, 3, 4]
reverse_move [1] = 1
reverse_move [2] = 5
reverse_move [3] = 2
reverse_move [4] = 3
reverse_move [5] = 4

Once we have the reverse_move list, we can perform the reverse shuffle 3 times

Finally, we will get the initial positions
'''

'''
Homework 8/07
1. review the diagrams sent on slack ("Circular Barn" and "Bovine Shuffle")
2. write code for Bovine Shuffle, based on step 1-4
'''

def solution():
      # 1. read input, and store the inputs into somewhere
      # 2. build reverse_move list: reverse_move[pos_after] = pos_before
      # 3. perform reverse shuffle 3 times
      # 4. return the cow list
      with open("usaco_bronze/input_files/shuffle.in", "r") as f:
            # code starts here....

            # 1.1 read the 1st line, trim white spaces, convert the text to int
            N = int(f.readline().strip())
            # 1.2 read the 2nd line, trim white spaces, split into single token, convert to int, and store in to a new list
            destinations =  list(map(int, (f.readline().strip().split())))
            # 1.3 read the 3rd line, trim white spaces, split into single token, store the values into a new list
            input_cow_ids = list(map(int, (f.readline().strip().split())))
            # 1.3.1 we re-map our final_cow_ids to make the index start at 1
            final_cow_ids = []
            for i in range(1, N+1):
                  final_cow_ids[i] = input_cow_ids[i-1]
                  '''
                  input_cow_ids[0] = 123
                  input_cow_ids[1] = 222
                  input_cow_ids[2] = 333
                  input_cow_ids[3] = 444
                  input_cow_ids[4] = 555
                  
                  final_cow_ids[1] = 123
                  final_cow_ids[2] = 222
                  final_cow_ids[3] = 333
                  final_cow_ids[4] = 444
                  final_cow_ids[5] = 555
                  '''

            # 2 build reverse_move list: reverse_shuffle_list[pos_after] = pos_before
            reverse_shuffle_list = []

            # extra work to do:
            # list index starts at 0, but cow posiotion start at 1, how we handle
            # solution: we re-map our list to make it start at 1
            for curr_pos in range(1, N+1): # re-map the range from 1 to N+1
                  dest = destinations[curr_pos-1] 
                  # why use curr_pos-1?
                  # becase the destinations use the index starting at 0
                  # destinations[0], ... destination[N-1]
                  # But the curr_pos here is in range 1 to N+1, will be 1, 2, 3, ... N
                  # if without -1, destinations[curr_pos] will return the wrong position value

                  # make reverse list, list[destination] = curr_pos
                  reverse_shuffle_list[dest] = curr_pos
                  '''
                  reverse_shuffle_list[1] = 1
                  reverse_shuffle_list[3] = 2
                  reverse_shuffle_list[4] = 3
                  reverse_shuffle_list[5] = 4
                  reverse_shuffle_list[2] = 5
                  '''
                  
            # 3. perform reverse shuffle 3 times
            original_cow_ids = []
            for final_pos in range(1, N+1):
                  # final_pos stands for each cow's final position after 3 shuffles
                  current_position = final_pos
                  for reverse_shuffle_round in range(3): 
                        # perform 3 reverse shuffle
                        # keep track the curre nt position after each reverse shuffle
                        # how to use current_position in reverse shuffle???
                        current_position = reverse_shuffle_list[current_position]
                        

                  # once we done 3 reverse shuffle, we need to update original_cow_ids[]
                  original_cow_ids[current_position] = final_cow_ids[final_pos]
      








