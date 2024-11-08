#!/usr/bin/env python3

def calculate_sum_of_squares(num_integers):
    """
    the sum of squares of positive integers in a given number of inputs.

    Args:
        num_integers: The number of integers to read.

    Returns:
        The sum of squares of positive integers.
    """

    sum_of_squares = 0
    numbers = input().split()
    #if len(numbers) < num_integers:
        #raise ValueError("Not enough numbers provided")
    for i in range(num_integers):
        number = int(numbers[i])
        if number > 0:
            sum_of_squares += number * number
    return sum_of_squares


def main():
    num_test_cases = int(input().strip())
    for _ in range(num_test_cases):
        num_integers = int(input().strip())
        result = calculate_sum_of_squares(num_integers)
        print(result)  # Print each result on a new line


if __name__ == "__main__":
    main()
