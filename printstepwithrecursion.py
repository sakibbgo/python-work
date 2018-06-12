n = int(input("Enter number of step(s)\n"))

list1 = [["" for y in range(n)] for x in range(n)]


print(list1)



def steps(n, y = 0, stair = ""):
    if (y == n):
        return;

    if (n == len(stair)):
        print(stair)
        return steps(n, y+1)

    if (len(stair) <= y):
        stair += "#"
    else:
        stair += "1"
    steps(n, y, stair)

steps(n)


