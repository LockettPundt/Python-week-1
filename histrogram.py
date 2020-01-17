#prints out a histogram from a user supplied word.

user_word = input("Enter a word and it will return a histogram. \n")

alphabet = {}
for x in user_word:
    if x in alphabet:
        alphabet[x] += 1
    else:
        alphabet[x] = 1

print(alphabet)
for item in alphabet:
    print(item + " : " + "*" * alphabet[item])

print(max(alphabet, key=alphabet.get) + " is your most used letter.")