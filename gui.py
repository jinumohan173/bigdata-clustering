
from tkinter import *
from k_means import plot_function



window = Tk()

window.title("Big Data Clustering")

window.geometry('350x200')

lbl = Label(window, text="Enter number of cluster ")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)


btn = Button(window, text="Generate", command=clicked)

btn.grid(column=2, row=0)


def clicked():
    res = "number of cluster " + txt.get()+" "
    data =  txt.get()
    plot_function(data)
    lbl.configure(text=res)



window.mainloop()