import random 



iteration = 0
flag = True
generateFlag = True

while(flag):
    if(generateFlag):
        guess_number = random.randint(1,100)
        generateFlag = False

    try:
     user_guess = int(input("guess your number = "))
    except ValueError:
       print("please select the number only ")
       continue
    iteration  = iteration  + 1  
    if(user_guess>0 and user_guess<=100):
        if(user_guess == guess_number):
            print(f" Machine Guess, {guess_number}, and your guess {user_guess} matching")
            print("Your Guess is Right")
             
            
            print("Do you want to play once again if yes select [Y] or [N]")
            play_again = str(input())
            if(play_again == 'Y'):
               print(f"Total Iteration you took to guess this {iteration}")
               iteration = 0 
               generateFlag = True
               continue
            else:
               print(f"Total Iteration you took to guess this {iteration}")
               flag = False

        elif(user_guess>guess_number):
            print("Your guess is too high")
            
        elif(user_guess<guess_number):
            print("Your guess is too low")
        
       
    else:
       print("Please select Number b/w 1 to 100")







    



