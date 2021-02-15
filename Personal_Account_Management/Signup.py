from tkinter import*    #For GUI
from tkinter import ttk  
from tkinter import messagebox
from PIL import ImageTk  # for Image related work 
import os   #for file 
from tkcalendar import Calendar,DateEntry
from datetime import datetime
#--------

class win2:
    def __init__(self,root):
        
        self.title("Sinup".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1350x700+0+0")

        bg_color ="#074463"
        font_=("times new roman")

        title= Label(self, bd=10, relief=GROOVE, text="SignUp Page", font=(font_,40,"bold"),bg=bg_color,fg="gold").pack(side=TOP, fill=X)


        #-----------variables-------------------

        self.uname=StringVar()
        self.pasw=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        

        now = datetime.now()
        self.today= now.strftime("%d/%m/%Y")
        self.label,self.calender="",""


        Manage_Frame=Frame(self,bd=10, relief=RIDGE,bg=bg_color)
        Manage_Frame.place(x=450, y=100, width=500, height=550)
        m_title=Label(Manage_Frame,text="SIGN UP", compound=LEFT, bg=bg_color,fg="white",font=(font_,30,"bold"))
        m_title.grid(row=0, columnspan=2,pady=20)

#-----------------------Entries------------------------------
        lbl1=Label(Manage_Frame,text="Username",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl1.grid(row=1, column=0,padx=20,pady=10,sticky="w")

        txt1=Entry(Manage_Frame,textvariable=self.uname,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt1.grid(row=1, column=1,padx=20,pady=10,sticky="w")
#*****************************************************************************************************

        lbl2=Label(Manage_Frame,text="Password",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl2.grid(row=2, column=0,padx=20,pady=10,sticky="w")

        txt2=Entry(Manage_Frame,textvariable=self.pasw,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt2.grid(row=2, column=1,padx=20,pady=10,sticky="w")
#*****************************************************************************************************

        lbl3=Label(Manage_Frame,text="Email",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl3.grid(row=3, column=0,padx=20,pady=10,sticky="w")

        txt3=Entry(Manage_Frame,textvariable=self.email,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt3.grid(row=3, column=1,padx=20,pady=10,sticky="w")
#*****************************************************************************************************

        self.label=(Label(Manage_Frame,text="D.O.B", bg=bg_color,fg="white",font=(font_,20,"bold")))
        self.label.grid(row=4, column=0,padx=20,pady=10,sticky="w")
        
        self.calendar=(DateEntry(Manage_Frame, textvariable=self.dob,font=("times new roman",18,"bold"), locale='en_GB', width=16,state="readonly"))
        self.calendar.place(x=180, y=290, anchor="w")

#*****************************************************************************************************

        gender_lbl=Label(Manage_Frame,text="Gender",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        gender_lbl.grid(row=5, column=0,padx=20,pady=10,sticky="w")
        
        
        gender=ttk.Combobox(Manage_Frame,textvariable=self.gender, font=(font_,13,"bold"),width=21,state="readonly")
        gender['values']=("Male","Female","Others")
        gender.grid(row=5, column=1,padx=20,pady=10,sticky="w")



#*****************************************************************************************************
        lbl6=Label(Manage_Frame,text="Contact",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl6.grid(row=6, column=0,padx=20,pady=10,sticky="w")

        txt6=Entry(Manage_Frame,textvariable=self.contact,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt6.grid(row=6, column=1,padx=20,pady=10,sticky="w")

#-------------------Button Frame------------------------------------
        
        Button_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
        Button_Frame.place(x=10, y=450,width=460,height=70)

        btn_sgnup = Button(Button_Frame, text="SignUp",width =8, command = self.signup, font="bold").grid(row = 0,column=0,padx=15,pady=15 )
        btn_back = Button(Button_Frame, text="Back",width =8, command = self.back, font="bold").grid(row = 0,column=1,padx=15,pady=15 )
        btn_Clear = Button(Button_Frame, text="Clear",width =8, command = self.clear, font="bold").grid(row = 0,column=2,padx=15,pady=15 )
        btn_Exit = Button(Button_Frame, text="Exit",width =8, command = self.exit, font="bold").grid(row = 0,column=3,padx=15,pady=15 )

    def exit(self):
        self.destroy()
    
    def back(self):
        self.destroy()
        import login

    def clear(self):
        self.uname.set("")
        self.pasw.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set(self.today)
    
    
    def signup(self):
        if self.uname.get()=="" and self.contact.get()=="" and self.pasw.get=="" and self.email.get()=="" and self.gender.get()=="" and self.dob.get()==self.today :
            return messagebox.showerror("Error","All Fields Required")
        
        if self.uname.get()==""  :
            return messagebox.showerror("Error","Username Required")
        if self.pasw.get=="" :
            return messagebox.showerror("Error","Password Required")
        if len(str(self.pasw.get()))<8:
            return messagebox.showerror("Error","Password should of minimum 8 character")
        
        if self.email.get()=="" :
            return messagebox.showerror("Error","Email Required")
        if "@" not in self.email.get():
            return messagebox.showerror("Error","Email Should have '@' character")
            
        if self.gender.get()==""  :
            return messagebox.showerror("Error","Gender Required")

        if self.dob.get()>=self.today  :
            return messagebox.showerror("Error","DOB Not Possible")
        
        if self.contact.get()==""  :
            return messagebox.showerror("Error","Contact Required")
        
        try:
            temp=self.contact.get()
            int(temp)
        except ValueError:
            return messagebox.showerror("Error","Contact should be Integer")
 
        if len(str(self.contact.get()))<10 or len(str(self.contact.get()))>10 :
            return messagebox.showerror("Error","Contact should consist of 10 numbers")     
        
        else:
            present ="no"
            f = os.listdir("User_F/")
            try:
                if len(f)>0:
                    for i in f:
                        if i.split(".")[0]==self.uname.get():
                            present="yes"
                    if present == "yes":
                        messagebox.showerror("Error","Username Already Exist")
                        
                    else:
                        self.get_data()
                else:
                    self.get_data()
            
            except EOFError:
                f.close()   

    def get_data(self):
        f=open("User_F/"+str(self.uname.get())+".txt","w")
        f.write(
                    str(self.uname.get())+","+
                    str(self.pasw.get())+","+
                    str(self.email.get())+","+
                    str(self.dob.get())+","+
                    str(self.contact.get())+","+
                    str(self.gender.get())
                )
        f.close()
        self.clear()
        messagebox.showinfo("Info","Succesfully Signed Up")

#create Window    
root = Tk()
obj = win2(root)
root.mainloop()
