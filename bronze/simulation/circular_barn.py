'''
link: https://usaco.org/index.php?page=viewproblem2&cpid=616
Circular Barn

Homework 7/17
1. review speeding ticket solution, make sure fully understand
2. read the question of circular barn, try to figure how sampe input result in sample output
3. brianstorm the solution, what approach you want to try

Homework 7/29
1. review speeding ticket solution, make sure fully understand
2. review the notes and hits, try to complete cicular barn
'''

def solution():
  # 1. read input, store capacity somewhere
  with open("usaco_bronze/input_files/cbarn.in", "r") as f:
    rooms = int(f.readline())
    cows = []
    for i in range(rooms):
      cows.append(int(f.readline()))
      
  # 2. have a variable to store the max total distance you got so far, initial could be 0
  min_total_distance = rooms * rooms * 100 # initially min_total_distance should be an impossible big number
  current_total_distance = 0
  # 3. loop all rooms, try to unlock the exterior door on every room, calculate the total distance
  for unlock in range(rooms): # try to unlock every room, unlock stands for the room you will unlock the door
    # Calculate the total distance with current unlock room
    # reset current_total_distance
    current_total_distance = 0 
    for offset in range(rooms): # offset stands for how far between the current and the original unlock room, offset could be 0, 1, 2, 3, 4, 5 ... n-1
      # clock: 12:00 and 1:00, offset = 1
      # clock: 12:00 and 6:00, offset = 6
      # clock: 12:00 and 11:00, offset = 11
      # clock: 12:00 and 12:00, offset = 0
      # offset: between 0 and 11
  
      # Currently, the clock points to 3:00, what's the number after the clock moving 7 hours => 10:00 
      # Currently, the clock points to 3:00, what's the number after the clock moving 15 hours => 6:00
      # 3:00 + 12 = (3 + 12) % 12 = 3
      # 3:00 + 3 = 6:00
  
      # 12:00 + 2000 hours = (12 + 2000) % 12 
      # 4:00 + 2000 hours = (4 + 2000) % 12 
      # unlock room + moving offset = (unlock + moving offset) % rooms
        
       current_total_distance += offset * cows[(unlock+offset) % rooms] # % rooms is to make sure the index doesn't get overflow

    
    
  # Hits: how to calculate current total distance
  # current_distance += offset * rooms[(unlock + offset) % n]
  # offset: the offset between current room and door unlocking room
  # unlock: the room you unlock the door
  # e.g. unlock room #0, current in room #0, offset is 0, rooms[(unlock+offset) % n] = rooms[0] = 4
  # e.g. unlock room #2, current in room #3, offset is 1, rooms[(unlock+offset) % n] = room[3] = 6
    
  # 4. comapre the min total distance with the current total distance this time, and keep the smaller one
    if(current_total_distance < min_total_distance):
      min_total_distance = current_total_distance

  # 5. Finally, the max total distance is the final answer
  return min_total_distance

    