firststring = input("Enter your first string: ")
secondstring = input("Enter your second string: ")

finalstring1 =(''.join(char for char in firststring if char.isalnum())).lower()
finalstring2 =(''.join(char for char in secondstring if char.isalnum())).lower()

print(finalstring1)
print(finalstring2)

def isAnagram():
   stringmap1 = dict(countMap(finalstring1))
   stringmap2 = dict(countMap(finalstring2))
   print(stringmap1)
   print(stringmap2)

   if len(stringmap1) != len(stringmap2):
       return False
   else:
       for char in stringmap1:
           if stringmap1[char] == stringmap2[char]:
               continue
           else:
                return False
                break
       return True
       





def countMap(strings):
    myCharCountMap = dict()
    for char in strings:
        if char in myCharCountMap:
            myCharCountMap[char] += 1
        else:
            myCharCountMap[char] = 1
            
    return dict(myCharCountMap)

print(isAnagram())
        
