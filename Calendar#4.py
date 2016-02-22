from tkinter import *
import calendar as cd#calendar usage info from https://pymotw.com/2/calendar/

month=int(input("Enter the number of a month, e.g. February = 2: "))
year=int(input("Enter the year,e.g. 2016: "))

str1=cd.month(year,month)

root = Tk() # open root window
root.title("Calendar") #sets title of window

Label(root,text="Calendar",height=3).grid(row=0,column = 2)

Label(root,text="Month:").grid(row=1,column=1)
month = IntVar()
Entry(root,textvariable=month,text="").grid(row=1,column=2)

Label(root,text="Year:").grid(row=2,column=1)
year = IntVar()
Entry(root,textvariable=year,text="").grid(row=2,column=2)

Label(root,text=str1,width=35, height=10, font=('courier', 14, 'bold'),justify=LEFT)\
                               .grid(row=3,column=1,columnspan=3) #calendar print out

Label(root,text="Date select: ").grid(row=4,column = 1)
dateSelect = IntVar()
Entry(root,textvariable=dateSelect,text="").grid(row=4,column=2)
eventSelectBtn= Button(root,text="Go").grid(row=4,column=3) #add message box containing info?

closeBtn= Button(root,text="Exit").grid(row=6,column=4)
root.mainloop()


