def sum(num):
    """
    Calculates the sum of even and odd numbers in a given list.

    Args:
        num (list of int): List of integers to be processed.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.
    """
    e= 0
    o = 0
    for i in num:
        if i % 2 == 0:
            e=e+i
        else:
            o=o+i
    return e,o
num = list(map(int, input("Enter numbers: ").split()))
e, o = sum(num)
print("Sum of even numbers:", e)
print("Sum of odd numbers:", o)
