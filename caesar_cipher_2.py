
message = "lbh zhfg hayrnea jung lbh unir yrnearq"
new_message = ""
plain = "abcdefghijklmnopqrstuvwxyz"
plain_split = []
rot_num = 13
for x in plain:
    plain_split.append(x)
i = 0

while len(message) > i:
    if message[i] == " ":
        new_message += " "
    else:
        index = plain_split.index(message[i])
        new_message += plain_split[index - rot_num]
    i += 1

print(new_message)