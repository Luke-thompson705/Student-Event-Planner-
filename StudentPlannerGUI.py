# python3 #http://stackoverflow.com/questions/7546050/#switch-between-two-frames-in-tkinter
#http://www.tkdocs.com/tutorial/widgets.html
import tkinter as tk
from tkinter import ttk
from tkinter import *
from LoginSystem import *
import tkinter as Tkinter
from tkinter import simpledialog as tkSimpleDialog
#import Tkinter as tk   # python
import CalendarWidget as ttkcalendar

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
        for F in (StartPage,Login, SignUp, Events, AddEvent,EditEvent,CreateGroup):
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

        button1 = tk.Button(self, text="Events Calendar",
                            command=lambda: main(controller))
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
        self.uNameEntry=tk.Entry(self,textvariable=tk.StringVar())
        self.uNameEntry.pack()

        passwordLbl=tk.Label(self,text="Password:").pack()
        self.pwEntry=tk.Entry(self,textvariable=tk.StringVar(),show="*")
        self.pwEntry.pack()
        button = tk.Button(self, text="Sign In",
                           command=lambda: self.login())
        signUpButton = tk.Button(self, text="Sign Up",
                           command=lambda: self.signUp())
        button.pack()
        signUpButton.pack()

    def login(self):
        if tryLogin(self.uNameEntry.get(),self.pwEntry.get()):
            global user
            user=self.uNameEntry.get()
            self.controller.show_frame("StartPage")
            self.uNameEntry.delete(0,"end")
            self.pwEntry.delete(0,"end")
        elif not tryLogin(self.uNameEntry.get(),self.pwEntry.get()):
            errorbox = Toplevel()
            centerDoNotUse(errorbox)
            errorbox.title("Attention")
            errormessage = Message(errorbox, text="Username/ Password combination incorrect")
            errormessage.pack()
            button = Button(errorbox, text="Ok", command=errorbox.destroy)
            button.pack()

    def signUp(self):
        self.uNameEntry.delete(0,"end")
        self.pwEntry.delete(0,"end")
        self.controller.show_frame("SignUp")

class SignUp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Sign Up", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        usernameLbl=tk.Label(self,text="Username:").pack()
        self.uNameEntry=tk.Entry(self,text="")
        self.uNameEntry.pack()

        passwordLbl=tk.Label(self,text="Enter Password:").pack()
        self.pwEntry=tk.Entry(self,text="",show="*")
        self.pwEntry.pack()

        confirmPasswordLbl=tk.Label(self,text="Confirm Password:").pack()
        self.confirmPwEntry=tk.Entry(self,text="",show="*")
        self.confirmPwEntry.pack()

        button = tk.Button(self, text="Create User",
                           command=lambda:self.createUser())
        button.pack()
        exitButton = tk.Button(self, text="Exit",
                           command=lambda: self.exit())
        exitButton.pack()

    def createUser(self):
        name=self.uNameEntry.get()
        pw=self.pwEntry.get()
        pwc=self.confirmPwEntry.get()
        if not isUser(name):
            if noSpaces(name):
                if noSpaces(pw):
                    if pw==pwc:
                        addUser(name,pw)
                        self.controller.show_frame("Login")
                        self.uNameEntry.delete(0,"end")
                        self.pwEntry.delete(0,"end")
                        self.confirmPwEntry.delete(0,"end")
                        errorbox = Toplevel()
                        centerDoNotUse(errorbox)
                        errorbox.title("Congratulations")
                        errormessage = Message(errorbox, text="An Account for "+name+" has been created. Please sign-in.")
                        errormessage.pack()
                        button = Button(errorbox, text="Ok", command=errorbox.destroy)
                        button.pack()
                    else:
                        errorbox = Toplevel()
                        centerDoNotUse(errorbox)
                        errorbox.title("Attention")
                        errormessage = Message(errorbox, text="Passwords do not match")
                        errormessage.pack()
                        button = Button(errorbox, text="Ok", command=errorbox.destroy)
                        button.pack()
                else:
                    errorbox = Toplevel()
                    centerDoNotUse(errorbox)
                    errorbox.title("Attention")
                    errormessage = Message(errorbox, text="Passwords cannot contain spaces")
                    errormessage.pack()
                    button = Button(errorbox, text="Ok", command=errorbox.destroy)
                    button.pack()
            else:
                errorbox = Toplevel()
                centerDoNotUse(errorbox)
                errorbox.title("Attention")
                errormessage = Message(errorbox, text="The username cannot contain spaces")
                errormessage.pack()
                button = Button(errorbox, text="Ok", command=errorbox.destroy)
                button.pack()
        elif isUser(name):
            errorbox = Toplevel()
            centerDoNotUse(errorbox)
            errorbox.title("Attention")
            errormessage = Message(errorbox, text="Please enter a different username")
            errormessage.pack()
            button = Button(errorbox, text="Ok", command=errorbox.destroy)
            button.pack()

    def exit(self):
        self.uNameEntry.delete(0,"end")
        self.pwEntry.delete(0,"end")
        self.confirmPwEntry.delete(0,"end")
        self.controller.show_frame("Login")

#main() and the CalendarDialog class are modifided virsions of the code found at
#https://github.com/moshekaplan/tkinter_components/tree/master/CalendarDialog
def main(controller):
    root = app
    root.wm_title("Calendar")

    cd = CalendarDialog(root)
    global eDate
    check=True
    while check:
        try:

            eDate=(cd.result.strftime('%m/%d/%Y'))
            print(cd.result.strftime('%m/%d/%Y'))
            check=False

        except AttributeError:
            cd = CalendarDialog(root)

    print(eDate)
    cd.destroy()
    controller.show_frame("Events")



class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection



class Events(tk.Frame):

    def __init__(self, parent, controller):
        import calendar as cd#calendar usage info from https://pymotw.com/2/calendar/
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global eDate
        label = tk.Label(self, textvariable=eDate, font=TITLE_FONT)
        label.pack()
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
        label = tk.Label(self, text="Create Group", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Exit")
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
    user=""
    eDate=StringVar
    app = StudentPlannerGUI()
    center(app)
    app.mainloop()
