#break used to EXIT from a loop
print("Using break :")
for i in range(11):
    print(i)
    if(i == 7):
        break
print("\n")


#continue is used to skip an iteration
print("Using continue :")
for i in range (11):
    if (i == 7):
        continue     #skips '7' and '9'
    if (i == 9):
        continue
    print(i)


#pass is a special keyword in python which 
# lets your code still working even if its incomplete
for i in range(10):
    pass