grocery_items = "milk cheese bread apples oranges chicken"

# Extract dairy and bakery items
# Assume milk, cheese, and bread are located together in the store
dairy1 = grocery_items[ 0 : 4 ] # 'milk'
dairy2 = grocery_items[ 5 : 11 ]  # 'cheese'
bakery1 = grocery_items[ 12 : 17 ] # 'bread'

# Use concatenation to create the output statement
print("We have dairy and bakery items: " + dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5")