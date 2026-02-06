# Functions are block of code that contains statements
# Functions are used to perform a particular task withour repeating the code

#declaration
def function():
    print("Hello from function.")

function() #function call

# passing argument in function
def avg_calculate (num1 : int , num2 : int , num3 : int):    # num1 , num2 , num3 are parameters
    return (num1 + num2 + num3) / 3          #return value

print(avg_calculate(2 , 2 , 2)) # 2 , 2 , 2 is argument passed

# Passing string
def greetings(name):
    print (f"Hello {name}! How are you ?")

greetings("Jennie")


#default argument
def user(name , phone = "Not available"):
    print ("Name : ", name)
    print ("Phone number : ", phone)

user("Siddhart" , 8585748588)
user("Abjijit")

