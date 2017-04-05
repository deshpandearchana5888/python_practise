#Instance variable ans class variable

class Employee:
    pay_range = 1.05#class variable
    no_of_emps = 0
    def __init__(self,first,last,pay):
        self.fname = first#instance variable
        self.lname = last#instance variable
        self.sal= pay
        Employee.no_of_emps += 1

    def fullname(self):
        print (self.fname + self.lname)
    def amount_range(self):
        self.sal = int(self.sal * self.pay_range)





emp1 = Employee('archana','deshpande',22000)
emp2 = Employee('suruchi','deshpande',12000)

emp1.pay_range = 1.04

print Employee.pay_range
print emp1.pay_range
print emp2.pay_range
print Employee.no_of_emps
#print emp1.fullname()
#print emp2.fullname()
#print emp1.sal
emp1.amount_range()
print emp1.sal