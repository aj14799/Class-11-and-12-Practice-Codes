# Inheritance Publication Class

class publication(object):
    def __init__(self):
        self.title = ''
        self.price = 0.0

    def getdata(self):
        self.title = input('Enter Title: ')
        try:
            self.price = float(input('Enter Price: '))
        except ValueError:
            print ("Invalid Input Enter again")
            self.price = float(input('Enter Price: '))

    def putdata(self):
        print ('Title:', self.title)
        print ('price', self.price)

class book(publication):
    def __init__(self):
        super(book, self).__init__()
        self.page_count = 0

    def getdata(self):
        print ('Enter detail of book--')
        super(book,self).getdata()
        self.page_count = int(input('Enter pages: '))

    def putdata(self):
        print ('The Details are--')
        super(book, self).putdata()
        print('Pages:', self.page_count)

class tape(publication):
    def __init__(self):
        super(tape, self).__init__()
        self.play_time = 0

    def getdata(self):
        print ('Enter Details of tape--')
        super(tape, self).getdata()
        self.play_time = input('Enter play time: ')

    def putdata(self):
        print ('The Details are--')
        super(tape, self).putdata()
        print ('Play time:', self.play_time)



#--Main--

t=tape()
t.getdata()
t.putdata()
b=book()
b.getdata()
b.putdata()




 
