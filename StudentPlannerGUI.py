# python3 #http://stackoverflow.com/questions/7546050/#switch-between-two-frames-in-tkinter
#http://www.tkdocs.com/tutorial/widgets.html
import tkinter as tk
from tkinter import ttk
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")

class StudentPlannerGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,Login, SignUp, Calendar, AddEvent,EditEvent,CreateGroup):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]  
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Homepage", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Calendar",
                            command=lambda: controller.show_frame("Calendar"))
        button2 = tk.Button(self, text="Add Event",
                            command=lambda: controller.show_frame("AddEvent"))
        button3 = tk.Button(self, text="Edit Event",
                            command=lambda: controller.show_frame("EditEvent"))
        button4 = tk.Button(self, text="Create Group",
                            command=lambda: controller.show_frame("CreateGroup"))
        button5 = tk.Button(self, text="Sign Out",
                            command=lambda: controller.show_frame("Login"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Sign In", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        usernameLbl=tk.Label(self,text="Username:").pack()
        uNameEntry=tk.Entry(self,text="").pack()

        passwordLbl=tk.Label(self,text="Password:").pack()
        pwEntry=tk.Entry(self,text="").pack()
        
        button = tk.Button(self, text="Sign In",
                           command=lambda: controller.show_frame("StartPage"))

        signUpButton = tk.Button(self, text="Sign Up",
                           command=lambda: controller.show_frame("SignUp"))
        button.pack()
        signUpButton.pack()

class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Sign Up", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        usernameLbl=tk.Label(self,text="Username:").pack()
        uNameEntry=tk.Entry(self,text="").pack()

        passwordLbl=tk.Label(self,text="Enter Password:").pack()
        pwEntry=tk.Entry(self,text="").pack()

        confirmPasswordLbl=tk.Label(self,text="Confirm Password:").pack()
        confirmPwEntry=tk.Entry(self,text="").pack()
        
        button = tk.Button(self, text="Create User",
                           command=lambda: controller.show_frame("Login"))
        button.pack() 

class Calendar(tk.Frame):

    def __init__(self, parent, controller):
        import calendar as cd#calendar usage info from https://pymotw.com/2/calendar/
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Calendar", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        month=2
        year=2016
        str1=cd.month(year,month)

        monthLbl=tk.Label(self,text="Month:").pack()
        monthEntry=tk.Entry(self,text="").pack()

        yearLbl=tk.Label(self,text="Year:").pack()
        YearEntry=tk.Entry(self,text="").pack()

        calendarLbl=tk.Label(self,text=str1,width=35, height=10, font=('courier', 14, 'bold'))\
                                       .pack() 

        dateSelectLbl=tk.Label(self,text="Select Date:").pack()
        dsEntry=tk.Entry(self,text="").pack()
        eventSelectBtn= tk.Button(self,text="Go").pack() #add message box containing info?

        button = tk.Button(self, text="Exit",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class AddEvent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Event", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        aidLbl=tk.Label(self,text="Fill in boxes and press 'Submit'").pack() #To help user understand GUI

        userLbl=tk.Label(self,text="User:").pack()
        userEntry=tk.Entry(self,text="").pack()

        eventLbl=tk.Label(self,text="Event:").pack()
        eventEntry=tk.Entry(self,text="").pack()   # Setting label names, variables, entry fields and positions

        startLbl=tk.Label(self,text="Start:").pack()
        startEntry=tk.Entry(self,text="").pack()

        endLbl=tk.Label(self,text="End:").pack()
        endEntry=tk.Entry(self,text="").pack()

        dateLbl=tk.Label(self,text="Date:").pack()
        dateEntry=tk.Entry(self,text="").pack()

        descrLbl=tk.Label(self,text="Description:").pack()
        descrTxt=tk.Text(self,width=35, height=3).pack()

        rb1=tk.Radiobutton(self, text="Username",value=1).pack(anchor='w')
        rb2=tk.Radiobutton(self, text="Username",value=2).pack(anchor='w')
        rb3=tk.Radiobutton(self, text="Username",value=3).pack(anchor='w')
        rb6=tk.Radiobutton(self, text="Username",value=6).pack(anchor='e')
        rb7=tk.Radiobutton(self, text="Username",value=7).pack(anchor='e')
        rb8=tk.Radiobutton(self, text="Username",value=8).pack(anchor='e')
        rb11=tk.Radiobutton(self, text="Select All",value=11).pack()
        
        submitBtn = tk.Button(self, text="Submit").pack() 
        button = tk.Button(self, text="Exit",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="right")

class EditEvent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Edit Event", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        
        aidLbl=tk.Label(self,text="Select event, make changes, then press 'Save Changes' or delete").pack()
        #To help user understand GUI

        eventListLB=tk.Label(self,text="Select Event:").pack()
        eventListCB=ttk.Combobox(self).pack()
        
        userLbl=tk.Label(self,text="User:").pack()
        userEntry=tk.Entry(self,text="").pack()

        eventLbl=tk.Label(self,text="Event:").pack()
        eventEntry=tk.Entry(self,text="").pack()   # Setting label names, variables, entry fields and positions

        startLbl=tk.Label(self,text="Start:").pack()
        startEntry=tk.Entry(self,text="").pack()

        endLbl=tk.Label(self,text="End:").pack()
        endEntry=tk.Entry(self,text="").pack()

        dateLbl=tk.Label(self,text="Date:").pack()
        dateEntry=tk.Entry(self,text="").pack()

        descrLbl=tk.Label(self,text="Description:").pack()
        descrTxt=tk.Text(self,width=35, height=3).pack()

        rb1=tk.Radiobutton(self, text="Username",value=1).pack(anchor='w')
        rb2=tk.Radiobutton(self, text="Username",value=2).pack(anchor='w')
        rb3=tk.Radiobutton(self, text="Username",value=3).pack(anchor='w')
        rb6=tk.Radiobutton(self, text="Username",value=6).pack(anchor='e')
        rb7=tk.Radiobutton(self, text="Username",value=7).pack(anchor='e')
        rb8=tk.Radiobutton(self, text="Username",value=8).pack(anchor='e')
        rb11=tk.Radiobutton(self, text="Select All",value=11).pack()
        
        submitBtn = tk.Button(self, text="Save Changes").pack() 
        deleteBtn = tk.Button(self, text="Delete Event").pack(side="right")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Exit",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side="left")

class CreateGroup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create Group", font=TITLE_FONT).pack(side="top", fill="x", pady=10)
        helpLbl=tk.Label(self,text="Click username to add to group:").pack()


        self.list_box_1 = tk.Listbox(self, selectmode="extended")
        self.list_box_1.pack()
        self.add_button = tk.Button(self, text="Add to Group",command=self.AddToList)
        self.add_button.pack()
        self.list_box_2 = tk.Listbox(self, selectmode="extended")
        self.list_box_2.pack()

        for i in  ["Oli", "Steven", "Luke", "Lee", "Harry"]:
            s = str(i)
            self.list_box_1.insert( "end",s )

        submitBtn = tk.Button(self, text="Save and Exit",command=lambda:controller.show_frame("StartPage")).pack()
        button = tk.Button(self, text="Cancel and Exit",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def AddToList(self) :
        items = self.list_box_1.curselection()
        pos = 0
        for i in items :
            idx = int(i) - pos
            s = self.list_box_1.get(idx)
            self.list_box_1.delete( idx,idx )
            self.list_box_2.insert("end",s)
            pos = pos + 1
            

        

        
if __name__ == "__main__":
    app = StudentPlannerGUI()
    app.mainloop()
