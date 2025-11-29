#                               TITLE PAGE
"""
    Student name: Gerardo Rodríguez Cuéllar 
    Student ID: 2530125
    Group: 1-1
"""

#                           EXECUTIVE SUMMARY

"""
    - This document works with numeric data types in Python: int and float.
    - The type int is used for whole numbers, while float is used for numbers with decimals.
    - Boolean values (True and False) are obtained from logical and comparison operations.
    - These booleans help the program make decisions using conditions such as if, and, or, and not.
    - Input validation is very important to avoid invalid values and division by zero.
    - This script includes six problems that apply calculations, comparisons, and logical evaluation.
    - Each problem demonstrates different uses of numeric operations and boolean logic.
    - The file also includes descriptions, test cases, validation rules, and conclusions.
"""

#                   PRINCIPLES AND GOOD PRACTICES

"""
    - Use int for counters and whole numbers, and float for decimal values.
    - Always validate input before performing any calculation.
    - Avoid division by zero by checking values before dividing.
    - Store intermediate results in variables to avoid repeated expressions.
    - Use descriptive variable names in lower_snake_case.
    - Display clear output messages so the user understands the results.
    - Always document what a boolean variable represents (what true and false mean).
"""

#                       PROBLEM 1

"""
    Problem 1: Temperature converter and range flag

    Description:
    Converts a temperature from Celsius to Fahrenheit and Kelvin.
    Also determines a boolean value that indicates if the temperature
    is considered high based on a fixed limit.

    Inputs:
    - temp_c (float)

    Outputs:
    - "Fahrenheit: <value>"
    - "Kelvin: <value>"
    - "High temperature: true | false"

    Validations:
    - temp_c must be convertible to float.
    - Temperature in Kelvin must not be less than 0.

    Test cases:
    1) Normal:
        Input: temp_c = 35
        Output:
        Fahrenheit: 95.0
        Kelvin: 308.15
        High temperature: True

    2) Border:
        Input: temp_c = 30
        Output:
        Fahrenheit: 86.0
        Kelvin: 303.15
        High temperature: True

    3) Error:
        Input: temp_c = "Americaa"
        Output:
        Error: invalid input
"""

print()
print("                     Problem 1")
print()

#                       CODE

temp_c_text = input("Enter temperature in Celsius: ")

# Validate numeric input
try:
    temp_c = float(temp_c_text)

    # Convert to Kelvin
    temp_k = temp_c + 273.15

    # Validate physical limit
    if temp_k < 0:
        print("Error: invalid input")
    else:
        # Convert to Fahrenheit
        temp_f = temp_c * 9 / 5 + 32

        # Boolean flag
        is_high_temperature = temp_c >= 30.0

        # Output
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)

except ValueError:
    print("Error: invalid input")

print("------------------------------------------------------------------")

#                       PROBLEM 2

"""
    Problem 2: Work hours and overtime payment

    Description:
    Calculates the total weekly payment of a worker.
    Up to 40 hours are paid at the normal hourly rate.
    Extra hours (over 40) are paid at 150% of the normal rate.
    Also generates a boolean value has_overtime to indicate if overtime was worked.

    Inputs:
    - hours_worked (float; number of hours worked during the week).
    - hourly_rate (float; payment per hour).

    Outputs:
    - "Regular pay: <value>"
    - "Overtime pay: <value>"
    - "Total pay: <value>"
    - "Has overtime: true|false"

    Validations:
    - hours_worked must be greater than or equal to 0.
    - hourly_rate must be greater than 0.
    - If any validation fails, display "Error: invalid input".

    Test cases:
    1) Normal:
        Input: hours_worked = 45, hourly_rate = 100
        Output:
        Regular pay: 4000.0
        Overtime pay: 750.0
        Total pay: 4750.0
        Has overtime: True

    2) Border:
        Input: hours_worked = 40, hourly_rate = 80
        Output:
        Regular pay: 3200.0
        Overtime pay: 0.0
        Total pay: 3200.0
        Has overtime: False

    3) Error:
        Input: hours_worked = -5, hourly_rate = 100
        Output:
        Error: invalid input
"""

print()
print("                     Problem 2")
print()

#                   CODE

hours_text = input("Enter worked hours: ")
rate_text = input("Enter hourly rate: ")

print()

