import random


def play_game(text, *options):
    print(text)
    choice = input(f"Please make your choice {options}: ")

    return choice

def main(name):
    print(f"Welcome, {name}!")

    first_part = "\n\nYou are passing through an unknown village while travelling.\nA friendly villager invites you to stay in his home for the night. Would you like to stay?"
    choice = play_game(first_part, "yes", "no")

    if choice.lower() == "yes":
        second_part = "\n\nYou are awakened by a scratching noise at midnight. Would you like to get up and check what's the matter?"
        choice = play_game(second_part, "yes", "no")

        if choice.lower() == "yes":
            third_part = "\n\nIt's a thief! You can try to catch him or call the others, or you can go back to bed. What would you like to do?"
            choice = play_game(third_part, "catch him", "call others", "go back")

            if choice.lower() == "catch him":
                player_speed = random.randint(1, 6)
                thief_speed = random.randint(1, 6)
                print(f"\nYour speed is {player_speed} unit(s)\nThe thief's speed is {thief_speed} unit(s)")
                if player_speed > thief_speed:
                    print("\nCongratulations, you caught the thief!\nThe villagers are very grateful and give you a bag of gold!")
                else:
                    print("\nUnfortunately, the thief escaped.")
                    print("\n\nThe villagers didn't see the thief, so you are suspected of theft. You will be killed unless you can find the thief in two days' time.")
                    play = input("Press 'Enter' to start looking for the thief.")
                    if play == "":
                        player_level = random.randint(1, 6)
                        thief_level = random.randint(1, 6)
                        print(f"\nThe level of your detective skill is {player_level}\nThe level of the thief's ability to hide is {thief_level}")
                        if player_level > thief_level:
                            print("\nCongratulations, you found the thief!\nThe villagers are very grateful and give you a bag of gold!")
                        else:
                            print("\nUnfortunately, you weren't able to find the thief.\nYou are killed by the angry villagers.")
                    else:
                        pass
            elif choice.lower() == "call others":
                print("\nCongratulations, you caught the thief with other villagers!\nThey are very grateful and give you a bag of gold!")
            elif choice.lower() == "go back":
                print("\nThe villagers found out that something was stolen, they thought that you were the thief.\nYou are killed by the angry villagers.")
        elif choice.lower() == "no":
            print("\n\nIn the morning, you are told that there was a thief last night.\nYou are suspected of theft, the villagers will kill you unless you can find the thief in two days' time.")
            play = input("Press 'enter' to start looking for the thief.")

            if play == "":
                player_level = random.randint(1, 6)
                thief_level = random.randint(1, 6)
                print(f"\nThe level of your detective skill is {player_level}\nThe level of the thief's ability to hide is {thief_level}")
                if player_level > thief_level:
                    print("\nCongratulations, you found the thief!\nThe villagers are very grateful and give you a bag of gold!")
                else:
                    print("\nUnfortunately, you weren't able to find the thief.\nYou are killed by the angry villagers.")
            else:
                pass
    elif choice.lower() == "no":
        second_part2 = "\n\nYou kept going and got out of the village. Now you can go into the forest or walk by the river. Where would you like to go?"
        choice = play_game(second_part2, "forest", "river")
        if choice.lower() == "forest":
            third_part2 = "\n\nYou encountered a bear in the forest! Would you like to run away or fight with it?"
            choice = play_game(third_part2, "run", "fight")
            if choice.lower() == "run":
                player_speed = random.randint(1, 6)
                bear_speed = random.randint(1, 6)
                print(f"\nYour speed is {player_speed} unit(s)\nThe bear's speed is {bear_speed} unit(s)")
                if player_speed > bear_speed:
                    print("\nCongratulations, you successfully escaped!\nYou are regarded as the fastest runner by other animals in the forest!")
                else:
                    print("\nUnfortunately, you are caught by the bear.")
            elif choice.lower() == "fight":
                player_strength = random.randint(1, 6)
                bear_strength = random.randint(1, 6)
                print(f"\nYour strength is {player_strength}\nThe bear's strength is {bear_strength}")
                if player_strength > bear_strength:
                    print("\nCongratulations, you defeated the bear!\nThe animals in the forest showed great admiration to you and shared their treasure with you!")
                else:
                    print("\nUnfortunately, you are killed by the bear.")
        elif choice.lower() == "river":
            third_part3 = "\n\nA fisherman was attacked by an alligator. Would you like to help him?"
            choice = play_game(third_part3, "yes", "no")
            if choice.lower() == "yes":
                player_strength = random.randint(1, 6)
                croc_strength = random.randint(1, 6)
                print(f"\nYour strength is {player_strength}\nThe crocodile's strength is {croc_strength}")
                if player_strength > croc_strength:
                    print("\nCongratulations, you defeated the crocodile!\nThe fisherman is very grateful and gave you a huge bag of fish!")
                else:
                    print("\nUnfortunately, you are killed by the crocodile.")
            elif choice.lower() == "no":
                print("\n\nThe desperate fisherman grabbed you into the river.\nUnfortunately, you are drowned.")


username = input("What is your name?\n")
main(username)

print("\n\nGame Over")
