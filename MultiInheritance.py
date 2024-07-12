class Employee:

    def __init__(self, name, age, salary):

        self.name = name
        self.age = age
        self.salary = salary

    def getSalary(self):

        return self.salary
    
    def getName(self):

        return self.name
    
    def getAge(self):

        return self.age
    

class Manager(Employee):

    def __init__(self, name, age, salary, managerial_pay):
        super().__init__(name, age, salary)
        self.managerial_pay = managerial_pay

    def getManagerPay(self):

        return self.managerial_pay

    def getData(self):

        print(f"Name: {self.getName()} \n Age: {self.getAge()}, \n  Basic Salary: {self.getSalary()}, \n Managerial Pay: {self.getManagerPay()}, \n Total Pay:{self.getSalary() + self.getManagerPay()}")
        


class Executive(Manager):

    def __init__(self, name, age, salary, managerial_pay, ex_designation):
        super().__init__(name, age, salary, managerial_pay)
        self.ex_designation = ex_designation


    def getData(self):

        print(f" Name: {self.getName()} \n Age: {self.getAge()}, \n Basic Salary: {self.getSalary()}, \n Managerial Pay: {self.getManagerPay()}, \n Total Pay:{self.getSalary() + self.getManagerPay()}, \n Executive: {self.ex_designation}")
        






