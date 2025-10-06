nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calculate_squares(numbers):
    """
    Calculate the squares of a list of numbers.

    Parameters:
    -----------
    numbers : list
        A list of integers.

    Returns:
    --------
    list
        A list containing the squares of the input numbers.
    """
    return [i * i for i in numbers]

# Calculate squares of the numbers
squares = calculate_squares(nums)

# Print the result
print(squares)