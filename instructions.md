# TCHS AERO SOFTWARE TRYOUT

## YOUR TASK
Your task is to design the movement for a ground-based robot.

## THE GRID
The robot lives on a 6x6 grid. It can only inhabit one tile at any time, and it begins in the top-left corner (0,0).
Your task is to use the provided interface to move the robot to the bottom right corner (5,5) and collect as many of the six apples as possible.

## INPUT
Your program will receive input in the form of function calls.
When you run your program, it will import the required tester modules, and send a single call to `initialize_robot()`, passing a single argument: the state of the board, represented as a two-dimensional List.

## API
You will have access to three api functions:
move_forwards() : alias - go() : moves the robot one tile in the direction it is facing. 
turn_right() : alias - rr() : rotates the robot to the right 90 degrees.
turn_left() : alias - rl() : rotates the robot to the left 90 degrees.

## BONUS POINTS
The task comes in three difficulties that you may select from.
BASIC: No changes, collect as many apples as possible.
HARD: There are now 7 "walls" on the grid that the robot must navigate around. Attempting to move into a wall will cause nothing to happen. Collect all of the apples.
TOUGH: The robot now only "sees" tiles orthogonally or diagonally adjacent to itself (<= 9 tiles at any time). Evading this restriction invalidates the difficulty. There are now 14 walls.
Brute force algorithms are discouraged. If you can solve the problem easily, push yourself to optimize your solution to use less steps. 

## FAQ
Boards are randomly generated. This includes walls and apples.
There will always be 6 apples.
The robot is guaranteed to have at least one path that collects every apple and reaches the exit.
Extra points if you can beat all three difficulties with the same program, but two or three is acceptable as well.
Collaboration is not allowed.
If you have additional questions, feel free to ask.

## ENVIRONMENT
The only provided environment is a Python3 environment. If you would like to use a different language, you may, but you will not receive instant feedback from the tester. 
If you choose to use a language other than python, syntax errors will not be held against you.
If you do not know any programming languages, or do not wish to use one, you may instead use pseudocode. If you choose this option, your solution(s) must be written on physical paper.

To be considered for the TCHS Aero team, you need to be able to collect at least one apple consistently. 
We also recommend that you learn enough Python to be able to complete this task in order to be successful on the team.

Good luck.