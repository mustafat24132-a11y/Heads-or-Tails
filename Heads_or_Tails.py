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
        user_guess=str(input("Heads or Tails"))
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

first_name = input("What is your name? ").strip()

# Validate first_name length and characters
if 2 <= len(first_name) <= 10 and first_name.isalpha():
    break
else:
   print('Your name must be more than 2 characters and less than 10 and contain only letters.')
   print(first_name)
else:
 
    


try:
    age = int(input("What is your age? "))
    # COndition to check the user's age
    if 12 < age < 20:
        print(f"Age accepted: {age}")
    else:
        print('You must be older than 12 and younger than 20')
except ValueError:
    print("Please enter a valid number for age.")

 

heads_tails() #this returns the function