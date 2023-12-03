#giv an offer on repeted bookings
#make a flag based check system for amt transfer (form fills)for bills
#give ticket 
#logs of each person in each persons field
#being able to book 1week b4
#check @gmail.com
#print ticket
#think of multiple theatres
#reduce lies of code by using modules 





from tkinter import *
import sys 
root=Tk()
root.geometry("300x300")
root.title("Movie Ticket Reservation System")
MyLabel=Label(root,text="Welcome to Movie Ticket Reservation System").pack()
MyLabel2=Label(root,text="\n").pack()
def Create():
    Create_screen=Toplevel(root)
    Create_screen.title("Create user")
    l=Label(Create_screen,text="Welcome to create page",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    l1=Label(Create_screen,text="Enter Username:",font=('Çalibri',12))
    l1.grid(row=1,sticky=W)
    l2=Label(Create_screen,text="Enter Password:",font=('Calibri',12))
    l2.grid(row=2,sticky=W)
    l3=Label(Create_screen,text="Enter Password Again:",font=('Calibri',12))
    l3.grid(row=3,sticky=W)
    global user
    global password
    global password2
    user=StringVar()
    password=StringVar()
    password2=StringVar()
    e1=Entry(Create_screen,text=user,width=20)
    e1.grid(row=1,column=2)
    e2=Entry(Create_screen,text=password,show='*',width=20)
    e2.grid(row=2,column=2)
    e3=Entry(Create_screen,text=password2,show='*',width=20)
    e3.grid(row=3,column=2)
    b1=Button(Create_screen,text="Create",command=finish_create,padx=30)
    b1.grid(row=5)
    global notif1
    notif1=Label(Create_screen,font=('Calibri',12))
    notif1.grid(row=7,sticky=N)

def finish_create():
    global a
    global b
    global c
    a=user.get()
    b=password.get()
    c=password2.get()
    if b!=c:
        notif1.config(fg="red",text="password does not match")
    else:
        notif1.config(fg="green",text="password matching")

def Login():
    global Login_screen
    Login_screen=Toplevel(root)
    Login_screen.title("Login page")
    l=Label(Login_screen,text="Welcome to login page",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    l1=Label(Login_screen,text="Enter Username:",font=('Çalibri',12))
    l1.grid(row=1,sticky=W)
    l2=Label(Login_screen,text="Enter Password:",font=('Calibri',12))
    l2.grid(row=2,sticky=W) 
    global usr
    global pwd
    usr=StringVar()
    pwd=StringVar()
    e1=Entry(Login_screen,text=usr,width=20)
    e1.grid(row=1,column=2)
    e2=Entry(Login_screen,text=pwd,show='*',width=20)
    e2.grid(row=2,column=2)
    global notif2
    notif2=Label(Login_screen,font=('Calibri',12))
    notif2.grid(row=6,sticky=N)
    b1=Button(Login_screen,text="Login",command=finish_login,padx=30)
    b1.grid(row=4)

def finish_login():
    global a1
    a1=usr.get()
    a2=pwd.get()
    if a1==a and a2==b:
        notif2.config(fg="green",text="Login Successful")
        Login_screen.destroy()
        acct_dashboard=Toplevel(root)
        acct_dashboard.title("Account dashboard")
        Label(acct_dashboard,text="Select your choice from the given below:",font=('Calibri',12)).grid(row=0,sticky=N)
        Button(acct_dashboard,text="Book a ticket",command=book,padx=20).grid(row=2)
        Button(acct_dashboard,text="View booked tickets",padx=20).grid(row=3)
        Button(acct_dashboard,text="Logout",padx=20).grid(row=4)
    else:
        notif2.config(fg="red",text="Invalid username or password")

def Kantara():
    Kantara_screen=Toplevel(root)
    Kantara_screen.title("Kantara")
    l=Label(Kantara_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1) 
    global tickets   
    tickets= OptionMenu(Kantara_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Kantara_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def KGF_2():
    KGF_2_screen=Toplevel(root)
    KGF_2_screen.title("KGF 2")
    l=Label(KGF_2_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1)  
    global tickets  
    tickets= OptionMenu(KGF_2_screen,n,1,2,3,4,5,6,7,8) #Creates a menu box
    l=Label(KGF_2_screen,text=n.get(),font=('Çalibri',12)).grid(row=1)
    l.grid(row=2,sticky=N)

def Jailer():
    Jailer_screen=Toplevel(root)
    Jailer_screen.title("Jailer")
    l=Label(Jailer_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1) 
    global tickets   
    tickets= OptionMenu(Jailer_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Jailer_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def Three_Idiots():
    Three_Idiots_screen=Toplevel(root)
    Three_Idiots_screen.title("Three Idiots")
    l=Label(Three_Idiots_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=13,sticky=N)
    n=IntVar()
    n.set(1)  
    global tickets  
    tickets= OptionMenu(Three_Idiots_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Three_Idiots_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def Avengers_Endgame():
    Avengers_Endgame_screen=Toplevel(root)
    Avengers_Endgame_screen.title("Avengers Endgame")
    l=Label(Avengers_Endgame_screen,text="Select number of tickets:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    n=IntVar()
    n.set(1)   
    global tickets 
    tickets= OptionMenu(Avengers_Endgame_screen,n,1,2,3,4,5,6,7,8).grid(row=1) #Creates a menu box
    l=Label(Avengers_Endgame_screen,text=n.get(),font=('Çalibri',12))
    l.grid(row=2,sticky=N)

def Display():
    Display_screen=Toplevel(root)
    Display_screen.title("Display movies")
    l=Label(Display_screen,text="The Movies available are:",font=('Çalibri',12))
    l.grid(row=0,sticky=N)
    l=Label(Display_screen,text="Kantara",font=('Çalibri',12))
    l.grid(row=1,sticky=W)
    l=Label(Display_screen,text="KGF 2",font=('Çalibri',12))
    l.grid(row=2,sticky=W)
    l=Label(Display_screen,text="Jailer",font=('Çalibri',12))
    l.grid(row=3,sticky=W)
    l=Label(Display_screen,text="3 Idiots",font=('Çalibri',12))
    l.grid(row=4,sticky=W)
    l=Label(Display_screen,text="Avengers:Endgame",font=('Çalibri',12))
    l.grid(row=5,sticky=W)

def book():
    global Book_screen
    Book_screen=Toplevel(root)
    Book_screen.title("Bookings") 
    Label(Book_screen,text=f"Logged in as {a1}",font=('Çalibri',12)).grid(row=0,sticky=N)
    Label(Book_screen,text="Kantara",font=('Çalibri',12)).grid(row=1,sticky=N)
    Label(Book_screen,text="KGF 2",font=('Çalibri',12)).grid(row=2,sticky=N)
    Label(Book_screen,text="Jailer",font=('Çalibri',12)).grid(row=3,sticky=N)
    Label(Book_screen,text="3 Idiots",font=('Çalibri',12)).grid(row=4,sticky=N)
    Label(Book_screen,text="Avengers:Endgame",font=('Çalibri',12)).grid(row=5,sticky=N)
    Button(Book_screen,text="Kantara",command=Kantara,padx=20).grid(row=7)
    Button(Book_screen,text="KGF 2",command=KGF_2,padx=20).grid(row=8)
    Button(Book_screen,text="Jailer",command=Jailer,padx=20).grid(row=19)
    Button(Book_screen,text="3 Idiots",command=Three_Idiots,padx=20).grid(row=10)
    Button(Book_screen,text="Avengers:Endgame",command=Avengers_Endgame,padx=20).grid(row=11)



def Exit():
    print("Successfully logged out")
    sys.exit()

myButton1=Button(root,text="Create user",padx=20,command=Create)
myButton1.pack()
myButton2=Button(root,text="Login",padx=20,command=Login)
myButton2.pack()
myButton3=Button(root,text="Display movies list",padx=20,command=Display)
myButton3.pack()
myButton4=Button(root,text="Exit",padx=20,command=Exit)
myButton4.pack()
root.mainloop()