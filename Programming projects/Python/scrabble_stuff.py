from english_words import words

scrabble_words = []

for word in words:
    if len(word) == 1 and word[0] == "a" and word[-1] == "a":
        scrabble_words.append(word)

print(" ".join(scrabble_words))
