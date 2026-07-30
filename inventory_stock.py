# 1. DEFINE THE DECORATOR 
def log_inventory_check(func):
    # 'wrapper' is the inner function that runs the extra steps
    def wrapper(*args, **kwargs):
        print("--- Log: Inventory Check Started ---")  # Prints the starting log
        return func(*args, **kwargs)                   # Runs the main function
    return wrapper                                     # Returns the wrapper recipe

# 2. DEFINE THE FUNCTION WITH SAFETY NET 
@log_inventory_check  # Attaches our logging stamp right above the function!
def calculate_stock_value(unit_price, quantity_in_stock):
    try:
        # Convert text inputs into numeric values so we can do math
        price = float(unit_price) 
        quantity = int(quantity_in_stock)

        # Check if price or quantity is zero or negative
        if price <= 0 or quantity <= 0:
            return "Invalid Data: Price and quantity must be greater than zero."

        # Calculate the total stock value
        total_stock_value = price * quantity
        return total_stock_value

    # Backup net 1: Catches invalid conversion errors (e.g. text instead of digits)
    except ValueError:
        return "Error: Price and quantity must be valid numbers!"
        
    # Backup net 2: Catches any other unexpected error
    except Exception as e:
        return f"Unexpected error: {e}"

# 3. RUN THE CODE 
# Call our function using clear keyword arguments!
final_result = calculate_stock_value(unit_price="12.50", quantity_in_stock="10")

# Print the result to our screen
print(final_result)