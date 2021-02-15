#Menu Driven Program in binary file to read and write data

import os
from pickle import load, dump

def Camera_Add():
    ch1 = input("Enter 1 to proceed or any key to exit")
    if ch1 == '1':
        Cobj = open("CAMERA.DAT", 'ab+')
        if not Cobj:
            print(" File doesn't created")
        else:
            print("Enter Camera Information")
            ch = 'Y'
    #-----Main-----
            while ch == 'Y' or  'y':
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
                ch = input("Add More? <y/n>: ")
                if ch == 'Y' or ch == 'y':
                    continue
                else:
            
                    break
        Cobj.close()
    else:
        exit()

Camera_Add()
            
            
        
