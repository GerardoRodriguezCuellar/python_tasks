#                               TITLE PAGE
"""
    Title: Handling Loops in Python
    Student name: Gerardo Rodríguez Cuéllar
    Student ID: 2530125
    Group: 1-1
"""

#                           EXECUTIVE SUMMARY

"""
    This document focuses on loop control structures 
    in Python: for and while. A for loop iterates over 
    sequences or ranges when the number of iterations 
    is known. A while loop repeats while a condition 
    remains true and is useful for sentinels and menus.
    Counters track how many times an action runs; 
    accumulators sum values across iterations. Defining 
    clear exit conditions and sentinels avoids infinite 
    loops and makes programs safe. The file contains six 
    problems that practice range(), list traversal, 
    sentinels, menus, and nested loops. Each problem 
    includes description, inputs, outputs, validations, 
    and tests.
"""

#                   PRINCIPLES AND GOOD PRACTICES

"""
    - Use for loops when the number of iterations is known 
    (e.g., for i in range(...)).
    - Use while loops when repetition depends on a condition 
    or a sentinel value.
    - Initialize counters and accumulators before the loop 
    (e.g., count = 0, total = 0).
    - Always update the loop control variable inside a while 
    loop to avoid infinite loops.
    - Validate inputs before starting loops 
    (e.g., n >= 1 for ranges, positive attempt limits).
    - Keep loop bodies simple; extract complex logic if 
    needed to keep code readable.
    - Use break and continue only when they make the logic 
    simpler and are documented.
"""

#                       PROBLEM 1

""" 

    Problem 1: Sum of range with for

    Description:
    This program calculates the sum of all integers from 1 up to n.
    It also calculates the sum of only the even numbers within the same range.
    A for loop with accumulators is used to perform both calculations.

    Inputs:
    - n (int; upper limit of the range).

    Outputs:
    - "Sum 1..n:" <total_sum>
    - "Even sum 1..n:" <even_sum>

    Validations:
    - n must be convertible to int.
    - n must be greater than or equal to 1.
    - If validation fails, display: "Error: invalid input".

    Test cases:
    1) Normal:
    Input: n = 10
    Output:
    Sum 1..n: 55
    Even sum 1..n: 30

    2) Border:
    Input: n = 1
    Output:
    Sum 1..n: 1
    Even sum 1..n: 0

    3) Error:
    Input: n = -5
    Output:
    Error: invalid input
"""

print()
print("                     Problem 1")
print()

#                   CODE

# Iniatilaze accumulators
try:

    # Read Input
    n = int(input("Enter n: "))
    print()

    # Validate Input
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i
            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except ValueError:
    print("Error: invalid input")

print("------------------------------------------------------------------")

#                       PROBLEM 2

"""

    Problem 2: Multiplication table with for

    Description:
    This program prints the multiplication table of a base number
    from 1 up to a limit m using a for loop.

    Inputs:
    - base (int): base number of the table.
    - m (int): upper limit of the table.

    Outputs:
    - One line per multiplication:
      "base x i = result"

    Validations:
    - base and m must be convertible to int.
    - m must be >= 1.

    Test cases:

    1) Normal:
       Input: base = 5, m = 4
       Output:
       5 x 1 = 5
       5 x 2 = 10
       5 x 3 = 15
       5 x 4 = 20

    2) Border:
       Input: base = 7, m = 1
       Output:
       7 x 1 = 7

    3) Error:
       Input: base = 5, m = 0
       Output:
       Error: invalid input
"""

print()
print("                     Problem 2")
print()

#                   CODE

# Read inputs
base_text = input("Enter the base number: ")
m_text = input("Enter the limit: ")
print()

# Validate integers
try:
    base = int(base_text)
    m = int(m_text)

    # Validate range
    if m < 1:
        print("Error: invalid input")
    else:
        # Loop from 1 to m
        for i in range(1, m + 1):
            result = base * i
            print(f"{base} x {i} = {result}")

except ValueError:
    print("Error: invalid input")

print("------------------------------------------------------------------")

#                       PROBLEM 3

"""

    Problem 3: Average of numbers with while and sentinel

    Description:
    This program reads numbers one by one until the user enters
    a sentinel value (-1). It calculates how many valid numbers
    were entered and their average.

    Inputs:
    - number (float): read repeatedly.
    - Sentinel value: -1 (fixed in the code).

    Outputs:
    - "Count:" <count>
    - "Average:" <average>
    - If no valid numbers were entered:
    - "Error: no data"

    Validations:
    - Each input must be convertible to float.
    - The sentinel value is not included in the calculation.

    Test cases:
    1) Normal:
       Inputs: 5, 10, 15, -1
       Output:
       Count: 3
       Average: 10.0

    2) Border:
       Inputs: 7, -1
       Output:
       Count: 1
       Average: 7.0

    3) Error:
       Inputs: -1
       Output:
       Error: no data
"""

print()
print("                     Problem 3")
print()

#                   CODE

SENTINEL_VALUE = -1

total_sum = 0
count = 0

