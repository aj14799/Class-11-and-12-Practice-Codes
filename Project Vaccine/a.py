from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk 
from tkcalendar import Calendar, DateEntry
import os, random, time
import sqlite3
from datetime import datetime
def Manage_Vaci():
    global root3
    root3 = Tk()    
    root3.title("Login Hospital".center(420))  
    root3.configure(background="black")  
    root3.geometry("1360x768+0+0")
    bg_color = "#e0b0ff"
    bg_icon = ImageTk.PhotoImage(file="PICs\\81736244-cell-background-with-futuristic-interface-elements-hud-ui-for-medical-app-futuristic-user-interface-.jpg")
    bg_lbl = Label(root3, image = bg_icon).pack(fill=Y) # we put image into our window
    hos_icon=ImageTk.PhotoImage(file="PICs\\image2(1).png")
    home_icon=ImageTk.PhotoImage(file="PICs\\Home.png")
    view_vacci_icon=ImageTk.PhotoImage(file="PICs\\View_Vacci.png")
    view_icon=ImageTk.PhotoImage(file="PICs\\View_All_dark.png")
    manage_icon=ImageTk.PhotoImage(file="PICs\\Manage.jpg")
    exit_icon=ImageTk.PhotoImage(file="PICs\\Exit.png")
    global lbl_hr, lbl_min, lbl_sec, lbl_abv
    product_TBL=StringVar()
    CVX_S_D=StringVar()
    Manuf_TBL_Code=StringVar()
    MVX_Status=StringVar()
    CVX_Code=StringVar()
    Manuf_TBL=StringVar()
    searchby=StringVar()
    searchby.set("Choose Option")
    searchval=StringVar()
    P_N_S=StringVar()
    P_N_S.set("Chosse Product Name Status")
    MVX_Status.set("Choose MVX_Status")
    PID=StringVar()
    a=random.randint(65,90)
    b=random.randint(65,90)
    c=random.randint(65,90)
    d=random.randint(65,90)
    e=random.randint(65,90)
    f=random.randint(65,90)
    PID.set(str(chr(a))+str(chr(b))+str(chr(b))+str(chr(c))+str(chr(e))+str(chr(f)))
    
    con2=""
    
    now = datetime.now()
    Time1=now.strftime('%H:%M:%S')

    today= now.strftime("%d/%m/%Y")

    label, calendar = "",""
    F1 = LabelFrame(root3,bd=10,relief=GROOVE,bg=bg_color)
    F1.place(x=0,relwidth=1,height=100 )
    lbl = Label(F1,text="Vaccine Search", bg=bg_color, font= ("times new roman",25,"bold")).place(x=120, y=15)
    lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
    lbl_hr.place(x=850, y=40)
    lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
    lbl_COLON.place(x=875, y=40)
    lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
    lbl_min.place(x=885, y=40)
    lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
    lbl_COLON.place(x=910, y=40)
    lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
    lbl_sec.place(x=920, y=40)
    lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
    lbl_abv.place(x=945, y=43)
    font=("times new roman",20,"bold")
    calendar = []
    calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly", width=10))
    calendar[-1].place(x=855, y=20, anchor="w")
    btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white").place(x=1145,y=20,anchor="w")
    btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black").place(x=1145,y=60,anchor="w")
    lbl2 = Label(F1,image=hos_icon,bg=bg_color)
    lbl2.place(x=25,y=10)
    F2 = LabelFrame(root3,bd=10,relief=GROOVE,bg=bg_color)
    F2.place(x=0,y=100,width=150,height=670 )
    F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F21.place(x=0,y=0,width=130,height=150 )
    F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F22.place(x=0,y=150,width=130,height=150)
    F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F23.place(x=0,y=300,width=130,height=150 )
    F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F24.place(x=0,y=450,width=130,height=150)
    btn_home = Button(F21,image= home_icon,bg=bg_color,relief=RAISED,width =115,height=145).place(x=0,y=63,anchor="w")
    btn_view = Button(F22,relief=RAISED,bg=bg_color,image=view_icon,width =115,height=145).place(x=0,y=63,anchor="w")
    btn_manage = Button(F23,relief=RAISED,image=manage_icon,bg=bg_color,width =115,height=145).place(x=0,y=63,anchor="w")
    btn_Exit = Button(F24,relief=RAISED,bg=bg_color,image=exit_icon,width =115,height=145).place(x=0,y=63,anchor="w")
    F3 = LabelFrame(root3,bd=5,relief=FLAT,bg="light gray")
    F3.place(x=150,y=100,relwidth=1,height=30 )
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    with open("Temp1.txt","r+") as file:
        read1=file.read()
    lbl_1= Label(F3,text="Dashboard / Hospital"+": HName : "+str(read1),font=("comic sans",15,"italic"),bg="light gray")
    lbl_1.place(x=0,y=0)

    F4 = Frame(root3,bd=5,relief=FLAT)
    F4.place(x=151,y=132,relwidth=1,height=600)
    lbl_1= Label(F4,text="Manage Vaccines",fg="#008080",font=("geometric sans-serif",30,"bold"))
    lbl_1.place(x=0,y=0)

    seprator1_style = ttk.Style()
    separator1 = ttk.Separator(F4, orient='horizontal',style="Line.TSeparator")
    separator1.place(x=0,width=700,y=50)
    seprator1_style.configure("Line.TSeparator")
    
    #---------------------------------------------Entries--------------------------------------------------------------------------------
    #---------------------------------------------Entries--------------------------------------------------------------------------------
    #---------------------------------------------Entries--------------------------------------------------------------------------------
    #---------------------------------------------Entries--------------------------------------------------------------------------------
    #---------------------------------------------Entries--------------------------------------------------------------------------------

    

    lbl_roll=Label(F4,text="Product ID",font=("times new roman",18,"bold"),bg="#F5F5F5")
    lbl_roll.place(x=0,y=90,anchor="w")
    txt_roll=Entry(F4, textvariable=PID,state="readonly", width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=90,anchor="w")

    #**************************************************************************************************

    lbl_roll=Label(F4,text="Product TBL",font=("times new roman",18,"bold"),bg="#F5F5F5")
    lbl_roll.place(x=0,y=140,anchor="w")
    txt_roll=Entry(F4, textvariable=product_TBL, width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=140,anchor="w")

    #***************************************************************************************************

    lbl_roll=Label(F4,text="CVX Short Desc",bg="#F5F5F5",font=("times new roman",18,"bold"))
    lbl_roll.place(x=0,y=190,anchor="w")
    txt_roll=Entry(F4, textvariable=CVX_S_D,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=190,anchor="w")
    
    #***************************************************************************************************


    lbl_roll=Label(F4,text="CVX Code",bg="#F5F5F5",font=("times new roman",18,"bold"))
    lbl_roll.place(x=0,y=240,anchor="w")
    txt_roll=Entry(F4, textvariable=CVX_Code,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=240,anchor="w")

    #***************************************************************************************************     

    lbl_roll=Label(F4,text="Manufactur TBL",bg="#F5F5F5",font=("times new roman",18,"bold"))
    lbl_roll.place(x=0,y=290,anchor="w")
    txt_roll=Entry(F4, textvariable=Manuf_TBL, width=17,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=290,anchor="w")

    #***********************************************************************************************

    lb_dep=Label(F4,text="Manufactur TBL Code", font=("times new roman",18,"bold"),bg="#F5F5F5")
    lb_dep.place(x=0, y=340, anchor="w")
    combo_dep=Entry(F4, textvariable=Manuf_TBL_Code,width=17, font=("times new roman",15,"bold"))
    combo_dep.place(x=230, y=340, anchor="w")

    #***********************************************************************************************    #***********************************************************************************************
    lb_dep=Label(F4,text="MVX_Status", font=("times new roman",18,"bold"),bg="#F5F5F5")
    lb_dep.place(x=0, y=390, anchor="w")
    combo_dep=ttk.Combobox(F4, textvariable=MVX_Status,width=17, font=("times new roman",13,"bold"),state='readonly')
    combo_dep['values']=("Active","Inactive")
    combo_dep.place(x=230, y=390, anchor="w")

    #***********************************************************************************************
    lb_dep=Label(F4,text="Product Name Status", font=("times new roman",18,"bold"),bg="#F5F5F5")
    lb_dep.place(x=0, y=440, anchor="w")
    combo_dep=ttk.Combobox(F4, textvariable=P_N_S,width=17, font=("times new roman",13,"bold"),state='readonly')
    combo_dep['values']=("Active","Inactive")
    combo_dep.place(x=228, y=440, anchor="w")

    F5 =Frame(F4,bd=10,relief=SUNKEN,bg="white")
    F5.place(x=0,y=480,width=700,height=80 )

    btn_update2 = Button(F5,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bg="navy blue",fg="yellow",bd=6,text="Update").grid(row=0,column=0,pady=6,padx=50,sticky="nesw")        
    btn_Delete = Button(F5,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bg="navy blue",fg="yellow",bd=6,text="Delete").grid(row=0,column=1,pady=6,padx=50,sticky="nesw")
    btn_Clear = Button(F5,relief=GROOVE, width=15,font=("times new roman",13,"bold"),bg="navy blue",fg="yellow",bd=6,text="Clear ALL").grid(row=0,column=2,pady=6,padx=5,sticky="nesw")
    btn_Add = Button(F4,relief=GROOVE, width=15,font=("times new roman",13,"bold"),bg="red",fg="white",bd=6,text="Add").place(x=510,y=440,anchor="w")       

    seprator2_style = ttk.Style()
    separator2 = ttk.Separator(F4, orient='vertical',style="Line.TSeparator")
    separator2.place(x=700,height=590,y=0)
    seprator2_style.configure("Line.TSeparator")

