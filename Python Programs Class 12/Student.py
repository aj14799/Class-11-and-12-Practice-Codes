while True:
    n =input("Enter '1' to Enter details or press any key to quit")
    if n =='1':
        class student:
            def __init__(self, AdmNo, Name, Class, English, Mathematics, Physics, Computer_Science):
                self.AdmNo = AdmNo
                self.Name = Name
                self.Class = Class
                self.English = English
                self.Mathematics = Mathematics
                self.Physics = Physics
                self.Computer_Science = Computer_Science
                self.Chemistry = Chemistry
                
            def student_cal(self):
               marks1 = marks
               percentage1 = percentage
               print ("Your total marks is",marks1,"and percenage is",percentage1,"%")
            def Cal_Grade(self):
                if percentage>=90:
                    Grade = 'A+'
                    print("Grade", Grade)
                elif percentage>=80:
                    Grade = 'A'
                    print("Grade", Grade)
                elif percentage>=70:
                    Grade = 'B+'
                    print("Grade", Grade)
                elif percentage>=60:
                    Grade = 'B'
                    print("Grade", Grade)
                elif percentage>=50:
                    Grade = 'C'
                    print("Grade", Grade)
                elif percentage>=40:
                    Grade = 'D'
                    print("Grade", Grade)
                elif percentage>=33:
                    Grade = 'e'
                    print("Grade", Grade)
                else:
                    Grade = 'F'
                    print("Grade", Grade)
            def show(self):
                print("Name", self.Name)
                print("Admission no.", self.AdmNo)
                print("Class", self.Class)
                
        AdmNo = int(input("Enter Admission Number"))
        Name = str(input("Enter Name"))
        Class = input("Enter Class")
        English = float(input("Enter marks of English"))
        Mathematics = float(input("Enter marks of Mathematics"))
        Physics = float(input("Enter marks of Physics"))
        Computer_Science = float(input("Enter marks of Computer_Science"))
        Chemistry = float(input("Enter marks of Chemistry"))
        marks =  English+Mathematics+Physics+Computer_Science+Chemistry
        percentage = (marks/500)*100
        S = student(AdmNo, Name, Class, English, Mathematics, Physics, Computer_Science)
        S.show()
        S.Cal_Grade()
        S.student_cal()
    else:
        quit()
        
        
