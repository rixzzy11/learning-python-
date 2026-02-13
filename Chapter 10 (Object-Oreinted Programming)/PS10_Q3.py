"""write a program to create a class train which has methods to book ticket
to check seat number and availibility and and get fare information """
class train_ticket:
    name = "Fazlur Rahman Sayyed"
    phone = 9383038322
    password = "fazlu1234"
    gender = "M"
    departing = "Pune"
    destination = "Mumbai"
    no_of_seat = 1

    def __init__(self , name , phone , password , gender , departing , destination , noofseat):
        self.name = name
        self.phone = phone 
        self.password = password
        self.gender = gender
        self.departing = departing
        self.destinatin = destination
        self.no_of_seat = noofseat

    def get_Status(self , phone , password ):
        ticket = 0
        if(ticket > 10):
            print("Booking unsuccessful. Seats not available.")
        else:
            print(f"Booking successful.\nSeat No: S{ticket}.\n")
        ticket += self.no_of_seat
        
    def get_fare(nega , phone , password ):
        print("Fare Details")
        print(f"{nega.name} , {nega.phone}")
        print(f"Fare : 110 rs. (incl. of all taxes)\nNO. of seat(S): {nega.no_of_seat}\nTotal fare: {110 * nega.no_of_seat}.")
        print("Thanks for Travelling from Indian Railways . Have a nice and safe journey.\n\n")


#creating object
p1 = train_ticket("Naushad Khan" , 5364342343 , "nochad3232" , 'M' , "Mumbai" , "Pune" , 2)
p1.get_Status(5364342343 , "nochad3232" )
p1.get_fare(5364342343 , "nochad3232")

p12 = train_ticket("Naushkghad Khjgkan" , 898698759 , "hkf7rkmu6" , 'U' , "Mumbai" , "Pune" , 5)
p12.get_Status(898698759 , "hkf7rkmu6" )
p12.get_fare(898698759 , "hkf7rkmu6")
