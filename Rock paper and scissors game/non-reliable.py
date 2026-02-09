def main():
    import random        #to chose from random value
    choices = ['r' , 'p' , 's']
    computer_input = random.choice(choices)   #assigning rock , paper or scissor randomly to computer
    # co_input = computer_input

    user_input = input("Enter 'r' for rock , 'p' for paper and 's' for scissors : ")  #taking input from user

    #To print what choices compute and the user made

    if(computer_input == 'r' and user_input == 'p'):
        print("Computer chose Rock and You Paper")

    elif(computer_input == 'r' and user_input == 's'):
        print("Computer chose Rock and You Scissors")

    elif(computer_input == 'p' and user_input == 'r'):
        print("Computer chose Paper and You Rock")                            

    elif(computer_input == 'p' and user_input == 's'):
        print("Computer chose Paper and You Scissors")

    elif(computer_input == 's' and user_input == 'r'):
        print("Computer chose Scissors and You Rock")

    elif(computer_input == 's' and user_input == 'p'):
        print("Computer chose Scissors and You Paper")

    elif(computer_input == user_input == 's'):
        print("You both chose Scissors")

    elif(computer_input == user_input == 'p'):
        print("You both chose Paper")
        
    elif(computer_input == user_input == 'r'):
        print("You both chose Rock")
        
    else:
        ("Enter 'r' , 'p' or 's' only as input.")

    #Logic behind which choice win and which lose

    if(computer_input == user_input):
        print("That's Draw.")
        
    else:
        if(computer_input == 'r' and user_input == 'p'):
            print("You Win!")

        elif(computer_input == 'r' and user_input == 's'):
            print("You Lose!")

        elif(computer_input == 'p' and user_input == 'r'):
            print("You Lose!")

        elif(computer_input == 'p' and user_input == 's'):
            print("You Win!")

        elif(computer_input == 's' and user_input == 'r'):
            print("You Win!")

        elif(computer_input == 's' and user_input == 'p'):
            print("You Lose!")


    user_input = input("Want to play again?(y/n)")
    if (user_input == 'y'):
        main()
    else :
        print("Thanks for playing.")
main() # to initiate the actual code

    