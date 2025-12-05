#                               TITLE PAGE
"""
    Title: Fibonacci Series with Python
    Student name: Gerardo Rodríguez Cuéllar
    Student ID: 2530125
    Group: 1-1
"""

#                           EXECUTIVE SUMMARY

"""
    The Fibonacci series is a numerical sequence 
    where each term is the sum of the two previous
    ones, starting with 0 and 1. This program reads 
    an integer n, validates it, and generates the 
    first n Fibonacci terms using a loop structure.
    It ensures correct handling of special cases 
    such as n = 1 or n = 2 and enforces proper 
    input validation before any computation. The 
    goal is to practice loops, variable handling, 
    and clean output formatting in Python.
"""

#                       PROBLEM FIBONACCI

""" 
    Description:
    This program reads an integer n from the user and 
    generates the first n terms of the Fibonacci series, 
    starting at 0 and 1. The program must validate the
    input before processing. The output should print 
    all terms on a single line, separated by spaces. 
    If n = 1, the output is only "0". If n = 2, the output
    is "0 1". For any n >= 3, the program continues the 
    sequence normally.

    Inputs:
    - n (int; number of terms that the user wants to generate)

    Outputs:
    - "Fibonacci series: <term_1> <term_2> ... <term_n>"
    - In case of invalid input:
      "Error: invalid input"

    Validations:
    - n must be convertible to an integer.
    - n must be >= 1.
    - Optional limit: n must be <= 50 to avoid excessive output.
    - If validation fails, the program must NOT calculate the series.

    Test cases:
    1) Normal case:
          Input: n = 7
          Expected output:
          Fibonacci series: 0 1 1 2 3 5 8

    2) Border case:
          Input: n = 1
          Expected output:
          Fibonacci series: 0

    3) Error case:
          Input: n = -4
          Expected output:
          Error: invalid input
    """

print()
print("                     Fibonacci")
print()

#                   CODE

try:
    n = int(input("How many terms: "))
    first_number, second_number, count_1 = 0, 1, 0
    if n >= 1 and n <= 50:
        print("Fibonacci series:", end=" ")
        while count_1 < n:
            print(first_number, end=" ")
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number
            count_1 = count_1 + 1
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")

print()

#                           CONCLUSIONS

"""
    This program helped me understand how loops 
    can be used to generate number sequences.
    Special cases such as n = 1 and n = 2 are 
    important because they change how the program 
    behaves. Input validation is essential to 
    avoid runtime errors. The Fibonacci logic 
    can be reused in mathematical programs, 
    games, or problem-solving tasks.
"""

#                           REFERENCES
"""
    1) https://www.programiz.com/python-programming/examples/fibonacci-sequence
    2) https://www.w3schools.com/python/python_while_loops.asp
    3) https://realpython.com/fibonacci-sequence-python/
    4) https://docs.python.org/3/tutorial/controlflow.html
"""