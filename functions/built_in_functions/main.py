# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

total_sales_list = []

# Use a for loop to iterate through the products dictionary
for name, data in products.items():
    # Convert types
    price = float(data[0])
    quantity = int(data[1])
    
    # Calculate total sales for the specific product
    total_sales = price * quantity
    
    # Append the result to the list
    total_sales_list.append(total_sales)
    
    # Output individual product result
    print(f"Total sales for {name}: ${total_sales:.2f}")

# Calculate summary statistics
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

# Final summary output
print("-" * 30)
print(f"Total sum of all sales: ${total_sum:.2f}")
print(f"Minimum sales: ${min_sales:.2f}")
print(f"Maximum sales: ${max_sales:.2f}")
