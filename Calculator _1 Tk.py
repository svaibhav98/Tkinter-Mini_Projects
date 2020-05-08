# Optimized code - Main code
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