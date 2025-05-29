from tkinter import *
from tkinter import messagebox

#setting up main window
root = Tk()
root.title("Denomination Calculator")

root.geometry("400x400")
label1 = Label(root, text="HELLO!! Welcome to my Denomination Calculator")
label1.pack(pady=20)

def msg():
    response = messagebox.askyesno("Conformation", "Do you want to calculate denomination")
    if response:
        open_calculator()
button1= Button(root, text="START CALCULATING")
button1.pack(pady=10)

def open_calculator():
    top = Toplevel()
    top.title("Qoutient")
    top.geometry("200x200")

    Label(top, text="ENTER THE THE AMOUNT").pack(pady=5)
    amount_entry = Entry(top)
    amount_entry.pack(pady=5)
    
    Label(top, text="₹1000 notes:").pack()
    t1 = Entry(top)
    t1.pack()

    Label(top, text="₹500 notes:").pack()
    t2 = Entry(top)
    t2.pack()

    Label(top, text="₹100 notes:").pack()
    t3 = Entry(top)
    t3.pack()

    def calculate():
        try:
            amount = int(amount_entry.get())
            note1000 = amount // 1000
            amount %= 1000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100
            amount %= 100

            t1.delete(0, END)
            t1.insert(END, str(note1000))

            t2.delete(0, END)
            t2.insert(END, str(note500))

            t3.delete(0, END)
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            
    Button(top, text="Calculate", command=calculate).pack(pady=10)

root.mainloop()