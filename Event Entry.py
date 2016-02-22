from tkinter import *

root = Tk() # open root window
root.title("Event Entry") #sets title of window

Label(root,text="Fill in boxes and press 'Submit'").grid(row=0,column = 1) #To help user understand GUI

Label(root,text="User:").grid(row=1,column = 0)
user = StringVar()
Entry(root,textvariable=user).grid(row=1,column=1)

Label(root,text="Event:").grid(row=2,column = 0)
event = StringVar()
Entry(root,textvariable=event).grid(row=2,column=1)   # Setting label names, variables, entry fields and positions

Label(root,text="Start:").grid(row=3,column = 0)
start = IntVar()
Entry(root,textvariable=start,text="").grid(row=3,column=1)

Label(root,text="End:").grid(row=4,column = 0)
end = IntVar()
Entry(root,textvariable=end,text="").grid(row=4,column=1)

Label(root,text="Date:").grid(row=5,column = 0)
date = IntVar()
Entry(root,textvariable=date,text="").grid(row=5,column=1)

Label(root,text="Description:",height=3).grid(row=6,column = 0)
description = StringVar()
Text(root,width=35, height=3).grid(row=7,column=1)

rb1=Radiobutton(root, text="Username",value=1).grid(row=8,column = 0)
rb2=Radiobutton(root, text="Username",value=2).grid(row=9,column = 0)
rb3=Radiobutton(root, text="Username",value=3).grid(row=10,column = 0)
rb4=Radiobutton(root, text="Username",value=4).grid(row=11,column = 0)
rb5=Radiobutton(root, text="Username",value=5).grid(row=12,column = 0)
rb6=Radiobutton(root, text="Username",value=6).grid(row=8,column = 1)
rb7=Radiobutton(root, text="Username",value=7).grid(row=9,column = 1)
rb8=Radiobutton(root, text="Username",value=8).grid(row=10,column = 1)
rb9=Radiobutton(root, text="Username",value=9).grid(row=11,column = 1)
rb10=Radiobutton(root, text="Username",value=10).grid(row=12,column = 1)
rb11=Radiobutton(root, text="Select All",value=11).grid(row=13,column = 1)

cancelBtn= Button(root,text="Cancel").grid(row=15,column=0)
submitBtn = Button(root, text="Submit").grid(row=15,column=1) 

root.mainloop()

#Github program for windows
#Talk to group about...
#edit/delete page
#Create Group page
