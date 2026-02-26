# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

# Use a for loop to go through each item in the inventory dictionary
for item_name in inventory:
    # Get current values from the list
    # Index 0: stock, Index 1: minimum, Index 2: restock qty, Index 3: sale status
    details = inventory[item_name]
    
    # Use a while loop to restock until at or above minimum
    while details[0] < details[1]:
        details[0] += details[2]
    
    # Update stock value in the dictionary
    inventory[item_name][0] = details[0]
    
    # Check if stock exceeds threshold and item is not already on sale
    if details[0] > discount_threshold and details[3] == False:
        inventory[item_name][3] = True
        
    # Print processing line for each item
    print(f"Processing {item_name}")

print("Processing completed")
