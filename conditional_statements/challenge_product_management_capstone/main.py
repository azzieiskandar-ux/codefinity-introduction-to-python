# Input variables
days_until_expiration = 5  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

# Placeholders for required print statements
# Uncomment and place these in your logic as needed:
# print("Big discount applied")
# print("Small discount applied")
# print("No discount for non-perishable items.")
if product_type == "Perishable":
    if days_until_expiration <= 3:
        print("Big discount applied.")
    else:
        print("Small discount applied.")
else:
        print("No discount for non-perishable items.")