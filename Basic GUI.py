from tkinter import *
window = Tk()


def add():
    value1 = int(txtfld1.get())
    value2 = int(txtfld2.get())
    txtfld3.delete(0, "end")
    txtfld3.insert(END, str(value1 + value2))

def substract():
    value1 = int(txtfld1.get())
    value2 = int(txtfld2.get())
    txtfld3.delete(0, "end")
    txtfld3.insert(END, str(value1 - value2))
    
def multiply():
    value1 = int(txtfld1.get())
    value2 = int(txtfld2.get())
    txtfld3.delete(0, "end")
    txtfld3.insert(END, str(value1 * value2))

def divide():
    value1 = int(txtfld1.get())
    value2 = int(txtfld2.get())
    txtfld3.delete(0, "end")
    txtfld3.insert(END, str(value1 / value2))

    
button1 = Button(window, text = "Add", fg = "black", command = add)
button2 = Button(window, text = "Substract", fg = "black", command = substract)
button3 = Button(window, text = "Multiply", fg = "black", command = multiply)
button4 = Button(window, text = "Divide", fg = "black", command = divide)

label1 = Label(window, text = "First Value", fg = "black", font = ("Verdana", 12))
label2 = Label(window, text = "Second Value", fg = "black", font = ("Verdana", 12))
label3 = Label(window, text = "Result", fg = "black", font = ("Verdana", 12))

txtfld1 = Entry(window, text = "", bd = 5)
txtfld2 = Entry(window, text = "", bd = 5)
txtfld3 = Entry(window, text = "", bd = 5)

button1.place(x = 20, y = 135)
button2.place(x = 20, y = 170)
button3.place(x = 20, y = 205)
button4.place(x = 20, y = 240)
label1.place (x = 15, y = 70)
label2.place (x = 215, y = 70)
label3.place (x = 415, y = 70)
txtfld1.place (x = 20, y = 100)
txtfld2.place (x = 220, y = 100)
txtfld3.place (x = 420, y = 100)

window.title("Calculator")
window.geometry("800x400")
window.mainloop()
