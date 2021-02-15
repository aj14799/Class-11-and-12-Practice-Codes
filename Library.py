#Class Library
while True:
    a = input("Enter 1 To Continue or press any key to Exit:")
    if a=='1':
        class library():
            def __init__(self):
                self.__Name = None
                self.__No_of_Hindibook = 0
                self.__No_of_Englishbook = 0 
                self.__Others = 0
                self.__Total = 0
            def Compute_book(self):
                self.__Total = self.__No_of_Hindibook+self.__No_of_Englishbook+self.__Others
                return self.__Total
            def Read_Book(self):
                self.__Name = str(input("Enter Name:"))
                self.__No_of_Hindibook = int(input("No. of Hnidi Book:"))
                self.__No_of_Englishbook = int(input("No. of English Book:"))
                self.__Others = int(input("No. of Other books:"))
            def Disp(self):
                print("Name:", self.__Name )
                print("No. of Hindi books:", self.__No_of_Hindibook)
                print("No. of English books:", self.__No_of_Englishbook)
                print("No. of other books", self.__Others)
                print("Total Books:", self.__Total)
        L=library()
        L.Read_Book()
        L.Compute_book()
        L.Disp()
    else:
        exit()
            
            
