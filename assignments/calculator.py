#Use float(input()) to collect two numbers from the user
#Calculate and display: addition, subtraction, multiplication, division
#Calculate and display: floor division (//) and modulus (%)
#Round all results to 2 decimal places using round()
#Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
#Display all results in a formatted table using f-strings

#Accepting user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Calculating addition, subtraction, multiplication, division
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

#Displaying addition, subtraction, multiplication, division
print (f"Addition for first and second number: {round(addition, 2)}")
print (f"Subtraction for first and second number: {round(subtraction, 2)}")
print (f"Multiplication for first and second number: {round(multiplication, 2)}")

if num2 == 0:
    print ("Error, you can't divide by zero")

else:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
    print (f"Division for first and second number: {round(division, 2)}")
    print (f"Floor division for first and second number: {round(floor_division, 2)}")
    print (f"Modulus for first and second number: {round(modulus, 2)}")

