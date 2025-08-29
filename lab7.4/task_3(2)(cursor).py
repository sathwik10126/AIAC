# Method 1: Using with statements (recommended approach)
print("Writing files using with statements:")
with open("data1.txt", "w") as f1:
    f1.write("First file content\n")
    f1.write("Additional line in first file\n")

with open("data2.txt", "w") as f2:
    f2.write("Second file content\n")
    f2.write("Additional line in second file\n")

print("Files written successfully using with statements")

# Method 2: Using explicit close() (alternative approach)
print("\nWriting files using explicit close():")
try:
    f1 = open("data3.txt", "w")
    f2 = open("data4.txt", "w")
    
    f1.write("Third file content\n")
    f2.write("Fourth file content\n")
    
    print("Files written successfully using explicit close()")
    
except Exception as e:
    print(f"Error writing files: {e}")
    
finally:
    # Always close files, even if an error occurs
    if 'f1' in locals():
        f1.close()
    if 'f2' in locals():
        f2.close()

# Read and display the content of the files
print("\nReading and displaying file contents:")
try:
    with open("data1.txt", "r") as f:
        content1 = f.read()
        print("Content of data1.txt:")
        print(content1)
        
    with open("data2.txt", "r") as f:
        content2 = f.read()
        print("Content of data2.txt:")
        print(content2)
        
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"Error reading files: {e}")