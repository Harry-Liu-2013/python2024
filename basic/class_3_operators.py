def demo():
  # logic of Boolean
  # and
  '''     
  and   |  True     False
  ------|----------------
  True  |  True     False
        |
  False |  False    False
  '''
  
  # or
  '''
  or    |  True    False
  ------|----------------
  True  |  True    True
        |
  False |  True    False
  '''
  
  
  '''
  Gravitational force is the attractive force that exists between two masses. It can be calculated by using the following formula:
  
  G * M * m / (r**2)
  
  where G is the gravitational constant, M and m are the two masses, and r is the distance between them.
  
  You must implement this equation in Python to calculate the gravitational force between Earth and the moon.
  
  Sample Input
  G = 6.67 * 10-11
  
  MEarth = 6.0 * 1024
  
  mMoon = 7.34 * 1022
  
  r = 3.84 * 108
  
  Sample Output
  FG = 1.99 * 1020
  
  Coding Challenge
  All the values have already been given to you. You must write the formula in Pythonic syntax and store the answer in the grav_force variable.
  
  If you feel stuck, refer to the solution review in the next lesson.
  
  Good luck!
  '''
  G = 6.67 * (10 ** -11)
  M = 6.0 * (10 ** 24)  # Mass of Earth
  m = 7.34 * (10 ** 22)  # Mass of the moon
  r = 3.84 * (10 ** 8)
  
  grav_force = G * M * m / (r**2)
  # Write your code here