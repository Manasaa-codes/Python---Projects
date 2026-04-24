import random
print ("Welcome to the number guessing game\n Try your level best to find the number ")
print("\n1. Easy (1-50)")
print("\n2. Medium (1-100)")
print("\n3. Hard (1-200)")
a = int(input("\n Please select any one of the above levels : "))
print("\n Great!! The level you've chosen is", a)
if (a == 1):
    max_range = 50
elif(a==2):
    max_range = 100
elif(a==3):
    max_range = 200
else:
    print("Invalid level selected")
    exit()
number = random.randint(1, max_range)
attempt = 0
while True :
    attempt += 1
    user_guess = int(input(f"\n Enter a number within {max_range} : "))
    if(user_guess > max_range):
       print(f"Number is greater than {max_range}. Try Again")
       continue
    elif(user_guess <= 0):
        print("The number is either negative or 0 which is not considerable. Try with a different number")
        continue
    elif (number == user_guess) :
          print ("That's so accurate, You won by guessing exact number")
          print ("You've guessed in", attempt, "attempts")
          break
    elif(number > user_guess):
        print ("The target number is greater than your guess")
    else :
        print ("The target number is less than your guess")
    if attempt > 5:
        print("Game over! The number was", number)
        break