from Database import *
from datetime import datetime

class EventManager:
    def __init__(self):
        
        self.schedules = Schedules("schedules.txt")
        
        datesDict = self.schedules.getDict()
        
        namesList = self.schedules.getAllStudents()
    
        def addEvent(name, date):
            #date as string in format 'April 17 2016 10:00PM'
            event = datetime.strptime(date, '%B %d %Y %I:%M%p')
            with open("schedules.txt") as dataFile:
                schedules = json.load(dataFile)
                schedules[name].append(event)
            with open("schedules.txt", "w") as newFile:
                json.dump(schedules, newFile)
                        
        def removeEvent(name, date):
            evemt = datetime.strptime(date, '%B %d %Y %I:%M%p')
            with open("schedules.txt") as dataFile:
                schedules = json.load(dataFile)
                for i in schedules:
                    if i == name:
                        for j in name:
                            if j == event:
                                schedules[name].remove(j)
            with open("schedules.txt", "w") as newFile:
                json.dump(schedules, newFile)

main = Main()
