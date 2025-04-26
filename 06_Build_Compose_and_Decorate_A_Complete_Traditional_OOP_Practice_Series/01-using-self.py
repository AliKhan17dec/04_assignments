class Student:
    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)    

student1 = Student("Ali", 87)
student1.display()

student2 = Student("Muneeb", 92)
student2.display()