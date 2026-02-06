# finding the greates of three in numbers in a function
def greatest(num1 : int , num2 : int , num3 : int):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    else :
        return num3
    
print(f"The greatest number is {greatest(3 , 5 , 1)}")

# converting tempreture from celsius to fahrenheit
def cel_to_farh (celsius):
    return 9/5 * celsius + 32

print(f"Temp is Fahrenheit is {cel_to_farh(36)}")


# Writing a recursive function to sum first n natural numbers
def sum_of_naturalnum(n : int):
    if(n == 0):
        return 0
    
    n += sum_of_naturalnum(n-1)
    return n

print(sum_of_naturalnum(10))


"""using recursive function printing the following patter
         * * * 
         * *        for n = 3
         *                               """

def pattern(n = 3):
    
    if(n == 0):
        return 0
    
    print('* ' * n )

    return pattern(n-1)
    

pattern()


# recursive function to print table of given number

def table(n = 8 , i = 1):

    if(i > 10):
        return 0
    
    print(n * i)
    
    table(n , i + 1)


table()

# writing a function to remove a given word from the list and strip it at the same time

def rem(li : list, word):
    n = []
    for item in li:
        if not (item == word):
            n.append(item.strip(word))

    return n

names = ["Salim" , "Aftab" , "Abbas" , "Rizwan" , "as"]
print(rem(names , "as"))