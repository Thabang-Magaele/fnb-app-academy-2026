#Simulate a bank transaction checking if a user has enough money.
#1. Set a fixed variable representing a bank balance, for example: balance = 500.
#2. Ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!).
#3. If the request is less than or equal to the balance, deduct the amount and print:
#“Withdrawal successful! Remaining balance: RX”.
#4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or equal to 0. If so, print: “Invalid amount”. You must withdraw more than “R0”.
#5. Otherwise (else), print: “Declined. Insufficient funds”

acc_balance = float(500)

print (f"Welcome to FNB App ATM!\nYour account balance is: R{round(acc_balance)}")

request = float(input("How much would you like to withdraw: R"))

if (request <= acc_balance) and (request != 0.00) and (request > 0):
    balance_rem = acc_balance - request
    print (f"Withdrawal successful! Remaining balance is: R{round(balance_rem, 2)}")
elif request <= 0.00:
    print ("Invalid amount, you must withdraw more than R0")
else:
    print ("Withdraw request declined: Insufficient Funds")
    print (f"Your available spend is: R{acc_balance}")