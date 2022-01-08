# higher or lower numbers

# computer generates random number and you have to guess it by asking if it is higher or lower than another number and

import random

num = random.randint(1, 101)


while True: 
    
    guess = input("Guess a number between 1 and 100: ii")
    
    if int(guess) == num: 
        print("you win!")
        break
        
    elif int(guess) < num: 
        print("Too low!")
    else: 
        print("Too high!")