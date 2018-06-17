import math

steps = int(input("Enter number of step(s)\n"))

list1 = [["" for y in range(2*steps+1)] for x in range(steps)]

midpoint = math.floor((2*steps)/2)
print(midpoint)

for x in range(steps):
    for y in range(2*steps+1):
            if( (midpoint - x) <= y and (midpoint + x) >= y ):
                list1[x][y] = "#"
            else:
                list1[x][y] = " "
            
    
print(list1)
for list in list1:
    print("".join(list))

