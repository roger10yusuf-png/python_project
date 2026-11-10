from tkinter import *
import random

window = Tk()
window.title("Rock, paper, scissors.")
window.geometry("800x500")
window.configure(bg= "yellow")

label = Label(window, text= "Rock, paper, scissors", bg= "yellow", fg= "black", font= ("bold", 40))
label.place(x= 200, y= 0)
label1 = Label(window, text= "your options:", bg= "yellow", fg= "black", font= ("bold", 18))
label1.place(x= 90, y= 100)
button = Button(window, text= "Rock", background= "green", fg= "black", font= ("bold", 18))
button.place(x= 200, y= 150)
button1 = Button(window, text= "Paper", font= ("bold", 18))
button1.place(x= 350, y= 150)
button2 = Button(window, text= "Scissors", font= ("bold", 18))
button2.place(x= 500, y= 150)
label2 = Label(window, text= "you selected:", bg= "yellow", fg= "black", font= ("bold", 18))
label2.place(x= 100, y= 250)
label3 = Label(window, text= "computer selected:", bg= "yellow", fg= "black", font= ("bold", 18))
label3.place(x= 100, y= 350)



window.mainloop()