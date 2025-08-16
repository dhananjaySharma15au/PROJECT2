import random
randomNum = random.randrange(-1,101)
print(randomNum,"\n")
guess = counter = 0
while(guess != -1):
 guess = input("Guess thr number : ")
 if not guess.isdigit():
         print("invalid input\n\nNOTE :- not be considered as a guess\n")
         print("please enter a number\n")
         continue

 if int(guess) <= -1 or int(guess) >= 101:
         print("invalid input\n\nNOTE :- not be considered as a guess\n\nTIP :- try to enter numbers only ranging from 0 to 100\n")
         continue
   
 if int(guess) == randomNum:
         print("you got it right in your try number : ",str(counter))
         break
 elif int(guess) < randomNum:
         counter += 1
         print("you got it less then the correct number\n")
         print("try again\n")
 else :
         counter += 1
         print("you got it more then the correct number\n")
         print("try again\n")
