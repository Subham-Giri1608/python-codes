from icecream import ic

class Student:
    new = []  # List to store all student instances

    def __init__(self, id, name, marks, dept):
        self.id = id
        self.name = name
        self.marks = marks
        self.dept = dept
        Student.new.append(self)  # Append instance to class-level list

    @staticmethod
    def user():
        new_id = int(input("Enter your ID: ")) 
        new_name = str(input("Enter your Name: "))
        new_marks = int(input("Enter your Marks: "))
        new_dept = str(input("Enter your Department: "))

        # Check if the student already exists
        for student in Student.new:
            if student.id == new_id and student.name == new_name:
                print("User Already Exists!")
                return

        # Create a new student if not found
        Student(new_id, new_name, new_marks, new_dept)
        print("New Student Added Successfully!")

# Collect a new student's details
Student.user()

# Print all students in the `Student.new` list
print("\nList of Students:")
for s in Student.new:
    print(f"ID: {s.id}, Name: {s.name}, Marks: {s.marks}, Department: {s.dept}")
