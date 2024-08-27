'''
https://usaco.org/index.php?page=viewproblem2&cpid=568

Speeding Ticket

07/10
1. understand the question and the example explaination
2. brianstorm the solution, e.g. what steps you might try

07/15
3. read / parse input and store the input into variable / list - we already did most work in the input_one()
4. print out those variable / list


Key info
1. The road is exactly 100 miles long
2. The road is divided into N segments, each described by a positive integer length in miles, as well as an integer speed limit in the range 1…100 miles per hour
3. Bessie's journey can also be described by a series of segments, M
4. During each segment, she travels for a certain positive integer number of miles, at a certain integer speed

Task: determine the maximum amount over the speed limit that Bessie travels during any part of her journey.
 

'''

def solution():
  #1. read the input
  with open("usaco_bronze/simulation/input_files/speeding.in", "r") as f:
    tokens = f.readline().strip().split()
    N = int(tokens[0])
    M = int(tokens[1])
    print(f"M is {M}, N is {N}")
    road_segments = []
    speed_limits = []
    for i in range(N):
      tokens = f.readline().strip().split()
      road_segments.append(int(tokens[0]))
      speed_limits.append(int(tokens[1]))
    print(f"road_segments[]: {road_segments}")
    print(f"speed_limits[]: {speed_limits}")
    travel_segments = []
    travel_speeds = []
    for i in range(M):
      tokens = f.readline().strip().split()
      travel_segments.append(int(tokens[0]))
      travel_speeds.append(int(tokens[1]))
    print(f'travel_segments[]: {travel_segments}')
    print(f'travel_speeds[]: {travel_speeds}')
    # 2. find out the max amount over the speed limit
    # we want to compare the travel speed with the speed limit mile by mile
    # at mile 1: speed limit = 75, travel speed = 76 => over speed limit = 1
    # at mile 50: speed limit = 35, travel speed = 30 => over speed limit = -5
    # at mile 75: speed limit = 35, travel speed = 40 => over speed limit = 5
    # at mile 100: speed limit = 45, travel speed = 40 => over speed limit = -5



    mile_speedlimit = 0
    mile_travelspeed = 0
    # 3. build detail speed limit list to get speed limit at every mile from mile 1 to mile 100
    detail_speed_limit = [] # speed limit at each mile from mile 0 - 99
    for i in range(N):
      segment_length = road_segments[i] # 40
      segment_speed_limit = speed_limits[i] # 75
      current_mile = 0
      for j in range(segment_length):
        current_mile +=1
        detail_speed_limit.append(segment_speed_limit)
    print(f"detail_speed_limit: {detail_speed_limit}, size is {len(detail_speed_limit)}")

    # 4. similar to detail_speed_limit, we need to build detail_travel_speed
    # build detail travel speed list to get travel speed at every mile from mile 1 to mile 100
    detail_travel_speed = []
    for i in range(M):
      travel_length = travel_segments[i]
      segment_travel_speed = travel_speeds[i]
      current_mile = 0
      for j in range(travel_length):
        current_mile += 1
        detail_travel_speed.append(segment_travel_speed)
    print(f"detail_travel_speed: {detail_travel_speed}, size is {len(detail_travel_speed)}")

    # 5. solution -> make the comparasion at every mile
    # for mile 0 - 99
    #     speed limit = ? --- good
    #     travel speed = ? --- good
    #     amount over limit = x 
    #     if x > what I found so far:
    #        replace current max with x
    #     else: keep current max
    # finally return current max
    max_over_limit = 0
    for mile in range(0, 100):

      curr_speed_limit = detail_speed_limit[mile]
      curr_travel_speed = detail_travel_speed[mile]
      curr_over_limit = curr_travel_speed - curr_speed_limit
      if curr_over_limit > max_over_limit:
        max_over_limit = curr_over_limit
    print(max_over_limit)
    
    
    
          
        
        
      
      
    
    
    

