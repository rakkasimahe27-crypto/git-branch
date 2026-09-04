def calculate_total(price, tax_rate=0.05):
    """Calculates the total cost including tax."""
    total = price + (price * tax_rate)
    return total

# Call the function
final_bill = calculate_total(100, 0.08)
print(f"Total Amount: ${final_bill}") # Output: Total Amount: $108.0

