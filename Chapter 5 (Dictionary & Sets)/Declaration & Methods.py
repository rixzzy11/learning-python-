#dictionary is combination of key and values
#key must be imutable like number, string or tuple 
#value of key could be anything number, string, list, etc.

Dictionary = {
    1 : "Interstellar" ,
    2 : "Insception" ,     #declaring keys and their values
    3 : "Oppenheimer" ,
    4 : "Tenet"
}
print(Dictionary.items(),"\n") #prints both keys and values in the dictionary
print(Dictionary,"\n")
print(Dictionary[2],"\n") #prints specific value from the dictionary

print(f"Values inside the Dictionary:\n{Dictionary.values()}\n") #prints specifically the values
print(f"Keys inside the Dictionary:\n{Dictionary.keys()}\n")    #prints sepcifcally the keys

#add and remove items inisde the Dictionary
Dictionary.update({5 : "La La Land"})     #adds value in the dictionary
print(f"After updating: \n{Dictionary}\n")
Dictionary.pop(5)                          #removes the sepcific value from the dictionary
print(f"After removing :\n{Dictionary}\n")

#pop last item in the Dictionary
Dictionary.popitem()
