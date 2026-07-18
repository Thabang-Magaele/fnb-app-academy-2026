#Collect first name, last name, and bio message using input()
#Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)
#Display the full name in Title Case using .title()
#Strip leading/trailing whitespace from the bio before displaying it using .strip()
#Count and display the number of characters in the bio using len()
#Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
#Display all output using f-strings

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
bio_msg = input("Write a short bio message: ").strip()

print (f"\nWelcome: {first_name[0].lower()}{last_name.lower()}")
print (f"Full Name: {first_name.title()} {last_name.title()}")
print (f"Bio Message: {bio_msg.replace("I am", "I'm")}")
print (f"Bio message count: {len(bio_msg)}")