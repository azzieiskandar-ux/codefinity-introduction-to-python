produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# Combine lists into a single list of lists
groceries = [produce, dairy]

# Outer loop iterates through each section (list)
for section in groceries:
    # Inner loop iterates through each item in the current section
    for item in section:
        print(f"Item name: {item}")
