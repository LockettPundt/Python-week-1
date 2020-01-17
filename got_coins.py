#asks user if they want a coin. if so it is nice and gives them one.
#this repeats until user has their share of coins.
coins = 0
desire_for_more = True
while desire_for_more == True:
    request = input("Would you like a coin? answer 'yes' or 'no'\n")
    if request == "yes":
        coins += 1
        print("You now have {} coins.".format(coins))
    elif request == "no":
        print("You have {} coins.".format(coins))
        break
    else:
        print("Did you say 'yes' or 'no'?\n")
        