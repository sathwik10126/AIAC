def calculate_squares(numbers):
    """
    Calculate the square of each number in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list containing the squares of the input integers.
    """
    return [n ** 2 for n in numbers]

# Example usage
numbers = [1, 2, 3, 4, 5]
squares = calculate_squares(numbers)
print(squares)