def area_of_rect(length: float, breadth: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        breadth (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If length or breadth is negative.
    """
    if length < 0 or breadth < 0:
        raise ValueError("Length and breadth must be non-negative.")
    return length * breadth

# Example usage
length = 10
breadth = 20
print(f"The area of the rectangle with length {length} and breadth {breadth} is {area_of_rect(length, breadth)}.")

