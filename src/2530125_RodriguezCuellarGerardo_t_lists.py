#                               TITLE PAGE
"""
    Title: Handling Lists, Tuples, and Dictionaries in Python
    Student name: Gerardo Rodríguez Cuéllar 
    Student ID: 2530125
    Group: 1-1
"""

#                           EXECUTIVE SUMMARY

"""
    This document explains how lists, tuples, and 
    dictionaries work in Python. A list is a mutable 
    collection that allows adding, removing, and modifying 
    elements. A tuple is an immutable collection, which 
    means its values cannot be changed once created. A dictionary 
    stores data using key-value pairs, allowing fast searches 
    by key. This document includes six practical problems 
    using these data structures. Each problem contains a 
    description, inputs, outputs, validations, and test cases.
    Real-life examples such as catalogs, grades, and contact 
    books are used. This work helps understand how collections 
    organize and process data.
"""

#                   PRINCIPLES AND GOOD PRACTICES

"""
    - Use lists when you need to add or remove elements frequently.
    - Use tuples for data that should not be modified, such as coordinates or fixed values.
    - Use dictionaries when searching data by a key is required.
    - Do not modify a list while looping through it unless necessary.
    - Always validate inputs before processing the data.
    - Use descriptive variable names for better readability.
    - Display clear and understandable output messages to the user.
"""

#                       PROBLEM 1

""" 
    Problem 1: Shopping list basics (list operations)

    Description:
    This program works with a list of product names.
    It allows creating the list from user input, adding a new item,
    and checking if a specific product exists in the list.

    Inputs:
    - initial_items_text (string; example: "apple,banana,orange")
    - new_item (string)
    - search_item (string)

    Outputs:
    - "Items list:" <items_list>
    - "Total items:" <len_list>
    - "Found item:" true|false

    Validations:
    - initial_items_text must not be empty after strip().
    - Each item must be cleaned using strip().
    - new_item and search_item must not be empty.
    - The list must not be empty after processing.

    Test cases:

    1) Normal:
    Input:
    initial_items_text = "apple, banana, orange"
    new_item = "grape"
    search_item = "banana"
    Output:
    Items list: ['apple', 'banana', 'orange', 'grape']
    Total items: 4
    Found item: true

    2) Border:
    Input:
    initial_items_text = "milk"
    new_item = "bread"
    search_item = "milk"
    Output:
    Items list: ['milk', 'bread']
    Total items: 2
    Found item: true

    3) Error:
    Input:
    initial_items_text = "   "
    new_item = "rice"
    search_item = "beans"
    Output:
    Error: invalid input
"""

print()
print("                     Problem 1")
print()

#                   CODE

# Read inputs
initial_items_text = input("Enter initial items (comma separated): ")
new_item = input("Enter a new item to add: ")
search_item = input("Enter item to search: ")
  
# Normalize main input
cleaned_text = initial_items_text.strip()

# Validate initial list
if cleaned_text == "":
    print()
    print("Error: invalid input")
else:
    # Split and clean items
    raw_items = cleaned_text.split(",")
    items_list = []

    for item in raw_items:
        item_clean = item.strip()
        if item_clean != "":
            items_list.append(item_clean)

    # Validate list not empty
    if len(items_list) == 0:
        print("Error: invalid input")

    # Validate new_item and search_item
    elif new_item.strip() == "" or search_item.strip() == "":
        print("Error: invalid input")

    else:
        # Add new item
        items_list.append(new_item.strip())

        # Search in list
        is_in_list = search_item.strip() in items_list

        # Output
        print()
        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print(f"Found item: {str(is_in_list).lower()}")

print("------------------------------------------------------------------")

#                       PROBLEM 2

"""
    Problem 2: Points and distances with tuples

    Description:
    This program uses tuples to represent two points in a 2D plane.
    It calculates the distance between both points and determines
    the midpoint between them.

    Inputs:
    - x1 (float)
    - y1 (float)
    - x2 (float)
    - y2 (float)

    Outputs:
    - "Point A:" (x1, y1)
    - "Point B:" (x2, y2)
    - "Distance:" <distance>
    - "Midpoint:" (mx, my)

    Validations:
    - All inputs must be convertible to float.
    - No additional range restrictions are required.

    Test cases:

    1) Normal:
    Input:
    x1 = 2
    y1 = 3
    x2 = 6
    y2 = 7
    Output:
    Point A: (2.0, 3.0)
    Point B: (6.0, 7.0)
    Distance: 5.66
    Midpoint: (4.0, 5.0)

    2) Border:
    Input:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    Output:
    Point A: (0.0, 0.0)
    Point B: (0.0, 0.0)
    Distance: 0.0
    Midpoint: (0.0, 0.0)

    3) Error:
    Input:
    x1 = "a"
    y1 = 5
    x2 = 2
    y2 = 9
    Output:
    Error: invalid input
"""

print()
print("                     Problem 2")
print()

#                   CODE

