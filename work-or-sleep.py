#Ask the user for a day and will alert them if they can sleep, or if they have to work...
user_day = int(input("Enter a day (0 - 6). \n"))
if (user_day == 0 or user_day == 6):
    print("It's the weekend! Go back to sleep!\n")
else:
    print("GET TO WORK!\n")