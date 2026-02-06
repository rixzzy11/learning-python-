# recursion when a function call itself 
# recursion works as a loop we can set a condition when to end a function recalling

def fact(n : int):
    if(n == 1 or n==0):  # base case 
        return 1             
    
    return n * fact((n-1))  # recursive statement (function calling iteself)
     
print(fact(5))