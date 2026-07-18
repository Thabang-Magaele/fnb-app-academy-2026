#Student information formatter

#collect user inputs
name = input("Name: ")
surname = input("Surname: ")
age = (int(input("Age: ")))
fav_num = (float(input("Enter your favourite number: ")))

#Display a formatted greeting
print (f"\nWelcome {name} {surname}!!!\n")

#Display the full name in uppercase and title case
full_name = f"{name} {surname}"
print ("Name in UPPERCASE: ", full_name.upper())
print ("Name in Title Case: ", full_name.title())

#Display the age in months
age_in_months = age * 12
print ("Your age in the number of months is: ", age_in_months)

#Round off favourite number to 2 decimal places
print("Favourite number (rounded off): ", round(fav_num,2))

#Display the data types
print ("\nName: " ,type(name))
print ("Surname: " ,type(surname))
print ("Age: " ,type(age))
print ("fav_num: " ,type(fav_num))