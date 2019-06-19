from tkinter import *
from plotting import plot_function
from cmeans import main
from BGV import Decrypt
from BGV import Encrypt
from BGV import Generate

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
    out = main()
    print("out",out)
    return 0


def clicked2():
    print("key ")
    Generate()
    return 0


def clicked3():
    print("Encrypt ")
    Encrypt()
    return 0


def clicked4():
    print("Decrypt ")
    Decrypt()
    return 0




generate = Button(window, text="Generate clusters", command=clicked)

generate.grid( row=0,column=2)


key = Button(window, text="key Generate", command=clicked2)

key.grid( row=1,column=2)

Encrypt = Button(window, text="Encrypt ", command=clicked3)

Encrypt.grid( row=2,column=2)


Decrypt = Button(window, text="Decrypt ", command=clicked4)

Decrypt.grid( row=3,column=2)



window.mainloop()