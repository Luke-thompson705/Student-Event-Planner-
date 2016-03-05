__author__ = 'Harry'
from tkinter import *


def tryLogin(username, password):
    myfile = open("PasswordDatabase")
    data = []
    for eachline in myfile:
        eachline = eachline.strip("\n")
        data = eachline.split(" ")
        if username == data[0]:
            if data[1] == password:
                return True

            else:
                return False
    myfile.close()
    return False


def addUser(username, password):
    myfile = open("PasswordDatabase", "a")
    myfile.write("\n" + username + " " + password)
    myfile.close()


def removeUser(username):
    data = []
    myfile = open("PasswordDatabase", "r+")
    contents = myfile.readlines()
    myfile.seek(0)
    for eachline in contents:
        thisline = eachline.strip("\n")
        data = thisline.split(" ")
        if data[0] != username:
            myfile.write(eachline)
    myfile.truncate()
    myfile.close()


def setPassword(username, newPassword):
    data = []
    myfile = open("PasswordDatabase", "r+")
    contents = myfile.readlines()
    myfile.seek(0)
    for eachline in contents:
        thisline = eachline.strip("\n")
        data = thisline.split(" ")
        if data[0] == username:
            removeUser(username)
            addUser(username, newPassword)





# This function "center(win)" is a modified version of the function found at:
# http://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_reqwidth()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_reqheight()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width , height , x, y))
    win.deiconify()

def centerDoNotUse(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_reqwidth()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_reqheight()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width-20 , height-100 , x, y))
    win.deiconify()
