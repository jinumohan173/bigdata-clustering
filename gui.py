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

lbl_accuracy = Label(window, text="accuracy")
 
lbl_accuracy.grid(column=0, row=2)

lbl_precision = Label(window, text="precision")
 
lbl_precision.grid(column=0, row=3)


lbl_status = Label(window, text="")
 
lbl_status.grid(column=2, row=6)


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
    Button(window, text="Generate clusters",bg="orange", fg="red")
    out = main()
    res_accuracy = "accuracy " + str(out[0][0])
    lbl_accuracy.configure(text= res_accuracy)
    res_precision = "precision " + str(out[1][0])
    lbl_precision.configure(text= res_precision)
    print("out",out)
    return 0


def clicked2():
    print("key ")
    Generate()
    res_status = "key genrating"
    lbl_status.configure(text= res_status)
    return 0


def clicked3():
    print("Encrypt ")
    Encrypt()
    res_status = ("File Encrypted ")
    lbl_status.configure(text= res_status)
    return 0


def clicked4():
    print("Decrypt ")
    Decrypt()
    res_status = ("File Decrypted ")
    lbl_status.configure(text= res_status)
    return 0




generate_button = Button(window, text="Generate clusters",bg="orange", fg="red" ,command=clicked)

generate_button.grid( row=0,column=2)


key_button = Button(window, text="key Generate", command=clicked2)

key_button.grid( row=1,column=2)

Encrypt_button = Button(window, text="Encrypt file ", command=clicked3)

Encrypt_button.grid( row=2,column=2)


Decrypt_button = Button(window, text="Decrypt file ", command=clicked4)

Decrypt_button.grid( row=3,column=2)



window.mainloop()