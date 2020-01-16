#Asks the user for a bull amount as well as the quality of the service. The function returns the total amount including tip.
#The second vesion adds the ability to divide it among x people in your party.
def tip_calc ():
    bill = float(input("Enter the amount of the bill. \n"))
    service = input("How was the service? Good, Fair or Bad? \n")
    people = int(input("How many people are in your party? \n"))
    while (people == 0):
        print("Sounds like an existential issue...\n")
        people = int(input("How many people are in your party? \n"))
    if (service.lower() == "good"):
        amount = float(((bill * .20) + bill) / people)
    elif (service.lower() == "fair"):
        amount = float(((bill * .15) + bill) / people)
    else:
        amount = float(((bill * .10) + bill) / people)
    return print("$%.2f would be your total divided amongst %s people.\n" % (amount, people))
tip_calc()
