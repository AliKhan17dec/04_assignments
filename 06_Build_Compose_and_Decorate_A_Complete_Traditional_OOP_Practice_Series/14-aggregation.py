class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: using an existing Employee object

    def show_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.show()  # Accessing Employee method

# Creating an Employee independently
emp = Employee("Ayesha")

# Aggregating Employee into Department
dept = Department("HR", emp)

# Showing info
dept.show_department()
