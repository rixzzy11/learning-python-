#take user input then print hello followed by user input
name = input("What's is your name?\nEnter here : ")
print("Hello",name,"!!")

birthdate = input("When you were born?\nEnter birthdata here : ")
print(f"""\tThank you {name} ,                                          
Your birthday cake will be delivered on {birthdate}
Have a good day! """)                                 #entering f is important otherwise it wont print variables 


#detect extra spaces between words in a string and replace them with single space
string = "Christopher Nolan  is  the best  director   ever"

print("Double space is at Index",string.find("  "),"and triple space is at Index",string.find("   "))

cleanedString = string.replace("   "," ").replace("  "," ")

print("Before :",string)
print("After :",cleanedString)
