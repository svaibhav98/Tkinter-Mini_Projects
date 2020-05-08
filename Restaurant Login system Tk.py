from tkinter import *
import  tkinter.messagebox
from tkinter import ttk   #to make the combo
import random
import time
import datetime



def main():
    root=Tk()
    app = window1(root)


class window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Restaurant login system")
        self.master.geometry('130x750+0+0')
        self.master.config(bg= "light blue")

        #this frame system is going to be resident or placed
        self.frame = Frame(self.master, bg="light blue")
        self.frame.pack()

        self.Username= StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="Restuarant Login System", font =('arial',50, 'bold'),bg="blue", fg= "black")
        self.lblTitle.grid(row=0,column = 0, columnspan = 2, pady=40)
#---------------------------------------------------------------------------------------------------------------------------------------------

        self.LoginFrame1= LabelFrame(self.frame, width=1350, height=600, font =('arial',20, 'bold'), relief = 'ridge',bg="cadet blue",bd =20)
        self.LoginFrame1.grid(row=1, column=0)


        self.LoginFrame2 = LabelFrame(self.frame, width=1350, height=600, font=('arial', 20, 'bold'), relief='ridge',
                                 bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=1, column=0)


#_____________________________________________Label and Entry_____________________________________________________________________________________________________________________
        self.lblUsername = Label(self.LoginFrame1, text="username",font=('arial', 20, 'bold'), bd=22, bg= "cadet blue",fg= "red")
        self.lblUsername.grid(row=0, column=0)

        self.txtUsername = Entry(self.LoginFrame1, font=('arial', 20, 'bold')textvariable = self.Username)
        self.txtUsername.grid(row=0, column=1, padx=100)


        self.lblPassword = Label(self.LoginFrame1, text="Password",font=('arial', 20, 'bold'), bd=22, bg= "cadet blue",fg= "red")
        self.lblPassword.grid(row=0, column=0)


        self.txtPassword = Entry(self.LoginFrame1, font=('arial', 20, 'bold'),show= '*', textvariable = self.Password)
        self.txtPassword.grid(row=1, column=1,columnspan=2,pady=30)

#buttons______________________________________________________________________________________________________________
        self.btnLogin = Button(self.LoginFrame2,text ="login", font=('arial', 20, 'bold'),width=17, command= self.Login_System)
        self.btnLogin.grid(row=3, column=0,pady=20, padx=8)

        self.btnReset = Button(self.LoginFrame2, text="Reset", width=17, font=('arial', 20, 'bold'), command=self.Rest)
        self.btnReset.grid(row=3, column=1,pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text="Exit", font=('arial', 20, 'bold'), width=17, command=self.iExit)
        self.btnExit.grid(row=3, column=2,pady=20, padx=8)
#______________________________________________________________________________________________________________
    def Login_System(self):
        u=(self.Username.get())
        p = (self.Password.get())

        if u == str(123456789) and p == str("vaibhav"):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Login Systems", "Too Bad, Invalid login details")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Rest(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
            self.iExit = tkinter.messagebox.askyesno("Login systems","comfirm if you want to exit")
            if self.iExit>0:
                self.master.destroy()
            else:
                command = self.new_window()
                return


#declaring a fn to call a app window
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

#second window ________
class window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Restaurant Management system")
        self.master.geometry('130x750+0+0')
        self.master.config(bg= "cadet blue")

        #this frame system is going to be resident or placed
        self.frame = Frame(self.master, bg="light blue")
        self.frame.pack()


#---------------------------------------------------------------------------------------------------------------------------
#             inside code window

#============================================================================================

if __main__=='main__':
    main()
