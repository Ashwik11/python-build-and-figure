def add_to_cart(cart, name, price, quantity):
    """Add a product or increase its quantity."""
    if price <= 0 or quantity <= 0:
        return False
    item = cart.setdefault(name, {"price": price, "quantity": 0})
    item["quantity"] += quantity
    return True


def remove_from_cart(cart, name, quantity):
    """Reduce a product quantity and remove it at zero."""
    if name not in cart or quantity <= 0:
        return False
    cart[name]["quantity"] -= quantity
    if cart[name]["quantity"] <= 0:
        del cart[name]
    return True


def cart_total(cart):
    """Return the current cart total."""
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return total


cart = {}
add_to_cart(cart, "Book", 20, 3)
print(cart, cart_total(cart))
remove_from_cart(cart, "Book", 1)
print(cart, cart_total(cart))
