# we can store different data types in one list 

List = ["item 1", "item 2" , "item 3" , 1 , 2 , 3.14, True]
NumList = [2 , 4 , 5 , 1 , 7 , 0 , 3 , 6 , 8 , 9]

#We can also store list inside of list
List_in_List = [["Rizwan" , 9.5] , ["Salim" , 5.6] , ["Aftab , 4.6"] , ["Abbas", "failed"]]
print(List_in_List)

print(List[3])
print(List[0:6]) 

# list is mutable means it can be changed unlike the string

List[0] = "First item"
print(List[0])

# Functions to perform various actions on a list

NumList.sort()     #sorts the list
print(NumList)     

NumList.reverse()  #reverse the list
print(NumList)

List.insert(1,"Second item")   #add another item in the list
print(List)

List.pop(5)    #removes the last item from the list
print(List)

List.append("New value")  #adds item at the last index of the list
print(List)
