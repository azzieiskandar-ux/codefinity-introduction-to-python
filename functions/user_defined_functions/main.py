# Task 1: Define the function to calculate total cost
def calculate_total_cost(price, quantity):
    # Calculate total cost
    total_cost = price * quantity
    # Task 2: Return the total cost
    return total_cost

# Call the function and print the result
apples_total_cost = calculate_total_cost(1.50, 10)
print(f"The total cost for apples is ${apples_total_cost}")