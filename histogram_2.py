#prints out a histogram from a user supplied sentence.

user_word = input("Enter a sentence and it will return a histogram. \n")
user_word_array = user_word.split()
alphabet = {}
for x in user_word_array:
    if x in alphabet:
        alphabet[x] += 1
    else:
        alphabet[x] = 1

print(alphabet)
for item in alphabet:
    print(item + " : " + "*" * alphabet[item])