#----------------------------------------------------F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------F4 Partion2-----------------------------------------------------------------------------
#----------------------------------------------------F4 Partion2-----------------------------------------------------------------------------

    seprator2_style = ttk.Style()
    separator2 = ttk.Separator(F4, orient='horizontal',style="Line.TSeparator")
    separator2.place(x=700,width=675,y=80)
    seprator2_style.configure("Line.TSeparator")

    lb_search=Label(F4,text="Search By", font=("times new roman",15,"bold"),bg="#F5F5F5")
    lb_search.place(x=720 ,y=17, anchor="w")
    combo_search=ttk.Combobox(F4, textvariable=searchby,width=17, font=("times new roman",13,"bold"),state='readonly')
    combo_search['values']=("Roll","PID")
    combo_search.place(x=830, y=17, anchor="w")

    lb_search2=Entry(F4,textvariable=searchval,width=15,relief=SUNKEN,bd=5,font=("times new roman",15,"bold"),bg="#F5F5F5")
    lb_search2.place(x=1030, y=15, anchor="w")
    

    btn_searchall = Button(F4,relief=RAISED,width=30,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6, text="Search All")
    btn_searchall.place(x=720,y=60,anchor="w")
    btn_search = Button(F4,relief=RAISED,width=30,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6,text="Search")        
    btn_search.place(x=970,y=60,anchor="w")

#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------            
#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------        
#----------------------------------------------------F6------------------------------------------------------------------------------------        
    F6 =Frame(F4,bd=10,relief=SUNKEN,bg="white")
    F6.place(x=720,y=85,width=475,height=500 )

    Table_Frame=Frame(F6,bd=4, relief=RIDGE,bg=bg_color)
    Table_Frame.place(x=0,y=0,width=455,height=480)

    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
    Student_table=ttk.Treeview(Table_Frame,columns=("PID" ,"First_name"  , "Last_name"  , "Roll", "code"  , "contact"  , "country" , "Class"  , "Manuf_TBL"  , "Department"  , "DOB" , "Email"  , "MVX_Statusester"  , "Gender"  , "L_URL" ,"F_URL","PIC_LINK"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Student_table.xview)
    scroll_y.config(command=Student_table.yview)

    root3.mainloop()

Manage_Vaci()