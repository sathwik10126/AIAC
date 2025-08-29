# First, create a sample input file for testing
print("Creating sample input file...")
with open("input.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python Programming\n")
    f.write("File Processing Example\n")
    f.write("Convert to Uppercase\n")

print("Sample input file created successfully!")

# Method 1: Using with statements (recommended approach)
print("\nProcessing files using with statements:")
try:
    with open("input.txt", "r") as input_file:
        data = input_file.readlines()
    
    with open("output.txt", "w") as output_file:
        for line in data:
            output_file.write(line.upper())
    
    print("Processing done using with statements")
    
except FileNotFoundError:
    print("Error: input.txt file not found!")
except Exception as e:
    print(f"Error processing files: {e}")

# Method 2: Using explicit close() (alternative approach)
print("\nProcessing files using explicit close():")
try:
    input_file = open("input.txt", "r")
    data = input_file.readlines()
    input_file.close()
    
    output_file = open("output2.txt", "w")
    for line in data:
        output_file.write(line.upper())
    output_file.close()
    
    print("Processing done using explicit close()")
    
except FileNotFoundError:
    print("Error: input.txt file not found!")
except Exception as e:
    print(f"Error processing files: {e}")
finally:
    # Ensure files are closed even if an error occurs
    if 'input_file' in locals() and not input_file.closed:
        input_file.close()
    if 'output_file' in locals() and not output_file.closed:
        output_file.close()

# Read and display the results
print("\nReading and displaying results:")
try:
    print("Original input file content:")
    with open("input.txt", "r") as f:
        print(f.read())
    
    print("\nOutput file content (uppercase):")
    with open("output.txt", "r") as f:
        print(f.read())
        
    print("\nOutput2 file content (uppercase):")
    with open("output2.txt", "r") as f:
        print(f.read())
        
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"Error reading files: {e}")