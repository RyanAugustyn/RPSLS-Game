from human_player import Human_Player
from ai_player import AI_Player

class Game: 
    def __init__(self):
        self.rpsls_list = ["rock", "paper", "scissors", "lizard", "spock"]
        self.single_player = False
        self.player_1 = Human_Player()
        self.player_2 = AI_Player()

# Runs the RPSLS game
    def run_game(self):
        self.print_greeting()
        self.print_instructions()
        self.single_player = self.game_mode_determiner()
        if self.single_player == False:
            self.player_2 = Human_Player()
        while self.player_1.round_wins < 2 and self.player_2.round_wins < 2:
            self.print_list(self.rpsls_list)
            player_choice_1 = self.player_1.get_gesture(self.rpsls_list)
            player_choice_2 = self.player_2.get_gesture(self.rpsls_list)
            player_1_win = self.gesture_comparison(player_choice_1, player_choice_2)
            self.who_won_round(player_1_win)
        if self.player_1.round_wins == 2:
            print("\n\nPlayer 1 wins the game!!!")
        if self.player_2.round_wins == 2:
            print("\n\nPlayer 2 wins the game!!!")


    #greeting
    def print_greeting(self):
        print("\nWelcome to Rock Paper Scissors...Lizard Spock!\n")


    #print out the rules 
    def print_instructions(self):
        print("The rules of the game are as follows:")
        print("Players take turns choose from one of five options,")
        print("Rock, Paper, Scissors, Lizard, Spock. Once both options are chosen")
        print("the game determines who wins the round based on the rules below. It ")
        print("is best out of three rounds, so first player to two wins wins overall.")
        print("\nThe rules for all of the options are as follows:\n")
        print("Rock beats Scissors, loses to Paper and Spock")
        print("Scissors beats Paper and Lizard, loses to Rock and Spock")
        print("Paper beats Rock and Spock, loses to Scissors and Lizard")
        print("Lizard beats Spock and Paper, loses to Rock and Scissors")
        print("Spock beats Scissors and Rock, loses to Lizard and Paper")
        
# Prints a given list in this format 1. Item 2. Item
    def print_list(self, rpsls_list):
        index = 1
        for item in rpsls_list:
            print(f"{index}. {item}")
            index += 1
    
# Prompts the user to enter in multiplayer or single player and returns a boolean
    def game_mode_determiner(self):
        user_input = ""
        single_player = False


        while single_player == False:
            user_input = input("\nPlease enter in Multiplayer or Single Player for game mode: ")
            if user_input == "single player":
                single_player = True
            elif user_input == "multiplayer":
                return single_player
            else:
                print("Incorrect input")

        return single_player

# Performs game logic according to RPSLS rules
    def gesture_comparison(self, choice_1, choice_2):
        choice_1_wins = False

        while choice_1 == choice_2:
            pass
    
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
    
# Tells user if player_1 or player_2 won
    def who_won_round(self, is_winner):
        if is_winner == True:
            print("\nPlayer 1 won this round!")
            self.player_1.round_wins += 1
        else:
            print("\nPlayer 2 won this round!")
            self.player_2.round_wins += 1