import re

word = input("Enter a word. \n")
if re.search("aa", word):
    print (word.replace("aa", "aaaaa"))
elif re.search("ee", word):
    print(word.replace("ee", "eeeeee"))
elif re.search("ii", word):
    print(word.replace("ii", "iiiii"))
elif re.search("oo", word):
    print(word.replace("oo", "ooooo"))
elif re.search("uu", word):
    print(word.replace("uu", "uuuuu"))
else:
    print(word)

    