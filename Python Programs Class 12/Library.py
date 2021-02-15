while True:
        n=input("Enter 1 to Enter or press any key to Exit:")
        if n=='1':
            class library():
                def __init__(self, book_number, book_name, author, publisher, price, number_of_copies, number_of_copies_issued):
                    self.book_number = book_number
                    self.book_name = book_name
                    self.author = author
                    self.publisher = publisher
                    self.price = price
                    self.number_of_copies = number_of_copies
                    self.number_of_copies_issued = number_of_copies_issued
                
                def member(self):
                    if book_name in self.book_name:
                        if(number_of_copies-number_of_copies_issued)<=0:
                            print("Book is not available")
                        
                        else:
                            print("You can Issue this book",book_name)

                def return1(self):
                    if(number_of_copies-number_of_copies_issued)>0:  
                        a = input("Enter 'Y' if You returned the book other wise pree any other key if u didnt retuned the book")
                        if a=='Y'or a=='y':
                            print("You have retured the book . Thank You! :)")
                        else:
                            print("Return the book please")
                    else:
                        print(" Book is not available")
                def display(self):
                    print ("Book Number",self.book_number)
                    print ("Book name", self.book_name) 
                    print ("Author", self.author)
                    print ("Publisher", self.publisher)
                    print ("Price", self.price)
                    print ("No. of Copies", self.number_of_copies)
         
            book_number = int(input("Enter Book Number:"))
            book_name = str(input("Enter Book Name:"))
            author = str(input("Enter Author:"))
            publisher = str(input("Enter publisher:"))
            price = float(input("Enter Price of book in Rupees:"))
            number_of_copies = int(input("Enter Number of Copies:"))
            number_of_copies_issued = int(input("Enter Number of Copies Issued:"))
            L = library(book_number, book_name, author, publisher, price, number_of_copies, number_of_copies_issued)
            L.member()
            L.return1()
            L.display()
        else:
            exit()
              