# Validate numeric conversion
try:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)

    # Validate values
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        REGULAR_HOURS = 40

        # Calculate regular and overtime hours
        if hours_worked > REGULAR_HOURS:
            regular_hours = REGULAR_HOURS
            overtime_hours = hours_worked - REGULAR_HOURS
            has_overtime = True
        else:
            regular_hours = hours_worked
            overtime_hours = 0
            has_overtime = False

        # Payments
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        # Output
        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)

except ValueError:
    print("Error: invalid input")

print("------------------------------------------------------------------")

#                       PROBLEM 3

"""
    Problem 3: Discount eligibility with booleans

    Description:
    Determines whether a customer gets a discount on a purchase.
    The customer is eligible if at least one of these conditions is true:
    - is_student is true
    - is_senior is true
    - purchase_total is greater than or equal to 1000.0
    If eligible, a 10% discount is applied to the final amount.

    Inputs:
    - purchase_total (float)
    - is_student_text (string: "YES" or "NO")
    - is_senior_text (string: "YES" or "NO")

    Outputs:
    - "Discount eligible: true|false"
    - "Final total: <amount>"

    Validations:
    - purchase_total must be greater than or equal to 0.
    - is_student_text and is_senior_text must be "YES" or "NO".
    - If any validation fails, print "Error: invalid input".

    Test cases:
    1) Normal:
       Input:
       purchase_total = 1200
       is_student_text = "NO"
       is_senior_text = "NO"
       Output:
       Discount eligible: true
       Final total: 1080.0

    2) Border:
       Input:
       purchase_total = 1000
       is_student_text = "NO"
       is_senior_text = "NO"
       Output:
       Discount eligible: true
       Final total: 900.0

    3) Error:
       Input:
       purchase_total = 500
       is_student_text = "MAYBE"
       is_senior_text = "NO"
       Output:
       Error: invalid input
"""

print()
print("                     Problem 3")
print()

#                   CODE

purchase_total_text = input("Enter purchase total: ")

# Validate and convert purchase_total
try:
    purchase_total = float(purchase_total_text)
    if purchase_total < 0:
        print("Error: invalid input")
        exit()
except:
    print("Error: invalid input")
    exit()

# Read student and senior text
is_student_text = input("Is the customer a student (YES/NO): ").strip().upper()
is_senior_text = input("Is the customer a senior (YES/NO): ").strip().upper()

# Validate YES / NO
if is_student_text != "YES" and is_student_text != "NO":
    print("Error: invalid input")
    exit()

f is_senior_text != "YES" and is_senior_text != "NO":
    print("Error: invalid input")
    exit()

# Convert to boolean
is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "YES")

# Determine eligibility
discount_eligible = is_student or is_senior or (purchase_total >= 1000)

# Apply discount if eligible
if discount_eligible:
    final_total = purchase_total * 0.9
else:
    final_total = purchase_total

# Output
print(f"Discount eligible: {discount_eligible}")
print(f"Final total: {final_total}")

print("------------------------------------------------------------------")

#                       PROBLEM 4

"""
    Problem 4: Basic statistics of three integers

    Description:
    Reads three integers and calculates basic statistics: sum, average,
    maximum, minimum and a boolean value that indicates whether all numbers
    are even.

    Inputs:
    - n1 (int)
    - n2 (int)
    - n3 (int)

    Outputs:
    - "Sum: <value>"
    - "Average: <value>"
    - "Max: <value>"
    - "Min: <value>"
    - "All even: true|false"

    Validations:
    - All inputs must be convertible to int.
    - Negative numbers are allowed.

    Test cases:

    1) Normal:
       Input:
       n1 = 4
       n2 = 7
       n3 = 10
       Output:
       Sum: 21
       Average: 7.0
       Max: 10
       Min: 4
       All even: false

    2) Border:
       Input:
       n1 = 2
       n2 = 6
       n3 = 8
       Output:
       Sum: 16
       Average: 5.33
       Max: 8
       Min: 2
       All even: true

    3) Error:
       Input:
       n1 = "a"
       n2 = 5
       n3 = 7
       Output:
       Error: invalid input
"""

print()
print("                     Problem 4")
print()


#                   CODE

n1_text = input("Enter first integer: ")
n2_text = input("Enter second integer: ")
n3_text = input("Enter third integer: ")

# Convert to integers with validation
try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)
except:
    print("Error: invalid input")
    exit()

