def apply_discount(price, discount=0.05):
    """Returns the price after applying the discount."""
    return price * (1 - discount)

def apply_tax(price, tax=0.07):
    """Returns the price after adding the tax."""
    return price * (1 + tax)

def calculate_total(price, discount=0.05, tax=0.07):
    """Uses apply_discount() and apply_tax() to return the total price."""
    # First apply discount, then apply tax to the discounted price
    discounted_price = apply_discount(price, discount)
    total_price = apply_tax(discounted_price, tax)
    return total_price

# Call using default values
total_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_default:.2f}")

# Call using custom values via keyword arguments
total_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_custom:.2f}")
