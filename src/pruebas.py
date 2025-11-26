# Read product name
product_name = input("Enter the product name: ")

# Normalize product name
cleaned_product_name = product_name.strip()

# Validate product name
if cleaned_product_name == "":
    print("Error: invalid input")
else:
    # Read price (only if product name is valid)
    price_value = input("Enter the price: ").strip()

    # Validate and convert price
    try:
        price_number = float(price_value)
        if price_number < 0:
            print("Error: invalid input")
        else:
            # Build base label
            label = f"Product: {cleaned_product_name} | Price: ${price_number}"

            # Ensure length is exactly 30 characters
            if len(label) > 30:
                label = label[:30]
            else:
                label = label.ljust(30)

            # Output
            print(f'Label: "{label}"')
    except ValueError:
        print("Error: invalid input")