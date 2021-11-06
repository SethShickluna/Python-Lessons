# rock_paper_sissors 
import random

def determine_winner(cpu, player): 
    # key-value: key wins against value 
    outcomes = {"rock":"sissors", "paper":"rock", "scissors":"paper"}

    
    if outcomes[cpu] == player: 
        print("You Lose!")
    elif outcomes[player] == cpu:
        print("You Win")
    else: 
        print("It's a tie!")


def rps(): 
    options = ['rock', 'paper', 'scissors']
    cpu_choice = options[random.randint(0, 2)]

    input_ = input("Please choose Rock, Paper, or Scissors: ")

    if input_.lower() in options: 
        print(cpu_choice)
        determine_winner(cpu_choice, input_)
    else: 
        print("Not a valid choice, please check spelling and try again")
        rps()


def play_game(): 
    playing = True

    while playing: 
        print("[n] play new game | [q] quit")
        input_ = input("~ ")

        if input_ == "n": 
            rps() 
        else: 
            playing = False


if __name__ == "__main__": 
    play_game() 




