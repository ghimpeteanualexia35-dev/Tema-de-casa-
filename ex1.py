class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

    def add_task(self, task_name):
        self.tasks[task_name] = "New"   

    def update_tasks(self, task_name, status):
        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgrCount = 0
    
    def __init__(self, name, salary, tasks, department):
        self.tasks=tasks
        self.department="F25" + department
        super().__init__(name, salary)
        Manager.mgrCount += 1

    X=16;
    Y=11;

    def display_employee(self):
       if Manager.X % 4 == 0:
         print("Salary : ", self.salary)

       elif Manager.X % 4 == 1:
         print("Name : ", self.name)

       elif Manager.X % 4 == 2:
         print("Department : ", self.department)

       elif Manager.X % 4 == 3:
         print ("Tasks : ", self.tasks)

employees = [
    Employee("Maria", 3200),
    Employee("Miruna", 3700),
    Employee("Madalin", 3000),
    Employee("Tudor", 4800),
    Employee("Eveline", 5200),
    Employee("Maria", 3400)
]


managers=[
    Manager("M1", 9100, {"Coordonation" : "Ongoing"}, "HR"),
    Manager("M2", 8700, {"Coding" : "New"}, "Logistics"),
    Manager("M3", 7800, {"Publishing" : "Finished"}, "Marketing")
]

n=len(managers)
N=len(employees)

for i in range(N):
    employees[i].display_employee()

for i in range(n):
    managers[i].display_employee()


print("Number of employees = ", Employee.empCount)
print("Number of Managers = ", Manager.mgrCount)
