"""
Find PI to the Nth Digit -
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
"""
# The decimal module provides support for fast correctly rounded decimal floating point arithmetic
from decimal import Decimal, getcontext


def find_pi():
    """
    Function to find pi, which used Bailey-Borwein-Plouffe formula.
    Limit of precition set to 1001.
    For loop with range 1000 will give more accurate result of PI
    """
    getcontext().prec = 1001
    num_pi = Decimal(0)
    for k in range(1000):
        first_part = 1/pow(Decimal(16), k)
        num_pi_bbp = first_part*((4/(8*k+Decimal(1))) - (2/(8*k+Decimal(4))) -
                                 (1/(8*k+Decimal(5))) - (1/(8*k+Decimal(6))))
        num_pi += num_pi_bbp

    return num_pi


def nth_digit():
    """
    Function to get non-negative integer as nth digit, which greater then 0 and within limit 1000.
    """
    while True:
        try:
            decim_places = int(input(
                """
            \rGet result of PI up to that many decimal places. Limit is 1000.
            \rPlease enter a non-negative integer number.
            \rHow many decimal places? : """))
            if 0 < decim_places <= 1000:
                return decim_places
            print("\nMore than limit, equal to 0 or negative")
            continue
        except ValueError:
            print("\nError. Please use nonnegative integer numbers")
            continue


# Data type of find_pi function will convert into string.
# Slicing will help to get as many decimal places as asked in nth_digit function.
# First two symbols will always print.

PROGRESS = "y"
while PROGRESS == "y":
    print(str(find_pi())[:(nth_digit() + 2)])
    while True:
        PROGRESS = input("\nContinue? y/n ")
        if PROGRESS.lower() == "n" or PROGRESS.lower() == "y":
            break
        print("\nError. Please use letters 'y' for yes and 'n' for no")
