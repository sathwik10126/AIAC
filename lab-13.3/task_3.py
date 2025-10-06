class Student:
    """
    A class to represent a student with their details and marks.
    Attributes:
    -----------
    name : str
        The name of the student.
    age : int
        The age of the student.
    marks : list
        A list of marks obtained by the student.
    Methods:
    --------
    details():
        Prints the student's name and age.
    total_marks():
        Returns the total marks obtained by the student.
    average_marks():
        Returns the average marks obtained by the student.
    """
    def __init__(self, name, age, marks):
        """
        Initialize a Student object.

        Parameters:
        -----------
        name : str
            The name of the student.
        age : int
            The age of the student.
        marks : list
            A list of marks obtained by the student.
        """
        self.name = name
        self.age = age
        self.marks = marks
    def details(self):
        """Print the student's name and age."""
        print(f"Name: {self.name}, Age: {self.age}")

    def total_marks(self):
        """Calculate and return the total marks."""
        return sum(self.marks)
    def average_marks(self):
        """Calculate and return the average marks."""
        return sum(self.marks) / len(self.marks)
# Example usage
if __name__ == "__main__":
    # Create a Student object
    student = Student("Alice", 20, [85, 90, 78])
    # Print student details
    student.details()
    # Print total and average marks
    print(f"Total Marks: {student.total_marks()}")
    print(f"Average Marks: {student.average_marks():.2f}")