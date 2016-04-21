from Database import *
from datetime import datetime

class EventManager:
    def __init__(self):
        
        self.schedules = Schedules("schedules.txt")
        
        datesDict = self.schedules.getDict()
        
        namesList = self.schedules.getAllStudents()
    
                def addEvent(name, date, description):
            event = {date: description}
            with open("schedules.txt") as dataFile:
                schedules = json.load(dataFile)
                schedules[name].append(event)
            with open("schedules.txt", "w") as newFile:
                json.dump(schedules, newFile)
                        
        def removeEvent(date):
            with open("schedules.txt") as dataFile:
                schedules = json.load(dataFile)
                for i in schedules:
                    for j in schedules[i]:
                        if j == date:
                            schedules[i].remove(j)
            with open("schedules.txt", "w") as newFile:
                json.dump(schedules, newFile)


main = Main()
