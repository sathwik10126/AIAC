def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
try:
    num = 5  # Ensure the input is an integer
    print(factorial(num))
except ValueError as e:
    print(e)