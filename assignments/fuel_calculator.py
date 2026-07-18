#With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:
#1. Ask the user how many kilometers they want to drive.
#2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).
#3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
#(Formula: liters_needed = kilometers / 10).
#4. Calculate the total cost (liters_needed * petrol_price).
#5. Use type casting to ensure your numbers work, and use round() to format the
#final cost to 2 decimal places.

kilometers = float(input("Enter the number of km you want to travel: "))
petrol_price = float(input("Enter the current petrol price per liter: R"))

#Assuming the car takes 1 liter per 10km
liters_needed = kilometers / 10
total_cost = liters_needed * petrol_price

print (f"You will need to purchase: {round(liters_needed, 2)} liters of fuel")
print (f"At R{round(petrol_price, 2)} per liter, {round(liters_needed, 2)} liters will cost you: R{round(total_cost, 2)}")