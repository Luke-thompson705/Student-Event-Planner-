class Database:
    def __init__(self, fileName):
        self.filename = fileName

#Reads the text file
    def readFile(self):
        studentFile = open(self.filename, "r")
        studentFileList = []
        for line in studentFile:
            currentline = line.split(",")
            studentFileList.append(currentline)
        studentFile.close()
        return studentFileList 

#Adds a student to the text file on a new line
    def addStudent(self, name, busyTimes, boundary):
        studentFile = open(self.filename, "a")
        studentFile.write(name + "," + busyTimes + "," + boundary + '\n')
        studentFile.close

#Finds a student by name and returns it
    def findStudentByName(self, name):
        studentFile = self.readFile()
        for students in studentFile[0]:
            if students == name:
                print("Found");
                return students
        else:
            print("Not found")