x1_text = input("Enter x1: ")
y1_text = input("Enter y1: ")
x2_text = input("Enter x2: ")
y2_text = input("Enter y2: ")

# Validate and convert inputs
try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)
except:
    print()
    print("Error: invalid input")
    exit()

# Create tuples
point_a = (x1, y1)
point_b = (x2, y2)

# Calculate distance
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Calculate midpoint
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

# Output
print()
print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", distance)
print("Midpoint:", midpoint)

print("------------------------------------------------------------------")

#                       PROBLEM 3

"""
    Problem 3: Product catalog with dictionary

    Description:
    This program manages a small product catalog using a dictionary.
    Each product has a name as key and a unit price as value.
    The program calculates the total cost of a purchase if the product exists.

    Inputs:
    - product_name (string)
    - quantity (int)

    Outputs:
    If the product exists:
    - "Unit price: <unit_price>"
    - "Quantity: <quantity>"
    - "Total: <total_price>"

    If the product does not exist:
    - "Error: product not found"

    Validations:
    - product_name must not be empty after strip().
    - quantity must be greater than 0.
    - The product name must exist as a key in the dictionary.

    Test cases:

    1) Normal:
    Input:
    product_name = "pen"
    quantity = 3
    Output:
    Unit price: 10.0
    Quantity: 3
    Total: 30.0

    2) Border:
    Input:
    product_name = "pencil"
    quantity = 1
    Output:
    Unit price: 5.0
    Quantity: 1
    Total: 5.0

    3) Error:
    Input:
    product_name = "calculator"
    quantity = 2
    Output:
    Error: product not found
"""

print()
print("                     Problem 3")
print()

#                   CODE

product_prices = {
    "pen": 10.0,
    "pencil": 5.0,
    "eraser": 7.5
}

# Read inputs
product_name = input("Enter product name: ").strip().lower()
quantity_text = input("Enter quantity: ")

# Validate product name
if product_name == "":
    print()
    print("Error: invalid input")
    exit()

# Validate quantity
try:
    quantity = int(quantity_text)
except:
    print() 
    print("Error: invalid input")
    exit()

if quantity <= 0:
    print()
    print("Error: invalid input")
    exit()

# Check if product exists
if product_name not in product_prices:
    print()
    print("Error: product not found")
    exit()

# Get price and calculate total
unit_price = product_prices[product_name]
total_price = unit_price * quantity

# Output
print()
print("Unit price:", unit_price)
print("Quantity:", quantity)
print("Total:", total_price)

print("------------------------------------------------------------------")

#                       PROBLEM 4

"""
    Problem 4: Student grades with dict and list

    Description:
    This program manages student grades using a dictionary of lists.
    Each student has a list of grades and the program calculates the average.
    It also determines if the student passed or failed using a boolean value.

    Inputs:
    - student_name (string)

    Outputs:
    If the student exists:
    - "Grades: <grades_list>"
    - "Average: <average>"
    - "Passed: true|false"

    If the student does not exist:
    - "Error: student not found"

    Validations:
    - student_name must not be empty after strip().
    - The student name must exist as a key in the dictionary.
    - The grade list must not be empty.

    Test cases:

    1) Normal:
    Input:
    student_name = "Victor"
    Output:
    Grades: [85, 90, 88]
    Average: 87.67
    Passed: true

    2) Border:
    Input:
    student_name = "Oswaldo"
    Output:
    Grades: [70, 70, 70]
    Average: 70.0
    Passed: true

    3) Error:
    Input:
    student_name = "Marisol"
    Output:
    Error: student not found
"""

print()
print("                     Problem 4")
print()


#                   CODE

# Initial dictionary of students and grades
grades = {
    "Victor": [85, 90, 88],
    "Oswaldo": [70, 70, 70],
    "Charly": [60, 65, 58]
}

# Read input
student_name = input("Enter student name: ").strip()

# Validate name
if student_name == "":
    print()
    print("Error: invalid input")
    exit()

# Check if student exists
if student_name not in grades:
    print()
    print("Error: student not found")
    exit()

# Get grades list
student_grades = grades[student_name]

# Validate grades list
if len(student_grades) == 0:
    print()
    print("Error: invalid input")
    exit()

# Calculate average
average = sum(student_grades) / len(student_grades)

# Determine pass/fail
is_passed = average >= 70.0

# Output
print()
print("Grades:", student_grades)
print("Average:", average)
print("Passed:", is_passed)

print("------------------------------------------------------------------")

#                       PROBLEM 5

