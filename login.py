from tkinter import *

root = Tk() # open root window
root.title("Sign in")

Label(root,text="Username:").grid(row=1,column = 1)
username = StringVar()
Entry(root,textvariable=username,text="").grid(row=1,column=2)

Label(root,text="Password:").grid(row=2,column = 1)
password = StringVar()
Entry(root,textvariable=password,text="").grid(row=2,column=2)

login=Button(root,text="Sign in").grid(row=4,column=2)
signUp=Button(root,text="Create User").grid(row=5,column=2)

root.mainloop()
