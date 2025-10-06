import math
def calculate_rectangle_area(x, y):
    """Calculate the area of a rectangle."""
    return x * y
def calculate_square_area(x, _):
    """Calculate the area of a square."""
    return x * x
def calculate_circle_area(x, _):
    """Calculate the area of a circle."""
    return math.pi * x * x
def calculate_area(shape, x, y=0):
    """
    Calculate the area of a given shape.

    Parameters:
    -----------
    shape : str
        The type of shape ("rectangle", "square", "circle").
    x : float
        The first dimension (e.g., side length, radius).
    y : float, optional
        The second dimension (e.g., height for a rectangle). Default is 0.

    Returns:
    --------
    float
        The calculated area of the shape.

    Raises:
    -------
    ValueError
        If the shape is not supported.
    """
    area_calculators = {
        "rectangle": calculate_rectangle_area,
        "square": calculate_square_area,
        "circle": calculate_circle_area
    }
    if shape not in area_calculators:
        raise ValueError(f"Unsupported shape: {shape}")
    return area_calculators[shape](x, y)
if __name__ == "__main__":
    print(calculate_area("rectangle", 5, 10))
    print(calculate_area("square", 4))      
    print(calculate_area("circle", 3))