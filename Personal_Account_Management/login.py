from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import os, pickle
class win1:
    def __init__(self):
        self.root=root
        self.root.title("Login Form".center(420))  
        self.root.configure(background="black")  
        self.root.geometry("1360x768+0+0")
        bg_color = "#2B547E"

        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================

        self.eye_icon = PhotoImage(file="Pics\\2.png")
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1.jpg")
        self.bank_icon = ImageTk.PhotoImage(file="Pics\\6.jpg")    
        self.user_icon = ImageTk.PhotoImage(file="Pics\\4.png")
        self.pasw_icon = ImageTk.PhotoImage(file="Pics\\3.png")
        self.user_ = ImageTk.PhotoImage(file="Pics\\5.png")


        # =========================== Variables ========================================
        # =========================== Variables ========================================
        # =========================== Variables ========================================
        # =========================== Variables ========================================

        self.uname = StringVar()
        self.pasw = StringVar()
        self.uname.set("User Id")
        self.pass_1 = StringVar()
        self.pass_1.set("Password Mode: Hidden")

        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================

        bg_lbl = Label(root, image=self.bg_icon).pack(fill=Y) 

        
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================

        self.F1 = LabelFrame(root, bd=10, relief=GROOVE, bg=bg_color)
        self.F1.place(x=195, y=95, width=600, height=480)
        
        F1=self.F1
        
        lbl = Label(F1, text="User Login ", bg=bg_color, fg="gold", font=("times new roman", 30, "bold")).grid(row=0, column=0, padx=80, pady=30)

        logolbl = Label(F1, image=self.user_icon).place(x=80, y=200, anchor="w")
        
        lbl6 = Label(F1, text="User ID", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).place(x=115, y=200, anchor="w")
        
        self.txtu = Entry(F1, bd=5, textvariable=self.uname, relief=GROOVE,font=("", 15)).place(x=250, y=200, anchor="w")

        logolbl2 = Label(F1, image=self.pasw_icon).place(x=80, y=260, anchor="w")
        
        lbl7 = Label(F1, text="Password", fg="white", bg=bg_color, font=("times new roman", 20, "bold"))
        
        lbl7.place(x=115, y=260, anchor="w")
        
        self.txtp = Entry(F1, bd=5, textvariable=self.pasw, show="*",relief=GROOVE, font=("", 15))
        
        self.txtp.place(x=250, y=260, anchor="w")

        
        self.txtp_1 = Entry(F1, bd=0, bg=bg_color, fg="white", textvariable=self.pass_1,relief=GROOVE, width="45", font=("times new roman", 10))
        
        self.txtp_1.place(x=250, y=10, anchor="w")

        
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================

        self.F2 = LabelFrame(root, bd=10, relief=GROOVE, bg="")
        self.F2.place(x=790, y=95, width=310, height=480)
        F2 = self.F2 
        
        lbl2 = Label(F2, bg=bg_color, image=self.user_).grid(row=0, column=0, padx=100, pady=20)
        
        lbl3 = Label(F2, text="Get you all account details at ", bg="white", fg="green", font=("times new roman", 15, "italic")).grid(row=1, column=0, padx=5)
        
        lbl4 = Label(F2, text="one place @PersonalAcc", fg="green", bg="white", font=("times new roman", 10, "italic")).grid(row=2, column=0, padx=10)

        lbl6 = Label(F2, text="Developed by Aditya",fg="#4863A0", bg="white", font=("times new roman", 20)).place(x=20, y=420)

        img_lbl7 = Label(F2, image=self.bank_icon).place(x=20, y=300, width=250, height=100) 
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================

        btn_login1 = Button(F1, text="SignIn", relief=RAISED, width=12, height=1, font=("times new roman", 12, "bold"), bg="green", foreground="#FEFCFF", command=self.logfun).place(x=530, y=330, width=150, anchor="e")

        btn_Signup = Button(F1, text="Sign Up", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Signup, font=("times new roman", 14, "bold"), bg="Red", fg="white").place(x=330, y=330, width=150, anchor="e")

        btn_Eye = Button(F1, image=self.eye_icon, relief=GROOVE, font=("times new roman", 14, "bold"), bg="light green", command=self.show_pasw).place(x=528, y=260, height=35, anchor="e")    

        btn_Exit = Button(F2, text="Exit", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Exit, font=("times new roman", 14, "bold"), bg="Red", fg="white").grid(row=5, column=0, padx=110, pady=60, sticky="w")

    def Signup(self):
        self.root.destroy()
        import Signup
        
    def logfun(self):
        if self.uname.get()=="" or self.pasw.get()=="":
            messagebox.showerror("Error","All fields should be entered")
        else:
            present ="no"
            f = os.listdir("User_F/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.uname.get():
                        present="yes"
                if present == "yes":
                    L=[]
                    file = open("User_F/"+self.uname.get()+".txt","r")
                    data = file.read()
                    words = data.split(",")
                    if str(words[1]) == self.pasw.get():
                        messagebox.showinfo("Successful","Successfully Logined")
                        self.root.destroy()
                        import main.py
                    else: 
                        messagebox.showerror("Error","Username or Password May be wrong")
            else:
                messagebox.showerror("Error","No Data Exist to this Username")

    def Exit(self):
        self.root.destroy()

    def show_pasw(self):
        a = self.pasw.get()
        self.pasw.set(a)
        if self.txtp_1.get() == "Password Mode: Hidden":
            self.txtp_1.config(state="normal")
            self.txtp_1.insert(0, "Password Mode: Shown")
            
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw, relief=GROOVE, font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pass_1.set("Password Mode: Shown")
            self.pasw.set(a)

        elif self.txtp_1.get() == "Password Mode: Shown":
            self.txtp_1.config(state="normal")
            self.txtp_1.delete(0, END)
            self.txtp_1.insert(0, "Password Mode: Hidden")
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw,
                                relief=GROOVE, show="*", font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pasw.set(a)


root=Tk()
obj=win1()
root.mainloop()

