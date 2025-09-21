import tester
from tester import test, move_forwards, turn_right, turn_left, go, tl, tr, grade, position_x, position_y, direction, get_grid

SELECT_DIFFICULTY = 0
test(SELECT_DIFFICULTY)

'''
WRITE YOUR SOLUTION HERE.

Note the available API calls:
move_forwards() / go() : moves forwards in the direction specified by direction.
turn_right() / tr() : turns right, or clockwise. This increments direction.
turn_left() / tl() : turns left, or counter-clockwise. This decrements direction.
get_grid() -> list : Returns the state of the grid and everything on it. '.' = empty, 'o' = fruit, '#' = wall. The robot will not be included.
position_x : int : The current x coordinate.
position_y : int : The current y coordinate.
direction : int : The current direction the robot is facing. 0 = North, 1 = East, 2 = South, 3 = West
'''


def sample():
    go()
    tr()
    go()
    go()

# Delete the following line to remove the sample execution from the program
sample()

# Your algorithm must end with a call to grade().
# Calling grade() will halt execution and print your score.
# You may call grade() at any point, but note that no operations will succeed after grade() is called.
# When grade() is called, the robot's position will be queried. If it is equal to (5,5), the "reach the end" task is successful.
# If it is called after moving away from the end, you will not receive the points for that task.
grade()