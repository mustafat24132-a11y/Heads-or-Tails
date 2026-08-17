'''
name: Mustafa Taha
date: 11/08/25
Version: 1.0
'''
#---------Libraries-------------------------------------
import random
#---------Functions-------------------------------------
def heads_tails():
    user_score=0
    computer_score=0
    options=["Heads","Tails"]
    while user_score!=2 and computer_score!=2:
        choice=random.randint(0,1)
        computer_guess=options[choice]
        user_guess=str(input("Heads or Tails")).strip().lower()
        if user_guess == computer_guess:
            print(f"It was {computer_guess}, you guessed {user_guess}, you won that round")
            user_score +=1
        else:
            print("It was {}, you guessed {}, you lost that round".format(computer_guess,user_guess))
            computer_score +=1
    #the loops has now ended and it will output won the best of 3 rounds
    if user_score==2:
        print("{}, you won that game".format(first_name))
    else:
        print("{}, you lost that game".format(first_name))

#---------------------main program-----------------------------
print("Hi! Welcome to my Heads or Tails game")

while True:
    first_name = input("What is your name? ").strip()
     # keeps the name lenght from 2-10 no more no less
    if 2 <= len(first_name) <= 10 and first_name.isalpha():
        print(f"welcome {first_name}")
        break
    else:
        print("Your name must be between 2 and 10 characters and contain only letters.")
   
   
 
while True:
    try:
        age = int(input("What is your age?  "))
        # Condition to check the user's age
        if 12 < age < 20:
            print(f"Age accepted: {age}")
            break  # Exits the loop when age is valid
        # boundary if the user enters a blank statement
        elif age == "": 
            print('You must enter an age to continue playing')
            continue
        # prevents the user from entering a word as their age and then asks them for a number
        if age_input.isalpha():
            print('You must only enter numbers and not words for this question')
            continue
        if age_input.isdigit():
            print('No symbols should be in side the age')
        else:
            print('You must be older than 12 and younger than 20')
    except:
        print("Please enter a valid number for age.")

 

heads_tails() #this returns the function