# Write to file
with open("example.txt", "w") as f:  # Fixed: added space before 'as'
    f.write("Hello, world!")

# Read from file and display content
try:
    with open("example.txt", "r") as f:
        content = f.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"Error reading file: {e}")

# Demonstrate additional file operations
print("\nAdditional file operations:")

# Append to file
with open("example.txt", "a") as f:
    f.write("\nThis is an appended line.")

# Read and display updated content
with open("example.txt", "r") as f:
    updated_content = f.read()
    print("Updated file content:")
    print(updated_content)