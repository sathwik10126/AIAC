# First, create a sample numbers file for testing
print("Creating sample numbers file...")
with open("numbers.txt", "w") as f:
    f.write("5\n")
    f.write("3\n")
    f.write("7\n")
    f.write("2\n")
    f.write("10\n")
    f.write("abc\n")  # Non-numeric to test filtering
    f.write("4\n")

print("Sample numbers file created successfully!")

# Method 1: Using with statements (recommended approach)
print("\nProcessing numbers using with statements:")
try:
    with open("numbers.txt", "r") as f:
        nums = f.readlines()  # Fixed: added assignment operator
    
    squares = []  # Fixed: added assignment operator
    for n in nums:
        n = n.strip()  # Fixed: added assignment operator
        if n.isdigit():
            squares.append(int(n) * int(n))  # Fixed: changed to multiplication
    
    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")
    
    print("Squares written successfully using with statements")  # Fixed: changed int() to print()
    
except FileNotFoundError:
    print("Error: numbers.txt file not found!")
except Exception as e:
    print(f"Error processing files: {e}")

# Method 2: Using explicit close() (alternative approach)
print("\nProcessing numbers using explicit close():")
try:
    f = open("numbers.txt", "r")
    nums = f.readlines()
    f.close()
    
    squares = []
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))
    
    f2 = open("squares2.txt", "w")
    for sq in squares:
        f2.write(str(sq) + "\n")
    f2.close()
    
    print("Squares written successfully using explicit close()")
    
except FileNotFoundError:
    print("Error: numbers.txt file not found!")
except Exception as e:
    print(f"Error processing files: {e}")
finally:
    # Ensure files are closed even if an error occurs
    if 'f' in locals() and not f.closed:
        f.close()
    if 'f2' in locals() and not f2.closed:
        f2.close()

# Read and display the results
print("\nReading and displaying results:")
try:
    print("Original numbers file content:")
    with open("numbers.txt", "r") as f:
        print(f.read())
    
    print("Squares file content:")
    with open("squares.txt", "r") as f:
        print(f.read())
        
    print("Squares2 file content:")
    with open("squares2.txt", "r") as f:
        print(f.read())
        
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"Error reading files: {e}")

# Show the calculation process
print("\nCalculation process:")
with open("numbers.txt", "r") as f:
    nums = f.readlines()
    for n in nums:
        n = n.strip()
        if n.isdigit():
            num = int(n)
            square = num * num
            print(f"{num}² = {square}")
        else:
            print(f"'{n}' is not a valid number, skipping...")
