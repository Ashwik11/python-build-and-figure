def add_expense(expenses, name, amount):
    """Add a named expense when its values are valid."""
    if not name.strip() or amount <= 0:
        return False
    expenses.append({"name": name.strip(), "amount": amount})
    return True


def expense_total(expenses):
    """Return total spending."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def highest_expense(expenses):
    """Return the highest expense or None for an empty list."""
    if not expenses:
        return None
    highest = expenses[0]
    for expense in expenses[1:]:
        if expense["amount"] > highest["amount"]:
            highest = expense
    return highest


expenses = []
add_expense(expenses, "Coffee", 4.5)
add_expense(expenses, "Coffee", 5)
print(expense_total(expenses), highest_expense(expenses))
