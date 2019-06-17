from tkinter import *
from plotting import plot_function
from cmeans import main

window = Tk()

window.title("Big Data Clustering")

window.geometry('350x200')



# Add a grid
mainframe = Frame(window)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )


# Create a Tkinter variable
tkvar = StringVar(window)


# Dictionary with options
choices = { '1','2','3','4','5'}
tkvar.set('1') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose clusters ").grid(row = 1, column = 0)
popupMenu.grid(row = 1, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )



def clicked():
    data = tkvar.get()
    plot_function(data)
    main()




btn = Button(window, text="Generate", command=clicked)

btn.grid( row=0,column=2)

window.mainloop()