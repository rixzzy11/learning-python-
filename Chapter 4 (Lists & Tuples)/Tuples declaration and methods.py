# Unlike Lists , Tuples are imutable and cannot be changed
# To change tuple we must save it to the another variable or tuple
# Tuples are declaared with () parenthesis and list are declared with [] brackets

Tuple = (1 , 2 , 4 , "item 1" , "Name" , False)
print(Tuple.count(2))     #prints the value at specific index in the tuple

# different operations to perform in tuples
Nums = (45 , 34 , 23 , 64 , 43 , 74 , 235 , 532 , 4 )

print(Nums.index(74))  #gives the index of value of an item

print("Min :",min(Nums))  #minimum value of the tuple

print("Max :",max(Nums))  #maximum value of the tuple

print("Sort :",sorted(Nums))  #sorts the tuple

print("Lenght :",len(Nums))   #gives length of the tuple

print("Sum :",sum(Nums)) #gives the sum of all values in the tuple
