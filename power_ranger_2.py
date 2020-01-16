power_rangers = ["Zach", "Billy", "Kim", "Tommy", "Jason", "Trini"]
who_to_remove = input(f"Who would you like to remove?\n{power_rangers}\n")


if who_to_remove in power_rangers:
    power_rangers.remove(who_to_remove)
    print(power_rangers)
else:
    print("%s isn't in this list." % (who_to_remove))
