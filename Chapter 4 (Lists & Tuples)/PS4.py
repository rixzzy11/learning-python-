# take input from user to enter five fruits name
Fruits = []
f1 = input("Enter your favouirate fruit: ")
Fruits.append(f1)
f2 = input("Enter your favouirate fruit: ")
Fruits.append(f2)
f3 = input("Enter your favouirate fruit: ")
Fruits.append(f3)
f4 = input("Enter your favouirate fruit: ")
Fruits.append(f4)
f5 = input("Enter your favouirate fruit: ")
Fruits.append(f5)

print("Your favoirate Fruits are",Fruits)

# to take students marks as input and display them in sorted manner
Marks = []

m1 = input("Enter marks of the first student: ")
Marks.append(m1)
m2 = input("Enter marks of the second student: ")
Marks.append(m2)
m3 = input("Enter marks of the third student: ")
Marks.append(m3)
m4 = input("Enter marks of the fourth student: ")
Marks.append(m4)
m5 = input("Enter marks of the fifth student: ")
Marks.append(m5)
m6 = input("Enter marks of the sixth student: ")
Marks.append(m6)

print("Students marks in Ascending order :",sorted(Marks))

# count how many times zero repeated

Numtuple = (23 , 4 , 0 , 2, 22 , 0 , 3 , 0)
print(f"The Number '0' is repeated {Numtuple.count(0)} times")