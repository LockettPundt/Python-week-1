#Asks the user for a bull amount as well as the quality of the service. The function returns the total amount including tip.

def tip_calc ():
    bill = float(input("Enter the amount of the bill. \n"))
    service = input("How was the service? Good, Fair or Bad? \n")
    if (service.lower() == "good"):
        amount = float((bill * .20) + bill)
    elif (service.lower() == "fair"):
        amount = float((bill * .15) + bill)
    else:
        amount = float((bill * .10) + bill)
    return print("$%.2f would be your total.\n" % (amount))
tip_calc()