while True:
    number_text = input("Enter a number (-1 to stop): ")

    try:
        number = float(number_text)

        # Check sentinel
        if number == SENTINEL_VALUE:
            break

        # Accumulate values
        total_sum = total_sum + number
        count = count + 1

    except ValueError:
        print("Error: invalid input")

print()

# After loop
if count == 0:
    print("Error: no data")
else:
    average = total_sum / count
    print("Count:", count)
    print("Average:", average)

print("------------------------------------------------------------------")

#                       PROBLEM 4

"""

    Problem 4: Password attempts with while

    Description:
    This program simulates a simple login system using a while loop.
    The user has a limited number of attempts to enter the correct password.

    Inputs:
    - user_password (string): entered on each attempt.

    Outputs:
    - "Login success" if the password is correct.
    - "Account locked" if all attempts are used.

    Validations:
    - MAX_ATTEMPTS must be greater than 0.
    - Attempts are counted correctly.

    Test cases:
    1) Normal:
       Correct password: gera123
       Inputs: gera123
       Output:
       Login success

    2) Border:
       Correct password: gera123
       Inputs: fortnite123, brawl321, gera123
       Output:
       Login success

    3) Error:
       Correct password: gera123
       Inputs: fortnite1, brawl2, minecraft3
       Output:
       Account locked
"""

print()
print("                     Problem 4")
print()


#                   CODE

# Constants
CORRECT_PASSWORD = "gera123"
MAX_ATTEMPTS = 3

attempts = 0

# Loop for attempts
while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")

    if user_password == CORRECT_PASSWORD:
        print()
        print("Login success")
        break
    else:
        attempts = attempts + 1
        print("Wrong password")
        print()

# Check if locked
if attempts == MAX_ATTEMPTS:
    print("Account locked")

print("------------------------------------------------------------------")

#                       PROBLEM 5

"""

    Problem 5: Simple menu with while

    Description:
    This program shows a simple menu using a while loop.
    The program repeats until the user chooses option 0.
    A counter is updated depending on the selected option.

    Inputs:
    - option (int): menu selection.

    Outputs:
    - "Hello!" for greeting.
    - "Counter:" <value> to show counter.
    - "Counter incremented" when adding.
    - "Bye!" when exiting.
    - "Error: invalid option" for wrong options.

    Validations:
    - Option must be convertible to int.
    - Only 0, 1, 2, and 3 are allowed.

    Test cases:
    1) Normal:
       Input: 1, 3, 2, 0
       Output:
       Hello!
       Counter incremented
       Counter: 1
       Bye!

    2) Border:
       Input: 0
       Output:
       Bye!

    3) Error:
       Input: 5, 0
       Output:
       Error: invalid option
       Bye!
"""

print()
print("                     Problem 5")
print()

#                   CODE

counter = 0
option = -1  # Initial value to enter the loop

while option != 0:
    print()
    print("Menu")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    print()

    option_text = input("Option: ")
    print()

    # Validate option
    try:
        option = int(option_text)
    except:
        print("Error: invalid option")
        continue

    # Menu options
    if option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter = counter + 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else:
        print("Error: invalid option")

print("------------------------------------------------------------------")

#                       PROBLEM 6

"""
    Problem 6: Pattern printing with nested loops

    Description:
    This program prints a right triangle pattern using asterisks (*).
    It uses nested for loops to control rows and columns.
    An optional inverted pattern is also printed.

    Inputs:
    - n (int): number of rows.

    Outputs:
    - Triangle pattern line by line.
    - Inverted triangle pattern (optional).

    Validations:
    - n must be convertible to int.
    - n must be >= 1.

        Test cases:

    1) Normal:
       Input: 4
       Output:
       *
       **
       ***
       ****

    2) Border:
       Input: 1
       Output:
       *

    3) Error:
       Input: 0
       Output:
       Error: invalid input
"""

print()
print("                     Problem 6")
print()

#                   CODE

n_text = input("Enter number of rows: ")

# Validate input
try:
    n = int(n_text)
except:
    print()
    print("Error: invalid input")
    exit()

if n < 1:
    print()
    print("Error: invalid input")
    exit()

# Normal pattern
print()
print("Triangle:")
print()
for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line = line + "*"
    print(line)

#                           CONCLUSIONS

"""
    In this task, the use of for and while loops 
    was essential to repeat tasks and control program 
    flow. The for loop was useful when the number of 
    iterations was known, such as ranges, tables, 
    and pattern generation. The while loop was better 
    for situations where repetition depends on a 
    condition, such as menus, password attempts, 
    and sentinel values. Counters and accumulators 
    helped keep track of data like totals, attempts, 
    and number of inputs processed. This practice also 
    showed the importance of validating input to avoid
    infinite loops and incorrect results. Finally, 
    nested loops helped understand how patterns and 
    multi-level repetition work in real programming problems.
"""

#                           REFERENCES
"""
    1) https://www.geeksforgeeks.org/loops-in-python/
    2) https://realpython.com/python-for-loop/
    3) https://youtu.be/0Sk-lmvE0ec?si=LEmzEWpdBiC3If_t
    4) https://docs.python.org/3/tutorial/controlflow.html
    5) https://youtu.be/abKLLfMn-pI?si=3oE0ztC7vmHnbulz
"""