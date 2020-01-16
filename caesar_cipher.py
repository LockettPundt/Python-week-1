
message = "lbh zhfg hayrnea jung lbh unir yrnearq"
new_message = ""
plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "bcdefghijklmnopqrstuvwxyza"
plain_split = []
cipher_split = []
for x in plain:
    plain_split.append(x)
for x in cipher:
    cipher_split.append(x)
i = 0

while len(message) > i:
    if message[i] == " ":
        new_message += " "
    else:
        index = cipher_split.index(message[i])
        new_message += plain_split[index - 12]
    i += 1

print(new_message)