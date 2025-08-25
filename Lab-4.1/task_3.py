# Program to parse nested dictionary and extract student information

# Take user input
first_name = input("first name: ")
last_name = input("Last name: ")
branch = input("Branch: ")
sgpa = input("SGPA: ")

# Create nested dictionary
student_info = {
    "name": {
        "first": first_name,
        "last": last_name
    },
    "details": {
        "branch": branch,
        "sgpa": sgpa
    }
}

# Extract required information
full_name = student_info["name"]["first"] + " " + student_info["name"]["last"]
branch = student_info["details"]["branch"]
sgpa = student_info["details"]["sgpa"]

# Display output
print("student information:")
print(f"Full name: {full_name}")
print(f"Branch: {branch}")
print(f"SGPA: {sgpa}")