# Get a word from the users
word = input("Enter your word: ")

# Find the length of the word
word_length = len(word)
print(f"The word '{word}' has {word_length} characters.")

# Reverse the word
reversed_word = word[::-1]
print(f"The reversed word is: {reversed_word}")

# Create a new word with the same length as the original word by repeating the first character
first_char = word[0]
new_word = first_char * word_length
print(f"The new word created by repeating the first character of the word '{word}' is: {new_word}")

# Concatenate the original word a suffix
suffix = 'eous'
suffixed_word = word + suffix
print(f"The word '{word}' with the suffix '{suffix}' is: {suffixed_word}")

# Convert the word to all carcters in uppercase
upper_word = word.upper()
print(f"The word '{word}' with all characters in uppercase looks like '{upper_word}'.")

# Replace a part of the word with another string
replaced_word1 = word.replace('atus', 'iece')
replaced_word2 = word.replace('atus', 'ephew')
print(f"The replaced words are '{replaced_word1}' and '{replaced_word2}'")