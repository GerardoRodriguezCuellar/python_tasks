#                               TITLE PAGE
"""
    Title: Handling Functions in Python 
    Student name: Gerardo Rodríguez Cuéllar
    Student ID: 2530125
    Group: 1-1
"""

#                           EXECUTIVE SUMMARY

"""
    A function in Python is a reusable block 
    of code that performs a specific task. 
    Functions allow programs to be cleaner,
    organized, and easier to maintain. Parameters 
    are the names defined in the function 
    declaration, while arguments are the real 
    values passed during the function call. 
    Separating logic into functions helps avoid 
    repetition and makes the code easier to test.

    A return value allows the function to send 
    data back to the caller, which is more flexible 
    than simply printing results. This document 
    includes six problems using functions with
    parameters, return values, input validation, 
    and basic testing through example cases.
"""

#                   PRINCIPLES AND GOOD PRACTICES

"""
    - Prefer small functions that perform a single task
      (single responsibility).
    - Avoid repeating code; extract repeated logic into functions.
    - Try to write pure functions when possible (same input produces
      same output, without external side effects).
    - Document each function with simple comments explaining what it
      does and what parameters it expects.
    - Use clear and meaningful names for functions and variables
      (calculate_area, summarize_numbers, apply_discount).
"""

#                           PROBLEM 1

""" 
    Problem 1: Rectangle area and perimeter

    Description:
        This problem defines two functions:
        - calculate_area(width, height): returns the area of a rectangle.
        - calculate_perimeter(width, height): returns the perimeter.
        The main code must validate the inputs, call both functions,
        and display their results.

    Inputs:
        - width (float)
        - height (float)

    Outputs:
        - "Area:" <area_value>
        - "Perimeter:" <perimeter_value>

    Validations:
        - width > 0
        - height > 0
        - If any validation fails, display "Error: invalid input"
        and do not call the functions.

    Test cases:
    1) Normal:
        width = 5, height = 3
        Output:
        Area: 15
        Perimeter: 16

    2) Border:
        width = 0.1, height = 0.1
        Output:
        Area: 0.01
        Perimeter: 0.4

    3) Error:
        width = -4, height = 2
        Output:
        Error: invalid input
    """

print()
print("                     Problem 1")
print()

#                   CODE

def calculate_area(width, height):
# Return the area of a rectangle.
    return width * height


def calculate_perimeter(width, height):
# Return the perimeter of a rectangle.
    return 2 * (width + height)

try:
    # Ask the user for the width and height
    width_value = float(input("Enter the width: "))
    height_value = float(input("Enter the height: "))

     # Validate that both values are greater than 0
    if width_value > 0 and height_value > 0:
        # Call the functions to calculate area and perimeter
        area_result = calculate_area(width_value, height_value)
        perimeter_result = calculate_perimeter(width_value, height_value)

        print() 
        print("Area:", area_result)
        print("Perimeter:", perimeter_result)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")

print()

print("------------------------------------------------------------------")

#                       PROBLEM 2

"""
    Problem 2: Grade classifier

    Description:
        This problem defines a function named classify_grade(score)
        that receives a numeric score (0–100) and returns a letter grade:
        - "A" if score >= 90
        - "B" if 80 <= score < 90
        - "C" if 70 <= score < 80
        - "D" if 60 <= score < 70
        - "F" if score < 60

        The main code must validate the input, call the function,
        and display the output in the required format.

    Inputs:
        - score (float or int)

    Outputs:
        - "Score:" <score>
        - "Category:" <grade_letter>

    Validations:
        - 0 <= score <= 100
        - If the input is invalid, display "Error: invalid input"
          and do not call the function.

    Test cases:
    1) Normal:
        score = 85
        Output:
        Score: 85
        Category: B

    2) Border:
        score = 100
        Output:
        Score: 100
        Category: A

    3) Error:
        score = -10
        Output:
        Error: invalid input
"""

print()
print("                     Problem 2")
print()

#                   CODE

def classify_grade(score):
    # Return the letter grade based on the score value.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    # Ask the user for the score
    score_value = float(input("Enter the score: "))

    # Validate that the score is between 0 and 100
    if 0 <= score_value <= 100:
        # Call the function to classify the grade
        category_result = classify_grade(score_value)

        print()
        print("Score:", score_value)
        print("Category:", category_result)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")

print()

