# #to print table of given number using for loop
# num = int(input("Enter a number to print table of : "))
# for i in range(1 , 11):
#     print(num * i)


# #greeting persons stored in a list which names starts with letter S
# name = ['Rizz' , 'Salim' , 'Aftab' , 'Rahul' , 'Sameer' , 'Sohel']

# for item in name :
#     if item.startswith('S'):
#         print(item)


# #to find if the given number is primr or not using while loop
# num2 = int(input("Enter your number ot check if it is a prime number or not : "))
# i = 2
# k = 1

# while (i != num2 - 1):
#     if(num2 % i == 0):
#         k = 0
#     i += 1


# if(k == 0):
#     print(f"Given number {num2} is not a prime number.")

# else:
#      print(f"Given number {num2} is a prime number.")


# # to print asterisk patter for n = 3
# """         *
#             * * *
#             * * * * *          """
# n = 3
# t = 1
# for i in range(n):
    
#     for j in range(t):
#         print('*' , end='')
       
#     t += 2
#     print()


# # to print following pattern for n = 3
# '''             * * *
#                 *   * 
#                 * * *                  '''

# #method 1
# for i in range(n):
    
#     print("* " ,end='')
# print()

# for i in range(n - 2):
#     print("* " ,end='')

#     for j in range (n-2):
#         print("  ", end='')
    
#     print("* " ,end='')
#     print()


# for i in range(n):
    
#     print("* " ,end='')


# #method 2 (easier)
# for i in range(0 , n):
#     if (i == 0 or i == n-1):
#         print("* " * n, end='')
#     else:
#         print("* " , end='')
#         print("  " * (n-2) , end='')
#         print("* " , end='')
#     print()
