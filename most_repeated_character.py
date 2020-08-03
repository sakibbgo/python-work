sentence = "Which letter is repeated most in this sentence?"

character_dictionary = {}

for letter in sentence:
    if letter in character_dictionary:
        character_dictionary[letter] += 1
    else:
        character_dictionary[letter] = 1

character_dictionary_sorted = sorted(character_dictionary.items(), 
key=lambda kv: kv[1], 
reverse=True)
print(character_dictionary_sorted[0])
