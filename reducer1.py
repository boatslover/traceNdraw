"""
Removes duplicate lines from .csv files
#TODO: combine into tracer.py
"""

print("Enter Filename: ")
newlst = []
last = 0
filename = input() + '.csv'
print("Filename entered: " + filename)

with open(filename) as f:
    num_of_lines = int(f.readline())
    for i in range(num_of_lines - 1):
        line = f.readline().strip()
        if line != last:
            newlst.append(line)
        last = line


print("Enter Filename: ")
filename2 = input() + ".csv"
print("Filename entered: " + filename2)

with open(filename2, 'w') as f:
    f.writelines(str(len(newlst)))
    for data in newlst:
        f.writelines('\n' + data)
