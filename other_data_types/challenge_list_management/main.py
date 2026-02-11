# Task 1: Use the data provided to initialize each list
meat = ["Ham", 3.99, 50, "Sliced"]  # Type, price, shelf quantity, specifics
cheese = ["Cheddar", 5.49, 100, "Sharp"]  # Type, price, shelf quantity, specifics
condiment = ["Mustard", 1.99, 75, "Spicy"]  # Type, price, shelf quantity, specifics

meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Create the main `deli_dept` list that contains these category lists
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)

deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)

# Task 2: Restock the "Ham" aisle.
if "Ham" in meat and meat[2] < 100:  # Check if "Ham" is in the meat list and if its quantity is less than 100
    meat[2] = 100  # Update the shelf quantity to 100

if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

# Task 3: Add another meat to the deli department
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# Task 4: Remove condiments from the deli_dept list
deli_dept.remove(condiment)
deli_dept.remove(condiment)

# Task 5: Sort the `deli_dept` list alphabetically by the type of item
deli_dept.sort()
deli_dept.sort()

# Print the updated deli list
print("Updated Deli List:", deli_dept)
print("Updated Deli List:", deli_dept)