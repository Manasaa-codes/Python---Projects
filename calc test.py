def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
while True:
    print ("Welcome to the Calculator Application")
    print ("Enter the two numbers to start the mathematical operations")
    number1 = int (input ("Enter the first number : "))
    number2=int(input ("Enter the second number : "))
    action = int(input("Enter any one of the below options to start the operation :\n 1.Add \n2.Subtract\n 3.Multiply \n 4.Divide \n5.Exit \n"))
    if(action ==1):
        print(add(number1,number2))
    elif(action == 2):
        print(subtract(number1,number2))
    elif(action ==3):
        print(multiply(number1,number2))
    elif (action ==4):
        if(number2 == 0):
            print("Cannot divide by 0")
        else : 
            print(divide(number1,number2))
    elif(action ==5):
        break
    else :
        print("Invalid option")
   


