class employee:
    def __init__(self, name, Salary, Designation, EmpNo):
        self.name = name
        self.EmpNo = EmpNo
        self.Salary = Salary
        self.Designation = Designation
    def bonus(salary):
        if (Salary)<50000:
            bonus = ((10/100)*(Salary)+(Salary))
            print ("Salary after bouns is",bonus)
        elif (Salary)>60000:
            bonus = ((25/100)*(Salary)+(Salary))
            print("Salary after bouns is",bonus)
        else:
            bonus = ((15/100)*(Salary)+(Salary))
            print("Salary after bouns is",bonus)
    def print(self):
        print("Name:", self.name)
        print("Emp_no." ,self.EmpNo)
        print("Salary Without bonus" ,self.Salary)
        print("Designation" ,self.Designation)
name = str(input("Enter Name:"))
EmpNo = int(input("Enter Emp_No."))
Designation = str(input("Enter Designation:"))
Salary = float(input("Enter Salary"))
employee = employee(name, Salary, Designation, EmpNo)
employee.print()
employee.bonus()
