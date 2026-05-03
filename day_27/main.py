from tkinter import *

window = Tk()

window.title("Miles to Kilometer converter")
window.minsize(width=200, height= 100)
window.config(padx=20,pady=20)

#entry
input = Entry(width=10)
input.grid(row = 0 , column = 1 )

label1 = Label(text= "Miles")
label1.grid(row = 0 , column = 2)

label2 = Label(text= "is equal to")
label2.grid(row = 1 , column = 0)

value = 0
label3 = Label(text= f"{value}")
label3.grid(row = 1 , column = 1)

label4 = Label(text= "Km")
label4.grid(row = 1 , column = 2)

#button
def button_click():
    a = input.get()
    f = float(a) * 1.6
    label3.config(text= round(f,2))


button = Button(text= "Calculate", command= button_click)
button.grid(row = 2 , column = 1)












window.mainloop()