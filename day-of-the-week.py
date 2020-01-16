#Takes an integer from 0-6 and converts it to a day of the week.
user_day = int(input("Enter a day (0 - 6) \n"))
if (user_day > 6 or user_day < 0):
    user_day = int(input("Try again. Enter a day (0 - 6) \n"))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(str(user_day) + " is a " + days[user_day])