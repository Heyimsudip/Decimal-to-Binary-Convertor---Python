from decimalToBinary import DecimalToBinary
from byteadder import binaryAdder
import Greeting
#Greeting at start

Greeting.GreetingAtBeginning()

Continue="yes"
while Continue=="yes":
    sucess=False
    while sucess==False:
        #try catch block
        try:
            First_number=int(input("Enter the First Decimal number: "))
            if (First_number>255):
                print("Invalid input!!! ")
                print("Please Re-enter the number between 0 to 255")
                print("\n")
            elif(First_number<0):
                print("Invalid input!!! ")
                print("Please Re-enter the number between 0 to 255")
                print("\n")
            else:
                sucess=True
        except:
            print("Please enter valid number!!!!")
    
    sucess=False
    while sucess==False:
        #try catch block
        try:
            Second_number=int(input("Enter the Second Decimal number: "))
            if (Second_number>255):
                print("Invalid input!!! ")
                print("Please Re-enter the number between 0 to 255")
                print("\n")
            elif(Second_number<0):
                print("Invalid input!!! ")
                print("Please Re-enter the number between 0 to 255")
                print("\n")
            else:
                sucess=True
        except:
            print("Please enter valid number!!!!")

    #Decimal to binary conversion
    print("The binary value of {} is: {}\n".format(First_number,DecimalToBinary(First_number)))
    print("The binary value of {} is: {}\n".format(Second_number,DecimalToBinary(Second_number)))
    a=DecimalToBinary(First_number)
    b=DecimalToBinary(Second_number)
    #bitadder addint two binary number
    summ=binaryAdder(str(a),str(b))
    print("The sum of {} and {} is :{}\n".format(First_number,Second_number,summ))
    Continue = input("Do you wish to continue? (yes/no): ").lower()
    print("\n")
    
   #Shown if the program is going to exit

#Greeting at end
Greeting.GreetingAtEnd()
    

        

    
 

    
                
