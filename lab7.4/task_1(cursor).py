def factr(n):
    # Convert string to integer if needed
    if isinstance(n, str):
        n = int(n)
    
    # Handle negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    else:
        return n * factr(n - 1)

print(factr("5"))