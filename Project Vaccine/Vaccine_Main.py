from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk 
import os, random, time
import sqlite3
from datetime import datetime
import mysql.connector
from tkcalendar import Calendar, DateEntry
now = datetime.now()
Time1 = now.strftime('%H:%M:%S')
date = now.strftime("%d-%b-%Y")

global View_Vaci1
def View_Vaci1():
    Exit4()
    global root4
    root4 = Tk()    
    root4.title("Login User".center(420))  
    root4.configure(background="black")  
    root4.geometry("1360x768+0+0")
    bg_color = "#e0b0ff"
    bg_icon = ImageTk.PhotoImage(file="PICs\\81736244-cell-background-with-futuristic-interface-elements-hud-ui-for-medical-app-futuristic-user-interface-.jpg")
    bg_lbl = Label(root4, image = bg_icon).pack(fill=Y) # we put image into our window
    hos_icon=ImageTk.PhotoImage(file="PICs\\image2(1).png")
    home_icon=ImageTk.PhotoImage(file="PICs\\Home.png")
    view_vacci_icon=ImageTk.PhotoImage(file="PICs\\View_Vacci.png")
    view_icon=ImageTk.PhotoImage(file="PICs\\View_All_dark.png")
    manage_icon=ImageTk.PhotoImage(file="PICs\\Manage.jpg")
    exit_icon=ImageTk.PhotoImage(file="PICs\\Exit.png")
    global lbl_hr, lbl_min, lbl_sec, lbl_abv
    F1 = LabelFrame(root4,bd=10,relief=GROOVE,bg=bg_color)
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
    btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=ChangePassword1).place(x=1145,y=20,anchor="w")
    btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=logout1).place(x=1145,y=60,anchor="w")
    lbl2 = Label(F1,image=hos_icon,bg=bg_color)
    lbl2.place(x=25,y=10)
    F2 = LabelFrame(root4,bd=10,relief=GROOVE,bg=bg_color)
    F2.place(x=0,y=100,width=150,height=670 )
    F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F21.place(x=0,y=0,width=130,height=150 )
    F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F22.place(x=0,y=150,width=130,height=150)
    F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F23.place(x=0,y=300,width=130,height=150 )
    F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F24.place(x=0,y=450,width=130,height=150)
    btn_home = Button(F21,image= home_icon,bg=bg_color,relief=RAISED,width =115,height=140,command=Home1).place(x=0,y=67,anchor="w")
    btn_view_vacci = Button(F22,image= view_vacci_icon,bg=bg_color,relief=RAISED,width =115,height=140,command=View_Vaci1).place(x=0,y=67,anchor="w")
    btn_view = Button(F23,relief=RAISED,bg=bg_color,image=view_icon,width =115,height=140,command=Name_V_Search1).place(x=0,y=67,anchor="w")
    btn_Exit = Button(F24,relief=RAISED,bg=bg_color,image=exit_icon,width =115,height=140,command=Exit4).place(x=0,y=67,anchor="w")
    F3 = LabelFrame(root4,bd=5,relief=FLAT,bg="light gray")
    F3.place(x=150,y=100,relwidth=1,height=30 )
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    with open("Temp.txt","r+") as file:
        read1=file.read()
    lbl_1= Label(F3,text="Dashboard / User"+": UName : "+str(read1),font=("comic sans",15,"italic"),bg="light gray")
    lbl_1.place(x=0,y=0)

    F4 =Frame(root4,bd=10,relief=SUNKEN)
    F4.place(x=180,y=200,width=1130,height=500 )
    lb_search_btn=Button(root4,text="Search", bd=6, relief=GROOVE,command=search1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
    lb_search_btn.place(x=180 ,y=163, height=30,width=200,anchor="w")
    lb_clear_btn=Button(root4,text="Clear", bd=6, relief=GROOVE,command=clear3,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
    lb_clear_btn.place(x=1110 ,y=163, height=30, width=200,anchor="w")
    Table_Frame=Frame(F4,bd=4, relief=RIDGE,bg="#000000")
    Table_Frame.place(x=15,y=0,width=1080,height=480)
    style=ttk.Style(Table_Frame)
    style.configure("Treeview",background="black",fieldbackground="black",foreground="white")
    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
    global Vaci_table
    Vaci_table=ttk.Treeview(Table_Frame,columns=('HosId', 'ACEKQ', 'BFGLS', 'CGHMT', 'DHINU', 'EIJOV', 'FJKPW', 'GKLQX', 'HLMRY', 'IMNSZ', 'ABCDA', 'BCDEB', 'CDEFC', 'DEFGD', 'EFGHE', 'FGHIF', 'GHIJG', 'HIJKH', 'IJKLI', 'JKLMJ', 'KLMNK', 'LMNOL', 'MNOPM', 'NOPQN', 'OPQRO', 'PQRSP', 'QRSTQ', 'RSTUR', 'STUVS', 'TUVWT', 'UVWXU', 'VWXYV', 'ABCDE', 'BCDEF', 'CDEFG', 'DEFGH', 'EFGHI', 'FGHIJ', 'GHIJK', 'HIJKL', 'IJKLM', 'JKLMN', 'KLMNO', 'LMNOP', 'MNOPQ', 'NOPQR', 'OPQRS', 'PQRST', 'QRSTU', 'RSTUV', 'STUVW', 'TUVWX', 'UVWXY', 'VWXYZ', 'AAAAB', 'BBBBC', 'CCCCD', 'DDDDE', 'EEEEF', 'FFFFG', 'GGGGH', 'HHHHI', 'IIIIJ', 'JJJJK', 'KKKKL', 'LLLLM', 'MMMMN', 'NNNNO', 'OOOOP', 'PPPPQ', 'QQQQR', 'RRRRS', 'SSSST', 'TTTTU', 'UUUUV', 'VVVVW', 'WWWWX', 'XXXXY', 'QAAAC', 'RBBBD', 'SCCCE', 'TDDDF', 'UEEEG', 'VFFFH', 'WGGGI', 'XHHHJ', 'YIIIK', 'ZJJJL', 'BJJJL', 'CKKKM', 'DLLLN', 'EMMMO', 'FNNNP', 'GOOOQ', 'HPPPR', 'IQQQS', 'JRRRT', 'KSSSU', 'LTTTV', 'MUUUW', 'NVVVX', 'OWWWY', 'PXXXZ', 'BBAAC', 'CCBBD', 'DDCCE', 'EEDDF', 'FFEEG', 'GGFFH', 'HHGGI', 'IIHHJ', 'JJIIK', 'KKJJL', 'LLKKM', 'MMLLN', 'NNMMO', 'OONNP', 'PPOOQ', 'QQPPR', 'RRQQS', 'SSRRT', 'TTSSU', 'UUTTV', 'VVUUW', 'WWVVX', 'XXWWY', 'YYXXZ', 'AADAA', 'BBEBB', 'CCFCC', 'DDGDD', 'EEHEE', 'FFIFF', 'GGJGG', 'HHKHH', 'IILII', 'JJMJJ', 'KKNKK', 'LLOLL', 'MMPMM', 'NNQNN', 'OOROO', 'PPSPP', 'QQTQQ', 'RRURR', 'SSVSS', 'TTWTT', 'UUXUU', 'VVYVV', 'WWZWW'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Vaci_table.xview)
    scroll_y.config(command=Vaci_table.yview)
    Vaci_table.column("HosId", width=100)
    Vaci_table.column("ACEKQ", width=100)
    Vaci_table.column("BFGLS", width=100)
    Vaci_table.column("CGHMT", width=100)
    Vaci_table.column("DHINU", width=100)
    Vaci_table.column("EIJOV", width=100)
    Vaci_table.column("FJKPW", width=100)
    Vaci_table.column("GKLQX", width=100)
    Vaci_table.column("HLMRY", width=100)
    Vaci_table.column("IMNSZ", width=100)
    Vaci_table.column("ABCDA", width=100)
    Vaci_table.column("BCDEB", width=100)
    Vaci_table.column("CDEFC", width=100)
    Vaci_table.column("DEFGD", width=100)
    Vaci_table.column("EFGHE", width=100)
    Vaci_table.column("FGHIF", width=100)
    Vaci_table.column("GHIJG", width=100)
    Vaci_table.column("HIJKH", width=100)
    Vaci_table.column("IJKLI", width=100)
    Vaci_table.column("JKLMJ", width=100)
    Vaci_table.column("KLMNK", width=100)
    Vaci_table.column("LMNOL", width=100)
    Vaci_table.column("MNOPM", width=100)
    Vaci_table.column("NOPQN", width=100)
    Vaci_table.column("OPQRO", width=100)
    Vaci_table.column("PQRSP", width=100)
    Vaci_table.column("QRSTQ", width=100)
    Vaci_table.column("RSTUR", width=100)
    Vaci_table.column("STUVS", width=100)
    Vaci_table.column("TUVWT", width=100)
    Vaci_table.column("UVWXU", width=100)
    Vaci_table.column("VWXYV", width=100)
    Vaci_table.column("ABCDE", width=100)
    Vaci_table.column("BCDEF", width=100)
    Vaci_table.column("CDEFG", width=100)
    Vaci_table.column("DEFGH", width=100)
    Vaci_table.column("EFGHI", width=100)
    Vaci_table.column("FGHIJ", width=100)
    Vaci_table.column("GHIJK", width=100)
    Vaci_table.column("HIJKL", width=100)
    Vaci_table.column("IJKLM", width=100)
    Vaci_table.column("JKLMN", width=100)
    Vaci_table.column("KLMNO", width=100)
    Vaci_table.column("LMNOP", width=100)
    Vaci_table.column("MNOPQ", width=100)
    Vaci_table.column("NOPQR", width=100)
    Vaci_table.column("OPQRS", width=100)
    Vaci_table.column("PQRST", width=100)
    Vaci_table.column("QRSTU", width=100)
    Vaci_table.column("RSTUV", width=100)
    Vaci_table.column("STUVW", width=100)
    Vaci_table.column("TUVWX", width=100)
    Vaci_table.column("UVWXY", width=100)
    Vaci_table.column("VWXYZ", width=100)
    Vaci_table.column("AAAAB", width=100)
    Vaci_table.column("BBBBC", width=100)
    Vaci_table.column("CCCCD", width=100)
    Vaci_table.column("DDDDE", width=100)
    Vaci_table.column("EEEEF", width=100)
    Vaci_table.column("FFFFG", width=100)
    Vaci_table.column("GGGGH", width=100)
    Vaci_table.column("HHHHI", width=100)
    Vaci_table.column("IIIIJ", width=100)
    Vaci_table.column("JJJJK", width=100)
    Vaci_table.column("KKKKL", width=100)
    Vaci_table.column("LLLLM", width=100)
    Vaci_table.column("MMMMN", width=100)
    Vaci_table.column("NNNNO", width=100)
    Vaci_table.column("OOOOP", width=100)
    Vaci_table.column("PPPPQ", width=100)
    Vaci_table.column("QQQQR", width=100)
    Vaci_table.column("RRRRS", width=100)
    Vaci_table.column("SSSST", width=100)
    Vaci_table.column("TTTTU", width=100)
    Vaci_table.column("UUUUV", width=100)
    Vaci_table.column("VVVVW", width=100)
    Vaci_table.column("WWWWX", width=100)
    Vaci_table.column("XXXXY", width=100)
    Vaci_table.column("QAAAC", width=100)
    Vaci_table.column("RBBBD", width=100)
    Vaci_table.column("SCCCE", width=100)
    Vaci_table.column("TDDDF", width=100)
    Vaci_table.column("UEEEG", width=100)
    Vaci_table.column("VFFFH", width=100)
    Vaci_table.column("WGGGI", width=100)
    Vaci_table.column("XHHHJ", width=100)
    Vaci_table.column("YIIIK", width=100)
    Vaci_table.column("ZJJJL", width=100)
    Vaci_table.column("BJJJL", width=100)
    Vaci_table.column("CKKKM", width=100)
    Vaci_table.column("DLLLN", width=100)
    Vaci_table.column("EMMMO", width=100)
    Vaci_table.column("FNNNP", width=100)
    Vaci_table.column("GOOOQ", width=100)
    Vaci_table.column("HPPPR", width=100)
    Vaci_table.column("IQQQS", width=100)
    Vaci_table.column("JRRRT", width=100)
    Vaci_table.column("KSSSU", width=100)
    Vaci_table.column("LTTTV", width=100)
    Vaci_table.column("MUUUW", width=100)
    Vaci_table.column("NVVVX", width=100)
    Vaci_table.column("OWWWY", width=100)
    Vaci_table.column("PXXXZ", width=100)
    Vaci_table.column("BBAAC", width=100)
    Vaci_table.column("CCBBD", width=100)
    Vaci_table.column("DDCCE", width=100)
    Vaci_table.column("EEDDF", width=100)
    Vaci_table.column("FFEEG", width=100)
    Vaci_table.column("GGFFH", width=100)
    Vaci_table.column("HHGGI", width=100)
    Vaci_table.column("IIHHJ", width=100)
    Vaci_table.column("JJIIK", width=100)
    Vaci_table.column("KKJJL", width=100)
    Vaci_table.column("LLKKM", width=100)
    Vaci_table.column("MMLLN", width=100)
    Vaci_table.column("NNMMO", width=100)
    Vaci_table.column("OONNP", width=100)
    Vaci_table.column("PPOOQ", width=100)
    Vaci_table.column("QQPPR", width=100)
    Vaci_table.column("RRQQS", width=100)
    Vaci_table.column("SSRRT", width=100)
    Vaci_table.column("TTSSU", width=100)
    Vaci_table.column("UUTTV", width=100)
    Vaci_table.column("VVUUW", width=100)
    Vaci_table.column("WWVVX", width=100)
    Vaci_table.column("XXWWY", width=100)
    Vaci_table.column("YYXXZ", width=100)
    Vaci_table.column("AADAA", width=100)
    Vaci_table.column("BBEBB", width=100)
    Vaci_table.column("CCFCC", width=100)
    Vaci_table.column("DDGDD", width=100)
    Vaci_table.column("EEHEE", width=100)
    Vaci_table.column("FFIFF", width=100)
    Vaci_table.column("GGJGG", width=100)
    Vaci_table.column("HHKHH", width=100)
    Vaci_table.column("IILII", width=100)
    Vaci_table.column("JJMJJ", width=100)
    Vaci_table.column("KKNKK", width=100)
    Vaci_table.column("LLOLL", width=100)
    Vaci_table.column("MMPMM", width=100)
    Vaci_table.column("NNQNN", width=100)
    Vaci_table.column("OOROO", width=100)
    Vaci_table.column("PPSPP", width=100)
    Vaci_table.column("QQTQQ", width=100)
    Vaci_table.column("RRURR", width=100)
    Vaci_table.column("SSVSS", width=100)
    Vaci_table.column("TTWTT", width=100)
    Vaci_table.column("UUXUU", width=100)
    Vaci_table.column("VVYVV", width=100)
    Vaci_table.column("WWZWW", width=100)
    clock()

    root4. mainloop()

global search1
def search1():
    global Vaci_table
    Vaci_table.heading("HosId", text="HosId")
    Vaci_table.heading("ACEKQ", text="ACEKQ")
    Vaci_table.heading("BFGLS", text="BFGLS")
    Vaci_table.heading("CGHMT", text="CGHMT")
    Vaci_table.heading("DHINU", text="DHINU")
    Vaci_table.heading("EIJOV", text="EIJOV")
    Vaci_table.heading("FJKPW", text="FJKPW")
    Vaci_table.heading("GKLQX", text="GKLQX")
    Vaci_table.heading("HLMRY", text="HLMRY")
    Vaci_table.heading("IMNSZ", text="IMNSZ")
    Vaci_table.heading("ABCDA", text="ABCDA")
    Vaci_table.heading("BCDEB", text="BCDEB")
    Vaci_table.heading("CDEFC", text="CDEFC")
    Vaci_table.heading("DEFGD", text="DEFGD")
    Vaci_table.heading("EFGHE", text="EFGHE")
    Vaci_table.heading("FGHIF", text="FGHIF")
    Vaci_table.heading("GHIJG", text="GHIJG")
    Vaci_table.heading("HIJKH", text="HIJKH")
    Vaci_table.heading("IJKLI", text="IJKLI")
    Vaci_table.heading("JKLMJ", text="JKLMJ")
    Vaci_table.heading("KLMNK", text="KLMNK")
    Vaci_table.heading("LMNOL", text="LMNOL")
    Vaci_table.heading("MNOPM", text="MNOPM")
    Vaci_table.heading("NOPQN", text="NOPQN")
    Vaci_table.heading("OPQRO", text="OPQRO")
    Vaci_table.heading("PQRSP", text="PQRSP")
    Vaci_table.heading("QRSTQ", text="QRSTQ")
    Vaci_table.heading("RSTUR", text="RSTUR")
    Vaci_table.heading("STUVS", text="STUVS")
    Vaci_table.heading("TUVWT", text="TUVWT")
    Vaci_table.heading("UVWXU", text="UVWXU")
    Vaci_table.heading("VWXYV", text="VWXYV")
    Vaci_table.heading("ABCDE", text="ABCDE")
    Vaci_table.heading("BCDEF", text="BCDEF")
    Vaci_table.heading("CDEFG", text="CDEFG")
    Vaci_table.heading("DEFGH", text="DEFGH")
    Vaci_table.heading("EFGHI", text="EFGHI")
    Vaci_table.heading("FGHIJ", text="FGHIJ")
    Vaci_table.heading("GHIJK", text="GHIJK")
    Vaci_table.heading("HIJKL", text="HIJKL")
    Vaci_table.heading("IJKLM", text="IJKLM")
    Vaci_table.heading("JKLMN", text="JKLMN")
    Vaci_table.heading("KLMNO", text="KLMNO")
    Vaci_table.heading("LMNOP", text="LMNOP")
    Vaci_table.heading("MNOPQ", text="MNOPQ")
    Vaci_table.heading("NOPQR", text="NOPQR")
    Vaci_table.heading("OPQRS", text="OPQRS")
    Vaci_table.heading("PQRST", text="PQRST")
    Vaci_table.heading("QRSTU", text="QRSTU")
    Vaci_table.heading("RSTUV", text="RSTUV")
    Vaci_table.heading("STUVW", text="STUVW")
    Vaci_table.heading("TUVWX", text="TUVWX")
    Vaci_table.heading("UVWXY", text="UVWXY")
    Vaci_table.heading("VWXYZ", text="VWXYZ")
    Vaci_table.heading("AAAAB", text="AAAAB")
    Vaci_table.heading("BBBBC", text="BBBBC")
    Vaci_table.heading("CCCCD", text="CCCCD")
    Vaci_table.heading("DDDDE", text="DDDDE")
    Vaci_table.heading("EEEEF", text="EEEEF")
    Vaci_table.heading("FFFFG", text="FFFFG")
    Vaci_table.heading("GGGGH", text="GGGGH")
    Vaci_table.heading("HHHHI", text="HHHHI")
    Vaci_table.heading("IIIIJ", text="IIIIJ")
    Vaci_table.heading("JJJJK", text="JJJJK")
    Vaci_table.heading("KKKKL", text="KKKKL")
    Vaci_table.heading("LLLLM", text="LLLLM")
    Vaci_table.heading("MMMMN", text="MMMMN")
    Vaci_table.heading("NNNNO", text="NNNNO")
    Vaci_table.heading("OOOOP", text="OOOOP")
    Vaci_table.heading("PPPPQ", text="PPPPQ")
    Vaci_table.heading("QQQQR", text="QQQQR")
    Vaci_table.heading("RRRRS", text="RRRRS")
    Vaci_table.heading("SSSST", text="SSSST")
    Vaci_table.heading("TTTTU", text="TTTTU")
    Vaci_table.heading("UUUUV", text="UUUUV")
    Vaci_table.heading("VVVVW", text="VVVVW")
    Vaci_table.heading("WWWWX", text="WWWWX")
    Vaci_table.heading("XXXXY", text="XXXXY")
    Vaci_table.heading("QAAAC", text="QAAAC")
    Vaci_table.heading("RBBBD", text="RBBBD")
    Vaci_table.heading("SCCCE", text="SCCCE")
    Vaci_table.heading("TDDDF", text="TDDDF")
    Vaci_table.heading("UEEEG", text="UEEEG")
    Vaci_table.heading("VFFFH", text="VFFFH")
    Vaci_table.heading("WGGGI", text="WGGGI")
    Vaci_table.heading("XHHHJ", text="XHHHJ")
    Vaci_table.heading("YIIIK", text="YIIIK")
    Vaci_table.heading("ZJJJL", text="ZJJJL")
    Vaci_table.heading("BJJJL", text="BJJJL")
    Vaci_table.heading("CKKKM", text="CKKKM")
    Vaci_table.heading("DLLLN", text="DLLLN")
    Vaci_table.heading("EMMMO", text="EMMMO")
    Vaci_table.heading("FNNNP", text="FNNNP")
    Vaci_table.heading("GOOOQ", text="GOOOQ")
    Vaci_table.heading("HPPPR", text="HPPPR")
    Vaci_table.heading("IQQQS", text="IQQQS")
    Vaci_table.heading("JRRRT", text="JRRRT")
    Vaci_table.heading("KSSSU", text="KSSSU")
    Vaci_table.heading("LTTTV", text="LTTTV")
    Vaci_table.heading("MUUUW", text="MUUUW")
    Vaci_table.heading("NVVVX", text="NVVVX")
    Vaci_table.heading("OWWWY", text="OWWWY")
    Vaci_table.heading("PXXXZ", text="PXXXZ")
    Vaci_table.heading("BBAAC", text="BBAAC")
    Vaci_table.heading("CCBBD", text="CCBBD")
    Vaci_table.heading("DDCCE", text="DDCCE")
    Vaci_table.heading("EEDDF", text="EEDDF")
    Vaci_table.heading("FFEEG", text="FFEEG")
    Vaci_table.heading("GGFFH", text="GGFFH")
    Vaci_table.heading("HHGGI", text="HHGGI")
    Vaci_table.heading("IIHHJ", text="IIHHJ")
    Vaci_table.heading("JJIIK", text="JJIIK")
    Vaci_table.heading("KKJJL", text="KKJJL")
    Vaci_table.heading("LLKKM", text="LLKKM")
    Vaci_table.heading("MMLLN", text="MMLLN")
    Vaci_table.heading("NNMMO", text="NNMMO")
    Vaci_table.heading("OONNP", text="OONNP")
    Vaci_table.heading("PPOOQ", text="PPOOQ")
    Vaci_table.heading("QQPPR", text="QQPPR")
    Vaci_table.heading("RRQQS", text="RRQQS")
    Vaci_table.heading("SSRRT", text="SSRRT")
    Vaci_table.heading("TTSSU", text="TTSSU")
    Vaci_table.heading("UUTTV", text="UUTTV")
    Vaci_table.heading("VVUUW", text="VVUUW")
    Vaci_table.heading("WWVVX", text="WWVVX")
    Vaci_table.heading("XXWWY", text="XXWWY")
    Vaci_table.heading("YYXXZ", text="YYXXZ")
    Vaci_table.heading("AADAA", text="AADAA")
    Vaci_table.heading("BBEBB", text="BBEBB")
    Vaci_table.heading("CCFCC", text="CCFCC")
    Vaci_table.heading("DDGDD", text="DDGDD")
    Vaci_table.heading("EEHEE", text="EEHEE")
    Vaci_table.heading("FFIFF", text="FFIFF")
    Vaci_table.heading("GGJGG", text="GGJGG")
    Vaci_table.heading("HHKHH", text="HHKHH")
    Vaci_table.heading("IILII", text="IILII")
    Vaci_table.heading("JJMJJ", text="JJMJJ")
    Vaci_table.heading("KKNKK", text="KKNKK")
    Vaci_table.heading("LLOLL", text="LLOLL")
    Vaci_table.heading("MMPMM", text="MMPMM")
    Vaci_table.heading("NNQNN", text="NNQNN")
    Vaci_table.heading("OOROO", text="OOROO")
    Vaci_table.heading("PPSPP", text="PPSPP")
    Vaci_table.heading("QQTQQ", text="QQTQQ")
    Vaci_table.heading("RRURR", text="RRURR")
    Vaci_table.heading("SSVSS", text="SSVSS")
    Vaci_table.heading("TTWTT", text="TTWTT")
    Vaci_table.heading("UUXUU", text="UUXUU")
    Vaci_table.heading("VVYVV", text="VVYVV")
    Vaci_table.heading("WWZWW", text="WWZWW")
    Vaci_table['show']='headings'

    Vaci_table.pack(fill=BOTH,expand=1)
    Vaci_table.bind("<ButtonRelease-1>",getcursor1)
    fetch_data1()

global fetch_data1
def fetch_data1():
    global Vaci_table
    try:
        conn=sqlite3.connect("vacisearch.db")
        c=conn.cursor()
        c.execute("select * from vaci")
        rows=c.fetchall()
        if len(rows)!=0:
                Vaci_table.delete(*Vaci_table.get_children())
                for row in rows:
                        Vaci_table.insert('',END,values=row)
                conn.commit()
        conn.close()
    except Exception:
        return messagebox.showerror("Error","Something Wrong")

global getcursor1
def getcursor1(ev):
    global Vaci_table
    cursor_row=Vaci_table.focus()
    Content=Vaci_table.item(cursor_row)
    row=Content['values']
    print(row)
    HosId.set(row[0])
    ACEKQ.set(row[1])
    BFGLS.set(row[2])
    CGHMT.set(row[3])
    DHINU.set(row[4])
    EIJOV.set(row[5])
    FJKPW.set(row[6])
    GKLQX.set(row[7])
    HLMRY.set(row[8])
    IMNSZ.set(row[9])
    ABCDA.set(row[10])
    BCDEB.set(row[11])
    CDEFC.set(row[12])
    DEFGD.set(row[13])
    EFGHE.set(row[14])
    FGHIF.set(row[15])
    GHIJG.set(row[16])
    HIJKH.set(row[17])
    IJKLI.set(row[18])
    JKLMJ.set(row[19])
    KLMNK.set(row[20])
    LMNOL.set(row[21])
    MNOPM.set(row[22])
    NOPQN.set(row[23])
    OPQRO.set(row[24])
    PQRSP.set(row[25])
    QRSTQ.set(row[26])
    RSTUR.set(row[27])
    STUVS.set(row[28])
    TUVWT.set(row[29])
    UVWXU.set(row[30])
    VWXYV.set(row[31])
    ABCDE.set(row[32])
    BCDEF.set(row[33])
    CDEFG.set(row[34])
    DEFGH.set(row[35])
    EFGHI.set(row[36])
    FGHIJ.set(row[37])
    GHIJK.set(row[38])
    HIJKL.set(row[39])
    IJKLM.set(row[40])
    JKLMN.set(row[41])
    KLMNO.set(row[42])
    LMNOP.set(row[43])
    MNOPQ.set(row[44])
    NOPQR.set(row[45])
    OPQRS.set(row[46])
    PQRST.set(row[47])
    QRSTU.set(row[48])
    RSTUV.set(row[49])
    STUVW.set(row[50])
    TUVWX.set(row[51])
    UVWXY.set(row[52])
    VWXYZ.set(row[53])
    AAAAB.set(row[54])
    BBBBC.set(row[55])
    CCCCD.set(row[56])
    DDDDE.set(row[57])
    EEEEF.set(row[58])
    FFFFG.set(row[59])
    GGGGH.set(row[60])
    HHHHI.set(row[61])
    IIIIJ.set(row[62])
    JJJJK.set(row[63])
    KKKKL.set(row[64])
    LLLLM.set(row[65])
    MMMMN.set(row[66])
    NNNNO.set(row[67])
    OOOOP.set(row[68])
    PPPPQ.set(row[69])
    QQQQR.set(row[70])
    RRRRS.set(row[71])
    SSSST.set(row[72])
    TTTTU.set(row[73])
    UUUUV.set(row[74])
    VVVVW.set(row[75])
    WWWWX.set(row[76])
    XXXXY.set(row[77])
    QAAAC.set(row[78])
    RBBBD.set(row[79])
    SCCCE.set(row[80])
    TDDDF.set(row[81])
    UEEEG.set(row[82])
    VFFFH.set(row[83])
    WGGGI.set(row[84])
    XHHHJ.set(row[85])
    YIIIK.set(row[86])
    ZJJJL.set(row[87])
    BJJJL.set(row[88])
    CKKKM.set(row[89])
    DLLLN.set(row[90])
    EMMMO.set(row[91])
    FNNNP.set(row[92])
    GOOOQ.set(row[93])
    HPPPR.set(row[94])
    IQQQS.set(row[95])
    JRRRT.set(row[96])
    KSSSU.set(row[97])
    LTTTV.set(row[98])
    MUUUW.set(row[99])
    NVVVX.set(row[100])
    OWWWY.set(row[101])
    PXXXZ.set(row[102])
    BBAAC.set(row[103])
    CCBBD.set(row[104])
    DDCCE.set(row[105])
    EEDDF.set(row[106])
    FFEEG.set(row[107])
    GGFFH.set(row[108])
    HHGGI.set(row[109])
    IIHHJ.set(row[110])
    JJIIK.set(row[111])
    KKJJL.set(row[112])
    LLKKM.set(row[113])
    MMLLN.set(row[114])
    NNMMO.set(row[115])
    OONNP.set(row[116])
    PPOOQ.set(row[117])
    QQPPR.set(row[118])
    RRQQS.set(row[119])
    SSRRT.set(row[120])
    TTSSU.set(row[121])
    UUTTV.set(row[122])
    VVUUW.set(row[123])
    WWVVX.set(row[124])
    XXWWY.set(row[125])
    YYXXZ.set(row[126])
    AADAA.set(row[127])
    BBEBB.set(row[128])
    CCFCC.set(row[129])
    DDGDD.set(row[130])
    EEHEE.set(row[131])
    FFIFF.set(row[132])
    GGJGG.set(row[133])
    HHKHH.set(row[134])
    IILII.set(row[135])
    JJMJJ.set(row[136])
    KKNKK.set(row[137])
    LLOLL.set(row[138])
    MMPMM.set(row[139])
    NNQNN.set(row[140])
    OOROO.set(row[141])
    PPSPP.set(row[142])
    QQTQQ.set(row[143])
    RRURR.set(row[144])
    SSVSS.set(row[145])
    TTWTT.set(row[146])
    UUXUU.set(row[147])
    VVYVV.set(row[148])
    WWZWW.set(row[149])

global Name_V_Search1
def Name_V_Search1():
    Exit4()
    global root4
    root4 = Tk()    
    root4.title("Login User".center(420))  
    root4.configure(background="black")  
    root4.geometry("1360x768+0+0")
    bg_color = "#e0b0ff"
    global searchby, searchval
    searchby = StringVar()
    searchval = StringVar()
    bg_icon = ImageTk.PhotoImage(file="PICs\\81736244-cell-background-with-futuristic-interface-elements-hud-ui-for-medical-app-futuristic-user-interface-.jpg")
    bg_lbl = Label(root4, image = bg_icon).pack(fill=Y) # we put image into our window
    hos_icon=ImageTk.PhotoImage(file="PICs\\image2(1).png")
    home_icon=ImageTk.PhotoImage(file="PICs\\Home.png")
    view_vacci_icon=ImageTk.PhotoImage(file="PICs\\View_Vacci.png")
    view_icon=ImageTk.PhotoImage(file="PICs\\View_All_dark.png")
    manage_icon=ImageTk.PhotoImage(file="PICs\\Manage.jpg")
    exit_icon=ImageTk.PhotoImage(file="PICs\\Exit.png")
    global lbl_hr, lbl_min, lbl_sec, lbl_abv
    F1 = LabelFrame(root4,bd=10,relief=GROOVE,bg=bg_color)
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
    btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=ChangePassword1).place(x=1145,y=20,anchor="w")
    btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=logout1).place(x=1145,y=60,anchor="w")
    lbl2 = Label(F1,image=hos_icon,bg=bg_color)
    lbl2.place(x=25,y=10)
    F2 = LabelFrame(root4,bd=10,relief=GROOVE,bg=bg_color)
    F2.place(x=0,y=100,width=150,height=670 )
    F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F21.place(x=0,y=0,width=130,height=150 )
    F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F22.place(x=0,y=150,width=130,height=150)
    F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F23.place(x=0,y=300,width=130,height=150 )
    F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F24.place(x=0,y=450,width=130,height=150)
    btn_home = Button(F21,image= home_icon,bg=bg_color,relief=RAISED,width =115,height=140,command=Home1).place(x=0,y=67,anchor="w")
    btn_view_vacci = Button(F22,image= view_vacci_icon,bg=bg_color,relief=RAISED,width =115,height=140,command=View_Vaci1).place(x=0,y=67,anchor="w")
    btn_view = Button(F23,relief=RAISED,bg=bg_color,image=view_icon,width =115,height=140,command=Name_V_Search1).place(x=0,y=67,anchor="w")
    btn_Exit = Button(F24,relief=RAISED,bg=bg_color,image=exit_icon,width =115,height=140,command=Exit4).place(x=0,y=67,anchor="w")
    F3 = LabelFrame(root4,bd=5,relief=FLAT,bg="light gray")
    F3.place(x=150,y=100,relwidth=1,height=30 )
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    with open("Temp.txt","r+") as file:
        read1=file.read()
    lbl_1= Label(F3,text="Dashboard / User"+": UName : "+str(read1),font=("comic sans",15,"italic"),bg="light gray")
    lbl_1.place(x=0,y=0)
    
    lb_search=Label(root4,text="Search By", font=("times new roman",15,"bold"))
    lb_search.place(x=180 ,y=165, anchor="w")
    combo_search=ttk.Combobox(root4, textvariable=searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
    combo_search['values']=("CVX_Code")
    combo_search.place(x=273, y=165, anchor="w")

    search1 = Entry(root4, bd=5,textvariable=searchval, bg="lightgrey", font=("times new roman", 18))
    search1.place(x=490, y=150,width=200, height=30)

    F4 =Frame(root4,bd=10,relief=SUNKEN)
    F4.place(x=180,y=200,width=1130,height=500 )
    
    
    lb_search_btn=Button(root4,text="Search", bd=6, relief=GROOVE,command=search2,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
    lb_search_btn.place(x=700 ,y=165, height=30,width=200,anchor="w")
    
    lb_clear_btn=Button(root4,text="Clear", bd=6, relief=GROOVE,command=clear4,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
    lb_clear_btn.place(x=1110 ,y=163, height=30, width=200,anchor="w")

    Table_Frame=Frame(F4,bd=4, relief=RIDGE,bg="#000000")
    Table_Frame.place(x=15,y=0,width=1080,height=480)
    style=ttk.Style(Table_Frame)
    style.configure("Treeview",background="black",fieldbackground="black",foreground="white")


    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
    global vaccineseaech_table
    vaccineseaech_table=ttk.Treeview(Table_Frame,columns=("Vacci_Product_ID","product_TBL","CVX_Short_Description","CVX_Code","manufacturer_TBL","manufacturer_TBL_MVX_CODE","MVX_status","product_name_status","product_TBL_Update_date"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=vaccineseaech_table.xview)
    scroll_y.config(command=vaccineseaech_table.yview)

    
    vaccineseaech_table.column("Vacci_Product_ID", width=150)
    vaccineseaech_table.column("product_TBL", width=150)
    vaccineseaech_table.column("CVX_Short_Description", width=150)
    vaccineseaech_table.column("CVX_Code", width=150)
    vaccineseaech_table.column("manufacturer_TBL", width=150)
    vaccineseaech_table.column("manufacturer_TBL_MVX_CODE", width=150)
    vaccineseaech_table.column("MVX_status", width=150)
    vaccineseaech_table.column("product_name_status", width=150)
    vaccineseaech_table.column("product_TBL_Update_date", width=150)

    vaccineseaech_table.bind("<ButtonRelease-1>",getcursor2)
    
    fetch_data2()
    clock()
    root4.mainloop()

global search2
def search2():
    global vaccineseaech_table
    vaccineseaech_table.heading("Vacci_Product_ID",text="Vacci_Product_ID")
    vaccineseaech_table.heading("product_TBL",text="product_TBL")
    vaccineseaech_table.heading("CVX_Short_Description",text="CVX_Short_Description")
    vaccineseaech_table.heading("CVX_Code",text="CVX_Code")
    vaccineseaech_table.heading("manufacturer_TBL",text="manufacturer_TBL")
    vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="manufacturer_TBL_MVX_CODE")
    vaccineseaech_table.heading("MVX_status",text="MVX_status")
    vaccineseaech_table.heading("product_name_status",text="product_name_status")
    vaccineseaech_table.heading("product_TBL_Update_date",text="product_TBL_Update_date")
    vaccineseaech_table['show']='headings'

    search_data1()

global search_data1
def search_data1():
    global searchby, searchval 
    print(searchby.get(),searchval.get())
    if searchby.get()=="" and searchval.get()=="":
        return messagebox.showwarning("Warning","Fields should be filled")
    if searchby.get()=="" :
        return messagebox.showwarning("Warning","Shearch By Option Should be filled")
    if searchval.get()=="":
        return messagebox.showwarning("Warning","Search box should be filled")
    
    else:
        if searchby.get() == "CVX_Code":
            try:
                conn=sqlite3.connect("vacisearch.db")
                c=conn.cursor()
                c.execute("SELECT * from vaci_info where CVX_Code="+searchval.get())
                rows=c.fetchall()
                if len(rows)!=0:
                    vaccineseaech_table.delete(*vaccineseaech_table.get_children())
                    for row in rows:
                            vaccineseaech_table.insert('',END,values=row)
                    conn.commit()
                    conn.close()
                                
                    vaccineseaech_table.pack(fill=BOTH,expand=1)
                    vaccineseaech_table.bind("<ButtonRelease-1>",getcursor2)
                else:
                    return messagebox.showerror("Error","CVX_Code Not Exist")        
            except Exception:
                return messagebox.showerror("Error", "Something Wrong")

global fetch_data2
def fetch_data2():
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    c.execute("select * from vaci_info")
    rows=c.fetchall()
    if len(rows)!=0:
            vaccineseaech_table.delete(*vaccineseaech_table.get_children())
            for row in rows:
                    vaccineseaech_table.insert('',END,values=row)
            conn.commit()
    conn.close()

global getcursor2
def getcursor2(ev):
    cursor_row=vaccineseaech_table.focus()
    Content=vaccineseaech_table.item(cursor_row)
    row=Content['values']
    #print(row)
    Product_ID.set(row[0])
    product_TBL.set(row[1])
    CVX_Short_Description.set(row[2])
    CVX_Code.set(row[3])
    manufacturer_TBL.set(row[4])
    manufacturer_TBL_MVX_CODE.set(row[5])
    MVX_status.set(row[6])
    product_name_status.set(row[7])
    product_TBL_Update_date.set(row[8])
    
global Data_update
def Data_update():
    print(len(PID.get()))
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    y= f"UPDATE vaci_info SET CVX_Code = {str(CVX_Code.get())} WHERE Vacci_Product_ID = {str(PID.get())}"
    c.execute(str(y))
    #c.execute("SELECT * from vaci_info WHERE Vacci_Product_ID="+str(PID.get()))
    #data=c.fetchall()
    #print(data)
    #if data:
    #        for i in data:
    #            print(i)
    #        a=(str(i[4])) 
    #        print (a)
    #        print(type(a)) 
    #        print("True")
    #        y= f"UPDATE Hospital SET pasw = {str(PID.get())} WHERE Vacci_Product_ID = {str(CVX_Code.get())}"
    #        c.execute(str(y))
                        
            #sql = ''' UPDATE vaci_info SET priority = ? , product_TBL = ?, CVX_Short_Description = ?, CVX_Code = ?,manufacturer_TBL = ?, manufacturer_TBL_MVX_CODE = ? , MVX_status = ?, product_name_status = ?, product_TBL_Update_date  = ?, WHERE Vacci_Product_ID = ?'''
            #task=(PID.get(),product_TBL.get(),CVX_S_D.get(),CVX_Code.get(),Manuf_TBL.get(),Manuf_TBL_Code.get(),MVX_Status.get(),P_N_S.get(),P_T_U_D.get())
            #c.execute(sql, task)
            #y=\
            #"""UPDATE vaci_info SET Vacci_Product_ID=\"""" +PID.get()+\
            #"""\" , product_TBL   =\""""+ product_get.get()+\
            #"""\" , CVX_Short_Description    =\""""+ CVX_S_D.get()+\
            #"""\" , CVX_Code   =\""""+ CVX_Code.get()+\
            #"""\" , manufacturer_TBL =\""""+ Manuf_TBL.get()+\
            #"""\" , manufacturer_TBL_MVX_CODE  =\""""+ Manuf_TBL_Code.get() +\
            #"""\" , MVX_status    =\""""+MVX_Status.get()  +\
            #"""\" , product_name_status  =\""""+ P_N_S.get() +\
            #"""\" , product_TBL_Update_date   =\""""+ P_T_U_D.get()+\
            #""" \""""
            #y=y+" WHERE Vacci_Product_ID= "+PDI.get()
            #print(str(y))              
    #c.execute(y)
    conn.commit()
    return messagebox.showinfo("Successful"," Data  Updated")
    conn.close()
    #else:
    #    return messagebox.showerror("Error","Roll No not Matched")

global Home1
def Home1():
    root4.destroy()
    Login_win1()

global Home2
def Home2():
    root3.destroy()
    Login_win2()

global logout1
def logout1():
    root4.destroy()
    GUI()

global logout2
def logout2():
    root3.destroy()
    HosGUI()

global View_Vaci2
def View_Vaci2():
    Exit2()
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
    btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=ChangePassword2).place(x=1145,y=20,anchor="w")
    btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=logout2).place(x=1145,y=60,anchor="w")
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
    btn_home = Button(F21,image= home_icon,bg=bg_color,relief=RAISED,width =115,height=145,command=Home2).place(x=0,y=63,anchor="w")
    btn_view = Button(F22,relief=RAISED,bg=bg_color,image=view_icon,width =115,height=145,command=View_Vaci2).place(x=0,y=63,anchor="w")
    btn_manage = Button(F23,relief=RAISED,image=manage_icon,bg=bg_color,width =115,height=145,command=Manage_Vaci).place(x=0,y=63,anchor="w")
    btn_Exit = Button(F24,relief=RAISED,bg=bg_color,image=exit_icon,width =115,height=145,command=Exit2).place(x=0,y=63,anchor="w")
    F3 = LabelFrame(root3,bd=5,relief=FLAT,bg="light gray")
    F3.place(x=150,y=100,relwidth=1,height=30 )
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    with open("Temp1.txt","r+") as file:
        read1=file.read()
    lbl_1= Label(F3,text="Dashboard / Hospital"+": HName : "+str(read1),font=("comic sans",15,"italic"),bg="light gray")
    lbl_1.place(x=0,y=0)

    F4 =Frame(root3,bd=10,relief=SUNKEN)
    F4.place(x=180,y=200,width=1130,height=500 )
    lb_search_btn=Button(root3,text="Search", bd=6, relief=GROOVE,command=search3,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
    lb_search_btn.place(x=180 ,y=163, height=30,width=200,anchor="w")
    lb_clear_btn=Button(root3,text="Clear", bd=6, relief=GROOVE,command=clear5,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
    lb_clear_btn.place(x=1110 ,y=163, height=30, width=200,anchor="w")
    Table_Frame=Frame(F4,bd=4, relief=RIDGE,bg="#000000")
    Table_Frame.place(x=15,y=0,width=1080,height=480)
    style=ttk.Style(Table_Frame)
    style.configure("Treeview",background="black",fieldbackground="black",foreground="white")

    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
    global vaccineseaech_table
    vaccineseaech_table=ttk.Treeview(Table_Frame,columns=("Vacci_Product_ID","product_TBL","CVX_Short_Description","CVX_Code","manufacturer_TBL","manufacturer_TBL_MVX_CODE","MVX_status","product_name_status","product_TBL_Update_date"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=vaccineseaech_table.xview)
    scroll_y.config(command=vaccineseaech_table.yview)

    
    vaccineseaech_table.column("Vacci_Product_ID", width=150)
    vaccineseaech_table.column("product_TBL", width=150)
    vaccineseaech_table.column("CVX_Short_Description", width=150)
    vaccineseaech_table.column("CVX_Code", width=150)
    vaccineseaech_table.column("manufacturer_TBL", width=150)
    vaccineseaech_table.column("manufacturer_TBL_MVX_CODE", width=150)
    vaccineseaech_table.column("MVX_status", width=150)
    vaccineseaech_table.column("product_name_status", width=150)
    vaccineseaech_table.column("product_TBL_Update_date", width=150)

    vaccineseaech_table.bind("<ButtonRelease-1>",getcursor3)
    
    fetch_data3()

    root3. mainloop()

global search3
def search3():
    global Vaci_table
    vaccineseaech_table.heading("Vacci_Product_ID",text="Vacci_Product_ID")
    vaccineseaech_table.heading("product_TBL",text="product_TBL")
    vaccineseaech_table.heading("CVX_Short_Description",text="CVX_Short_Description")
    vaccineseaech_table.heading("CVX_Code",text="CVX_Code")
    vaccineseaech_table.heading("manufacturer_TBL",text="manufacturer_TBL")
    vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="manufacturer_TBL_MVX_CODE")
    vaccineseaech_table.heading("MVX_status",text="MVX_status")
    vaccineseaech_table.heading("product_name_status",text="product_name_status")
    vaccineseaech_table.heading("product_TBL_Update_date",text="product_TBL_Update_date")
    vaccineseaech_table['show']='headings'
    vaccineseaech_table.pack(fill=BOTH,expand=1)
    vaccineseaech_table.bind("<ButtonRelease-1>",getcursor3)
    fetch_data3()

global fetch_data3
def fetch_data3():
    global vaccineseaech_table
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    c.execute("select * from vaci_info")
    rows=c.fetchall()
    if len(rows)!=0:
            vaccineseaech_table.delete(*vaccineseaech_table.get_children())
            for row in rows:
                    vaccineseaech_table.insert('',END,values=row)
            conn.commit()
    conn.close()

global getcursor3
def getcursor3(ev):
    global vaccineseaech_table
    cursor_row=vaccineseaech_table.focus()
    Content=vaccineseaech_table.item(cursor_row)
    row=Content['values']
    #print(row)
    Product_ID.set(row[0])
    product_TBL.set(row[1])
    CVX_Short_Description.set(row[2])
    CVX_Code.set(row[3])
    manufacturer_TBL.set(row[4])
    manufacturer_TBL_MVX_CODE.set(row[5])
    MVX_status.set(row[6])
    product_name_status.set(row[7])
    product_TBL_Update_date.set(row[8])

global clear6
def clear6():
    a=random.randint(65,90)
    b=random.randint(65,90)
    c=random.randint(65,90)
    d=random.randint(65,90)
    e=random.randint(65,90)
    f=random.randint(65,90)
    PID.set(str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str(chr(e))+str(chr(f)))
    product_TBL.set("") 
    CVX_S_D.set("")
    CVX_Code.set("")
    Manuf_TBL.set("")
    Manuf_TBL_Code.set("")
    MVX_Status.set("Choose MVX_Status")
    P_N_S.set("Choose Product Name Status")
    P_T_U_D.set("")
    searchby.set("Choose Option")
    searchval.set("")
    vaccineseaech_table.delete(*vaccineseaech_table.get_children())
    vaccineseaech_table.heading("Vacci_Product_ID",text="")
    vaccineseaech_table.heading("product_TBL",text="")
    vaccineseaech_table.heading("CVX_Short_Description",text="")
    vaccineseaech_table.heading("CVX_Code",text="")
    vaccineseaech_table.heading("manufacturer_TBL",text="")
    vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="")
    vaccineseaech_table.heading("MVX_status",text="")
    vaccineseaech_table.heading("product_name_status",text="")
    vaccineseaech_table.heading("product_TBL_Update_date",text="")    
    vaccineseaech_table['show']='headings'

global add
def add():
    global product_TBL,CVX_S_D,Manuf_TBL_Code,MVX_Status,CVX_Code,Manuf_TBL,searchby,searchval,P_N_S,P_T_U_D,PID,a,b,c,d,e,f,label, calendar
 
    if product_TBL.get()=="" or CVX_S_D.get()=="" or Manuf_TBL_Code.get()=="" or MVX_Status.get()=="Choose MVX_Status" or CVX_Code.get()== "" or Manuf_TBL.get()=="" or P_N_S.get()=="Choose Product Name Status" or P_T_U_D.get()=="" or PID.get=="" :
        return messagebox.showerror("Error!","All Feilds Required")
    try:
        tmp=CVX_Code.get()
        int(tmp)
    except ValueError:
        return messagebox.showinfo('Error','CVX_Code Should Be Integer')
    else:
        conn=sqlite3.connect("vacisearch.db")
        c=conn.cursor()
        try:
            c.execute("INSERT INTO vaci_info (Vacci_Product_ID,product_TBL,CVX_Short_Description,CVX_Code,manufacturer_TBL,manufacturer_TBL_MVX_CODE,MVX_status,product_name_status,product_TBL_Update_date) VALUES (?,?,?,?,?,?,?,?,?)",(PID.get(),product_TBL.get(),CVX_S_D.get(),CVX_Code.get(),Manuf_TBL.get(),Manuf_TBL_Code.get(),MVX_Status.get(),P_N_S.get(),P_T_U_D.get()))
            conn.commit()
            c.close()
            conn.close()
            messagebox.showinfo("Successfull","Successfully Added Data")
            clear6()
        except Exception:
            messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
            #messagebox.showinfo("Error!!", "May be your Roll No. already exist. Please Check")        

global delete_data
def delete_data():
    try:
        conn=sqlite3.connect("vacisearch.db")
        c=conn.cursor()
        c.execute("DELETE FROM vaci_info WHERE CVX_Code = "+(str(CVX_Code.get())))
        conn.commit()
        conn.close()
        messagebox.showinfo("Info","Succesfully Deleted")
        clear6()
    except sqlite3.Error as error:
        messagebox.showerror("error","Failed to update Database table")

global Manage_Vaci
def Manage_Vaci():
    Exit2()
    global root3
    root3 = Tk()    
    root3.title("Login Hospital".center(420))  
    root3.configure(background="black")  
    root3.geometry("1360x768+0+0")
    bg_color = "#e0b0ff"
    global product_TBL,CVX_S_D,Manuf_TBL_Code,MVX_Status,CVX_Code,Manuf_TBL,searchby,searchval,P_N_S,P_T_U_D,PID,a,b,c,d,e,f,label, calendar
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
    P_N_S.set("Choose Product Name Status")
    MVX_Status.set("Choose MVX_Status")
    PID=StringVar()
    P_T_U_D=StringVar()
    a=random.randint(65,90)
    b=random.randint(65,90)
    c=random.randint(65,90)
    d=random.randint(65,90)
    e=random.randint(65,90)
    f=random.randint(65,90)
    PID.set(str(chr(a))+str(chr(b))+str(chr(c))+str(chr(d))+str(chr(e))+str(chr(f)))
    label, calendar = "",""
    bg_icon = ImageTk.PhotoImage(file="PICs\\81736244-cell-background-with-futuristic-interface-elements-hud-ui-for-medical-app-futuristic-user-interface-.jpg")
    bg_lbl = Label(root3, image = bg_icon).pack(fill=Y) # we put image into our window
    hos_icon=ImageTk.PhotoImage(file="PICs\\image2(1).png")
    home_icon=ImageTk.PhotoImage(file="PICs\\Home.png")
    view_vacci_icon=ImageTk.PhotoImage(file="PICs\\View_Vacci.png")
    view_icon=ImageTk.PhotoImage(file="PICs\\View_All_dark.png")
    manage_icon=ImageTk.PhotoImage(file="PICs\\Manage.jpg")
    exit_icon=ImageTk.PhotoImage(file="PICs\\Exit.png")
    global lbl_hr, lbl_min, lbl_sec, lbl_abv
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
    btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=ChangePassword2).place(x=1145,y=20,anchor="w")
    btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=logout2).place(x=1145,y=60,anchor="w")
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
    btn_home = Button(F21,image= home_icon,bg=bg_color,relief=RAISED,width =115,height=145,command=Home2).place(x=0,y=63,anchor="w")
    btn_view = Button(F22,relief=RAISED,bg=bg_color,image=view_icon,width =115,height=145,command=View_Vaci2).place(x=0,y=63,anchor="w")
    btn_manage = Button(F23,relief=RAISED,image=manage_icon,bg=bg_color,width =115,height=145,command=Manage_Vaci).place(x=0,y=63,anchor="w")
    btn_Exit = Button(F24,relief=RAISED,bg=bg_color,image=exit_icon,width =115,height=145,command=Exit2).place(x=0,y=63,anchor="w")
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
    lbl_roll=Label(F4,text="Product ID",font=("times new roman",18,"bold"),bg="#F5F5F5")
    lbl_roll.place(x=0,y=90,anchor="w")
    txt_roll=Entry(F4, textvariable=PID,state="readonly", width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=90,anchor="w")
    lbl_roll=Label(F4,text="Product TBL",font=("times new roman",18,"bold"),bg="#F5F5F5")
    lbl_roll.place(x=0,y=140,anchor="w")
    txt_roll=Entry(F4, textvariable=product_TBL, width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=140,anchor="w")
    lbl_roll=Label(F4,text="CVX Short Desc",bg="#F5F5F5",font=("times new roman",18,"bold"))
    lbl_roll.place(x=0,y=190,anchor="w")
    txt_roll=Entry(F4, textvariable=CVX_S_D,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=190,anchor="w")
    lbl_roll=Label(F4,text="CVX Code",bg="#F5F5F5",font=("times new roman",18,"bold"))
    lbl_roll.place(x=0,y=240,anchor="w")
    txt_roll=Entry(F4, textvariable=CVX_Code,width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=240,anchor="w")
    lbl_roll=Label(F4,text="Manufactur TBL",bg="#F5F5F5",font=("times new roman",18,"bold"))
    lbl_roll.place(x=0,y=290,anchor="w")
    txt_roll=Entry(F4, textvariable=Manuf_TBL, width=17,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_roll.place(x=230,y=290,anchor="w")
    lb_dep=Label(F4,text="Manufactur TBL Code", font=("times new roman",16,"bold"),bg="#F5F5F5")
    lb_dep.place(x=0, y=340, anchor="w")
    combo_dep=Entry(F4, textvariable=Manuf_TBL_Code,width=17, font=("times new roman",15,"bold"))
    combo_dep.place(x=230, y=340, anchor="w")
    lb_dep=Label(F4,text="MVX_Status", font=("times new roman",18,"bold"),bg="#F5F5F5")
    lb_dep.place(x=0, y=390, anchor="w")
    combo_dep=ttk.Combobox(F4, textvariable=MVX_Status,width=17, font=("times new roman",13,"bold"),state='readonly')
    combo_dep['values']=("Active","Inactive")
    combo_dep.place(x=230, y=390, anchor="w")
    lb_dep=Label(F4,text="Product Name Status", font=("times new roman",18,"bold"),bg="#F5F5F5")
    lb_dep.place(x=0, y=440, anchor="w")
    combo_dep=ttk.Combobox(F4, textvariable=P_N_S,width=17, font=("times new roman",13,"bold"),state='readonly')
    combo_dep['values']=("Active","Inactive")
    combo_dep.place(x=228, y=440, anchor="w")
    lb_dep=Label(F4,text="Product TBL Update Date", font=("times new roman",16,"bold"),bg="#F5F5F5")
    lb_dep.place(x=445, y=90, anchor="w")
    txt_dep=Entry(F4, textvariable=P_T_U_D,width=17, bg="grey",font=("times new roman",13,"bold"),fg="white")
    txt_dep.place(x=445, y=140, anchor="w")
    F5 =Frame(F4,bd=10,relief=SUNKEN,bg="white")
    F5.place(x=0,y=480,width=700,height=80 )
    btn_update2 = Button(F5,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bg="navy blue",fg="yellow",bd=6,text="Update",command=Data_update).grid(row=0,column=0,pady=6,padx=50,sticky="nesw")        
    btn_Delete = Button(F5,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bg="navy blue",fg="yellow",bd=6,text="Delete",command=delete_data).grid(row=0,column=1,pady=6,padx=50,sticky="nesw")
    btn_Clear = Button(F5,relief=GROOVE, width=15,font=("times new roman",13,"bold"),bg="navy blue",fg="yellow",bd=6,text="Clear ALL",command=clear6).grid(row=0,column=2,pady=6,padx=5,sticky="nesw")
    btn_Add = Button(F4,relief=GROOVE, width=15,font=("times new roman",13,"bold"),bg="red",fg="white",bd=6,text="Add",command=add).place(x=510,y=440,anchor="w")       
    seprator2_style = ttk.Style()
    separator2 = ttk.Separator(F4, orient='vertical',style="Line.TSeparator")
    separator2.place(x=700,height=590,y=0)
    seprator2_style.configure("Line.TSeparator")
    seprator2_style = ttk.Style()
    separator2 = ttk.Separator(F4, orient='horizontal',style="Line.TSeparator")
    separator2.place(x=700,width=675,y=80)
    seprator2_style.configure("Line.TSeparator")
    lb_search=Label(F4,text="Search By", font=("times new roman",15,"bold"),bg="#F5F5F5")
    lb_search.place(x=720 ,y=17, anchor="w")
    combo_search=ttk.Combobox(F4, textvariable=searchby,width=17, font=("times new roman",13,"bold"),state='readonly')
    combo_search['values']=("CVX_Code")
    combo_search.place(x=830, y=17, anchor="w")
    lb_search2=Entry(F4,textvariable=searchval,width=15,relief=SUNKEN,bd=5,font=("times new roman",15,"bold"),bg="#F5F5F5")
    lb_search2.place(x=1030, y=15, anchor="w")
    btn_searchall = Button(F4,relief=RAISED,width=30,command=search4,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6, text="Search All")
    btn_searchall.place(x=720,y=60,anchor="w")
    btn_search = Button(F4,relief=RAISED,width=30,command=search_data2,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6,text="Search")        
    btn_search.place(x=970,y=60,anchor="w")
    F6 =Frame(F4,bd=10,relief=SUNKEN,bg="white")
    F6.place(x=720,y=85,width=475,height=500 )
    Table_Frame=Frame(F6,bd=4, relief=RIDGE,bg=bg_color)
    Table_Frame.place(x=0,y=0,width=455,height=480)
    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
    global vaccineseaech_table
    vaccineseaech_table=ttk.Treeview(Table_Frame,columns=("Vacci_Product_ID","product_TBL","CVX_Short_Description","CVX_Code","manufacturer_TBL","manufacturer_TBL_MVX_CODE","MVX_status","product_name_status","product_TBL_Update_date"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=vaccineseaech_table.xview)
    scroll_y.config(command=vaccineseaech_table.yview)
    vaccineseaech_table.column("Vacci_Product_ID", width=150)
    vaccineseaech_table.column("product_TBL", width=150)
    vaccineseaech_table.column("CVX_Short_Description", width=150)
    vaccineseaech_table.column("CVX_Code", width=150)
    vaccineseaech_table.column("manufacturer_TBL", width=150)
    vaccineseaech_table.column("manufacturer_TBL_MVX_CODE", width=150)
    vaccineseaech_table.column("MVX_status", width=150)
    vaccineseaech_table.column("product_name_status", width=150)
    vaccineseaech_table.column("product_TBL_Update_date", width=150)
    vaccineseaech_table.heading("Vacci_Product_ID",text="Vacci_Product_ID")
    vaccineseaech_table.heading("product_TBL",text="product_TBL")
    vaccineseaech_table.heading("CVX_Short_Description",text="CVX_Short_Description")
    vaccineseaech_table.heading("CVX_Code",text="CVX_Code")
    vaccineseaech_table.heading("manufacturer_TBL",text="manufacturer_TBL")
    vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="manufacturer_TBL_MVX_CODE")
    vaccineseaech_table.heading("MVX_status",text="MVX_status")
    vaccineseaech_table.heading("product_name_status",text="product_name_status")
    vaccineseaech_table.heading("product_TBL_Update_date",text="product_TBL_Update_date")
    vaccineseaech_table['show']='headings'
    fetch_data4()
    clock()
    root3.mainloop()

global fetch_data4
def fetch_data4():
    global vaccineseaech_table
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    c.execute("select * from vaci_info")
    rows=c.fetchall()
    if len(rows)!=0:
            vaccineseaech_table.delete(*vaccineseaech_table.get_children())
            for row in rows:
                    vaccineseaech_table.insert('',END,values=row)
            conn.commit()
    conn.close()

global getcursor4
def getcursor4(ev):
    global vaccineseaech_table,PID
    cursor_row=vaccineseaech_table.focus()
    Content=vaccineseaech_table.item(cursor_row)
    row=Content['values']
    PID.set(row[0])
    product_TBL.set(row[1]) 
    CVX_S_D.set(row[2])
    CVX_Code.set(row[3])
    Manuf_TBL.set(row[4])
    Manuf_TBL_Code.set(row[5])
    MVX_Status.set(row[6])
    P_N_S.set(row[7])
    P_T_U_D.set(row[8])

global search4
def search4():
    vaccineseaech_table.heading("Vacci_Product_ID",text="Vacci_Product_ID")
    vaccineseaech_table.heading("product_TBL",text="product_TBL")
    vaccineseaech_table.heading("CVX_Short_Description",text="CVX_Short_Description")
    vaccineseaech_table.heading("CVX_Code",text="CVX_Code")
    vaccineseaech_table.heading("manufacturer_TBL",text="manufacturer_TBL")
    vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="manufacturer_TBL_MVX_CODE")
    vaccineseaech_table.heading("MVX_status",text="MVX_status")
    vaccineseaech_table.heading("product_name_status",text="product_name_status")
    vaccineseaech_table.heading("product_TBL_Update_date",text="product_TBL_Update_date")
    vaccineseaech_table['show']='headings'
    vaccineseaech_table.pack(fill=BOTH,expand=1)
    vaccineseaech_table.bind("<ButtonRelease-1>",getcursor4)
    fetch_data4()

def search_data2():
    if searchby.get()=="" and searchval.get()=="":
        return messagebox.showwarning("Warning","Fields should be filled")
    if searchby.get()=="" :
        return messagebox.showwarning("Warning","Shearch By Option Should be filled")
    if searchval.get()=="":
        return messagebox.showwarning("Warning","Search box should be filled")
    
    else:
        if searchby.get() == "CVX_Code":
            conn=sqlite3.connect("vacisearch.db")
            c=conn.cursor()
            c.execute("select * from vaci_info where CVX_Code="+searchval.get())
            rows=c.fetchall()
            if len(rows)!=0:
                vaccineseaech_table.delete(*vaccineseaech_table.get_children())
                for row in rows:
                        vaccineseaech_table.insert('',END,values=row)
                conn.commit()
                conn.close()
                vaccineseaech_table.heading("Vacci_Product_ID",text="Vacci_Product_ID")
                vaccineseaech_table.heading("product_TBL",text="product_TBL")
                vaccineseaech_table.heading("CVX_Short_Description",text="CVX_Short_Description")
                vaccineseaech_table.heading("CVX_Code",text="CVX_Code")
                vaccineseaech_table.heading("manufacturer_TBL",text="manufacturer_TBL")
                vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="manufacturer_TBL_MVX_CODE")
                vaccineseaech_table.heading("MVX_status",text="MVX_status")
                vaccineseaech_table.heading("product_name_status",text="product_name_status")
                vaccineseaech_table.heading("product_TBL_Update_date",text="product_TBL_Update_date")                
                vaccineseaech_table['show']='headings'
                vaccineseaech_table.pack(fill=BOTH,expand=1)
                vaccineseaech_table.bind("<ButtonRelease-1>",getcursor4)
            #else:
            #    return messagebox.showerror("Error","CVX Code Not Exist")        
            #conn.close()

