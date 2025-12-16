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

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, tasks, department):
        super().__init__(name, salary)
        self.tasks = tasks
        self.department = f"F03_{department}"

        Manager.mgr_count += 1

    def display_employee(self):
        print(self.name)

e1 = Employee("Alex Pop", 4500)
e2 = Employee("Ana Oancea", 5000)

tasks_m1 = {"Raport lunar": "In progress", "Ședință echipă": "New"}
tasks_m2 = {"Plan buget": "New", "Evaluare performanță": "New"}

m1 = Manager("George Mihai", 5500, tasks_m1, "Financiar")
m2 = Manager("Anca Anghel", 6500, tasks_m2, "IT")

print("Employee:")
e1.display_employee()
e2.display_employee()

print("\nManager:")
m1.display_employee()
m2.display_employee()

print("\nContoare de clasă:")
print("empCount din Employee:", e1.empCount)
print("mgr_count din Manager:", m1.mgr_count)
#x=9 y=8
#x%4=1=>suprascrierea metodei display_employee astfel încât obiectele de tip Manager să afișeze doar numele angajatului.
