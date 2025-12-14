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
        print("Name : ", self.name)

    def _del_ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

    def add_task(self, task_name):
        self.tasks[task_name] = "New"   # needs tasks defined before (in _init_)

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
    mgr_count = 0

    def __init__(self, name, salary, tasks, department):
        super().__init__(name, salary)
        self.tasks = tasks
        self.department = "F03" + department
        Manager.mgr_count += 1

    def display_mgr_count(self):
        print(f"Total number of manager(s) is {Manager.mgr_count}")

manager1 = Manager( "Lazar Andu", 40000, {"Rezolva Tickete" : "In Lucru"}, "Backend Devs Team" )
employee1 = Employee( "Cibea Anya", 500)

print("\nNumele Managerului prin apelarea metodei display_employee")
manager1.display_employee()

print("\nNumele Angajatului prin apelarea metodei display_employee")
employee1.display_employee()

print("\nValoarea atributului empCount pentru o instanta a clasei \nEmployee")
manager1.display_emp_count()

print("\nValoarea atributului empCount pentru o instanta a clasei \nManager")
employee1.display_emp_count()

print("\nValoarea atributului mgr_count")
manager1.display_mgr_count()

# X = 13
# Y = 5 
# X % 4 = 1
# Y / 3 = 1