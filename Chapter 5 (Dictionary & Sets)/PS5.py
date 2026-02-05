# Create a dictionary with Hindi words as keys and their English translation as values

Hindi_to_English = {
    "Achha" : "Good" ,
    "Behtar" : "Better" ,
    "Badlaw" : "Change" ,
    "Vyast" : "Busy" ,
    "Alag" : "Different" ,
    "Jeet" : "Win" ,
    "Sabar" : "Patience"
}

word = input("Enter a word to Translate : ")
print(Hindi_to_English[word])


# Taking input of 8 numbers and printing only the unique values among them 

Set = set()
num = input("Input the number : ")
Set.add(int(num))
num = input("Input the number : ")
Set.add(int(num))
num = input("Input the number : ")
Set.add(int(num))
num = input("Input the number : ")
Set.add(int(num))
num = input("Input the number : ")
Set.add(int(num))
num = input("Input the number : ")
Set.add(int(num))
num = input("Input the number : ")
Set.add(int(num))
num = input("Input the number : ")
Set.add(int(num))
print(Set)


#can we have 18 as a int and 18 as a string in a set
Set2 = set()
Set2.add(18)
Set2.add("18")
print(Set2)      #output : {18, '18'} so the answer is yes


# take 4 friends name as keys as input and their faavourite coidnig languages as values in a dictionary

Favourite_Coding = {}
name = input("Enter Name : ")
lang = input("Enter coding lang : ")
Favourite_Coding.update({name : lang})
name = input("Enter Name : ")
lang = input("Enter coding lang : ")
Favourite_Coding.update({name : lang})
name = input("Enter Name : ")
lang = input("Enter coding lang : ")
Favourite_Coding.update({name : lang})
name = input("Enter Name : ")
lang = input("Enter coding lang : ")
Favourite_Coding.update({name : lang})
print(Favourite_Coding)