"""

.........          boatslover
.........
.........          14/01/2022

===============================================================================
This program allows users to trace images and output contents to a .csv file
===============================================================================
"""
# Imports
from pynput import keyboard
from pynput.mouse import Controller

print('listener starting')

# assign variables
mouse = Controller()
position_data = []

def on_press(key):
    try:
        # print(key.char)
        if key.char == 'a':
            position_data.append(mouse.position)
    except AttributeError:
        [print('special key {0} pressed'.format(
            key))]


def on_release(key):
    print(key)
    curr_mouse = mouse.position
    position_data.append([curr_mouse[0], curr_mouse[1], 0])
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print(position_data)
print("Enter Filename: ")
filename = input() + ".csv"
print("Filename entered: " + filename)

with open(filename, 'w') as f:
    f.writelines(str(len(position_data)))
    for data in position_data:
        line = '\n'
        for num in data:
            line += str(num) + ','
        f.writelines(line[:-1])
