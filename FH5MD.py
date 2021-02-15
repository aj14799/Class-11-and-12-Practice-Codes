# Program to search and modify data
import pickle
from pickle import load, dump
import os
def Camera_Search():
    ch = input("Enter 1 to read the file and search and modify or any key to exit") 
    while True:
        if ch=='1':
            ch = 'Y'
            while ch == 'Y' or  'y':
                Cobj = open("CAMERA2.DAT", 'ab+')
                Clist = []
                ModelNo = input("Enter camera model no. : ").upper()
                try:
                    MegaPixel = int(input("Enter pixel/resolution support: "))
                except ValueError:
                    print ("Invalid Input Please ReEnter: ")
                    MegaPixel = int(input("Enter pixel/resolution support: "))                
                Color = input("Enter Camera color : ").upper()
                Company = input("Enter Company Name : ").upper()
                Clist.append(ModelNo)
                Clist.append(MegaPixel)
                Clist.append(Color)
                Clist.append(Company)
                dump(Clist, Cobj)
                ch = input("Add More? <y/n>:y for proceed to add data or n for modify older data ")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
                    Cobj = open("CAMERA2.DAT", 'rb')
                    tCam = []
                    TModelNo = input("Enter Camera Model No. to search : ")
                    flag = False
                    if TModelNo == ModelNo:
                        print ("CAMERA exist")
                        ch2=input("Enter '3'to modify or any key to exit")
                        if ch2 == '3':
                            Cobj2 = open("temp.DAT", 'wb')
                            data = Cobj.read()
                            Cobj2.write(data)
                            Cobj.close()
                            Cobj2.close()
                            os.remove('CAMERA2.DAT')
                            os.rename('temp.DAT', 'CAMERA2.DAT')
                        else:
                            print ('Exited')
                            quit()
                    else:
                        print("Camera doesnt Exist")
                        quit()
            Cobj.close()
        else:
            quit()
Camera_Search()
           
