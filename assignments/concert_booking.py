#Create a program that acts as a digital ticket counter.
#1. Ask the user for their name.
#2. Ask them for the name of the band/artist they want to see.
#3. Print a personalized confirmation message using 
# an f-string that says something like: “Hey [Name]! 
# Your tickets to see [Artist] are booked successfully!”

print ("Welcome to Pro Tickets!\n")

#collecting user info
full_name = input("Enter your full name: ")
band_name = input("Enter the name of the band or artist you wish to see: ")

print ("\nAll set, here is your ticket for confirmation:\n")
print (f"Full name: {full_name}\nBand/Artist name: {band_name} \nThank you!")
