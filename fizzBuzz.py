number = input("Enter the number: ")

def fizzBuzz(number):
    for each in range(1, int(number)+1):
        if ((each % 3) == 0) & ((each % 5) == 0):
            print("FizzBuzz")
        elif (each % 3 == 0):
            print("Fizz")
        elif (each % 5 == 0):
            print("Buzz")
        else:
            print(each)

fizzBuzz(number)
