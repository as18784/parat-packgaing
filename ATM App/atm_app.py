print("Hi there! Welcome to the ABC Bank ATM.")

enter_pin = input("Please enter your 4-digit PIN")

print("Login successful!")

print("What do you want to do today?")
print("1. check balance")
print("2. withdraw money")

user_choice = input("Enter 1 or 2: ")

if user_choice == "1":
    print("Your balance is ₹1,00,000,000,000")
    print("You're rich!")

elif user_choice == "2":
    withdraw_amount = input("How much would you like to withdraw? ₹")
    print("Withdrawing ₹" + withdraw_amount)

print("Thank you for using ABC Bank ATM. Have a great day!")