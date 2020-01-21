
# #​The Restaurant is about to open for Brunch and the menu isn't complete yet, help fix the menu!

# Fix the price of the steak salad. It should be 15.99
# Add a specials menu that includes: Soup of the Day (8.99), Catch of the Day (14.99), Chef Special (15.99)
# Change "Three Egg Breakfast" to have the options of: Without Bacon (8.99) and With Bacon (9.99)​
# I hear you, that was easy right? Let's step it up a notch (good luck!)​

# The Menu is set, get ready the first guest has arrived!
# For each table you will need to print a reciept for the requested items

# Assume all tables will have one payer

# On the 'receipt' you will need to:

# print out each menu item order and the price of the item
# calculate the total for their bill
# calculate the sales tax (7%)
# print out suggested tips (25%, 20%, 15%)
# calculate total bill with sales tax included
# TABLE 1:

# Guest 1: Egg Benedict, Coffee
# Guest 2: Biscuit and Gravy, Coffee
# Guest 3: Steak and Eggs, Soft Drink​
# TABLE 2:

# Guest 1: Steak Salad, Soft Drink
# Guest 2: Soup of the Day, Chicken Wrap, Water
# Guest 3: Chicken Fingers, Soft Drink
# For the Table: Chef Special
# Example:


# Egg Benedict                   $  11.99
# Biscuit and Gravy              $   7.99
# Steak and Eggs                 $  16.99
# Coffee                         $   1.99
# Coffee                         $   1.99
# Soft Drink                     $   1.99

#                        Price: $  42.94
#                        Taxes: $   3.01
#                        Total: $  45.95
# **Suggested Tip**
# Tip 25%:       11.49
# Tip 20%:        9.19
# Tip 15%:        6.89
menu = {
    "Specials": {
        "Soup of the Day": 8.99,
        "Catch of the Day": 14.99,
        "Chef Special" : 15.99
    },
   "Brunch" : {
        "Steak and Eggs": 16.99,
        "Three Egg Breakfast": {
            "Without Bacon": 8.99,
            "With Bacon": 9.99
        },
        "Egg Benedict": 11.99,
        "Biscuit and Gravy": 7.99,
        "Chicken Fingers": 10.99,
        "Chicken Wrap": 8.99,
        "Steak Salad" : 15.99
    },
    "Drinks": {
      "Soft Drink": 1.99,
      "Coffee": 1.99,
      "Orange Juice": 0.99,
      "Milk": 0.55,
      "Water": 0.00
    }
}
tables = {
    "Table 1": {
        "Guest 1": {
            "Eggs Benedict": menu["Brunch"]["Egg Benedict"],
            "Coffee": menu["Drinks"]["Coffee"]
        },
        "Guest 2": {
            "Biscuit and Gravy": menu["Brunch"]["Biscuit and Gravy"],
            "Coffee": menu["Drinks"]["Coffee"]
        },
        "Guest 3": {
            "Steak and Eggs": menu["Brunch"]["Steak and Eggs"],
            "Soft Drink": menu["Drinks"]["Soft Drink"]
        }
    },
    "Table 2": {
        "Guest 1": {
            "Steak Salad": menu["Brunch"]["Steak Salad"],
            "Soft Drink": menu["Drinks"]["Soft Drink"]
        },
        "Guest 2": {
            "Soup of the Day": menu["Specials"]["Soup of the Day"],
            "Chicken Wrap": menu["Brunch"]["Chicken Wrap"],
            "Water": menu["Drinks"]["Water"]
        },
        "Guest 3": {
            "Chicken Fingers": menu["Brunch"]["Chicken Fingers"],
            "Soft Drink": menu["Drinks"]["Soft Drink"]
        }
    }
}
tables["Table 2"]["For the Table."] = {
    "Chef Special" : menu["Specials"]["Chef Special"]
}

def print_reciept(table):
    total_sans_tax = 0
    tax = 0

    print("\n" + "*" * 30 + "\n\n")
    for guest in table:
        print("\n** {} **\n".format(guest))
        for item in table[guest]:
            print("{}{}".format(item, (30 - len(item)) * " ") + "$" + str(format(table[guest][item], '.2f')))
            total_sans_tax += table[guest][item]
    total_with_tax = ((total_sans_tax * .08) + total_sans_tax )
    print("\n")
    print("{}Your total is: ${:.2f}".format(15 * " ", total_sans_tax))
    print("{}Sales tax: ${:.2f}".format(19 * " ", total_sans_tax * .08))
    print("{}Your total is: ${:.2f}".format(15 * " ", (total_sans_tax * .08) + total_sans_tax ))
    print("\n**Tip**")
    print("25%: ${:.2f}".format(total_with_tax * .25))
    print("20%: ${:.2f}".format(total_with_tax * .20))
    print("15%: ${:.2f}".format(total_with_tax * .15))

    


    print("\n ")




print_reciept(tables["Table 1"])
print_reciept(tables["Table 2"])
