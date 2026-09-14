def add_product(inventory, name, price, quantity):
    """Add a new product after validating its values."""
    key = name.strip().lower()
    if not key or price < 0 or quantity < 0 or quantity != int(quantity) or key in inventory:
        return False
    inventory[key] = {"name": name.strip(), "price": price, "quantity": int(quantity)}
    return True


def update_quantity(inventory, name, quantity):
    """Update a product quantity."""
    product = inventory.get(name.strip().lower())
    if product is None or quantity < 0 or quantity != int(quantity):
        return False
    product["quantity"] = int(quantity)
    return True


def inventory_value(inventory):
    """Return the total value of all products."""
    total = 0
    for product in inventory.values():
        total += product["price"] * product["quantity"]
    return total


inventory = {}
add_product(inventory, "Mouse", 700, 3)
add_product(inventory, "Keyboard", 1500, 2)
print(inventory)
print(inventory_value(inventory))
