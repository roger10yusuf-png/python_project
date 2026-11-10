from tkinter import *
window = Tk()
window.title("temperature converter")
window.geometry("800x800")
window.configure(bg= "green")

def NGN_to_EUR():
    c = float(entry.get())
    calc = c * 0.00066
    label2.configure(text= calc)

label = Label(window, text= "Money converter", bg= "green", fg= "black", font= ("bold", 40))
label.place(x= 200, y= 0)
label1 = Label(window, text= "NGN", bg= "green", fg= "black", font= ("bold", 16))
label1.place(x= 150, y= 300)
entry = Entry(window, width= 10)
entry.place(x= 275, y= 325)
label2 = Label(window, text= "EUR", bg= "green", fg= "black", font= ("bold", 16))
label2.place(x= 450, y= 325)
button = Button(window, text= "convert", font= ("boldd", 16), command= NGN_to_EUR)
button.place(x= 350, y= 375)

window.mainloop()