
power_rangers = ["Zach", "Billy", "Kim", "Tommy", "Jason", "Trini"]
#this print statement is here to showl the difference after the .remove()
print(power_rangers)

if "Tommy" in power_rangers:
    power_rangers.remove("Tommy")
    print(power_rangers)
else:
    print("Tommy isn't in this list.")

