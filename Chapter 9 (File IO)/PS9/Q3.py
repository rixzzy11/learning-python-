"""write a program to store tables from 1 to 20 in text files 
each for a table stored in folder called tables"""

def tables(n):
    table = ""
    for i in range(1 ,11):
        table += f"{i} X {n} = {i*n}\n"

    return table    
    

for i in range(1 , 21):
    with open(f"Chapter 9 (File IO)/PS9/Tables/table of {i}.txt" , "w") as file:
        file.write(tables(i))
