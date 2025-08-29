try:
    with open("example.txt", "w") as f:  # Ensure the file path is correct
        f.write("Hello, world!")
    print("File written successfully.")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")