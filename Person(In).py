# Person Class (Inheritance)

class Person:
    def __init__(self,name,ph):
        self.name = name
        self.ph = ph

    def display(self):
        print ('The Details are---')
        print('Name:', self.name)
        print('Phone No.:', self.ph)

    def __del__(self):
        print('Class Deletedd')

class Spouse(Person):
    def __init__(self, name, ph, spname):
        Person.__init__(self, name, ph)
        self.spName=spname

    def display(self):
        Person.display(self)
        print('Spouse Name: ', self.spName)

C=Spouse('A', 8345567778, 'B')
C.display()
del C
