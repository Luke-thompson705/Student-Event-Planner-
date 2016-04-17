from Database import *
from datetime import datetime

class EventManager:
    def __init__(self):
        
        self.schedules = Schedules("schedules.txt")
        
        datesDict = self.schedules.getDict()
        
        namesList = self.schedules.getAllStudents()
    
        def addEvent(name, date):
            file = open('schedules.txt', 'w')
            #date as string in format 'April 17 2016 10:00PM'
            event = datetime.strptime(date, '%b %d %Y %I:%M%p')
            for i in file:
                if name == key:
                    value.add(event)
    
        def removeGarment(name, date):
            file = open('schedules.txt', 'w')
            event = datetime.strptime(date, '%b %d %Y %I:%M%p')
            for i in file:
                if name == key:
                    if value[i] = event:
                        value.remove(event) 

main = Main()
