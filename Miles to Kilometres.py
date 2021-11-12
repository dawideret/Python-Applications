from tkinter import *
window = Tk()

miles = 0
kilometres = 0

def Button1Click():
    miles = int(txtfld1.get())
    kilometres = miles * 1.61
    txtfld2.delete(0, "end")
    txtfld2.insert(END, str(kilometres))

def Button2Click():
    kilometres = int(txtfld2.get())
    miles = kilometres * 0.62
    txtfld1.delete(0, "end")
    txtfld1.insert(END, str(miles))
    
button1 = Button(window, text = "Convert Miles to KM", fg = "black", command = Button1Click)
button2 = Button(window, text = "Convert KM to Miles", fg = "black", command = Button2Click)

label1 = Label(window, text = "Miles", fg = "black", font = ("Verdana", 12))
label2 = Label(window, text = "Kilometres", fg = "black", font = ("Verdana", 12))

txtfld1 = Entry(window, text = "", bd = 5)
txtfld2 = Entry(window, text = "", bd = 5)

button1.place(x = 240, y = 240)
button2.place(x = 240, y = 280)

label1.place (x = 140, y = 140)
label2.place (x = 140, y = 170)

txtfld1.place (x = 280, y = 140)
txtfld2.place (x = 280, y = 170)

window.title("Form1")
window.geometry("640x480")
window.mainloop()
