import math

steps = int(input("Enter number of step(s)\n"))

list1 = [["" for y in range(1+steps+(steps-2))] for x in range(steps)]


count = 0
print(count)
position = int((steps + (steps - 2))/2)
start = int((steps + (steps - 2))/2)
print(position)

for x in range(steps):
    for y in range(1+(x+1)+((x+1)-2)+1):
            list1[x][position-(count-y)] = "#"
            count = x+1
            print(count)

for x in range(steps):
    for y in range(1+steps+(steps-2)):
        if(list1[x][y] != "#"):
            list1[x][y] = " "
            
    
print(list1)
for list in list1:
    print("".join(list))

