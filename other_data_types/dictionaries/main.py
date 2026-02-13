# Task 1: Define a dictionary for grocery inventory with proper syntax
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# Task 2: Retrieve and print the details of "Bread"
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)

# Task 3: Add "Cookies" to the inventory
grocery_inventory.update({"Cookies": (143, "Bakery")}) 
print("Inventory after adding Cookies:", grocery_inventory)

# Task 4: Remove "Eggs" from the inventory
grocery_inventory.pop("Eggs")  
print("Inventory after removing Eggs:", grocery_inventory)