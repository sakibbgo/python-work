text = input('Enter your text: ')
d = dict()
dup = dict()
def getAllMaxChar():
    maxcount = 0
    maxChar = ""
    for char in text:
        if char in d:
            d[char] += 1  
        else:
            d[char] = 1  

    for char in d:
        if d[char] > maxcount and char != " ":
            maxcount = d[char]
            maxChar = char

    for char in d:
        if d[char] == d[maxChar]:
            dup[char] = char
    print("The most used character(s): ")
    for char in dup:
        print(char)
    print("They appeared "+str(d[maxChar])+" time(s)")

getAllMaxChar()
            
            
    
    