print("------------------------------------------------------------------")

#                       PROBLEM 3

"""
    Problem 3: List statistics (min, max, average)

    Description:
        This problem defines a function named summarize_numbers(numbers_list)
        that receives a list of numbers and returns a dictionary with:
        - "min": minimum value
        - "max": maximum value
        - "average": average of the numbers

        The main code must build the list from user input, validate it,
        call the function, and display the results.

    Inputs:
        - numbers_text (string: e.g., "10,20,30")
        - Internally: numbers_list (list of float)

    Outputs:
        - "Min:" <min_value>
        - "Max:" <max_value>
        - "Average:" <average_value>

    Validations:
        - numbers_text must not be empty after strip()
        - The resulting list must not be empty
        - All elements must be valid numbers
        - If any validation fails, display "Error: invalid input"

    Test cases:
    1) Normal:
        numbers_text = "10,20,30"
        Output:
        Min: 10
        Max: 30
        Average: 20.0

    2) Border:
        numbers_text = "5"
        Output:
        Min: 5
        Max: 5
        Average: 5.0

    3) Error:
        numbers_text = "10, hello, 20"
        Output:
        Error: invalid input
"""

print()
print("                     Problem 3")
print()

#                   CODE

def summarize_numbers(numbers_list):
    # Return a dictionary with min, max, and average of the list.
    summary = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return summary

try:
    # Ask the user for the numbers separated by commas
    numbers_text = input("Enter numbers separated by commas: ").strip()

    # Validate input is not empty
    if numbers_text == "":
        print("Error: invalid input")
    else:
        # Split text into list of strings
        raw_list = numbers_text.split(",")

        numbers_list = []

        # Convert each element to float
        for item in raw_list:
            try:
                number = float(item)
                numbers_list.append(number)
            except ValueError:
                print("Error: invalid input")
                numbers_list = []
                break

        # Validate that the list is not empty
        if len(numbers_list) > 0:
            # Call the function to get the summary
            result = summarize_numbers(numbers_list)

            print()
            print("Min:", result["min"])
            print("Max:", result["max"])
            print("Average:", result["average"])
        # If list is empty after errors, do nothing
    # End of main validation

except Exception:
    print("Error: invalid input")

print()

print("------------------------------------------------------------------")

#                       PROBLEM 4

"""
    Problem 4: Apply discount list (pure function)

    Description:
        This problem defines a function named apply_discount(prices_list, discount_rate)
        that receives a list of prices and a discount rate (0 to 1),
        and returns a NEW list with the discounted prices.
        The original list must not be modified (pure function).

        The main code must build the list from user input, validate the data,
        call the function, and display both the original and discounted lists.

    Inputs:
        - prices_text (string: e.g., "100,200,300")
        - discount_rate (float: 0 to 1)

    Outputs:
        - "Original prices:" <original_list>
        - "Discounted prices:" <discounted_list>

    Validations:
        - prices_text must not be empty after strip()
        - The resulting prices list must not be empty
        - All prices must be > 0
        - 0 <= discount_rate <= 1
        - If any validation fails, display "Error: invalid input"

    Test cases:
    1) Normal:
        prices_text = "100,200,300"
        discount_rate = 0.10
        Output:
        Original prices: [100.0, 200.0, 300.0]
        Discounted prices: [90.0, 180.0, 270.0]

    2) Border:
        prices_text = "50"
        discount_rate = 0
        Output:
        Original prices: [50.0]
        Discounted prices: [50.0]

    3) Error:
        prices_text = "100,-20,30"
        discount_rate = 0.20
        Output:
        Error: invalid input
"""

print()
print("                     Problem 4")
print()


#                   CODE

def apply_discount(prices_list, discount_rate):
    # Return a NEW list with discounted prices (pure function).
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted

try:
    # Ask the user for the prices separated by commas
    prices_text = input("Enter prices separated by commas: ").strip()

    # Validate that the input is not empty
    if prices_text == "":
        print("Error: invalid input")
    else:
        raw_prices = prices_text.split(",")
        prices_list = []

        valid_conversion = True

        # Convert each element to float and validate price > 0
        for item in raw_prices:
            try:
                price = float(item)
                if price > 0:
                    prices_list.append(price)
                else:
                    valid_conversion = False
                    break
            except ValueError:
                valid_conversion = False
                break

        # Ask for discount rate
        try:
            discount_rate = float(input("Enter the discount rate (0 to 1): "))
        except ValueError:
            valid_conversion = False

        # Validate discount rate
        if not (0 <= discount_rate <= 1):
            valid_conversion = False

        # If everything is valid, call the function
        if valid_conversion and len(prices_list) > 0:
            discounted_list = apply_discount(prices_list, discount_rate)

            print()
            print("Original prices:", prices_list)
            print("Discounted prices:", discounted_list)
        else:
            print("Error: invalid input")
    # End of validations

