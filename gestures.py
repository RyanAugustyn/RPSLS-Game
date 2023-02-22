class Gestures():
    def __init__(self) -> None:
        pass

#use the 'in' function 
#maybe inheritance 
#final result should be 2-3 lines in game.py




# Performs game logic according to RPSLS rules
    def gesture_comparison(self, choice_1, choice_2):
        choice_1_wins = False

        if choice_1 == "rock":
            if choice_2 == "paper" or choice_2 == "spock":
                choice_1_wins = False
            else:
                choice_1_wins = True
        elif choice_1 == "scissors":
            if choice_2 == "rock" or choice_2 == "spock":
                choice_1_wins = False
            else:
                choice_1_wins = True
        elif choice_1 == "paper":
            if choice_2 == "scissors" or choice_2 == "lizard":
                choice_1_wins = False
            else:
                choice_1_wins = True
        elif choice_1 == "lizard":
            if choice_2 == "rock" or choice_2 == "scissors":
                choice_1_wins = False
            else:
                choice_1_wins = True
        elif choice_1 == "spock":
            if choice_2 == "lizard" or choice_2 == "paper":
                choice_1_wins = False
            else:
                choice_1_wins = True

        return choice_1_wins