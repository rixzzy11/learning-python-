# object oreinted programming resolve around classes and object 
# class is like a blueprint and and object is copy of those blueprint
# imagine class as an empty form and object are data we insert in it 

class employee:      
    Id = "00"              
    name = "Rahul Kamble"   #Id , name , age and field are all objects
    age = 20                # togetherly it make a class
    field = "Finance"       # class contains class attributes

Salim = employee()
Salim.id = "01"
Salim.name = "Salim Majid Momin"    #instance attributes
Salim.age = 17
Salim.field = "E-Sports"
print(f"Emp Id: {Salim.Id}\nEmp Name: {Salim.name}\nEmp age: {Salim.age}\nField: {Salim.field}")