"""
    Problem 5: Word frequency counter (list + dict)

    Description:
    This program counts how many times each word appears in a sentence.
    It uses a list to store the words and a dictionary to store frequencies.
    The program also shows the most common word in the sentence.

    Inputs:
    - sentence (string)

    Outputs:
    - "Words list: <words_list>"
    - "Frequencies: <freq_dict>"
    - "Most common word: <word>"

    Validations:
    - sentence must not be empty after strip().
    - The words list must not be empty.

    Test cases:

    1) Normal:
    Input:
    sentence = "apple orange apple banana apple"
    Output:
    Words list: ['apple', 'orange', 'apple', 'banana', 'apple']
    Frequencies: {'apple': 3, 'orange': 1, 'banana': 1}
    Most common word: apple

    2) Border:
    Input:
    sentence = "hello hello"
    Output:
    Words list: ['hello', 'hello']
    Frequencies: {'hello': 2}
    Most common word: hello

    3) Error:
    Input:
    sentence = "    "
    Output:
    Error: invalid input
"""

print()
print("                     Problem 5")
print()

#                   CODE

# Read input
sentence = input("Enter a sentence: ").strip()

# Validate sentence
if sentence == "":
    print()
    print("Error: invalid input")
    exit()

# Normalize and split
sentence = sentence.lower()
words_list = sentence.split()

# Validate words list
if len(words_list) == 0:
    print()
    print("Error: invalid input")
    exit()

# Dictionary for frequencies
freq_dict = {}

# Count words
for word in words_list:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

# Find most common word
most_common_word = ""
max_count = 0

for word in freq_dict:
    if freq_dict[word] > max_count:
        max_count = freq_dict[word]
        most_common_word = word

# Output
print()
print("Words list:", words_list)
print("Frequencies:", freq_dict)
print("Most common word:", most_common_word) 

print("------------------------------------------------------------------")

#                       PROBLEM 6

"""
    Problem 6: Simple contact book (dictionary CRUD)

    Description:
    Implements a mini contact book using a dictionary where:
    - key: contact name (string)
    - value: phone number (string)

    The program must:
    1) Create an initial dictionary with some contacts.
    2) Read an action action_text ("ADD", "SEARCH" or "DELETE").
    3) According to the action:
    - "ADD": read name and phone, add or update the contact.
    - "SEARCH": read name and show phone if exists.
    - "DELETE": read name and delete the contact if exists.
    4) Show a message indicating the result of the operation.

    Inputs:
    - action_text (string; "ADD", "SEARCH" or "DELETE")
    - name (string; depends on the action)
    - phone (string; only for "ADD")

    Outputs:
    - For "ADD":
    - "Contact saved:" name, phone
    - For "SEARCH":
    - If exists: "Phone:" <phone>
    - If not: "Error: contact not found"
    - For "DELETE":
    - If exists: "Contact deleted:" name
    - If not: "Error: contact not found"

    Validations:
    - Normalize action_text to uppercase.
    - Verify action_text is one of the three valid options.
    - name must not be empty after strip().
    - For "ADD": phone must not be empty after strip().

    Test cases:

    1) Normal:
    Input:
        Enter action: ADD
        Enter name: Carlos
        Enter phone: 999888777
    Output:
        Contact saved: Carlos, 999888777

    2) Border:
    Input:
        Enter action: DELETE
        Enter name: Juan
    Output:
        Error: contact not found

    3) Error:
        Enter action: ADD
        Enter name: Laura
        Enter phone: 
    Output:
        Error: invalid input
"""

print()
print("                     Problem 6")
print()

#                   CODE

print()
print("              Problem 6")
print()

# Initial dictionary
contacts = {
    "Ana": "8345692059",
    "Luis": "8340685675",
    "Maria": "8341343934",
}

action_text = input("Enter action (ADD / SEARCH / DELETE): ").strip().upper()

# Validate action
if action_text != "ADD" and action_text != "SEARCH" and action_text != "DELETE":
    print("Error: invalid input")
else:
    name = input("Enter name: ").strip().title()

    # Validate name
    if name == "":
        print("Error: invalid input")

    # ADD
    elif action_text == "ADD":
        phone = input("Enter phone: ").strip()

        if phone == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name + ",", phone)

    # SEARCH
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts.get(name))
        else:
            print("Error: contact not found")

    # DELETE
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")

#                           CONCLUSIONS

"""
    Lists are useful when data needs to be modified frequently 
    such as adding or removing elements during program execution. 
    Tuples are better for fixed data that should not change once 
    defined, such as coordinates or constant system configurations.
    Dictionaries allow fast access to data using a key, which makes 
    them ideal for catalogs, contact books, and student records.
    Combining data structures (for example, dictionary of lists) 
    helps organize complex information in a clean and logical way.
    Using only the necessary structure improves performance, 
    readability, and code maintenance. This practice showed the 
    importance of validating input before processing to avoid errors 
    and incorrect data.
"""

#                           REFERENCES
"""
    1) https://www.geeksforgeeks.org/python-data-structures/
    2) https://docs.python.org/3/tutorial/datastructures.html
    3) https://youtu.be/v25-m1LOUiU?si=X6FoD1NaKTtxQbHy
    4) https://docs.python.org/3/library/stdtypes.html
    5) https://youtu.be/CCUNuqqn7PQ?si=K2Z1Qm4nrDu3L9sv
"""