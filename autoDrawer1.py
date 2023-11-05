"""

.........          boatslover
.........
.........          14/01/2022

===============================================================================
This project is to create a program that can automatically draw images
from .csv files
===============================================================================
"""
from pynput.mouse import Button, Controller
import time

# Wait before doing anything
# time.sleep(1)

# Assigns variables
mouse = Controller()
x = 0
y = 0

print('Enter A filename to draw: ')
filename = input() + '.csv'

# (countdown timer)
input('press enter to continue')
for x in range(5):
    print('Starting drawing in ' + str(5 - x))
    time.sleep(1)

# Scale #TODO
scale = 0

mouse.press(Button.left)

with open(filename) as f:
    num_of_lines = int(f.readline())
    for i in range(num_of_lines - 1):
        # wait commend
        # (so mouse inputs don't go to fast that it doesnt draw correctly)
        #time.sleep(0.005)

        # reads line (['x', 'y'])
        line = f.readline().strip().split(',')

        # calculate mouse movement
        x_move = (int(line[0])) - (x)
        y_move = (int(line[1])) - (y)

        # print('total moves: \t ' + str(i) + '\t\t x: \t' + str(x_move) + '\t y: \t' + str(y_move))

        if i > 0:
            mouse.move(x_move + (scale*x_move), y_move + (scale*y_move))
            # mouse.move(x_move - (x_move//2), y_move - (y_move//2))

        # saving current position for use in next line
        x = int(line[0])
        y = int(line[1])

        # reset drawing input
        mouse.press(Button.left)

        # code to stop drawing temporarily
        if len(line) > 2:
            # time.sleep(0.000005)
            mouse.release(Button.left)
            # time.sleep(0.000005)
            mouse.release(Button.left)

mouse.release(Button.left)
