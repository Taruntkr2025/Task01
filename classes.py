#Classes myclass:
# pass

class employee():

    def __init__(self,name,salary):
        self.empName=name
        self.empSalary=salary
        

    def get_employee(self):
        return f"{self.empName} salary is{self.empSalary}"


Tarun_instance1=employee("Tarun",2100)
print(Tarun_instance1.get_employee())

Arvind_instance1=employee("Arvind",3100)
print(Arvind_instance1.get_employee())