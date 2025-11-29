# Read values
weight_text = input("Enter weight in kg: ")
height_text = input("Enter height in meters: ")

# Validate and convert
try:
    weight_kg = float(weight_text)
    height_m = float(height_text)
except:
    print()
    print("Error: invalid input")
    exit()

if weight_kg <= 0 or height_m <= 0:
    print()
    print("Error: invalid input")
    exit()

# Calculate BMI
bmi = weight_kg / (height_m * height_m)

# Boolean flags
is_underweight = bmi < 18.5
is_normal = bmi >= 18.5 and bmi < 25
is_overweight = bmi >= 25

# Output
print(f"BMI: {bmi}")
print(f"Underweight: {is_underweight}")
print(f"Normal: {is_normal}")
print(f"Overweight: {is_overweight}")