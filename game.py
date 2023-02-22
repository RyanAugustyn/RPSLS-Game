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
        self.get_gesture(self.rpsls_list)

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
            else:
                single_player = False

        return single_player

#Set players equal to either human or ai 
    def set_players(self, single_player):
        if single_player == False:
            self.player_2 = Human_Player()
