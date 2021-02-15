while True:
    a = input("Enter 1 To Continue or press any key to Exit:")
    if a=='1':
        class library():
            def __init__(self):
                self.Name = None
                self.No_of_Hindibook = 0
                self.No_of_Englishbook = 0 
                self.Others = 0
                self.Total = 0
            def Compute_book(self):
                self.Total = self.No_of_Hindibook+self.No_of_Englishbook+self.Others
                return self.Total
            def Read_Book(self):
                self.Name = str(input("Enter Name:"))
                self.No_of_Hindibook = int(input("No. of Hnidi Book:"))
                self.No_of_Englishbook = int(input("No. of English Book:"))
                self.Others = int(input("No. of Other books:"))
            def Disp(self):
                print("Name:", self.Name )
                print("No. of Hindi books:", self.No_of_Hindibook)
                print("No. of English books:", self.No_of_Englishbook)
                print("No. of other books", self.Others)
                print("Total Books:", self.Total)
        L=library()
        L.Read_Book()
        L.Compute_book()
        L.Disp()
    else:
        exit()
            
            
