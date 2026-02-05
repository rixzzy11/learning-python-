#Basic of strings
#single line string declaration
string = "something"
string1 = 'something'

#multiline string declaration
multi_line_string = '''this is line 1
this is line 2
this is line 3 
this is line 4 '''
print(multi_line_string)

#negative indexing 
name = "Rizwan"

#   R   I    Z     W     A    N
#   0   1    2     3     4    5

print(name[0:6])
print(name[0:4])  #From zeroth index including till the range you set (exluding the range order)
print(name[0:3])
print(name[0:2])
print(name[0:1])
print(name[1:4])
print("\n")

#   R   I    Z    W     A    N
#  -6  -5   -4   -3    -2   -1    

print(name[-6:])
print(name[-6:-1])
print(name[-6:-2])
print(name[-6:-3])
print(name[-6:-4])
print(name[-6:-5])
print(name[-5:-2],"\n")

#Index slicing 
alphabets = "abcdefghijklmnopgrstuvwxyz"

print(alphabets[0:26:3]) #[starting range : ending range :skip char between]