# Test generator and validator
import random

difficulty : int = 0
def generate_grid():
    new_grid = [['.' for i in range(6)] for j in range(6)]


    if (difficulty >= 1): # need to add obstacles
        for i in range(4):
            new_obstacle = [random.randint(0,5),random.randint(0,5)]
            new_grid[newo]


