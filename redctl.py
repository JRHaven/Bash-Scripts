# The python redctl file contains a graphic frontend to the redctl script. This was my first Tk project.

# Libraries Needed
from tkinter import Tk, StringVar, Radiobutton, Label, Button
from os import system

# Function to figure out what to execute depending on what entered
def execu():
    '''
    print("Execute Called")
    print(var.get())
    '''
    if(var.get() == "1"):
        #print("Got to If")
        system("~/bin/redctl off")
    elif(var.get() == "2"):
        #print("Got to If")
        system("~/bin/redctl 1")
    elif(var.get() == "3"):
        #print("Got to If")
        system("~/bin/redctl 2")
    elif(var.get() == "4"):
        #print("Got to If")
        system("~/bin/redctl 3")
    elif(var.get() == "5"):
        #print("Got to If")
        system("~/bin/redctl 4")
    elif(var.get() == "6"):
        system("~/bin/redctl 5")
    elif(var.get() == "7"):
        #print("Got to If")
        system("~/bin/redctl 6")
    elif(var.get() == "8"):
        #print("Got to If")
        system("~/bin/redctl 7")
    else:
        statuslabel.configure(text="Unexpected Error. Closing in 5 seconds...")
        statuslabel.after(5000, func=dest)

# Close
def dest():
    root.destroy()

# Select
def select():
    print(var.get())
    
# Get the window ready
root = Tk()
root.title("Redctl Tk Frontend")
var = StringVar()

# Interface
Label(root, text="Welcome to the Redctl Graphic Frontend!!!").grid(row=0, column=5, padx=5, pady=5)
Radiobutton(root, text="Off", variable=var, value=1).grid(row=1, column=1)
Radiobutton(root, text="Level 1", variable=var, value=2).grid(row=2, column=1)
Radiobutton(root, text="Level 2", variable=var, value=3).grid(row=3, column=1)
Radiobutton(root, text="Level 3", variable=var, value=4).grid(row=4, column=1)
Radiobutton(root, text="Level 4", variable=var, value=5).grid(row=5, column=1)
Radiobutton(root, text="Level 5", variable=var, value=6).grid(row=6, column=1)
Radiobutton(root, text="Level 6", variable=var, value=7).grid(row=7, column=1)
Radiobutton(root, text="Level 7", variable=var, value=8).grid(row=8, column=1)

# Labels for spacing
Label(root, text=" ").grid(row=0, column=0)
Label(root, text=" ").grid(row=0, column=6)
Label(root, text=" ").grid(row=0, column=2)
Label(root, text=" ").grid(row=0, column=3)
Label(root, text=" ").grid(row=0, column=4)
Label(root, text=" ").grid(row=0, column=7)
Label(root, text=" ").grid(row=0, column=8)
Label(root, text=" ").grid(row=0, column=9)
Label(root, text=" ").grid(row=0, column=10)
Label(root, text=" ").grid(row=0, column=11)
Label(root, text=" ").grid(row=0, column=12)
Label(root, text=" ").grid(row=0, column=13)
Label(root, text=" ").grid(row=0, column=14)
Label(root, text=" ").grid(row=0, column=15)

# Create a status lable
statuslabel = Label(root, text="")
statuslabel.grid(row=9, column=5)

# Execute button
Button(root, text="Execute", command=execu).grid(row=10, column=5, padx=5, pady=5)

# Loop
root.mainloop()
