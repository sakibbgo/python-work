steps = int(input("Enter number of step(s)\n"))

for step in range(steps):
    print("#"*(step+1)+(steps-(step+1))*" ")

