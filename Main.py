from Database import *

class Main:
    def __init__(self):
        
        self.database = Database("Database.txt")
        
        datesDict = self.database.getDict()
        
        namesList = self.database.getAllStudents()
        
        year = int(input("Please enter the year: "))
        month = int(input("Please enter the month: "))
        day = int(input("Please enter the day: "))
        start = int(input("Please enter the start time: "))
        end = int(input("Please enter the end time: "))
        tag = input("Tag this meeting: ")

        meetingDate = (datetime(year, month, day, start, 0), datetime(year, month, day, end, 0), tag)

        #Creates a list of all bad times to meet on the desired date.
        badTimes = set()
        for name, schedule in datesDict.items():
            for _name in namesList:
                if _name == name:
                    for hour in schedule:
                        if int(hour[-8:]) == meetingDate:
                            badTimes.add(int(hour[:2]))

        #Finds an availble time not on the badTimes list.
        goodTimes = set(range(24)) - badTimes

        print("The hours avaiable to meet are: ")
        print(", ".join("{:02d}".format(hour) for hour in sorted(goodTimes)))

             
main = Main()
