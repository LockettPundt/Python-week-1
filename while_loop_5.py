

title = "H e r e i s a s t r i n g ."

count = 0

#prints every other character and omits whitespaces.
while len(title) > count:
    if (count % 2) == 0 and title[count] != " ":
        print(" " * count + title[count])
    count += 1


