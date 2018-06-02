str = input("Provide your string\n")

def isPalindrome(str):
	reversed = ''
	for character in str:
		reversed = character + reversed
		
	if (reversed == str):
		return True
	else:
		return False
	
if (isPalindrome(str) == True):
	print("The string "+str+" is a Palindrome.")
else:
	print("Not a Palidrome")