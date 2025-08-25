def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(n, 0, -1):
            result *= i
        return result

def show_factorial_calculation(n):
    """Show the factorial calculation process"""
    if n == 0 or n == 1:
        return f"{n}! = 1"
    else:
        calculation = " * ".join(str(i) for i in range(n, 0, -1))
        return f"{n}! = {calculation} = {factorial(n)}"

# Main program
print("Factorial Calculator")
print("Enter 'quit' to exit")

while True:
    try:
        user_input = input("Enter a number: ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if not user_input:
            print("Please enter a number.")
            continue
            
        number = int(user_input)
        
        # Show calculation process
        print(show_factorial_calculation(number))
        
        # Show result
        result = factorial(number)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {result}")
            
        print("-" * 40)
        
    except ValueError:
        print("Error: Please enter a valid integer")
    except KeyboardInterrupt:
        print("\nExiting...")
        break

print("Thank you!")
