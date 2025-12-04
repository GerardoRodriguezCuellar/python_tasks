#                               TITLE PAGE
"""
    Title: Fibonacci Series with Python
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

try:
    n = int(input("How many terms: "))
    first_number, second_number, count_1 = 0, 1, 0
    if n>=1 and n<=50:
        while n >= count_1:
            print(f"{first_number}, {second_number}")
            first_number = first_number + second_number
            second_number = first_number + second_number
            count_1 = count_1 + 1
except ValueError:
    print("Error Invalid Input")