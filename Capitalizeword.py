text = input("Enter yout sentense: ")
wordlist = text.split(" ")
capitalized = ' '.join([letter[0].upper()+letter[1:] for letter in wordlist])
print(capitalized)
