import random
import os
import time


cubes = [
"""
   * * * * *
   *       *
   *   X   *
   *       *
   * * * * *
""",
"""
   * * * * *
   *       *
   * X   X *
   *       *
   * * * * *
""",
"""
   * * * * *
   *     X *
   *   X   *
   * X     *
   * * * * *
""",
"""
   * * * * *
   * X   X *
   *       *
   * X   X *
   * * * * *
""",
"""
   * * * * *
   * X   X *
   *   X   *
   * X   X *
   * * * * *
""",
"""
   * * * * *
   * X   X *
   * X   X *
   * X   X *
   * * * * *
"""
]

running = True
t = 0
orig_cube = cubes[:]
os.system('cls' if os.name == 'nt' else 'clear')
p1 = int(input('Player 1 guess [1-6]: '))
p2 = int(input('Player 2 guess [1-6]: '))
while running:
   t += 0.01
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f'Player 1 guess is {p1}')
   print(f'Player 2 guess is {p2}')
   random.shuffle(cubes)
   print(cubes[0])
   res = orig_cube.index(cubes[0])+1
   time.sleep(t)
   if t >= 0.3:
      print()
      print("Your dice is nr: ",res)
      running = False
if abs(p1-res) < abs(p2 - res):
   print("THE WINNER IS PLAYER 1 !!!")
elif abs(p1-res) > abs(p2 - res):
   print("THE WINNER IS PLAYER 2 !!!")
else:
   print("IT IS A DRAW !!!")
