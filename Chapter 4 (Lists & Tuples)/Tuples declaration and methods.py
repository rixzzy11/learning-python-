# Unlike Lists , Tuples are imutable and cannot be changed
# To change tuple we must save it to the another variable or tuple
# Tuples are declaared with () parenthesis and list are declared with [] brackets
Tuple = (1 , 2 , 4 , "item 1" , "Name" , False)
print(Tuple.count(2))

# different operations to perform in tuples
Nums = (45 , 34 , 23 , 64 , 43 , 74 , 235 , 532 , 4 )

print(Nums.index(74))
print("Min :",min(Nums))
print("Max :",max(Nums))
print("Sort :",sorted(Nums))
print("Lenght :",len(Nums))
print("Sum :",sum(Nums))
