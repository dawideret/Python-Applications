
class Student:
    def __init__(self, StudentName, StudentAge):
        self.StudentName = StudentName
        self.StudentAge = StudentAge
        self.StudentNumber = "N" + str((len(StudentList) + 1) * 13)
       
StudentList = [] 
StudentList.append(Student("John", 18))
StudentList.append(Student("Carl", 21)) 

def AddStudent(): 
    StudentList.append(Student(str(input("Enter Student Name: ")), str(input("Enter Student Age: ")))) 

while True: 
    print("Choose an option:") 
    print("1. Add a new student") 
    print("2. View the student list") 
    
    userinput = str(input(" >>> ")) 

    if userinput == "1": 
        AddStudent()
    elif userinput == "2": 
        for obj in StudentList: 
            print(str(obj.StudentName) + ", Age: " + str(obj.StudentAge) + " Student Number: " + str(obj.StudentNumber)) 
    else: 
        print("Please input '1' or '2' instead.")

