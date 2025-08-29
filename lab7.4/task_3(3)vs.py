try:
    # Open the input file and read lines
    with open("input.txt", "r") as input_file:
        data = input_file.readlines()
    
    # Open the output file and write uppercase lines
    with open("output.txt", "w") as output_file:
        for line in data:
            output_file.write(line.upper())
    
    print("Processing done")
except IOError as e:
    print(f"An error occurred while processing the files: {e}")