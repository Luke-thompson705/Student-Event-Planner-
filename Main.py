from Database import *

class Main:
    def __init__(self):
        
        self.database = Database("Database.txt")
        
        datesDict = self.database.getDict()
        
        namesList = self.database.getAllStudents()
        

        meetingDate = int(input("Please enter the date you would like to meet in the format yyyymmdd: "))

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

             
mian=Main()
