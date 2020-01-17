#prints out a histogram from a user supplied letter.


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

print("\n")
print("\n")

def top_3():
    temp = alphabet
    i = 1
    while i < 4:
        print("%s most used: %s" % (i, max(alphabet, key=alphabet.get)))
        del temp[max(alphabet, key=alphabet.get)]
        i += 1

top_3()
