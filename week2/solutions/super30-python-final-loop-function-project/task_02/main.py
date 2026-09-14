def deposit(balance, history, amount):
    """Deposit a positive amount and record it."""
    if amount <= 0:
        return balance, "Amount must be positive"
    balance += amount
    history.append(("Deposit", amount, balance))
    return balance, "Deposit successful"


def withdraw(balance, history, amount):
    """Withdraw an affordable positive amount and record it."""
    if amount <= 0:
        return balance, "Amount must be positive"
    if amount > balance:
        return balance, "Insufficient balance"
    balance -= amount
    history.append(("Withdrawal", amount, balance))
    return balance, "Withdrawal successful"


def main():
    """Run the banking menu."""
    balance = 1000.0
    history = []
    while True:
        print("1. Balance  2. Deposit  3. Withdraw  4. History  5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            print(balance)
        elif choice == "2":
            balance, message = deposit(balance, history, float(input("Amount: ")))
            print(message)
        elif choice == "3":
            balance, message = withdraw(balance, history, float(input("Amount: ")))
            print(message)
        elif choice == "4":
            print(history)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
