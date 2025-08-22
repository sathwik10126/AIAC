# Define a Student class to encapsulate student-related data and behavior
class Student:
    def __init__(self, name, roll_no, marks):
        # Initialize instance variables with the provided values
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_details(self):
        # Print the student's details in a readable format
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")
# Helper to read an integer from the user with validation

def read_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")
 # Helper to read a float from the user with validation
def read_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

# Main loop to collect multiple students and display them
def main():
    students = []  # List to store Student objects
    while True:
        # Collect user-defined inputs for a single student
        name = input("Enter student name: ").strip()
        roll_no = read_int("Enter roll number: ")
        marks = read_float("Enter marks: ")
        # Create a Student instance and store it
        students.append(Student(name, roll_no, marks))
        # Ask whether to continue adding more students
        cont = input("Add another student? (y/n): ").strip().lower()
        if cont not in ("y", "yes"):
            break
    # Display details for all added students
    print("\nStudent Details:")
    for student in students:
        student.display_details()
# Entry point guard
if __name__ == "__main__":
    main()

