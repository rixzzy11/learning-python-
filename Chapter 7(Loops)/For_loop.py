#range (start, end , skip)
for i in range (100): 
    print(i)

#to print items in the lists , tuples and sets
tpl = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0)
print("Items in tpl :")
for item in tpl :
    print (item)

#to print keys and values in the dictionaries
dictionary = { 1 : "one" , 2 : "two" , 3 : "three" , 4 : "four"}
print("Keys inside dict:")
for key in dictionary :
    print(key)

print("Values inside dict:")
for value in dictionary.values() :        #You must use .values() to actually get dictionary values 
        print(value)              #because Python dictionaries default to returning keys when iterated directly.
    

#using else with for loop 
names = ["Aftab" , "Salim" , "Rahul" , "Abbas"]
for item in names :
     print(item)

else: print("Printed name successfully!")

