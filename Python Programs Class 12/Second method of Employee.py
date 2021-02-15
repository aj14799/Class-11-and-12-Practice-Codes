class employee:
    def __init__(self, name=None, Salary=0, Designation=None, EmpNo=0):
        self.name = name
        self.EmpNo = EmpNo
        self.Salary = Salary
        self.Designation = Designation
    def bonus(self):
        if (self.Salary)<50000:
            bonus = ((10/100)*(self.Salary)+(self.Salary))
            print ("Salary after bouns is",bonus)
        elif (self.Salary)>60000:
            bonus = ((25/100)*(self.Salary)+(self.Salary))
            print("Salary after bouns is",bonus)
        else:
            bonus = ((15/100)*(self.Salary)+(self.Salary))
            print("Salary after bouns is",bonus)
    def show(self):
        print("Name:", self.name)
        print("Emp_no." ,self.EmpNo)
        print("Salary Without bonus" ,self.Salary)
        print("Designation" ,self.Designation)
    def getdata(self):
        self.name = str(input("Enter Name:"))
        self.EmpNo = int(input("Enter Emp_No."))
        self.Designation = str(input("Enter Designation:"))
        self.Salary = float(input("Enter Salary"))
E1 = employee(name=None, Salary=0, Designation=None, EmpNo=0)
E1.getdata()
E1.bonus()
E1.show()
