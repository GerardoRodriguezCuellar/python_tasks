#                               TITLE PAGE
"""
    Student name: Gerardo Rodríguez Cuéllar 
    Student ID: 2530125
    Group: 1-1
    GitHub repository URL: 
"""

#                           EXECUTIVE SUMMARY

"""
    This Python script contains six small programs designed to exercise and
    demonstrate common string operations in Python. A string in Python is a
    text sequence type (str) which is immutable: every transformation returns a
    new string rather than modifying the original. The problems cover creating,
    indexing, slicing, concatenation, searching, replacing, splitting, joining
    and formatting text. The assignment also emphasizes input validation and
    normalization (strip(), lower(), title(), etc.) to avoid common user-input
    errors. Each problem includes a description, specified inputs and outputs,
    validation rules, and three concrete test cases (normal, border, error).
"""

#                   PRINCIPLES AND GOOD PRACTICES

"""
    - Strings are immutable: operations produce new strings; 
        avoid assuming in-place modification.
    - Always normalize input using strip() and, when appropriate, 
        lower() or title() before comparing or processing.
    - Avoid magic numbers in slices; comment what each slice extracts.
    - Prefer built-in string methods (replace, split, join, startswith) 
        over re-implementing low-level logic.
    - Validation order: first ensure input is not empty after strip(), 
        then check format-specific rules (e.g., email structure, numeric price).
    - Use descriptive variable names in lower_snake_case and clear 
        English output messages (e.g., "Error: invalid input").
"""

#                       PROBLEM 1

""" 
    Problem 1: Full name formatter (name + initials)

    Description: Given a person's full name in a single 
    string (e.g., "juan carlos tovar"), the program should:

    1) Normalize the text (strips, extra spaces, uppercase/lowercase).

    2) Display the formatted name in a Title Case and the initials 
    (e.g., J.C.T.).

    Inputs:
    - full_name (string)

    Outputs:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"

    Validations:
    - full_name must not be empty after strip().
    - Must contain at least two words.
    - Input must not be only spaces.

    Test cases:
    1) Normal: "juan carlos tovar"
    2) Border: "Ana Maria"
    3) Error: " " (only spaces)
"""

print()
print("                     Problem 1")
print()

#                   CODE

# CONVERT TO STRING 
full_name = str(input("Enter your name and last name:"))

# ELIMINATE THE WHITESPACES AND VALIDATE 
cleaned_name = full_name.strip()
if cleaned_name == "":
    print("Error: invalid input (empty name)")
    exit()

# SEPARATE THE WORDS AND VALIDATE 
parts = cleaned_name.split()
if len(parts) < 2:
    print("Error: invalid input (need at least two words)")
    exit()

title_name = cleaned_name.title()
# GENERATE THE INITIALS 
initials = "".join([p[0].upper() + "." for p in parts])

print(f"Formatted name: {title_name}")
print(f"Initials: {initials}")

print("------------------------------------------------------------------")

#                       PROBLEM 2

"""
    Problem 2: Simple email validator (structure + domain)

    Description:
    Validate whether an email address has a basic correct structure:
    - Contains exactly one '@'.
    - After '@' there must be at least one '.'.
    - Must not contain spaces.
    If valid, print the domain part.

    Inputs:
    - email_text (string)

    Outputs:
    - "Valid email: true" or "Valid email: false"
    - If valid: "Domain: <domain_part>"

    Validations:
    - email_text must not be empty after strip().
    - Email must contain exactly one '@'.
    - Must not contain blank spaces.
    - After '@' there must be at least one '.'.

    Test cases:
    1) Normal: "tilinsito@email.com"
    2) Border: "a@b.co"
    3) Error: "tilinsito@@mail.com" (two '@')
"""

print()
print("                     Problem 2")
print()

#                   CODE

# Convert to string
email_text = str(input("Enter your email:"))

# Eliminate the whiteespaces
email_text_cleaned = email_text.strip()

# Validate Email
if email_text_cleaned == "":
    print("Valid email: false")
    exit() 

# Validate Email
if " " in email_text_cleaned:
    print("Valid email: false")
    exit()

# Count '@'
if email_text_cleaned.count('@') != 1:
    print("Valid email: false")
    exit()

# Extract domain part
at_index = email_text_cleaned.find('@')
domain = email_text_cleaned[at_index + 1:]

# Domain must contain '.'
if '.' not in domain:
    print("Valid email: false")
    exit()

# If everything is good
print("Valid email: true")
print(f"Domain: {domain}")

print("------------------------------------------------------------------")

#                       PROBLEM 3

"""
    Problem 3: Palindrome checker (ignoring spaces and case)

    Description:
    Determines whether a phrase is a palindrome by comparing it to its reversed
    version, ignoring spaces and case.

    Inputs:
    - phrase (string)

    Outputs:
    - "Is palindrome: true" or "Is palindrome: false"
    - Optional: print the normalized phrase

    Validations:
    - phrase must not be empty after strip().
    - After removing spaces, length must be >= 3.

    Test cases:
    1) Normal: "Yo hago yoga hoy"
    2) Border: "Aba"
    3) Error: " " (only spaces)
"""

