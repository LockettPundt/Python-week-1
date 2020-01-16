#prompt user for number 1-10.
#the function below checks to see if it matches a randomly generated number.

user_number = int(input("Guess a number between 1 and 10. \n"))
import random
MY_NUMBER = random.randint(1, 10)
count = 0
if (user_number > 10 or user_number < 1):
    user_number = int(input("Enter another number between 1 and 10. \n"))
def magic_number():
    if user_number == MY_NUMBER:
        print("Good job! You guessed it!!\n")
        count += 1
    else:
        print("Sorry that's incorrect\n")
    
#while loop to run the function until they guess correctly.

magic_number()
while count == 0:
    user_number = int(input("Guess again... \n"))
    if (user_number > 10 or user_number < 1):
        user_number = int(input("Enter another number between 1 and 10... \n"))
    magic_number()