def is_valid_indian_mobile(number: str) -> bool:
    """
    Validates if the input string is a valid Indian mobile number.
    Criteria:
    - Starts with 6, 7, 8, or 9
    - Contains exactly 10 digits
    """
    return number.isdigit() and len(number) == 10 and number[0] in '6789'

# Example usage:
user_input = input("Enter mobile number: ")
if is_valid_indian_mobile(user_input):
    print("Valid Indian mobile number.")
else:
    print("Invalid mobile number.")