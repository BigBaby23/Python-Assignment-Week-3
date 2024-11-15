def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Fixed inputs for testing
original_price = 30000  # Fixed input for original price
discount_percentage = 20  # Fixed input for discount percentage

try:
    # Calculate and print the final price
    final_price = calculate_discount(original_price, discount_percentage)
    print(f"Original Price: ${original_price}")
    print(f"Discount Percentage: {discount_percentage}%")
    print(f"The final price after discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input! Please ensure you provide numbers for price and discount percentage.")
