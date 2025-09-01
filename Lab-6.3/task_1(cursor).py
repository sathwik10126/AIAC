class student:
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
name =input("enter the student's name:")
rollno =int(input("enter the student's roll number:"))
marks =float(input("enter the student's marks:"))
student1 = student(name, rollno, marks)
student1.display()
print("Grade:", student1.calculate_grade())