global search_data
def search_data():
    search_data2()

global ChangePassword1
def ChangePassword1():
    global root5
    root5 = Toplevel(root4)  # Child Window "Tk() can Also be use here"
    root5.title("Change Password")
    root5.geometry("750x370+350+150")
    root5.configure(bg="black")
    root5.grab_set() 
    root5.resizable(False, False)
    title_child = Label(root5, text="Change Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)  
    global pass_, passcon, phoneno_
    pass_lbl = Label(root5, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=140)
    pass_ = Entry(root5, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    pass_.place(x=260, y=140)
    passcon_lbl = Label(root5, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=190)
    passcon = Entry(root5, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    passcon.place(x=260, y=190)
    phoneno_lbl = Label(root5, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=240)
    phoneno_ = Entry(root5, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    phoneno_.place(x=260, y=240)
    CP_btn = Button(root5, text="Change Password", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=CP1)
    CP_btn.place(x=435, y=280, width=200, height=30) 

global CP1
def CP1():
    global pass_, passcon, phoneno, root5
    with open("Temp.txt","r+") as file:
        read1=file.read()
    conn = sqlite3.connect("vacisearch.db")
    c = conn.cursor()
    c.execute("SELECT uname from Userinfo WHERE contact=" + str(phoneno_.get()))
    data = c.fetchall()
    #print(data)
    if data==[]:
        return messagebox.showerror("Error"," Current Phone not Matched to Your ID" , parent=root5)
    else:
         for i in data:
            if i[0] == read1:
                if len(str(pass_))>=8:
                    if pass_.get() == passcon.get():
                        y= f"UPDATE Userinfo SET pasw = {str(pass_.get())} WHERE contact = {str(phoneno_.get())}"
                        c.execute(str(y))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Info", "Successfully Changed!!", parent=root5)
                        root5.destroy()                    
                    else:
                        return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=root5)
                else:
                    return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=root5)
            else:
                return messagebox.showerror("Error","Contact No. or Id is wrong")

global ChangePassword2
def ChangePassword2():
    global root5
    root5 = Toplevel(root3)  # Child Window "Tk() can Also be use here"
    root5.title("Change Password")
    root5.geometry("750x370+350+150")
    root5.configure(bg="black")
    root5.grab_set() 
    root5.resizable(False, False)
    title_child = Label(root5, text="Change Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)  
    global pass_, passcon, phoneno_
    pass_lbl = Label(root5, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=140)
    pass_ = Entry(root5, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    pass_.place(x=260, y=140)
    passcon_lbl = Label(root5, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=190)
    passcon = Entry(root5, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    passcon.place(x=260, y=190)
    phoneno_lbl = Label(root5, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=240)
    phoneno_ = Entry(root5, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    phoneno_.place(x=260, y=240)
    CP_btn = Button(root5, text="Change Password", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=CP2)
    CP_btn.place(x=435, y=280, width=200, height=30) 

global CP2
def CP2():
    global pass_, passcon, phoneno, root5
    with open("Temp1.txt","r+") as file:
        read1=file.read()
    conn = sqlite3.connect("vacisearch.db")
    c = conn.cursor()
    c.execute("SELECT Hname from Hospital WHERE contact=" + str(phoneno_.get()))
    data = c.fetchall()
    #print(data)
    if data==[]:
        return messagebox.showerror("Error"," Current Phone not Matched to Your ID" , parent=root5)
    else:
         for i in data:
            if i[0] == read1:
                if len(str(pass_))>=8:
                    if pass_.get() == passcon.get():
                        y= f"UPDATE Hospital SET pasw = {str(pass_.get())} WHERE Contact = {str(phoneno_.get())}"
                        c.execute(str(y))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Info", "Successfully Changed!!", parent=root5)
                        root5.destroy()                    
                    else:
                        return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=root5)
                else:
                    return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=root5)
            else:
                return messagebox.showerror("Error","Contact No. or Id is wrong")

global Exit
def Exit():
    root.destroy()   

global Exit1
def Exit1():
    root2.destroy() 

global Exit2
def Exit2():
    root3.destroy() 

global Exit3
def Exit3():
    root1.destroy() 

global Exit4
def Exit4():
    root4.destroy()

global Back
def Back():
    root3.destroy()
    GUI()

global Back1
def Back1():
    root1.destroy()
    HosGUI()

global clear1
def clear1():
    fname.set("")
    lname.set("")
    uname.set("")
    pasw.set("")
    email.set("")
    gender.set("Choose Gender")
    contact.set("")
    now = datetime.now()
    today= now.strftime("%d/%m/%Y")
    DOB.set(today)

global clear2
def clear2():
    hosname.set("")
    hname.set("")
    pasw1.set("")
    email1.set("")
    area.set("")
    contact1.set("")
    pin = StringVar()
    now1 = datetime.now()
    today1= now1.strftime("%d/%m/%Y")
    DOE.set(today1)

global clear3
def clear3():
    global Vaci_table
    Vaci_table.delete(*Vaci_table.get_children())
    Vaci_table.heading("HosId", text="")
    Vaci_table.heading("ACEKQ", text="")
    Vaci_table.heading("BFGLS", text="")
    Vaci_table.heading("CGHMT", text="")
    Vaci_table.heading("DHINU", text="")
    Vaci_table.heading("EIJOV", text="")
    Vaci_table.heading("FJKPW", text="")
    Vaci_table.heading("GKLQX", text="")
    Vaci_table.heading("HLMRY", text="")
    Vaci_table.heading("IMNSZ", text="")
    Vaci_table.heading("ABCDA", text="")
    Vaci_table.heading("BCDEB", text="")
    Vaci_table.heading("CDEFC", text="")
    Vaci_table.heading("DEFGD", text="")
    Vaci_table.heading("EFGHE", text="")
    Vaci_table.heading("FGHIF", text="")
    Vaci_table.heading("GHIJG", text="")
    Vaci_table.heading("HIJKH", text="")
    Vaci_table.heading("IJKLI", text="")
    Vaci_table.heading("JKLMJ", text="")
    Vaci_table.heading("KLMNK", text="")
    Vaci_table.heading("LMNOL", text="")
    Vaci_table.heading("MNOPM", text="")
    Vaci_table.heading("NOPQN", text="")
    Vaci_table.heading("OPQRO", text="")
    Vaci_table.heading("PQRSP", text="")
    Vaci_table.heading("QRSTQ", text="")
    Vaci_table.heading("RSTUR", text="")
    Vaci_table.heading("STUVS", text="")
    Vaci_table.heading("TUVWT", text="")
    Vaci_table.heading("UVWXU", text="")
    Vaci_table.heading("VWXYV", text="")
    Vaci_table.heading("ABCDE", text="")
    Vaci_table.heading("BCDEF", text="")
    Vaci_table.heading("CDEFG", text="")
    Vaci_table.heading("DEFGH", text="")
    Vaci_table.heading("EFGHI", text="")
    Vaci_table.heading("FGHIJ", text="")
    Vaci_table.heading("GHIJK", text="")
    Vaci_table.heading("HIJKL", text="")
    Vaci_table.heading("IJKLM", text="")
    Vaci_table.heading("JKLMN", text="")
    Vaci_table.heading("KLMNO", text="")
    Vaci_table.heading("LMNOP", text="")
    Vaci_table.heading("MNOPQ", text="")
    Vaci_table.heading("NOPQR", text="")
    Vaci_table.heading("OPQRS", text="")
    Vaci_table.heading("PQRST", text="")
    Vaci_table.heading("QRSTU", text="")
    Vaci_table.heading("RSTUV", text="")
    Vaci_table.heading("STUVW", text="")
    Vaci_table.heading("TUVWX", text="")
    Vaci_table.heading("UVWXY", text="")
    Vaci_table.heading("VWXYZ", text="")
    Vaci_table.heading("AAAAB", text="")
    Vaci_table.heading("BBBBC", text="")
    Vaci_table.heading("CCCCD", text="")
    Vaci_table.heading("DDDDE", text="")
    Vaci_table.heading("EEEEF", text="")
    Vaci_table.heading("FFFFG", text="")
    Vaci_table.heading("GGGGH", text="")
    Vaci_table.heading("HHHHI", text="")
    Vaci_table.heading("IIIIJ", text="")
    Vaci_table.heading("JJJJK", text="")
    Vaci_table.heading("KKKKL", text="")
    Vaci_table.heading("LLLLM", text="")
    Vaci_table.heading("MMMMN", text="")
    Vaci_table.heading("NNNNO", text="")
    Vaci_table.heading("OOOOP", text="")
    Vaci_table.heading("PPPPQ", text="")
    Vaci_table.heading("QQQQR", text="")
    Vaci_table.heading("RRRRS", text="")
    Vaci_table.heading("SSSST", text="")
    Vaci_table.heading("TTTTU", text="")
    Vaci_table.heading("UUUUV", text="")
    Vaci_table.heading("VVVVW", text="")
    Vaci_table.heading("WWWWX", text="")
    Vaci_table.heading("XXXXY", text="")
    Vaci_table.heading("QAAAC", text="")
    Vaci_table.heading("RBBBD", text="")
    Vaci_table.heading("SCCCE", text="")
    Vaci_table.heading("TDDDF", text="")
    Vaci_table.heading("UEEEG", text="")
    Vaci_table.heading("VFFFH", text="")
    Vaci_table.heading("WGGGI", text="")
    Vaci_table.heading("XHHHJ", text="")
    Vaci_table.heading("YIIIK", text="")
    Vaci_table.heading("ZJJJL", text="")
    Vaci_table.heading("BJJJL", text="")
    Vaci_table.heading("CKKKM", text="")
    Vaci_table.heading("DLLLN", text="")
    Vaci_table.heading("EMMMO", text="")
    Vaci_table.heading("FNNNP", text="")
    Vaci_table.heading("GOOOQ", text="")
    Vaci_table.heading("HPPPR", text="")
    Vaci_table.heading("IQQQS", text="")
    Vaci_table.heading("JRRRT", text="")
    Vaci_table.heading("KSSSU", text="")
    Vaci_table.heading("LTTTV", text="")
    Vaci_table.heading("MUUUW", text="")
    Vaci_table.heading("NVVVX", text="")
    Vaci_table.heading("OWWWY", text="")
    Vaci_table.heading("PXXXZ", text="")
    Vaci_table.heading("BBAAC", text="")
    Vaci_table.heading("CCBBD", text="")
    Vaci_table.heading("DDCCE", text="")
    Vaci_table.heading("EEDDF", text="")
    Vaci_table.heading("FFEEG", text="")
    Vaci_table.heading("GGFFH", text="")
    Vaci_table.heading("HHGGI", text="")
    Vaci_table.heading("IIHHJ", text="")
    Vaci_table.heading("JJIIK", text="")
    Vaci_table.heading("KKJJL", text="")
    Vaci_table.heading("LLKKM", text="")
    Vaci_table.heading("MMLLN", text="")
    Vaci_table.heading("NNMMO", text="")
    Vaci_table.heading("OONNP", text="")
    Vaci_table.heading("PPOOQ", text="")
    Vaci_table.heading("QQPPR", text="")
    Vaci_table.heading("RRQQS", text="")
    Vaci_table.heading("SSRRT", text="")
    Vaci_table.heading("TTSSU", text="")
    Vaci_table.heading("UUTTV", text="")
    Vaci_table.heading("VVUUW", text="")
    Vaci_table.heading("WWVVX", text="")
    Vaci_table.heading("XXWWY", text="")
    Vaci_table.heading("YYXXZ", text="")
    Vaci_table.heading("AADAA", text="")
    Vaci_table.heading("BBEBB", text="")
    Vaci_table.heading("CCFCC", text="")
    Vaci_table.heading("DDGDD", text="")
    Vaci_table.heading("EEHEE", text="")
    Vaci_table.heading("FFIFF", text="")
    Vaci_table.heading("GGJGG", text="")
    Vaci_table.heading("HHKHH", text="")
    Vaci_table.heading("IILII", text="")
    Vaci_table.heading("JJMJJ", text="")
    Vaci_table.heading("KKNKK", text="")
    Vaci_table.heading("LLOLL", text="")
    Vaci_table.heading("MMPMM", text="")
    Vaci_table.heading("NNQNN", text="")
    Vaci_table.heading("OOROO", text="")
    Vaci_table.heading("PPSPP", text="")
    Vaci_table.heading("QQTQQ", text="")
    Vaci_table.heading("RRURR", text="")
    Vaci_table.heading("SSVSS", text="")
    Vaci_table.heading("TTWTT", text="")
    Vaci_table.heading("UUXUU", text="")
    Vaci_table.heading("VVYVV", text="")
    Vaci_table.heading("WWZWW", text="")    
    Vaci_table['show']='headings'

global clear4
def clear4():
    vaccineseaech_table.delete(*vaccineseaech_table.get_children())
    vaccineseaech_table.heading("Vacci_Product_ID",text="")
    vaccineseaech_table.heading("product_TBL",text="")
    vaccineseaech_table.heading("CVX_Short_Description",text="")
    vaccineseaech_table.heading("CVX_Code",text="")
    vaccineseaech_table.heading("manufacturer_TBL",text="")
    vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="")
    vaccineseaech_table.heading("MVX_status",text="")
    vaccineseaech_table.heading("product_name_status",text="")
    vaccineseaech_table.heading("product_TBL_Update_date",text="")    
    vaccineseaech_table['show']='headings'
    searchby.set("")
    searchval.set("")

global clear5
def clear5():
    vaccineseaech_table.delete(*vaccineseaech_table.get_children())
    vaccineseaech_table.heading("Vacci_Product_ID",text="")
    vaccineseaech_table.heading("product_TBL",text="")
    vaccineseaech_table.heading("CVX_Short_Description",text="")
    vaccineseaech_table.heading("CVX_Code",text="")
    vaccineseaech_table.heading("manufacturer_TBL",text="")
    vaccineseaech_table.heading("manufacturer_TBL_MVX_CODE",text="")
    vaccineseaech_table.heading("MVX_status",text="")
    vaccineseaech_table.heading("product_name_status",text="")
    vaccineseaech_table.heading("product_TBL_Update_date",text="")    
    vaccineseaech_table['show']='headings'

global Reset1
def Reset1():
    global root6
    root6 = Toplevel(root)  # Child Window "Tk() can Also be use here"
    root6.title("Change Password")
    root6.geometry("750x370+350+150")
    root6.configure(bg="black")
    root6.grab_set() 
    root6.resizable(False, False)
    title_child = Label(root6, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)  
    global phone_, current_, pass_, passcon
    phone_lbl = Label(root6, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
    phone_ = Entry(root6, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    phone_.place(x=260, y=120)
    current_lbl = Label(root6, text="User Id", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
    current_ = Entry(root6, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    current_.place(x=260, y=170)
    pass_lbl = Label(root6, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
    pass_ = Entry(root6, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    pass_.place(x=260, y=220)
    passcon_lbl = Label(root6, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
    passcon = Entry(root6, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    passcon.place(x=260, y=270)
    Reset_btn = Button(root6, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=reset1)
    Reset_btn.place(x=495, y=310, width=140, height=30) 

global reset1
def reset1():
    global phone_, current_, pass_, passcon, root6
    phone1_ = phone_.get()
    conn = sqlite3.connect("vacisearch.db")
    c = conn.cursor()
    c.execute("SELECT UID from Userinfo WHERE Contact=" + str(phone1_))
    data = c.fetchall()
    #print(data)
    if data==[]:
        return messagebox.showerror("Error"," Current Phone not Matched to Your ID" , parent=root6)
    else:
         for i in data:
            if i[0] == current_.get():
                if len(str(pass_))>=8:
                    if pass_.get() == passcon.get():
                        y= f"UPDATE Userinfo SET pasw = {str(pass_.get())} WHERE contact = {str(phone_.get())}"
                        c.execute(str(y))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Info", "Successfully Changed!!", parent=root6)
                        root6.destroy()                    
                    else:
                        return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=root6)
                else:
                    return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=root6)
            else:
                return messagebox.showerror("Error","Contact No. or Id is wrong")

global Reset2
def Reset2():
    global root7
    root7 = Toplevel(root2)  # Child Window "Tk() can Also be use here"
    root7.title("Change Password")
    root7.geometry("750x370+350+150")
    root7.configure(bg="black")
    root7.grab_set() 
    root7.resizable(False, False)
    title_child1 = Label(root7, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
    global phone1_, current1_, pass1_, passcon1
    phone_lbl1 = Label(root7, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
    phone1_ = Entry(root7, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    phone1_.place(x=260, y=120)
    current_lbl1 = Label(root7, text="HosId", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
    current1_ = Entry(root7, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    current1_.place(x=260, y=170)
    pass_lbl1 = Label(root7, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
    pass1_ = Entry(root7, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    pass1_.place(x=260, y=220)
    passcon_lbl1 = Label(root7, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
    passcon1 = Entry(root7, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
    passcon1.place(x=260, y=270)   
    Reset_btn1 = Button(root7, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=reset2)
    Reset_btn1.place(x=495, y=310, width=140, height=30) 

global reset2
def reset2():
    global phone1_, current1_, pass1_, passcon1, root7
    phone3_ = phone1_.get()
    conn = sqlite3.connect("vacisearch.db")
    c = conn.cursor()
    c.execute("SELECT HosId from Hospital WHERE Contact=" + str(phone3_))
    data = c.fetchall()
    #print(data)
    if data==[]:
        return messagebox.showerror("Error"," Current Phone not Matched to Your ID" , parent=root7)
    else:
         for i in data:
            if i[0] == current1_.get():
                if len(str(pass1_))>=8:
                    if pass1_.get() == passcon1.get():
                        y= f"UPDATE Hospital SET pasw = {str(pass1_.get())} WHERE Contact = {str(phone1_.get())}"
                        c.execute(str(y))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Info", "Successfully Changed!!", parent=root7)
                        root7.destroy()                    
                    else:
                        return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=root7)
                else:
                    return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=root7)
            else:
                return messagebox.showerror("Error","Contact No. or Id is wrong")
            
global Login_win1    
def Login_win1():
    global root4
    root4 = Tk()    
    root4.title("Login User".center(420))  
    root4.configure(background="black")  
    root4.geometry("1360x768+0+0")
    bg_color = "#e0b0ff"
    bg_icon = ImageTk.PhotoImage(file="PICs\\81736244-cell-background-with-futuristic-interface-elements-hud-ui-for-medical-app-futuristic-user-interface-.jpg")
    bg_lbl = Label(root4, image = bg_icon).pack(fill=Y) # we put image into our window
    hos_icon=ImageTk.PhotoImage(file="PICs\\image2(1).png")
    home_icon=ImageTk.PhotoImage(file="PICs\\Home.png")
    view_vacci_icon=ImageTk.PhotoImage(file="PICs\\View_Vacci.png")
    view_icon=ImageTk.PhotoImage(file="PICs\\View_All_dark.png")
    manage_icon=ImageTk.PhotoImage(file="PICs\\Manage.jpg")
    exit_icon=ImageTk.PhotoImage(file="PICs\\Exit.png")
    global lbl_hr, lbl_min, lbl_sec, lbl_abv
    F1 = LabelFrame(root4,bd=10,relief=GROOVE,bg=bg_color)
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
    btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=ChangePassword1).place(x=1145,y=20,anchor="w")
    btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=logout1).place(x=1145,y=60,anchor="w")
    lbl2 = Label(F1,image=hos_icon,bg=bg_color)
    lbl2.place(x=25,y=10)
    F2 = LabelFrame(root4,bd=10,relief=GROOVE,bg=bg_color)
    F2.place(x=0,y=100,width=150,height=670 )
    F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F21.place(x=0,y=0,width=130,height=150 )
    F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F22.place(x=0,y=150,width=130,height=150)
    F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F23.place(x=0,y=300,width=130,height=150 )
    F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
    F24.place(x=0,y=450,width=130,height=150)
    btn_home = Button(F21,image= home_icon,bg=bg_color,relief=RAISED,width =115,height=140,command=Home1).place(x=0,y=67,anchor="w")
    btn_view_vacci = Button(F22,image= view_vacci_icon,bg=bg_color,relief=RAISED,width =115,height=140,command=View_Vaci1).place(x=0,y=67,anchor="w")
    btn_view = Button(F23,relief=RAISED,bg=bg_color,image=view_icon,width =115,height=140,command=Name_V_Search1).place(x=0,y=67,anchor="w")
    btn_Exit = Button(F24,relief=RAISED,bg=bg_color,image=exit_icon,width =115,height=140,command=Exit4).place(x=0,y=67,anchor="w")
    F3 = LabelFrame(root4,bd=5,relief=FLAT,bg="light gray")
    F3.place(x=150,y=100,relwidth=1,height=30 )
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    with open("Temp.txt","r+") as file:
        read1=file.read()
    lbl_1= Label(F3,text="Dashboard / User"+": UName : "+str(read1),font=("comic sans",15,"italic"),bg="light gray")
    lbl_1.place(x=0,y=0)
    F4 = LabelFrame(root4,bd=10,relief=GROOVE,bg="#DC143C")
    F4.place(x=300,y=170,width=400,height=250 )
    F41 = LabelFrame(F4,bd=5,relief=SUNKEN,bg="#DC143C")
    F41.place(x=0,y=0,width=380,height=60 )
    lbl_2= Label(F41,text="Total Users",fg="#FFFFFF",bg="#DC143C",font=("times new roman",25,"bold"))
    lbl_2.place(x=0,y=0)
    F42 = LabelFrame(F4,bd=5,relief=GROOVE)
    F42.place(x=0,y=60,width=380,height=180 )
    text1=Text(F42,bd=5, font=("times new roman",30,"bold"))
    c.execute("SELECT COUNT(*) FROM Userinfo")
    results1 = ((c).fetchall())        
    text1.insert(INSERT,("\n             Total\n           Users: "))
    text1.insert(INSERT,results1)
    text1.place(x=0,y=0,width=370,height=170)
    text1.configure(state="disabled")
    F5 = LabelFrame(root4,bd=10,relief=GROOVE)
    F5.place(x=800,y=170,width=400,height=250 )
    F51 = LabelFrame(F5,bd=5,relief=SUNKEN, bg="#3B9C9C")
    F51.place(x=0,y=0,width=380,height=60 )
    lbl_3= Label(F51,text="Login Id",fg="#FFFFFF",bg="#3B9C9C",font=("times new roman",30,"bold"))
    lbl_3.place(x=0,y=0)
    F52 = LabelFrame(F5,bd=5,relief=GROOVE)
    F52.place(x=0,y=60,width=380,height=180 )
    text2=Text(F52,bd=5, fg="white",font=("times new roman",15,"bold"),bg="#151B54")
    c.execute("SELECT * FROM Userinfo WHERE uname =\""+str(read1)+"\"")
    results2 = ((c).fetchall())        
    text2.insert(INSERT,(""))
    if results2:
        for i in results2:
            a=i    
        #EmpID.set(i[0])  
        text2.insert(INSERT,("\nUID                             :   "+str(i[0]+" ")))
        text2.insert(INSERT,("\nEmail                          :   "+str(i[5])+"\n"))
        text2.insert(INSERT,("UName                       :   "+str(i[3])+"\n"))
        text2.insert(INSERT,("Time of Registration :   "+str(i[10])+"\n"))
        text2.place(x=0,y=0,width=370,height=170)
        text2.configure(state="disabled")
    F6 = LabelFrame(root4,bd=10,relief=GROOVE)
    F6.place(x=300,y=450,width=400,height=250 )
    F61 = LabelFrame(F6,bd=5,relief=SUNKEN,fg="#FFFFFF",bg="black")
    F61.place(x=0,y=0,width=380,height=60 )
    lbl_4= Label(F61,text="Total Types of Vaccines",bg="black",fg="#FFFFFF",font=("times new roman",25,"bold"))
    lbl_4.place(x=0,y=0)
    F62 = LabelFrame(F6,bd=5,relief=GROOVE)
    F62.place(x=0,y=60,width=380,height=180 )
    text3=Text(F62,bd=5, fg="white",font=("times new roman",25,"bold"),bg="#151B54")
    c.execute("SELECT COUNT(*) FROM vaci_info")
    results3 = ((c).fetchall())        
    text3.insert(INSERT,("\n             Total\n   No. of Vaccine: "))
    text3.insert(INSERT,results3)
    text3.place(x=0,y=0,width=370,height=170)
    text3.configure(state="disabled")
    F7 = LabelFrame(root4,bd=10,relief=GROOVE)
    F7.place(x=800,y=450,width=400,height=250 )    
    F71 = LabelFrame(F7,bd=5,relief=SUNKEN,bg="white")
    F71.place(x=0,y=0,width=380,height=60 )
    lbl_4= Label(F71,text="Developer",bg="white",font=("times new roman",30,"bold"),fg="#DC143C")
    lbl_4.place(x=0,y=0)
    F72 = LabelFrame(F7,bd=5,relief=RAISED)
    F72.place(x=0,y=60,width=380,height=180 )
    text7=Text(F72,bd=5,font=("times new roman",15, "italic"),fg="#FFFFFF", bg="#DC143C",relief=GROOVE)
    text7.insert(INSERT,("                       Developed By\n\nUtkarsh\nEmail Id:aj147ps@gmail.com\nAlternate Email Id:codewithajofficial14@gmail.com\nFollow on #codewithajofficial on insta "))
    text7.place(x=0,y=0,width=370,height=170)
    text7.configure(state="disabled")
    clock()
    root4.mainloop()

global Login_win2       
def Login_win2():
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
    btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=ChangePassword2).place(x=1145,y=20,anchor="w")
    btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=logout2).place(x=1145,y=60,anchor="w")
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
    btn_home = Button(F21,image= home_icon,bg=bg_color,relief=RAISED,width =115,height=145,command=Home2).place(x=0,y=63,anchor="w")
    btn_view = Button(F22,relief=RAISED,bg=bg_color,image=view_icon,width =115,height=145,command=View_Vaci2).place(x=0,y=63,anchor="w")
    btn_manage = Button(F23,relief=RAISED,image=manage_icon,bg=bg_color,width =115,height=145,command=Manage_Vaci).place(x=0,y=63,anchor="w")
    btn_Exit = Button(F24,relief=RAISED,bg=bg_color,image=exit_icon,width =115,height=145,command=Exit2).place(x=0,y=63,anchor="w")
    F3 = LabelFrame(root3,bd=5,relief=FLAT,bg="light gray")
    F3.place(x=150,y=100,relwidth=1,height=30 )
    conn=sqlite3.connect("vacisearch.db")
    c=conn.cursor()
    with open("Temp1.txt","r+") as file:
        read1=file.read()
    lbl_1= Label(F3,text="Dashboard / Hospital"+": HName : "+str(read1),font=("comic sans",15,"italic"),bg="light gray")
    lbl_1.place(x=0,y=0)
    F4 = LabelFrame(root3,bd=10,relief=GROOVE,bg="#DC143C")
    F4.place(x=300,y=170,width=400,height=250 )
    F41 = LabelFrame(F4,bd=5,relief=SUNKEN,bg="#DC143C")
    F41.place(x=0,y=0,width=380,height=60 )
    lbl_2= Label(F41,text="Total Hospitals",fg="#FFFFFF",bg="#DC143C",font=("times new roman",25,"bold"))
    lbl_2.place(x=0,y=0)
    F42 = LabelFrame(F4,bd=5,relief=GROOVE)
    F42.place(x=0,y=60,width=380,height=180 )
    text1=Text(F42,bd=5, font=("times new roman",30,"bold"))
    c.execute("SELECT COUNT(*) FROM Hospital")
    results1 = ((c).fetchall())        
    text1.insert(INSERT,("\n             Total\n       Hospitals: "))
    text1.insert(INSERT,results1)
    text1.place(x=0,y=0,width=370,height=170)
    text1.configure(state="disabled")
    F5 = LabelFrame(root3,bd=10,relief=GROOVE)
    F5.place(x=780,y=170,width=500,height=250 )
    F51 = LabelFrame(F5,bd=5,relief=SUNKEN, bg="#3B9C9C")
    F51.place(x=0,y=0,width=480,height=60 )
    lbl_3= Label(F51,text="Login Id",fg="#FFFFFF",bg="#3B9C9C",font=("times new roman",30,"bold"))
    lbl_3.place(x=0,y=0)
    F52 = LabelFrame(F5,bd=5,relief=GROOVE)
    F52.place(x=0,y=60,width=480,height=180 )
    text2=Text(F52,bd=5, fg="white",font=("times new roman",13,"bold"),bg="#151B54")
    c.execute("SELECT * FROM Hospital WHERE Hname =\""+str(read1)+"\"")
    results2 = ((c).fetchall())        
    text2.insert(INSERT,(""))
    if results2:
        for i in results2:
            a=i    
        #EmpID.set(i[0])  
        text2.insert(INSERT,("\n\nHID             :   "+str(i[0]+" ")))
        text2.insert(INSERT,("\nEmail          :   "+str(i[4])+"\n"))
        text2.insert(INSERT,("HosName    :   "+str(i[1])+"\n"))
        text2.insert(INSERT,("TOR             :   "+str(i[9])+"\n"))
        text2.place(x=0,y=0,width=470,height=170)
        text2.configure(state="disabled")
    F6 = LabelFrame(root3,bd=10,relief=GROOVE)
    F6.place(x=300,y=450,width=400,height=250 )
    F61 = LabelFrame(F6,bd=5,relief=SUNKEN,fg="#FFFFFF",bg="black")
    F61.place(x=0,y=0,width=380,height=60 )
    lbl_4= Label(F61,text="Total Types of Vaccines",bg="black",fg="#FFFFFF",font=("times new roman",25,"bold"))
    lbl_4.place(x=0,y=0)
    F62 = LabelFrame(F6,bd=5,relief=GROOVE)
    F62.place(x=0,y=60,width=380,height=180 )
    text3=Text(F62,bd=5, fg="white",font=("times new roman",25,"bold"),bg="#151B54")
    c.execute("SELECT COUNT(*) FROM vaci_info")
    results3 = ((c).fetchall())        
    text3.insert(INSERT,("\n             Total\n   No. of Vaccine: "))
    text3.insert(INSERT,results3)
    text3.place(x=0,y=0,width=370,height=170)
    text3.configure(state="disabled")
    F7 = LabelFrame(root3,bd=10,relief=GROOVE)
    F7.place(x=780,y=450,width=500,height=250 )    
    F71 = LabelFrame(F7,bd=5,relief=SUNKEN,bg="white")
    F71.place(x=0,y=0,width=480,height=60 )
    lbl_4= Label(F71,text="Developer",bg="white",font=("times new roman",30,"bold"),fg="#DC143C")
    lbl_4.place(x=0,y=0)
    F72 = LabelFrame(F7,bd=5,relief=RAISED)
    F72.place(x=0,y=60,width=480,height=180 )
    text7=Text(F72,bd=5,font=("times new roman",15, "italic"),fg="#FFFFFF", bg="#DC143C",relief=GROOVE)
    text7.insert(INSERT,("                       Developed By\n\nUtkarsh\nEmail Id:aj147ps@gmail.com\nAlternate Email Id:codewithajofficial14@gmail.com\nFollow on #codewithajofficial on insta "))
    text7.place(x=0,y=0,width=480,height=170)
    text7.configure(state="disabled")
    clock()
    root3.mainloop()

global clock
def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    if int(h)>=12 and int(h)<15 and int(m)>0:
        lbl_abv.config(text="PM")
    if int(h)>=15 and int(h)<20 and int(m)>0:
        lbl_abv.config(text="PM")
    if int(h)>=20 and int(h)<24 and int(m)>0:
        lbl_abv.config(text="PM")
    if int(h)>12 and int(h)<15 and int(m)>0:
        lbl_abv.config(text="PM")
    if int(h)>0 and int(h)<12 and int(m)>0:
        lbl_abv.config(text="AM")
    lbl_hr.config(text = h)
    lbl_min.config(text = m)
    lbl_sec.config(text = s)
    lbl_hr.after(200,clock)

global LoginU
def LoginU():
    if uname.get() == "User Id" or pasw.get() == "":
        return messagebox.showerror("Error!", "All field should be filled")
    else:
        try:
            with open("Temp.txt", "w+") as file:
                file.write(uname.get())
            conn = sqlite3.connect("vacisearch.db")
            c = conn.cursor()
            find_user = ("SELECT * FROM Userinfo WHERE uname = ?  AND pasw = ?")
            c.execute(str(find_user), (str(uname.get()), str(pasw.get())))
            results = c.fetchall()
            if results:
                for i in results:
                    messagebox.showinfo("Success","Successfully Logined")
                    root.destroy()
                    Login_win1() 
            else:
                messagebox.showerror(
                    "Error!", "Username or Password may be wrong")
        except Exception:
            messagebox.showerror("Error","Database May not Exist")

global LoginH
def LoginH():
    if hname.get() == "Hos Id" or pasw1.get() == "":
        messagebox.showerror("Error!", "All field should be filled")
    else:
        try:
            with open("Temp1.txt", "w+") as file:
                file.write(hname.get())
            conn = sqlite3.connect("vacisearch.db")
            c = conn.cursor()
            find_user = ("SELECT * FROM Hospital WHERE Hname = ?  AND pasw = ?")
            c.execute(str(find_user), (str(hname.get()), str(pasw1.get())))
            results = c.fetchall()
            if results:
                for i in results:
                    messagebox.showinfo("Success","Successfully Logined")
                    root2.destroy()
                    Login_win2()
            else:
                messagebox.showerror("Error!", "Username or Password may be wrong")
        except Exception:
            return messagebox.showerror("Error","Database May not Exist")

global data_Signup1
def data_Signup1():
    if fname.get()=="" and pasw.get()=="" and email.get()=="" and contact.get()=="" and DOB.get()== today and gender.get()=="Choose Gender" :
        return messagebox.showerror("Error!","All Feilds Required")
    if fname.get()=='':
        return messagebox.showinfo('Error','Enter a Name')
    if email.get()=='':
        return messagebox.showinfo('Error','Enter a Email address')
    if "@" not in email.get():
        return messagebox.showwarning("Warrning","Email should have '@' Character")        
    if pasw.get()=='':
        return messagebox.showinfo('Error','Enter a password')
    if len(str(pasw.get()))<8:
        return messagebox.showwarning("Warning","Password should be Minimum 8 charactrs")
    if contact.get()=='':
        return messagebox.showinfo('Error','Enter a contact')
    try:
        tmp=contact.get()
        int(tmp)
    except ValueError:
        return messagebox.showinfo('Error','Contact No. Should Be Integer')
    if len(contact.get())<10 and len(contact.get())>15:
        return messagebox.showinfo('Error','Enter a valid contact')      
    else:
        code = random.randint(10000, 999999)
        UID = str(code)
        uname = str(fname.get())+UID
        try:
            conn=sqlite3.connect("vacisearch.db")
            c=conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS Userinfo(UID TEXT UNIQUE NOT NULL ,first_name TEXT NOT NULL, last_name TEXT, uname TEXT PRIMARY KEY UNIQUE NOT NULL, pasw TEXT NOT NULL, email TEXT UNIQUE NOT NULL,gender TEXT NOT NULL, contact TEXT UNIQUE NOT NULL,User_Entry TEXT NOT NULL, DOB TEXT NOT NULL, Time1 TEXT NOT NULL )")
            find_user = ("SELECT * FROM Userinfo WHERE email= ?  or contact = ?")
            c.execute(str(find_user),(email.get(),contact.get()))
            results = (c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                try:
                    c.execute("INSERT INTO Userinfo (UID, first_name, last_name, uname, pasw, email, gender, contact, User_Entry, DOB, Time1) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (UID,fname.get(),lname.get(),uname,pasw.get(),email.get(),gender.get(),contact.get(),today,DOB.get(),Time1))
                    conn.commit()
                    c.close()
                    conn.close()
                    messagebox.showinfo("Successfull","Successfully Added Data")
                    clear1()
                except Exception:
                    messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
                    clear1()        
        except Exception:
            return messagebox.showerror("Error!!","Somthing went wrong not able to connect database  ")

global data_Signup2
def data_Signup2():
    if hosname.get()=="" and pasw1.get()=="" and email1.get()=="" and contact1.get()=="" and DOE.get()== today1 and area.get()=="" and pin.get() == "" :
        return messagebox.showerror("Error!","All Feilds Required")
    if hosname.get()=='':
        return messagebox.showinfo('Error','Enter a Name')
    if email1.get()=='':
        return messagebox.showinfo('Error','Enter a Email address')
    if "@" not in email1.get():
        return messagebox.showwarning("Warrning","Email should have '@' Character")
    if pasw1.get()=='':
        return messagebox.showinfo('Error','Enter a password')
    if len(str(pasw1.get()))<8:
        return messagebox.showwarning("Warning","Password should be Minimum 8 charactrs")
    if contact1.get()=='':
        return messagebox.showinfo('Error','Enter a contact')
    try:
        tmp=contact1.get()
        int(tmp)
    except ValueError:
        return messagebox.showinfo('Error','Contact No. Should Be Integer')
    if len(contact1.get())<10 and len(contact1.get())>15:
        return messagebox.showinfo('Error','Enter a valid contact')        
    if area.get()=='':
        return messagebox.showinfo('Error','Enter a Area')
    if pin.get()=='':
        return messagebox.showinfo('Error','Enter a Pin Code')
    else:
        code = random.randint(10000, 999999)
        HosId = str(code)
        Hname = str(hosname.get())+HosId
        try:
            conn=sqlite3.connect("vacisearch.db")
            c=conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS Hospital(HosId TEXT UNIQUE NOT NULL ,HosName TEXT NOT NULL, Hname TEXT PRIMARY KEY UNIQUE NOT NULL, pasw TEXT NOT NULL, Email TEXT UNIQUE NOT NULL,Area TEXT NOT NULL, Pin_Code TEXT NOT NULL,  Contact TEXT UNIQUE NOT NULL, DOE TEXT NOT NULL, TIME TEXT NOT NULL )")
            find_user = ("SELECT * FROM Userinfo WHERE Email= ?  or Contact = ?")
            c.execute(str(find_user),(email1.get(),contact1.get()))
            results = (c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                try:
                    c.execute("INSERT INTO Hospital (HosId, HosName, Hname, pasw, Email, Area, Pin,  Contact, DOE, TIME) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (HosId,hosname.get(),Hname,pasw1.get(),email1.get(),area.get(),pin.get(),contact1.get(),DOE.get(),Time1))
                    conn.commit()
                    c.close()
                    conn.close()
                    messagebox.showinfo("Successfull","Successfully Added Data")
                    clear2()
                except Exception:
                    messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
                    clear2()        
        except Exception:
            return messagebox.showerror("Error!!","Somthing went wrong not able to connect database  ")

global Signup1
def SignUp1():
    try:
        root.destroy()
    except:
        pass
    global root3
    root3 = Tk()  
    root3.title("Vacci Search".center(420))
    root3.geometry("1350x700+0+0")
    root3.configure(background = "black")
    bg_color="#074463"
    bg_icon3 = ImageTk.PhotoImage(file="PICs/1360-x-768-wallpapers-universe-scenery-hd-1360x768.jpg")
    F21 = ImageTk.PhotoImage(file="PICs\pngtree-vector-users-icon-png-image_4144740.jpg")
    bg_lbl = Label(root3, image = bg_icon3).pack(fill=Y) # we put image into our window    
    global fname, lname, uname, pasw, email, gender, contact, Role, DOB, code, gender
    global label, calendar, now, Time1, today
    fname=StringVar()
    lname=StringVar()
    uname=StringVar()
    pasw=StringVar()
    email=StringVar()
    gender=StringVar()
    contact=StringVar()
    Role="Admin"
    DOB=StringVar()
    code=IntVar()
    gender.set("Choose Gender")
    label, calendar = "", ""
    now = datetime.now()
    Time1=now.strftime('%H:%M:%S')
    today= now.strftime("%d/%m/%Y")
    Manage_Frame=LabelFrame(root3,bd=10, relief=RIDGE,bg=bg_color,text="SignUp",font=("times new roman", 40, "bold"),fg="white")
    Manage_Frame.place(x=260,y=70,width=500,height=560)
    lbl1=Label(Manage_Frame,text="First Name",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl1.grid(row=0, column=0,padx=20,pady=10,sticky="w")
    txt1=Entry(Manage_Frame, textvariable=fname, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt1.grid(row=0, column=1,padx=20,pady=10,sticky="w")
    lbl2=Label(Manage_Frame,text="Last Name",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl2.grid(row=1, column=0,padx=20,pady=10,sticky="w")
    txt2=Entry(Manage_Frame, textvariable=lname, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt2.grid(row=1, column=1,padx=20,pady=10,sticky="w")
    lbl3=Label(Manage_Frame, text="Password",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl3.grid(row=2, column=0,padx=20,pady=10,sticky="w")
    txt3=Entry(Manage_Frame,textvariable=pasw, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,show="*")
    txt3.grid(row=2, column=1,padx=20,pady=10,sticky="w")
    lbl4=Label(Manage_Frame,text="Email",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl4.grid(row=3, column=0,padx=20,pady=10,sticky="w")
    txt4=Entry(Manage_Frame, textvariable=email, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt4.grid(row=3, column=1,padx=20,pady=10,sticky="w")
    font=("times new roman",20,"bold")
    labels = ['DOB']
    label=(Label(Manage_Frame, text="D.O.B",bg=bg_color, fg="white", font=font))
    label.place(x=20, y=260, anchor="w")
    calendar=(DateEntry(Manage_Frame,textvariable=DOB, font=("times new roman",15,"bold"), locale='en_GB',state="readonly", width=19))
    calendar.place(x=200, y=260, anchor="w")
    lbl5=Label(Manage_Frame,text="Contact",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl5.place(x=20, y=310, anchor="w")
    txt5=Entry(Manage_Frame, width=25, textvariable=contact, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
    txt5.place(x=200,y=300)
    lb_gender=Label(Manage_Frame,text="Gender", font=("times new roman",20,"bold"),bg=bg_color,fg="white")
    lb_gender.place(x=20, y=370, anchor="w")
    combo_gender=ttk.Combobox(Manage_Frame, textvariable=gender, font=("times new roman",13,"bold"),width=21,state='readonly')
    combo_gender['values']=("Male","Female","Others") 
    combo_gender.place(x=200, y=370, anchor="w")
    F2 = LabelFrame(root3,bd=10,relief=SUNKEN, bg="")
    F2.place(x=760,y=70,width=310,height=560 )
    lbl2 = Label(F2,bg=bg_color, image = F21).grid(row=0, column=0,padx=10,pady=20)
    lbl6 = Label(F2, text = "Developed by Code \n with Utkarsh",fg="#4863A0",bg="white", font= ("times new roman",20)).place(x=30,y=400)
    btn_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
    btn_Frame.place(x=10,y=420)
    SignUpbtn=Button(btn_Frame, text="SignUp", font="bold", width=8, command=data_Signup1).grid(row=0,column=0,padx=15, pady=10)
    Backbtn=Button(btn_Frame,text="Back",font="bold", width=8, command=Back).grid(row=0,column=4,padx=15, pady=10)
    Clearbtn=Button(btn_Frame,text="Clear",font="bold", width=8, command=clear1).grid(row=0,column=8,padx=15, pady=10)
    Exitbtn=Button(btn_Frame,text="Exit", font="bold", width=8, command=Exit2).grid(row=0,column=12,padx=15, pady=10)
    root3.mainloop()

global Signup2
def SignUp2():
    try:
        root2.destroy()
    except:
        pass
    global root1
    root1 = Tk()  
    root1.title("Vacci Search".center(420))
    root1.geometry("1350x700+0+0")
    root1.configure(background = "black")
    bg_color="#074463"
    bg_icon1 = ImageTk.PhotoImage(file="PICs\\1360-x-768-wallpapers-universe-scenery-hd-1360x768.jpg")
    F21 = ImageTk.PhotoImage(file="PICs\pngtree-vector-users-icon-png-image_4144740.jpg")
    bg_lbl = Label(root1, image = bg_icon1).pack(fill=Y) # we put image into our window
    global hosname, hname, pasw1, email1, area, contact1, pin, DOE, code1
    global label1, calendar1, now1, Time2, today1
    hosname=StringVar()
    hname=StringVar()
    pasw1=StringVar()
    email1=StringVar()
    area=StringVar()
    contact1=StringVar()
    pin = StringVar()
    DOE=StringVar()
    code1=IntVar()
    label1, calendar1 = "", ""
    now1 = datetime.now()
    Time2 = now1.strftime('%H:%M:%S')
    today1= now1.strftime("%d/%m/%Y")
    Manage_Frame=LabelFrame(root1,bd=10, relief=RIDGE,bg=bg_color,text="SignUp",font=("times new roman", 40, "bold"),fg="white")
    Manage_Frame.place(x=260,y=70,width=500,height=560)
    lbl_hosname=Label(Manage_Frame,text="Hos Name",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl_hosname.grid(row=0, column=0,padx=20,pady=10,sticky="w")
    txt_hosname=Entry(Manage_Frame, textvariable=hosname, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_hosname.grid(row=0, column=1,padx=20,pady=10,sticky="w")
    lbl_pasw=Label(Manage_Frame,text="Password",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl_pasw.grid(row=1, column=0,padx=20,pady=10,sticky="w")
    txt_pasw=Entry(Manage_Frame, textvariable=pasw1, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,show="*")
    txt_pasw.grid(row=1, column=1,padx=20,pady=10,sticky="w")
    lbl_email=Label(Manage_Frame, text="Email",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl_email.grid(row=2, column=0,padx=20,pady=10,sticky="w")
    txt_email=Entry(Manage_Frame,textvariable=email1, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_email.grid(row=2, column=1,padx=20,pady=10,sticky="w")
    font=("times new roman",20,"bold")
    labels = ['DOE']
    label1=(Label(Manage_Frame, text="D.O.E",bg=bg_color, fg="white", font=font))
    label1.place(x=20, y=200, anchor="w")
    calendar1=(DateEntry(Manage_Frame,textvariable=DOE, font=("times new roman",15,"bold"), locale='en_GB',state="readonly", width=19))
    calendar1.place(x=190, y=195, anchor="w")
    lbl_area=Label(Manage_Frame,text="Area",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl_area.place(x=20, y=250, anchor="w")
    txt_area=Entry(Manage_Frame, textvariable=area, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_area.place(x=190, y=250, anchor="w")
    lbl_pin=Label(Manage_Frame,text="Pin",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
    lbl_pin.place(x=20, y=300, anchor="w")
    txt_pin=Entry(Manage_Frame, width=25, textvariable=pin, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
    txt_pin.place(x=190,y=290)
    lb_contact=Label(Manage_Frame,text="Contact", font=("times new roman",20,"bold"),bg=bg_color,fg="white")
    lb_contact.place(x=20, y=350, anchor="w")
    txt_contact=Entry(Manage_Frame, width=25, textvariable=contact1, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
    txt_contact.place(x=190,y=350)
    F2 = LabelFrame(root1,bd=10,relief=SUNKEN, bg="")
    F2.place(x=760,y=70,width=310,height=560 )
    lbl2 = Label(F2,bg=bg_color, image = F21).grid(row=0, column=0,padx=10,pady=20)
    lbl6 = Label(F2, text = "Developed by Code \n with Utkarsh",fg="#4863A0",bg="white", font= ("times new roman",20)).place(x=30,y=400)
    btn_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
    btn_Frame.place(x=10,y=420)
    SignUpbtn=Button(btn_Frame, text="SignUp", font="bold", width=8, command=data_Signup2).grid(row=0,column=0,padx=15, pady=10)
    Backbtn=Button(btn_Frame,text="Back",font="bold", width=8, command=Back1).grid(row=0,column=4,padx=15, pady=10)
    Clearbtn=Button(btn_Frame,text="Clear",font="bold", width=8, command=clear2).grid(row=0,column=8,padx=15, pady=10)
    Exitbtn=Button(btn_Frame,text="Exit", font="bold", width=8,command=Exit3).grid(row=0,column=12,padx=15, pady=10)
    root1.mainloop()

global show_pasw1
def show_pasw1():
    global hname, pasw1, pass_2
    a = pasw1.get()
    #print(a)
    pasw1.set(a)
    if txtp_2.get() == "Password Mode: Hidden":
        txtp_2.config(state="normal")
        txtp_2.insert(0, "Password Mode: Shown")
        txtp1 = Entry(FU1, bd=5, textvariable=pasw1, relief=GROOVE, font=("", 15))
        txtp1.place(x=250, y=260, anchor="w")
        pass_2.set("Password Mode: Shown")
        pasw1.set(a)
    elif txtp_2.get() == "Password Mode: Shown":
        txtp_2.config(state="normal")
        txtp_2.delete(0, END)
        txtp_2.insert(0, "Password Mode: Hidden")
        # txtp_1.config(state="readonly")
        txtp1 = Entry(FU1, bd=5, textvariable=pasw1,
                            relief=GROOVE, show="*", font=("", 15))
        txtp1.place(x=250, y=260, anchor="w")
        pasw1.set(a)

global HosGUI
def HosGUI():
    try:
        root.destroy()
    except:
        pass
    global root2 
    root2=Tk()
    root2.title("Login Form".center(420))  # title for Window
    root2.configure(background="black")  # background color for window
    root2.geometry("1360x768+0+0")
    bg_color = "#2B547E"
    global eye_icon, bg_icon, F2, icon1, icon2, icon3,icon4, user_icon, pasw_icon, user_
    eye_icon = PhotoImage(file="PICs\show-password.png")
    bg_icon = ImageTk.PhotoImage(file="PICs\medicine-user-interface-media-medicine-background-image-as-dna-research-concept-d-rendering-101728155.jpg")
    F2 = ImageTk.PhotoImage(file="PICs\download1.jpeg")
    icon1 = ImageTk.PhotoImage(file="PICs\download.jpg")
    icon2 = ImageTk.PhotoImage(file="PICs\download (1).png")
    icon3 = ImageTk.PhotoImage(file="PICs\download.png")
    icon4 = ImageTk.PhotoImage(file="PICs\images.png")
    user_icon = ImageTk.PhotoImage(file="PICs\images.png")
    pasw_icon = ImageTk.PhotoImage(file="PICs\images (1).png")
    user_ = ImageTk.PhotoImage(file="PICs\image_icon.png")
    global hname, pasw1, pass_2
    hname = StringVar()
    pasw1 = StringVar()
    hname.set("Hos Id")
    pass_2 = StringVar()
    pass_2.set("Password Mode: Hidden")
    bg_lbl = Label(root2, image=bg_icon).pack(fill=Y)  # we put image into our window
    global FU1
    FU1 = LabelFrame(root2, bd=10, relief=GROOVE, bg=bg_color)
    FU1.place(x=195, y=95, width=600, height=480)
    lbl = Label(FU1, text="Hospital Login ", bg=bg_color, fg="gold", font=("times new roman", 30, "bold")).grid(row=0, column=0, padx=80, pady=30)
    F2 = LabelFrame(root2, bd=10, relief=GROOVE, bg="#787878")
    F2.place(x=790, y=95, width=310, height=480)
    lbl2 = Label(F2, bg=bg_color, image=user_).grid(row=0, column=0, padx=100, pady=20)
    lbl3 = Label(F2, text="Also Sign Up for the new Hospital", bg="#787878", fg="green", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=5)
    lbl4 = Label(F2, text="Users \n@Vaccisearch", fg="green", bg="#787878", font=("times new roman", 18, "italic")).grid(row=2, column=0, padx=10)
    lbl6 = Label(F2, text="Developed by Utkarsh",fg="white", bg="#787878", font=("times new roman", 20)).place(x=20, y=420)
    logolbl = Label(FU1, image=user_icon).place(x=80, y=200, anchor="w")
    lbl6 = Label(FU1, text="HOS Id", fg="white", bg=bg_color, font=("times new roman", 20, "bold")).place(x=115, y=200, anchor="w")
    global txtu1
    txtu1 = Entry(FU1, bd=5, textvariable=hname, relief=GROOVE,font=("", 15)).place(x=250, y=200, anchor="w")
    logolbl2 = Label(FU1, image=pasw_icon).place(x=80, y=260, anchor="w")
    lbl7 = Label(FU1, text="Password", fg="white", bg=bg_color, font=("times new roman", 20, "bold"))
    lbl7.place(x=115, y=260, anchor="w")
    global txtp1
    txtp1 = Entry(FU1, bd=5, textvariable=pasw1, show="*",relief=GROOVE, font=("", 15))
    txtp1.place(x=250, y=260, anchor="w")
    global txtp_2
    txtp_2 = Entry(FU1, bd=0, bg=bg_color, fg="white", textvariable=pass_2,relief=GROOVE, width="45", font=("times new roman", 10))
    txtp_2.place(x=250, y=10, anchor="w")
    btn_login1 = Button(FU1, text="Login", relief=RAISED, width=12, height=1, font=("times new roman", 12, "bold"), bg="green", foreground="#FEFCFF", command=LoginH).place(x=370, y=330, width=150, anchor="e")
    btn_login2 = Button(FU1, text="Login as User", relief=GROOVE, width=12, height=1, font=("times new roman", 12, "bold"), bg="light green", command=GUI).place(x=530, y=330, width=150, anchor="e")
    btn_Eye = Button(FU1, image=eye_icon, relief=GROOVE, font=("times new roman", 14, "bold"), bg="light green", command=show_pasw1).place(x=528, y=260, height=35, anchor="e")
    btn_SignUp = Button(F2, text="SignUp", width=20, height=1, relief=RAISED, activebackground="#1569C7", activeforeground="#FEFCFF", font=("times new roman", 14, "bold"), bg="#1569C7", foreground="#FEFCFF",command=SignUp2).place(x=30,y=200)
    btn_Exit = Button(F2, text="Exit", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", font=("times new roman", 14, "bold"), command=Exit1, bg="Red", fg="white").place(x=50,y=300)
    btn_Reset = Button(F2, text="Reset", relief=GROOVE, activeback="yellow",  width=8, height=1, font=("times new roman", 14, "bold"), bg="yellow", command = Reset2).place(x=150, y=300)
    root2 = mainloop()

global show_pasw
def show_pasw():
    global email, pasw, pass_1
    a = pasw.get()
    #print(a)
    pasw.set(a)
    if txtp_1.get() == "Password Mode: Hidden":
        txtp_1.config(state="normal")
        txtp_1.insert(0, "Password Mode: Shown")
        txtp = Entry(F1, bd=5, textvariable=pasw, relief=GROOVE, font=("", 15))
        txtp.place(x=250, y=260, anchor="w")
        pass_1.set("Password Mode: Shown")
        pasw.set(a)
    elif txtp_1.get() == "Password Mode: Shown":
        txtp_1.config(state="normal")
        txtp_1.delete(0, END)
        txtp_1.insert(0, "Password Mode: Hidden")
        # txtp_1.config(state="readonly")
        txtp = Entry(F1, bd=5, textvariable=pasw,
                            relief=GROOVE, show="*", font=("", 15))
        txtp.place(x=250, y=260, anchor="w")
        pasw.set(a)

global GUI
def GUI():
    try:
        root2.destroy()
    except:
        pass
    global root
    root = Tk()    
    root.title("Login Form".center(420))  
    root.configure(background="black")  
    root.geometry("1360x768+0+0")
    bg_color = "#2B547E"
    global eye_icon, bg_icon, F2, icon1, icon2, icon3,icon4, user_icon, pasw_icon, user_
    eye_icon = PhotoImage(file="PICs\show-password.png")
    bg_icon = ImageTk.PhotoImage(file="PICs\\1.jpg")
    F2 = ImageTk.PhotoImage(file="PICs\download1.jpeg")
    icon1 = ImageTk.PhotoImage(file="PICs\download.jpg")
    icon2 = ImageTk.PhotoImage(file="PICs\download (1).png")
    icon3 = ImageTk.PhotoImage(file="PICs\download.png")
    icon4 = ImageTk.PhotoImage(file="PICs\images.png")
    user_icon = ImageTk.PhotoImage(file="PICs\images.png")
    pasw_icon = ImageTk.PhotoImage(file="PICs\images (1).png")
    user_ = ImageTk.PhotoImage(file="PICs\image_icon.png")
    global uname, pasw, pass_1
    uname = StringVar()
    pasw = StringVar()
    uname.set("User Id")
    pass_1 = StringVar()
    pass_1.set("Password Mode: Hidden")
    bg_lbl = Label(root, image=bg_icon).pack(fill=Y) 
    global F1
    F1 = LabelFrame(root, bd=10, relief=GROOVE, bg=bg_color)
    F1.place(x=195, y=95, width=600, height=480)
    lbl = Label(F1, text="User Login ", bg=bg_color, fg="gold", font=("times new roman", 30, "bold")).grid(row=0, column=0, padx=80, pady=30)
    F2 = LabelFrame(root, bd=10, relief=GROOVE, bg="#787878")
    F2.place(x=790, y=95, width=310, height=480)
    lbl2 = Label(F2, bg=bg_color, image=user_).grid(row=0, column=0, padx=100, pady=20)
    lbl3 = Label(F2, text="Also Sign Up for the new Account", bg="#787878", fg="green", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=5)
    lbl4 = Label(F2, text="@PersonalAcc", fg="green", bg="#787878", font=("times new roman", 18, "italic")).grid(row=2, column=0, padx=10)
    lbl6 = Label(F2, text="Developed by Utkarsh",fg="white", bg="#787878", font=("times new roman", 22)).place(x=20, y=400)
    logolbl = Label(F1, image=user_icon).place(x=80, y=200, anchor="w")
    lbl6 = Label(F1, text="User ID", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).place(x=115, y=200, anchor="w")
    global txtu
    txtu = Entry(F1, bd=5, textvariable=uname, relief=GROOVE,font=("", 15)).place(x=250, y=200, anchor="w")
    logolbl2 = Label(F1, image=pasw_icon).place(x=80, y=260, anchor="w")
    lbl7 = Label(F1, text="Password", fg="white", bg=bg_color, font=("times new roman", 20, "bold"))
    lbl7.place(x=115, y=260, anchor="w")
    global txtp
    txtp = Entry(F1, bd=5, textvariable=pasw, show="*",relief=GROOVE, font=("", 15))
    txtp.place(x=250, y=260, anchor="w")
    global txtp_1
    txtp_1 = Entry(F1, bd=0, bg=bg_color, fg="white", textvariable=pass_1,relief=GROOVE, width="45", font=("times new roman", 10))
    txtp_1.place(x=250, y=10, anchor="w")
    btn_login1 = Button(F1, text="SignIn", relief=RAISED, width=12, height=1, font=("times new roman", 12, "bold"), bg="green", foreground="#FEFCFF", command=LoginU).place(x=330, y=330, width=150, anchor="e")
    btn_login2 = Button(F1, text="Login as Hospital", relief=GROOVE, width=12, height=1, font=("times new roman", 12, "bold"), bg="light green", command=HosGUI).place(x=530, y=330, width=150, anchor="e")
    btn_Eye = Button(F1, image=eye_icon, relief=GROOVE, font=("times new roman", 14, "bold"), bg="light green", command=show_pasw).place(x=528, y=260, height=35, anchor="e")
    btn_SignUp = Button(F2, text="SignUp", width=20, height=1, relief=RAISED, activebackground="#1569C7", activeforeground="#FEFCFF", font=("times new roman", 14, "bold"), bg="#1569C7", foreground="#FEFCFF",command=SignUp1).place(x=30,y=200)
    btn_Exit = Button(F2, text="Exit", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", font=("times new roman", 14, "bold"), command=Exit, bg="Red", fg="white").place(x=50,y=300)
    btn_Reset = Button(F2, text="Reset", relief=GROOVE, activeback="yellow",  width=8, height=1, font=("times new roman", 14, "bold"), bg="yellow", command=Reset1).place(x=150, y=300)

    root.mainloop()

if __name__=="__main__":
    GUI()