from cgi import print_arguments
from tkinter.tix import DECREASING

class Employee:
    def _init_(self,name,desig, dept, salary, skills = None):
        self.name = name
        self.designation = desig
        self.department = dept
        self.salary = salary
        self.skills = skills

    def do_task(self, task):
        print(f"Employee{self.name}is doing task {task}")

    def info(self):
        print("EMPLOYEE DETAILS")
        print(f"Name:{self.name}")
        print(f"Department: {self.department}")
        print(f"Designation: {self.designation}")
        print(f"Salary:{self.salary}")
        print(f"skills:{", ".join(self.skills)}")
    
    def add_skills(self, skillname):
        if self.skills is None:
            self.skills = [skillname]
        else:
            self.skills.append(skillname)

e1 = Employee("Raj", "Assistant 2", "Sales", 40000, ["Talking"])
e2 = Employee("Sonu", "Staff officer", "Finance", 70000, ["management", "leadership"])

e1.info()
e2.info()
e1.do_task("Masking some sales")
e2.do_task("Firing employees")
e1.add_skills("")

        