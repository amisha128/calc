from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x900")
root.title("Calculator")
root.resizable(0, 0)
root.configure(bg="lightblue")

#Entry box for taking input
calc_var = StringVar()
calc_entry = Entry(root, textvar=calc_var, font="time 25 bold", width=28, fg="red")
calc_entry.place(x=53, y=10, height=100)

#Click function
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if calc_var.get().isdigit():
            value = int(calc_var.get())
        else:
            value = eval(calc_var.get())

        calc_var.set(value)
        root.update()

    elif text == "C":
        calc_var.set("")
        root.update()

    elif text == "Q":
        root.destroy()

    elif text == "H":
        tmsg.showinfo("Help Section", "Basic Calculator\n'+': Addition\n'-': Subtraction\n'*': Multiplication\n'/': Divide\n'%': Returns Remainder\n'C': To Cancel\n'Q': To exit\n'H': Help section")

    else:
        calc_var.set(calc_var.get() + text)
        root.update()




#Frame 1
f1 = Frame(root, bg="lightgray")
f1.place(x=50, y=130)
f1_btn_list = ["7", "8", "9", "+"]
for i in f1_btn_list:
    btn = Button(f1, text=i, font="georgia 25 bold", padx=20, pady=20)
    btn.pack(side=LEFT, padx=17, pady=12)
    btn.bind("<Button-1>", click)


#Frame 2
f2 = Frame(root, bg="lightgray")
f2.place(x=50, y=270)
f2_btn_list = ["4", "5", "6", "-"]
for i in f2_btn_list:
    btn2 = Button(f2, text=i, font="georgia 25 bold", padx=20, pady=20)
    btn2.pack(side=LEFT, padx=18, pady=12)
    btn2.bind("<Button-1>", click)


#Frame 3
f3 = Frame(root, bg="lightgray")
f3.place(x=50, y=410)
f3_btn_list = ["1", "2", "3", "*"]
for i in f3_btn_list:
    btn3 = Button(f3, text=i, font="georgia 25 bold", padx=20, pady=20)
    btn3.pack(side=LEFT, padx=18, pady=12)
    btn3.bind("<Button-1>", click)

#Frame 4
f4 = Frame(root, bg="lightgray")
f4.place(x=50, y=550)
f4_btn_list = ["0", "/", "C", "="]
for i in f4_btn_list:
    btn4 = Button(f4, text=i, font="georgia 25 bold", padx=18, pady=20)
    btn4.pack(side=LEFT, padx=18, pady=12)
    btn4.bind("<Button-1>", click)

#Frame 5
f5 = Frame(root, bg="lightgray")
f5.place(x=50, y=690)
f5_btn_list = ["%", ".","H", "Q"]
for i in f5_btn_list:
    btn5 = Button(f5, text=i, font="georgia 25 bold", padx=18, pady=20)
    btn5.pack(side=LEFT, padx=16, pady=12)
    btn5.bind("<Button-1>", click)




root.mainloop()
