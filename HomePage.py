from tkinter import *

root = Tk() # open root window
root.title("Home") #sets title of window

addEventBtn=Button(root,text="Add Event").grid(row=1,column=1)
createGroup=Button(root,text="Create a Group").grid(row=1,column=2)#need page for this
viewCalendarBtn=Button(root,text="View Calendar").grid(row=1,column=3)
signIn=Button(root,text="Sign Out").grid(row=3,column=2)
