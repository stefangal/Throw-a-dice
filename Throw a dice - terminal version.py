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
while running:
    t += 0.01
    os.system('cls' if os.name == 'nt' else 'clear')
    random.shuffle(cubes)
    print(cubes[0])
    time.sleep(t)
    if t >= 0.3:
        print()
        print("Ready")
        running = False
