import time

# User data: card number -> PIN and balance
cards_pin = {123456789: 1234}
cards_balance = {123456789: 5000}

def check_pin(card_no):
    """Check PIN with 3 attempts"""
    attempts = 3
    while attempts > 0:
        pin = int(input(f"Enter PIN for card {card_no}: "))
        if cards_pin.get(card_no) == pin:
            print("PIN correct! Welcome to ATM.")
            time.sleep(1)
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! {attempts} attempts left.")
            time.sleep(1)
    print("Card locked! Too many wrong attempts.")
    return False

def show_balance(card_no):
    """Display current balance"""
    balance = cards_balance[card_no]
    print(f"Your balance: Rs. {balance:,}")

def deposit(card_no):
    """Add money to account"""
    try:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            cards_balance[card_no] += amount
            print(f"Deposited Rs. {amount:,}. New balance: Rs. {cards_balance[card_no]:,}")
        else:
            print("Amount must be positive!")
    except ValueError:
        print("Enter valid number!")

def withdraw(card_no):
    """Withdraw money if enough balance"""
    try:
        amount = int(input("Enter withdraw amount: "))
        balance = cards_balance[card_no]
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Amount must be positive!")
        else:
            cards_balance[card_no] -= amount
            print(f"Withdrew Rs. {amount:,}. New balance: Rs. {cards_balance[card_no]:,}")
    except ValueError:
        print("Enter valid number!")

# Main ATM function
def atm_main():
    print("=== Welcome to Simple ATM
