# methods are function inside a class used to perform a specific task
class student:
    std_name = "Bruce Wayne"
    clas_s = 12
    roll_no = 110
    div = "B"

    # method 
    def get_info(self):  # methods requires a parameter
        print(f"Hello Mr. {self.std_name}. Your Roll No is {self.roll_no} and you belongs to Division {student.div}")

    # declaring method that doesnt require argument declared through @staticmethod
    @staticmethod 
    def print_hello():
        print("Hello !")

Batman = student()
student.get_info(Batman) #passing object as argument

spiderman = student()
spiderman.std_name = "Peter Parker" 
spiderman.div = 'A'
spiderman.roll_no = "111"
spiderman.get_info() # equivalent to student.get_info(spiderman) aoutomatically passes the arguement

student.print_hello()
spiderman.print_hello()
#both gives the same output "Hello !"

