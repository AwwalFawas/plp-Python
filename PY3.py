def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price


# Ask the user for input
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount)

# Print the result
print("Final price after discount:", final_price)
