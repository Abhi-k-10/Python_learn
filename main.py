import os
import random
import pygame
from random import randint


computer = randint(0 , 100)

def playRandomSound(): #ab ispe kaam karna ha 
    pass
    
def matchTheNumber():

    guesses = 1
    initial_score = 100

    
    def scoreCalculator(score):
        score -= 10 
        print(f"Score : {score}")


            
        if (initial_score == 0):
            print("Game End, Please restart")

        return score



    while True :



        user = input("Enter the number between 0 to 100 :")

        initial_score = scoreCalculator(initial_score)

        if initial_score == 0:
            break

        try:
            value = int(user)
            user = int(user)

            if (computer == user ):
                print(f"Comp : GG's , You win!! That is correct guess {computer}! in Guesses {guesses}")
                print(f"Final Score Remaining :{initial_score}")
                break
            
            
            elif (computer > user):
                print(f"Comp : Your Number is too low then mine , Guess again !!")
                guesses += 1

            
            elif (computer < user ):
                print(f"Comp : Your Number is too high then mine , Guess again !!")
                guesses += 1
        
        except ValueError:
            print(f'"{user}" is Not an integer !!')
            guesses +=1
    
matchTheNumber()



choice = input("Enter 'R' to restart or Enter 'Q' to Exit : " )

def restart():



        if( choice == "R" or choice =="r" ):
            print("Restarting")
            matchTheNumber()
            

        elif (choice == "Q" or choice == "q"):
            print("Thank You for Playing , Exiting")

        else :
            print("Invalid input ")

while True :
    if ( choice == "r" or choice == "R"):
        computer = randint(0 , 100)
        restart()
        matchTheNumber()
    else :
        break   
