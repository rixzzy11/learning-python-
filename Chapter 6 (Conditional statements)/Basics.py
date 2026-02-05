# like every coding language if else and else if are used for conditional statements 

#else if ladder

age = int(input("Enter your age : "))

if(age < 0) :
    print("Age can't be Negative !")

elif(age == 0) :
    print("Age can't be zero !")

elif (age < 11) :
    print("You are still considered as a kid.")

elif(age < 18) :
    print("You are a Teen.")

elif(age >= 18 and age <= 59) :
    print("You are an Adult.")

elif(age >= 60 and age <= 99) :
    print("You are an Old person.")

elif(age >= 100) :
    print("Age cannot be this much.")