# Calculations
sum_value = n1 + n2 + n3
average_value = sum_value / 3
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)

# Check if all are even
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

# Output
print()
print(f"Sum: {sum_value}")
print(f"Average: {round(average_value, 2)}")
print(f"Max: {max_value}")
print(f"Min: {min_value}")
print(f"All even: {all_even}")

print("------------------------------------------------------------------")

#                       PROBLEM 5

"""
    Problem 5: Loan eligibility (income and debt ratio)

    Description:
    Determines whether a person is eligible for a loan based on monthly income,
    monthly debt, and credit score.

    Inputs:
    - monthly_income (float)
    - monthly_debt (float)
    - credit_score (int)

    Outputs:
    - "Debt ratio: <value>"
    - "Eligible: true|false"

    Validations:
    - monthly_income must be greater than 0.
    - monthly_debt must be 0 or greater.
    - credit_score must be 0 or greater.
    - If any validation fails, print "Error: invalid input".

    Test cases:

    1) Normal:
       Input:
       monthly_income = 10000
       monthly_debt = 3000
       credit_score = 700
       Output:
       Debt ratio: 0.3
       Eligible: true

    2) Border:
       Input:
       monthly_income = 8000
       monthly_debt = 3200
       credit_score = 650
       Output:
       Debt ratio: 0.4
       Eligible: true

    3) Error:
       Input:
       monthly_income = 0
       monthly_debt = 1000
       credit_score = 600
       Output:
       Error: invalid input
"""

print()
print("                     Problem 5")
print()

#                   CODE

monthly_income_text = input("Enter monthly income: ")
monthly_debt_text = input("Enter monthly debt: ")
credit_score_text = input("Enter credit score: ")

# Validate and convert
try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)
except:
    print("Error: invalid input")
    exit()

if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
    print()
    print("Error: invalid input")
    exit()

# Calculate debt ratio
debt_ratio = monthly_debt / monthly_income

# Determine eligibility
eligible = (monthly_income >= 8000) and (debt_ratio <= 0.4) and (credit_score >= 650)

# Output
print()
print(f"Debt ratio: {debt_ratio}")
print(f"Eligible: {eligible}")

print("------------------------------------------------------------------")

#                       PROBLEM 6

"""
    Problem 6: Body Mass Index (BMI) and category flag

    Description:
    Calculates the Body Mass Index (BMI) using weight and height.
    Then classifies the result into underweight, normal or overweight
    using boolean flags.

    Inputs:
    - weight_kg (float)
    - height_m (float)

    Outputs:
    - "BMI: <value>"
    - "Underweight: true|false"
    - "Normal: true|false"
    - "Overweight: true|false"

    Validations:
    - weight_kg must be greater than 0.
    - height_m must be greater than 0.
    - If any validation fails, print "Error: invalid input".

    Test cases:

    1) Normal:
       Input:
       weight_kg = 70
       height_m = 1.75
       Output:
       BMI: 22.86
       Underweight: false
       Normal: true
       Overweight: false

    2) Border:
       Input:
       weight_kg = 77
       height_m = 1.75
       Output:
       BMI: 25.14
       Underweight: false
       Normal: false
       Overweight: true

    3) Error:
       Input:
       weight_kg = -60
       height_m = 1.70
       Output:
       Error: invalid input
"""

print()
print("                     Problem 6")
print()

#                   CODE

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

#                           CONCLUSIONS

"""
    Integers and floats are commonly used together to solve 
    real-world problems such as payments and statistics.
    Comparisons between numbers generate boolean values that 
    control program decisions using if statements. Validating 
    ranges and avoiding division by zero prevents crashes and 
    incorrect results. Combining conditions with and, or, and 
    not allows building more precise decision rules. These 
    structures are useful in situations like payroll calculations, 
    discounts, and loan evaluations. Working with numerical data 
    and booleans improves program logic and reliability. Understanding 
    these types helps write cleaner and more predictable code.
"""

#                           REFERENCES

"""
    1) https://ellibrodepython.com/booleano-python
    2) https://realpython.com/python-boolean/
    3) https://www.youtube.com/watch?v=wuBMbkDejhM
    4) https://www.geeksforgeeks.org/python/how-to-convert-float-to-int-in-python/
    5) https://docs.python.org/es/3/library/stdtypes.html
"""