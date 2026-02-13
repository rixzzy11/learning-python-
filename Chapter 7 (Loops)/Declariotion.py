# loops  make code more resuable and saves time and resources

#there are two types of loop in python 
# 1 for loop 

for i in range(1 , 11 , 1):
    print(i)

print("\nTable of 3 : ")
for i in range(3 , 31 , 3):
    print(i)

cars = ['BMW' , "Mercedes" , "Volswagen" , "Audi" , "Volvo" , "Lexus" , "Range Rover"]
index = 0
print("Items in the List :")
for index in range(0 , len(cars)):
    print(cars[index])


#second type of loop in the python is the while loop
a = 1
while (a < 11):
    print(a)
    a+=1
