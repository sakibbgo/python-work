mylist = [int(x) for x in input("Enter list element separated by space: ").split()]
size = int(input("Enter chunk size: "))

def chunklist(items, size):
    chunked = []
    new_list = []
    for item in items:
        if not chunked or len(new_list) == size:
            new_list = [item]
            chunked.append(new_list)
        else:
            new_list.append(item)
    print(chunked)

chunklist(mylist, size)
    
