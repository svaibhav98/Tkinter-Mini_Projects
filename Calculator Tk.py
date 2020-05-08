from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("450x850")
root.title("Calculator by Vaibhav")
root.configure(background="lightyellow")
root.wm_iconbitmap("calc.ico")


# #adding menu:
mainmenu = Menu(root)
mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)

# Button(text="Exit", command = root.destroy).pack(side=BOTTOM)   >>destroy fn


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


#9-7
f = Frame(root, bg="")
b = Button(f, text="7", padx=15, pady=15, font="lucida 20 bold",fg="black")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

#6-4
f = Frame(root, bg="")
b = Button(f, text="4", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

#3-1
f = Frame(root, bg="")
b = Button(f, text="1", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=15, pady=15, font="lucida 20 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()


#0-*
f = Frame(root, bg="")
b = Button(f, text="0", padx=12.6, pady=14, font="lucida 23 bold")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=15.4, pady=12, font="lucida 25 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=15.6, pady=15, font="lucida 22 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()




f = Frame(root, bg="")
b = Button(f, text="/", padx=18.6, pady=21.5, font="lucida 21 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=15.4, pady=24.7, font="lucida 18 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=16.7, pady=27.3, font="lucida 17 bold",bg="lightblue",fg="red")        #modification req
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="")
b = Button(f, text="C", padx=16.4, pady=19.9, font="lucida 18 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=16.9, pady=17.6, font="lucida 20 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="X", padx=15.2, pady=20.5, font="lucida 18 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()


#+
f = Frame(root, bg="grey")
b = Button(f, text="+", padx=13, pady=13, font="lucida 18 bold",fg= "Blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()

exit()

# Optimized code - Main code but some problem
from tkinter import *

def click(event):
   # global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

    elif text == X:
        try:
            fullstring = value.get()
            # we are replacing the last string item[-1] with blank or ""
            # String slicing method
            newstring = fullstring.replace(fullstring[-1], "")
            value.set(newstring)

            # print(newstring)
            entry1.update()
        except Exception as e:
            print(e)


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("450x400")
root.title("Calculator by Vaibhav")
root.configure(background="lightblue")



root.wm_iconbitmap("calc.ico")


#adding menu:
mainmenu = Menu(root)
mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)



#Making entry widget ....
scvalue = StringVar()
scvalue.set("")
#Modifying entry widget
screen = Entry(root, textvar=scvalue, font="lucida 30 bold", borderwidth=3, relief=SUNKEN)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)    #pack entry widget



#frame of button
f1= Frame(root,bg="")

listofbuttons = ["9", "8", "7", "C", "6", "5", "4", "/", "3", "2", "1", "*", "00", "0", ".", "-", "%", "DEL", "=", "+"]
i = 0  #initially i==0

#for loop in list
for n in listofbuttons:
    # here width of button means 1 text width
    button = Button (f1, text=n, font="lucida 20 ", padx=35, width=1, )
    button.grid(row=int(i / 4), column=i % 4)         #buttons ko pack
    i = i + 1

    button.bind("<Button-1>", click)      #button ko bind kiyaa...

f1.pack()    #frame pack



root.mainloop()