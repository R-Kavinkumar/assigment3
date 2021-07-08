#EMPLOYEE AND MANAGER ARE MEMBERS IN THIS COMPANY
class Member:
    def __init__(self):
        self.name=None
        self.phone=None
        self.age=None
        self.add=None
        self.sal=None
    #METHOD FOR PRINT SALARY DETAILS WITH NAME OF THE MEMBER
    def printSalary(self):
        print("salary of MR/MRS.",self.name,"is :",self.sal)
        return
# CLASS FOR EMPLOYEE INHERIT THE MEMBER
class Employee(Member):
    def __init__(self):
        self.spcialization=None
#CLASS FOR MANAGER INHERIT THE MEMBER
class Manager(Member):
    def __init__(self):
        self.department=None

#DETAILS OF EMPLOYEE
emp=Employee()
emp.name="kavin"
emp.sal="10000"
emp.add="""
91/90c kavin kumar R,
kk.nagar,rayapuram,
chennai.
chennai-600028
"""
emp.age=28
emp.phone=939392929
emp.spcialization="dynamic full stack developer"
emp.printSalary()


#DETAILS OF MANAGER
mang=Manager()
mang.name="kumar"
mang.sal="1000000000"
mang.add="""
21/20c kumar R,
kk.nagar,rayapuram,
chennai.
chennai-600028
"""
mang.age=35
mang.phone=1234567890
mang.spcialization="biussnes maths and CA"
mang.printSalary()

