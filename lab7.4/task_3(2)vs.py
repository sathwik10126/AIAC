try:
    with open("data1.txt", "w") as f1, open("data2.txt", "w") as f2:
        f1.write("First file content\n")
        f2.write("Second file content\n")
    print("Files written successfully.")
except IOError as e:
    print(f"An error occurred while writing to the files: {e}")