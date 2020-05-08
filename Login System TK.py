from tkinter import *
from PIL import  ImageTk, Image
from tkinter import messagebox

#------------------------------------------------------------------------------------------------------------------------
def login():
    if uservalue.get() == "" or passvalue.get() == "":
        messagebox.showerror("error", "all fields are required")

    elif uservalue.get() == "vaibhav" and passvalue.get() == "thorsingh":
        messagebox.showinfo("sucessfull", f" welcome {uservalue.get()}")
    else:
        messagebox.showerror("Error", "invalid username or password")

#-------------------------------------------------------------------------------------------------------------------------------
# def getvals():
#     print(f"The value of username is {uservalue.get()}")
#     print(f"The value of password is {passvalue.get()}")


root = Tk()
root.title("Login System Gui by Vaibhav")

#--------------------------------------------------------------------------------------------------------------------------------------
#adding image all here
photo=PhotoImage(file = "gg.png")
bgd=PhotoImage(file = "bg.png")
bgf=PhotoImage(file = "bg (1).png")
# pwd=PhotoImage(file = "pwd.png")

#adding bg image to window
#complete window >>> background image place above all because placed below it will cover the frame above line
bgdimage = Label(root,image= bgd).pack(side=TOP)
#-------------------------------------------------------------------------------------------------------------------------------------------



#haeding frame
f0 = Frame(root)
heading=Label(root,text="Login System", font =("Times new roman", 30 ,"bold"), fg= "red",bg= "Yellow", bd=10, relief= SUNKEN)
heading.place(relwidth=1)   #place at this position because place means complete stretch and you cannot do that wth grid frame


#Login Frame
f1=Frame(root)  #pass this frame in root
Login_frame= Label(root,image=bgf, bd=15, relief= SUNKEN)
Login_frame.place(x=600,y=150)      #use place because position


#now making label of username and password ------------------------------------------------
#fixing them with grid
#pass this in login frame because we want this in login frame
user = Label(Login_frame, text="Username",fg= "yellow",bg= "black",font =("Lucida", 12 ,"bold")).grid(row=3,pady=5)
password = Label(Login_frame, text="Password",fg= "red",bg= "black",font =("Lucida", 12 ,"bold")).grid(row=4,pady=5)


#entry widger------------------------------
uservalue = StringVar()    #entry widget and remember to write value in variable
passvalue = StringVar()  #entry widget and remember to write value in variable
foodservicevalue = IntVar()

userentry = Entry (Login_frame,bd=5,width=30, textvariable = uservalue)
passentry = Entry (Login_frame,bd=5,width=30, textvariable = passvalue)

userentry.grid(row=3, column=1)
passentry.grid(row=4, column=1)


#------------------ Making CHeckbox Button
foodservice = Checkbutton(Login_frame,text="Keep me logged in",width=14,bg="orange", variable = foodservicevalue)  #if check box is tick then op will be 1
foodservice.grid(row=5,column=1,pady=8)



#-----------------------------------------------------------------------------------------------------------

#now making button
Button(Login_frame,text="Login",font="arial 12 bold",width=8 ,bg="pink",fg="black",command=login).grid(pady=10,row=6, column=1)

#---------------------------------------------------------------------------------------------

#image in frame
userimage = Label(Login_frame,image= photo).grid(row=0,columnspan=3,padx=80, pady=8)


#finally packing this Login frame ===f1
f1.pack(fill=X,pady=10)





root.mainloop()

