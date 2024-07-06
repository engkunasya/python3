# A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).

# For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.

# Example: The quick brown fox jumps over the lazy dog.

# Your task is to figure out if a sentence is a pangram.

def pangram(sentence_set):
    pangram_set = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if pangram_set.issubset(sentence_set):
        return f"It is Pangram"
    else:
        return f"It is NOT Pangram"


sentence_input = input("Please enter the phrase: ").upper()
sentence_set = set(sentence_input)
# sentence_list = [c for c in sentence]
# print(sentence_list)

print (pangram(sentence_set))