print()
print("                     Problem 3")
print()

#                   CODE

# Convert to string
phrase = str(input("Enter the phrase:"))

# Eliminate whitespaces
phrase_cleaned = phrase.strip()

# Validate empty
if phrase_cleaned == "":
    print("Is palindrome: false")
    exit()

# Normalize: remove spaces and lowercase
normalized = phrase_cleaned.replace(" ", "").lower()

# Validate length
if len(normalized) < 3:
    print("Is palindrome: false")
    exit()

# Reverse string using slicing
reversed_text = normalized[::-1]

if normalized == reversed_text:
    print("Is palindrome: true")
else:
    print("Is palindrome: false")

print("------------------------------------------------------------------")

#                       PROBLEM 4

"""
    Problem 4: Sentence word stats (lengths and first/last word)

    Description:
    Given a sentence, the program normalizes whitespace, splits words by spaces,
    and prints statistics: total number of words, first word, last word,
    shortest word and longest word (by length).

    Inputs:
    - sentence (string)

    Outputs:
    - "Word count: <n>"
    - "First word: <...>"
    - "Last word: <...>"
    - "Shortest word: <...>"
    - "Longest word: <...>"

    Validations:
    - sentence must not be empty after strip().
    - After splitting, there must be at least one valid word.

    Test cases:
    1) Normal: "  This is an example sentence.  "
    2) Border: "Star"  (single-word sentence)
    3) Error: "    "    (only spaces)
"""

print()
print("                     Problem 4")
print()

#                   CODE

# Convert to string 
sentence = str(input("Enter a sentence:"))

# Eliminate whitespaces
sentence_cleaned = sentence.strip()

# Validate empty
if sentence_cleaned == "":
    print("Error: invalid input")
    exit()

# Split into words
words = sentence_cleaned.split()

# Validation: at least one valid word
if not words:
    print("Error: invalid input")
    exit()

# Word count
word_count = len(words)

# First and last word (preserve original case)
first_word = words[0]
last_word = words[-1]

# Shortest and longest by length (if ties, first occurrence is chosen)
shortest_word = min(words, key=len)
longest_word = max(words, key=len)

# Outputs (messages in English as required)
print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")

print("------------------------------------------------------------------")

#                       PROBLEM 5

"""
    Problem 5: Password strength classifier

    Description:
    Classifies a password as weak, medium, or strong based on simple rules
    regarding length and the presence of different character types.

    Inputs:
    - password_input (string)

    Outputs:
    - "Password strength: weak"
    - "Password strength: medium"
    - "Password strength: strong"

    Validations:
    - password_input must not be empty after strip().
    - Length must be checked using len().

    Test cases:
    1) Normal: "Primobs12345!@" → strong
    2) Border: "Primobs12345" → medium
    3) Error: "" (empty string)
"""

print()
print("                     Problem 5")
print()

#                   CODE

# Convert to string 
password_input = str(input("Enter a password:"))

# Normalize input
cleaned_password = password_input.strip()

# Validation: not empty
if cleaned_password == "":
    print("Error: invalid input")
    exit()

# Flags for character types
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

# Check each character
for char in cleaned_password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_symbol = True

length = len(cleaned_password)

# Strength classification rules
if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
    strength = "strong"
elif length >= 8 and (has_upper or has_lower) and has_digit:
    strength = "medium"
else:
    strength = "weak"

# Output
print(f"Password strength: {strength}")

print("------------------------------------------------------------------")

#                       PROBLEM 6

"""
    Problem 6: Product label formatter (fixed-width text)

    Description:
    Generates a single-line product label with a fixed width of exactly
    30 characters. If the label is shorter, it is padded with spaces.
    If it is longer, it is truncated.

    Inputs:
    - product_name (string)
    - price_value (string or number)

    Outputs:
    - "Label: <exactly 30 characters>"

    Validations:
    - product_name must not be empty after strip().
    - price_value must be convertible to a positive number.

    Test cases:
    1) Normal: ("Notebook", 25)
    2) Border: ("A", 0.01)
    3) Error: ("", "abc")
"""

print()
print("                     Problem 6")
print()

#                   CODE

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

#                           CONCLUSIONS

"""
    Working with strings is essential for handling user input 
    and producing clear output in programs.Methods like strip(), 
    lower(), split(), and join() help clean and organize text 
    efficiently.Normalizing text before comparing prevents errors 
    caused by extra spaces or different letter cases.Proper input 
    validation avoids processing incorrect data and reduces unexpected 
    crashes. This work showed how strings are immutable, meaning 
    every modification creates a new string. Slicing is a powerful 
    way to extract specific parts of text with precision and clarity.
    Overall, mastering string operations improves the reliability 
    and readability of programs.
"""

#                           REFERENCES

"""
    1) https://ellibrodepython.com/cadenas-python
    2) https://www.youtube.com/watch?v=Ctqi5Y4X-jA
    3) https://www.geeksforgeeks.org/python/python-string/
    4) https://www.youtube.com/watch?v=8tuyYql2duA
    5) https://www.programiz.com/python-programming/string
"""

