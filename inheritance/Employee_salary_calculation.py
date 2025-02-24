#Use method overriding to handle different salary calculation methods for full-time and part-time employees.

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = float(salary)

    def calculate_salary(self):
        print(f"\nEmployee name : {self.name}")
        print(f"Base salary : {self.salary}")


class FullTimeEmployee(employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus

    def calculate_salary(self):
        super().calculate_salary()
        print(f"Bonus : {self.bonus}")
        print(f"Total salary : {self.salary + bonus}")

class PartTimeEmployee(employee):
    def __init__(self,name,salary,hours,wage):
        super().__init__(name,salary)
        self.hours = hours
        self.wage = wage
    
    def calculate_salary(self):
        print(f"\nHourly Wage : {self.wage}")
        print(f"Hours worked : {self.hours}")
        print(f"Base salary : {self.wage*self.hours}")

print("Enter 1 for Full Time Employee")
print("Enter 2 for Part Time Employee")
option = int(input("\nEnter any option : "))

if option==1:
    name = input("Enter Employee name : ")
    salary = float(input("Enter employee salary : "))
    bonus = salary//10

    emp1 = FullTimeEmployee(name, salary, bonus)
    emp1.calculate_salary()

elif option==2:
    name = input("Enter Employee name : ")
    hours = float(input("Enter hours worked : "))
    wage = float(input("Enter hourly wage : "))

    emp2 = PartTimeEmployee(name,0,hours,wage)
    emp2.calculate_salary()

else:
    print("Enter valid option...")