import random
randomNum = random.randrange(-1,101)
print(randomNum)
guess = counter = 0
while(guess != -1):
 guess = input("Guess thr number :")
 if int(guess) == randomNum:
         print("you got it right in your try number : "+ str(counter))
         break
 elif int(guess) < randomNum:
         counter += 1
         print("you got it less then the correct number")
         print("try again")
 else :
         counter += 1
         print("you got it more then the correct number")
         print("try again")
