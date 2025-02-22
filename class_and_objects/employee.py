class employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = float(salary)

    #getter for salary

    def get_salary(self):
        return self._salary
    
    #setter for salary

    def set_salary(self , new_salary):
        if new_salary < 0:
            print("Error : Salary can't be negative!")
        else:
            self._salary = new_salary
            print("Salary updated successfully!!")
            print(f"New salary : {self._salary}")


    def info(self):
        print(f"Employee name = {self.name}")
        print(f"Employee salary = {self._salary}")

name = input("Enter employee name : ")
salary = float(input("Enter employee salary : "))
emp1 = employee(name,salary)
emp1.info()

new_salary = float(input("Enter new salary : "))
emp1.set_salary(new_salary)