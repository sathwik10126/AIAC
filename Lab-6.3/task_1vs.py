class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)

    def calculate_grade(self):
        if self.marks >= 90:
            grade = 'A'
        elif self.marks >= 75:
            grade = 'B'
        elif self.marks >= 60:
            grade = 'C'
        else:
            grade = 'Fail'
        return grade

# Taking user input
name = input("Enter the student's name: ")
rollno = int(input("Enter the student's roll number: "))
marks = float(input("Enter the student's marks: "))

# Creating a student object
student1 = Student(name, rollno, marks)

# Displaying details and grade
student1.display()
print("Grade:", student1.calculate_grade())