steps = int(input("Enter number of step(s)\n"))

list1 = [["" for y in range(steps)] for x in range(steps)]


print(list1)
x=0
y=0

for x in range(steps):
    for y in range(steps):
        if(x == y or y < x):
            list1[x][y] = "2"
        else:
            list1[x][y] = " "
            

for list in list1:
    print(list)
    print("\n")
