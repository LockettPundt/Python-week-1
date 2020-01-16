#Prompt the user for a celcius reading and the function will convert it to Fahrenheit.
temp = float(input("Enter a temperature in Celcius. \n"))

def converter(c):
    return float((c * 1.8) + 32)

print(converter(temp))