except Exception:
    print("Error: invalid input")

print()

print("------------------------------------------------------------------")

#                       PROBLEM 5

"""
    Problem 5: Greeting function with default parameters

    Description:
        Define a function greet(name, title="") that:
        - Optionally concatenates the title before the name (for example, "Dr. Alice").
        - Returns the message: "Hello, <full_name>!"
        If title is empty, only the name is used.
        The main code must call the function using positional and named arguments.

    Inputs:
        - name (string)
        - title (optional string)

    Outputs:
        - "Greeting:" <greeting_message>

    Validations:
        - name must not be empty after strip().
        - title may be empty, but if not empty, it must also be stripped.

    Test cases:
    1) Normal:
        name = "Victor", title = "Dr."
        Output:
        Greeting: Hello, Dr. Victor!

    2) Border:
        name = "Ramón", title = "" 
        Output:
        Greeting: Hello, Ramón!

    3) Error:
        name = "   ", title = "Eng."
        Output:
        Error: invalid input
"""

print()
print("                     Problem 5")
print()

#                   CODE

def greet(name, title=""):
    
    # Return a greeting message. 
    name = name.strip()
    title = title.strip()

    if title == "":
        full_name = name
    else:
        full_name = f"{title} {name}"

    return f"Hello, {full_name}!"

try:
    # Ask the user for name and title
    name_value = input("Enter the name: ")
    title_value = input("Enter the title (optional): ")

    # Validate name
    if name_value.strip() == "":
        print("Error: invalid input")
    else:
        # Call the function
        greeting_message = greet(name_value, title_value)

        print()
        print("Greeting:", greeting_message)

except Exception:
    print("Error: invalid input")

print()

print("------------------------------------------------------------------")

#                       PROBLEM 6

"""
    Problem 6: Factorial function (iterative)

    Description:
        Define a function factorial(n) that returns n! (n factorial).
        The program must read or define n, validate it, call the function,
        and show the factorial result.
        The implementation here uses the iterative version.

    Inputs:
        - n (int)

    Outputs:
        - "n:" <n>
        - "Factorial:" <factorial_value>

    Validations:
        - n must be an integer.
        - n must be >= 0.
        - Optional: limit n to a maximum of 20.
        - If invalid, show: "Error: invalid input".

    Test cases:
    1) Normal:
        n = 5
        Output:
        n: 5
        Factorial: 120

    2) Border:
        n = 0
        Output:
        n: 0
        Factorial: 1

    3) Error:
        n = -3
        Output:
        Error: invalid input
"""

print()
print("                     Problem 6")
print()

#                   CODE

def factorial(n):
    # Iterative factorial function.
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    # Ask the user for n
    n_value = input("Enter n: ")

    # Validate if it's an integer
    if "." in n_value:
        print("Error: invalid input")
    else:
        n_value = int(n_value)

        # Validate range
        if n_value < 0 or n_value > 20:
            print("Error: invalid input")
        else:
            # Call factorial function
            factorial_result = factorial(n_value)

            print()
            print("n:", n_value)
            print("Factorial:", factorial_result)

except ValueError:
    print("Error: invalid input")

print()

#                           CONCLUSIONS

"""
    Throughout these problems, I learned how functions help organize
    and reuse logic in a clean and structured way. Using return values
    instead of only printing makes the code more flexible and easier
    to test. Parameters and default values also allow functions to be
    used in different situations without rewriting code. Separating
    the main logic from helper functions made the programs easier to
    understand and maintain. Overall, these exercises improved my
    ability to design clear, reusable and well-validated functions.
"""

#                           REFERENCES
"""
    1) https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    2) https://docs.python.org/3/library/functions.html
    3) https://realpython.com/defining-your-own-python-function/
    4) https://www.w3schools.com/python/python_functions.asp
    5) https://www.geeksforgeeks.org/python-functions/
"""