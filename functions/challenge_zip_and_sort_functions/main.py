# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# 1. Combine the three lists into a list of tuples
combined_list = list(zip(products, prices, quantities_sold))

# 2. Sort by product name (the first element in the tuple) in ascending order
sorted_products = sorted(combined_list)

# 3. Loop through and print in the specified format
for product_name, price, quantity_sold in sorted_products:
    print(f"Product: {product_name}, Price: {price}, Quantity Sold: {quantity_sold}")
