prices = [29.99, 45.50, 12.75, 38.20]

prices = [29.99, 45.50, 12.75, 38.20]

# Iterate over the indices of the prices list
for i in range(len(prices)):
    # Check the current index to determine the discount rate
    if i == 0:
        prices[i] = prices[i] * 0.90  # 10% discount
    elif i == 1:
        prices[i] = prices[i] * 0.80  # 20% discount
    elif i == 2:
        prices[i] = prices[i] * 0.85  # 15% discount
    elif i == 3:
        prices[i] = prices[i] * 0.95  # 5% discount
    
    # Print the result using the specified format
    print(f"Updated price for item {i}: ${prices[i]:.2f}")
