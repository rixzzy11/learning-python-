#to find the greatest number among 4 numbers entered by the user

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4 = int(input("Enter number 4 : "))

if(num1 > num2 and num1 > num3 and num1 > num4) :
    print(f"Number 1 \"{num1}\" is greatest number") 

elif(num2 > num1 and num2 > num3 and num2 > num4) :
      print(f"Number 2 \"{num2}\" is greatest number") 

elif(num3 > num1 and num3 > num2 and num3 > num4) :
      print(f"Number 3 \"{num3}\" is greatest number") 

elif(num4 > num1 and num4 > num3 and num4 > num2) :
      print(f"Number 4 \"{num4}\" is greatest number") 

else :
    print("Error !")


#to check if the student passed or failed in the exam

chem = int(input("Enter marks of chemistry : "))
phy = int(input("Enter marks of Physics : "))
bio = int(input("Enter marks of Biology : "))

if(chem <= 33) :
     print("You failed in Chemistry exam.")
else : print("You passed the Chemistry exam.")

if(phy <= 33) :
     print("You failed in Physics exam.")
else : print("You passed the Physics exam.")

if(bio < 40) :
     print("You failed in Biology exam")
else : print("You passed the biology exam.")


#to detect a spam message 

s1 = "click this"
s2 = "make money"
s3 = "free iphone"
s4 = "you won lottery"
s5 = "join telegram"
s6 = "click this link"

message = input("Enter your message : ")

if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message) or (s5 in message) or (s6 in message)) :
    print("Spam Alert !!")

else :
    print(message)


#to check whether the username is less than 10 characters

username = input("Enter an Username : ")
number_of_charcters = len(username)

if(number_of_charcters > 10):
    print("Username too long ! (enter username less than 10 characters)")
else :
    print(f"Username : {username}")


#to check whther if your name is present in the list or not 

name = input("Enter your name : ")
li = ["Rahul" , "Aftab" , "Salim" , "Abbas" , "Asif"]

if(name in li):
    print(f"your name {name} is present in the list.")

else:
    print(f"Your name {name} is not present in the list.")

