str = input("Provide your string\n")

def reverseString(str):
	reversed = ''
	for character in str:
		reversed = character + reversed
		
	print(reversed);
	
reverseString(str)