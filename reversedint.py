number = int(input("Provide your string\n"))

if (isinstance(number,int)):
	def reverseInt(number):
		reversed = ''
		if (number < 0):
			convertednumber = str(number)
			for character in convertednumber[1:]:
				reversed = character+reversed
			print(int(convertednumber[:1]+reversed)) 
		else:
			convertednumber = str(number)
			for character in convertednumber:
				reversed = character+reversed
			print(int(reversed)) 
	reverseInt(number)
else:
	print("Your input was not a number")
