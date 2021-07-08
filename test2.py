class employee:
    def find_salary(self,name):
        print(name)
    def message(self):
        print("iam from employee class")
class department (employee):
    def findsalary(self,position,work_time,experience):
        print(10000*position*work_time*experience)
    def message(self):
        print("iam from department class")
a=employee()
a.find_salary("kavin")
a.message()
b=department()
b.findsalary(10,8,20)
b.message()

