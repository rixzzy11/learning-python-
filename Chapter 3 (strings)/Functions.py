string = "Rizwan Alim Pathan"
string2 = "***rizwan****"
print(len(string)) #TO to get length of the string

print(string.split()) #splits all the words of the string into an indivial words

print(string2.strip("a")) #Removes a specific character from start and end of the string the string 

print(string.upper(),string.lower()) #converts string into uppercase and lowercase 

print(string.replace('Rizwan','Salim')) #Exchanges two words with eachother

print(string.count('a'),string.count('Rizwan')) #Counts specific characters and words in a string

print(string.startswith('Rizwan')) #states true or false whether if a string starts with a particular word

print(sorted(string)) #individualises the letters in the string

#still there are many string function that we can use according to our need