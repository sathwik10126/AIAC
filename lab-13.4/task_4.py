def perform_operation(operation, a, b):
    """
    Perform a mathematical operation based on the given operation string.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply").
        a (int or float): The first operand.
        b (int or float): The second operand.

    Returns:
        int, float, or None: The result of the operation, or None if the operation is invalid.
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
    }
    return operations.get(operation, lambda x, y: None)(a, b)

# Example usage
operation = "multiply"
a, b = 5, 3
result = perform_operation(operation, a, b)
print(result)