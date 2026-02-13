# write a class programmer to save data of programmers working at microsoft 
# and using a static function to greet the user
class programmer:
    emp_id = 321
    emp_name = "Mohammad Hasnain"
    code_lang = "Java"
    emp_salary = 28000

    def __init__(self , empid , empname , codelang , empsalary):
        self.emp_id = empid
        self.emp_name = empname
        self.code_lang = codelang
        self.emp_salary = empsalary

    def getinfo(self):
        print(f"Employee Name : {self.emp_name}\nEmployee ID : {self.emp_id}\nCoding Language : {self.code_lang}\nEmployee Salary : {self.emp_salary}")

    @staticmethod
    def greet():
        print("Hello There!")

# e1 = programmer(332 , "Aaliya Pathan" , "Html . CSS . JS" , 12000)
# e1.getinfo()
# e1.greet()


#a program to calculate a numbers square , cube and square root inside a claass
import math
class calculator:
    num = 1

    def __init__(self , num):
        self.num = num

    def calculate(self):
        print(f"Square root of {self.num} is {self.num ** 2} , Cube is {self.num ** 3} and Square root is {math.sqrt(self.num)}")
        

num1 = calculator(5)
num1.calculate()