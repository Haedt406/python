
class Employee:
    def __init__(self,name,empID,salary):
        self.name = name
        self.empID = empID
        self.salary = salary

    def getName(self):
        return self.name

    def getEmpID(self):
        return self.empID
    
    def getSalary(self):
        return self.salary
        

class Accountant(Employee):

    def __init__(self,name,empID,salary,cpaID):
        Employee.__init__(self,name,empID,salary)
        self.cpaID = cpaID


    def getCpaID(self):
        return self.cpaID

class Developer(Employee):
    
    def __init__(self,name,empID,salary,language):
        Employee.__init__(self,name,empID,salary)
        self.language = language

    def getLanguage(self):
        return self.language

class Salesperson(Employee):
    def __init__(self,comission):
        self.commission = commission
    def getComission(self):
        return self.commission

class DeveloperIntern(Developer):
    def __init__(self,name,empID,salary,language,college):
        Developer.__init__(self,name,empID,salary,language)
        self.College = college
        
    def getCollege(self):
        return self.College

    
emp1 = Accountant("Kevin ", "123", 400000, "234ljd")
emp2 = Developer("pax ", "4984", 95995959, "python")
emp3 = DeveloperIntern("why", "4343", 9, "pythonagain", "msu")

print(emp2)
print(emp2.getSalary())
print(emp1.getName())
print(emp3.getCollege())
