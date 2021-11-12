ExpelledStudentList = []                                            #Expelled Student List

class Student: 
    def __init__(self, Name, Age, Debt):                    #Student Class
        self.Name = Name
        self.Age = Age
        self.Debt = Debt

    def DuePayment(self, Debt , CostAmount):         #This method calculates new debt
        self.CostAmount = CostAmount
        self.Debt = Debt
        self.Debt += CostAmount
        

    def ExpelStudent(self):                                         #This method puts the student on expelled list if debt is over 10000
        global ExpelledStudentList

        if self.Debt >= 10000:
            ExpelledStudentList.append(self)

Thomas = Student("Thomas", 19, 1000)                #This creates a new Object

print(Thomas.Name, Thomas.Age, Thomas.Debt)
    
Thomas.DuePayment(Thomas.Debt, 10000)          #This adds debt to the Object

print(Thomas.Name, Thomas.Age, Thomas.Debt)
      
Thomas.ExpelStudent()                                            #This calls the ExpelStudent method for the Thomas object

for i in ExpelledStudentList:
    print(i.Name + " Got Expelled")

