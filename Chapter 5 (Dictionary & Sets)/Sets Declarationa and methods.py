#set is collection of unique values 
#set is mutable which means we can add and remove value from it

#declaring empty set
empty_set = set()
print(type(empty_set))

#declaration of set
Set = {2, 4, 6, 8, 10, 10, 2, "naman"}
print(Set)

#methods using set

Set.add(69) #add value in the set

Set.remove(69) #deletes selected value

Set.pop() #removes random value or from a selected range

Set.update([66, 55, 44]) #adds multiples values to the set

Set.clear() #deletes all of the values from the set
