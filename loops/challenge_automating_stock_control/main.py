# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item, details in inventory.items():
    print(f"Processing {item}")
    
    # Extract values for easier reading
    current_stock = details[0]
    min_stock = details[1]
    restock_amount = details[2]
    on_sale = details[3]

    # Rule 2: The While Loop (Restocking)
    while current_stock < min_stock:
        current_stock = current_stock + restock_amount
    
    # Update the dictionary with the new stock
    inventory[item][0] = current_stock

    # Rule 3: The Discount Logic (if-and-not)
    if current_stock > discount_threshold and not on_sale:
        inventory[item][3] = True

print("Processing completed")
