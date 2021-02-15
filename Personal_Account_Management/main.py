from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import random
import os, pickle


class Acc_File_App:
    def __init__(self,root):
   
        self.title("Personal Bank Account Record System".center(420))
        self.configure(background = "black")
        bg_color="#4169E1" 
        self.geometry("1350x700+0+0")
        
        title=Label(self,text="Personal Bank Account Record System",font=("times new roman",35,"bold"),bd=5,relief=GROOVE ,bg="#9370DB",pady=2).pack(fill=X)

        UserF1=LabelFrame(self, bd=10, text="Account Details",relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        UserF1.place(x=0,y=70,height=460)


        #--------------Variables-----------------

        self.u_id =StringVar()
        self.name =StringVar()
        self.state =StringVar()
        self.city =StringVar()
        self.pin =StringVar()
        self.house_no =StringVar()
        self.contact =StringVar()
        self.date =StringVar()
        self.bank =StringVar()
        self.id_proof =StringVar()
        self.total =StringVar()
        self.withdraw =StringVar()
        self.deposite =StringVar()
        self.acc_no =StringVar()
        self.all_acc_total = StringVar()
        self.u_id.set(str(random.randint(100000,999999)))
        self.total.set("0.0")
        self.withdraw.set("0.0")
        self.deposite.set("0.0")
        
        
        lbluid=Label(UserF1,text="User Id",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=2,padx=20,pady=10,sticky="w")
        txtuid=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.u_id,width=21,state="readonly",font="arial 15 bold").grid(row=0,column=3,padx=20,pady=10)
        
        lblacc=Label(UserF1,text="Account No.",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=0,padx=20,pady=10,sticky="w")
        txtacc=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.acc_no,width=21,font="arial 15 bold").grid(row=0,column=1,padx=20,pady=10)
    
        lblname=Label(UserF1,text="Name",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=1,column=0,padx=20,pady=10)
        txtname=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.name, width=21,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10,sticky="w")

        lblcontact=Label(UserF1,text="Contact",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=1,sticky="w",column=2,padx=20,pady=10)
        txtcontact=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.contact,width=21,font="arial 15 bold").grid(row=1,column=3,padx=20,pady=10)

        
        lbldate=Label(UserF1,text="Date(dd/mm/yyyy)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=2,column=2,padx=20,pady=10)
        txtdate=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.date,width=21,font="arial 15 bold").grid(row=2,column=3,padx=20,pady=10)

        
        lblstate=Label(UserF1,text="State",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=2,sticky="w",column=0,padx=20,pady=10)
        txtstate=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.state,width=21,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10)

        
        lblSD=Label(UserF1,text="Select Bank",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=3,sticky="w",column=2,padx=20,pady=10)

        
        lblcity=Label(UserF1,text="City",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=3,sticky="w",column=0,padx=20,pady=10)
        txtcity=Entry(UserF1,bd=7,textvariable=self.city,relief=GROOVE,width=21,font="arial 15 bold").grid(row=3,column=1,padx=20,pady=10)

        
        lblIP=Label(UserF1,text="ID Proof",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=4,sticky="w",column=2,padx=20,pady=10)

        lblhouse=Label(UserF1,text="House No.",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=4,column=0,sticky="w",padx=20,pady=10)
        txthouse=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.house_no,width=21,font="arial 15 bold").grid(row=4,column=1,padx=20,pady=10)

        lblpin=Label(UserF1,text="Pin and Locality",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=5,column=0,sticky="w",padx=20,pady=10)
        txtpin=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.pin,width=21,font="arial 15 bold").grid(row=5,column=1,padx=20,pady=10)

    
        lblwithdraw=Label(UserF1,text="Withdraw (INR)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=5,column=2,sticky="w",padx=20,pady=10)
        txtwithdraw=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.withdraw,width=21,font="arial 15 bold").grid(row=5,column=3,padx=20,pady=10)

        lbldeposite=Label(UserF1,text="Deposite (INR)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=6,column=0,sticky="w",padx=20,pady=10)
        txtdeposite=Entry(UserF1,bd=7,relief=GROOVE,textvariable=self.deposite,width=21,font="arial 15 bold").grid(row=6,column=1,padx=20,pady=10)
        
        lblT=Label(UserF1,text="Total Amount (INR)",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(sticky="w",row=6,column=2,padx=20,pady=10)
        Ttxt=Entry(UserF1,bd=7,textvariable=self.total,relief=GROOVE,width=21,font="arial 15 bold")
        Ttxt.grid(row=6,column=3,pady=10, padx=20)
        
        
        bankcombobox=ttk.Combobox(UserF1,width=20, textvariable=self.bank,font="arial 15 bold")
        bankcombobox['values']=("SBI","HDFC","ICICI","PNB","COB","BOI","Yes","Axis","PostOffice")
        bankcombobox.grid(row=3,column=3,pady=10, padx=20)   
        
        IPcombobox=ttk.Combobox(UserF1,width=20, textvariable=self.id_proof,state="readonly",font="arial 15 bold")
        IPcombobox['values']=("Addhar Card","Pan Card","Driving Licence","PassPort","VoterId Card")
        IPcombobox.grid(row=4,column=3,pady=10, padx=20)

# ================================== Buttons ========================================
# ================================== Buttons ========================================
# ================================== Buttons ========================================
# ================================== Buttons ========================================

        btnalter = Button(self,text="Alter User ID",bd=5, relief=GROOVE,command=self.alter, font="arial 15 bold",activebackground="red",activeforeground="white",fg="white",bg="red").place(x=1200,y=10)

        btnframe=Frame(self,bd=10,relief=GROOVE, bg="light blue")
        btnframe.place(x=0,y=535,width=1350, height=290)

        btnsave=Button(btnframe,text="Save", command=self.save_data, font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=0,padx=15,pady=30)
        btndelete=Button(btnframe,text="Delete",command=self.delete, font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=1,padx=15,pady=30)
        btnclear=Button(btnframe,text="Clear", command=self.clear,font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=2,padx=15,pady=30)
        btnlog=Button(btnframe,text="Logout", command=self.logout,font="arial 15 bold", bd=7, width=18,height=3,bg="yellow").grid(row=0,column=3,padx=15,pady=30)
        btnexit=Button(btnframe,text="Exit", command=self.exit,font="arial 15 bold", bd=7, width=18,height=3, bg="yellow").grid(row=0,column=4,padx=15,pady=30)


# =========================== Acc File Showing Window ================================
# =========================== Acc File Showing Window ================================
# =========================== Acc File Showing Window ================================
# =========================== Acc File Showing Window ================================

        fileframe=Frame(self,bd=10,relief=GROOVE)
        fileframe.place(x=995, y=70,width=365,height=420)

        ftitle=Label(fileframe,text="Your all Account Files", font="arial 20 bold",bd=5,relief=GROOVE,bg="light blue").pack(side=TOP,fill=X)

        scroll_y=Scrollbar(fileframe,orient=VERTICAL)
        self.f_list=Listbox(fileframe,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.f_list.yview)
        self.f_list.pack(fill=BOTH,expand=1)

        self.f_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()

        self.frame=Frame(self,bd=10,bg=bg_color,relief=GROOVE)
        self.frame.place(x=995, y=470,width=365,height=60)
    
        self.totalamt_allfiles()

    def save_data(self):
        present="no"
        self.final = float(self.total.get())-float(self.withdraw.get())+float(self.deposite.get())
        
        
        if len(self.acc_no.get())<11 or len(self.contact.get())>16:
            return messagebox.showerror("Error","Invalid Account Number")

        if self.total.get()=="":
            return messagebox.showerror("Error", "Total amount should be filled")
                       
        if self.final < 0.0:
            return messagebox.showerror("Error","Not Sufficient Balance to Withdraw")

        if len(self.contact.get())<10 or len(self.contact.get())>10:
            return messagebox.showerror("Error","Contact invalid")

        try:
            tmp=self.acc_no.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Account No. Should Be Integer')

        try:
            tmp=self.contact.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer')
        try:
            b=self.total.get()
            float(b)
        except ValueError:
            return messagebox.showerror("Error","Total Amount should be float Value")   
                
        try:
            c=self.withdraw.get()
            float(c)
        except ValueError:
            return messagebox.showerror("Error","Withdrawal Amount should be float Value")   
        
        try:
            d=self.deposite.get()
            float(d)
        except ValueError:
            return messagebox.showerror("Error","Deposite Amount should be float Value")   
        
        else:
        
            f=os.listdir("Files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.u_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesnocancel("Update","File already presennt \nDo you really want to Update?!!")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has Been saved!!")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved","Record has Been saved!!")
                    self.show_files()      
    
            else:
                self.save_file()
                messagebox.showinfo("Saved","Record has Been saved!!")
                self.show_files()      
    
    def save_file(self):
        a="Withdraw: "
        b="Deposite: "
        f=open("Files/"+str(self.u_id.get())+str(self.bank.get())+".txt","w")
        f.write(
                    str(self.u_id.get())+","+
                    str(self.acc_no.get())+","+
                    str(self.name.get())+","+
                    str(self.state.get())+","+
                    str(self.city.get())+","+
                    str(self.house_no.get())+","+
                    str(self.pin.get())+","+
                    str(self.contact.get())+","+
                    str(self.date.get())+","+
                    str(self.bank.get())+","+
                    str(self.id_proof.get())+","+
                    str(a)+","+
                    str(self.withdraw.get())+","+
                    str(b)+","+
                    str(self.deposite.get())+","+
                    str(self.final)
                )
        f.close()
        self.clear()
        self.totalamt_allfiles()
        self.show_files()    
            
    def show_files(self):
        Files=os.listdir("Files/")
        self.f_list.delete(0,END)
        if len(Files)>0:        
            for i in Files:
                self.f_list.insert(END,i)

    def get_data(self,ev):
        getcursor=self.f_list.curselection()
        #print(self.f_list.get(getcursor))
        f1=open("Files/"+self.f_list.get(getcursor))
        value=[]
        for f in f1:
            value=f.split(",")
            #print(value)
        self.u_id.set(value[0])
        self.acc_no.set(value[1])
        self.name.set(value[2])
        self.state.set(value[3])
        self.city.set(value[4])
        self.house_no.set(value[5])
        self.pin.set(value[6])
        self.contact.set(value[7])
        self.date.set(value[8])
        self.bank.set(value[9])
        self.id_proof.set(value[10])
        self.withdraw.set(value[12])
        self.deposite.set(value[14])
        self.total.set(value[15])
        


    def clear(self):
        self.u_id.set(str(random.randint(100000,999999)))
        self.acc_no.set("")
        self.name.set("")
        self.state.set("")
        self.city.set("")
        self.pin.set("")
        self.house_no.set("")
        self.contact.set("")
        self.date.set("")
        self.bank.set("")
        self.id_proof.set("")
        self.total.set("0.0")
        self.withdraw.set("0.0")
        self.deposite.set("0.0")

    def delete(self):
        present="no"
        if self.u_id.get()=="":
            messagebox.showerror("Error","UserF1 Id must be Required!!!")
        else:
            f=os.listdir("Files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == (str(self.u_id.get())+str(self.bank.get())):  
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesnocancel("Delete","Do you really want to delete?!!")
                    if ask>0:
                        os.remove("Files/"+self.u_id.get()+self.bank.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully")
                        self.show_files()
                        self.clear()
                else:
                    messagebox.showerror("Error","File not found!!!!")
    
    def alter(self):
        self.u_id.set(str(random.randint(100000,999999)))

    def totalamt_allfiles(self):    
        file_list=os.listdir(r"Files\\")
        #print (file_list)
        self.s=0.0
        for i in file_list:
            #print(i)
            f1=open("Files/"+str(i))
            value=[]
            for f in f1:
               value=f.split(",")
            self.s+=float(value[-1])
        
        lbltxt=Label(self.frame,text="Amount (INR) in All",bg="#4169E1", fg="white",font=("times new roman",15, "bold")).place(x=5, y=5)
        newtxt=Entry(self.frame,bd=7,textvariable=self.all_acc_total,relief=GROOVE,width=21,font="arial 15 bold")
        newtxt.place(x=190,width=150)
        self.all_acc_total.set(str(self.s))
    
    
 
    def exit(self):
        ask=messagebox.askyesnocancel("Exit","Do you really want to Exit?!!")
        if ask>0:
            self.destroy()
        else:
            return

    def logout(self):
        ask=messagebox.askyesno("Logout","Do you really want to Logout?!!")
        if ask>0:
            messagebox.showinfo("Logout","Loged Out Successfully")
            self.destroy()
            import login
        else:
            return

root=Tk()
obj=Acc_File_App(root)
root.mainloop()
