class Game: 
    def __init__(self):
        self.rpsls_list = ["rock", "paper", "scissors", "lizard", "spock"]
        self.single_player = False

# Runs the RPSLS game
    def run_game(self):
        self.print_greeting()
        self.print_instructions()
        self.game_mode_determiner()
        self.get_gester()

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
    def game_mode_determiner(self, single_player):
        user_input = ""

        while single_player == False:
            user_input = input("Please enter in Multiplayer or Single Player for game mode: ")
            if user_input.lower != "multiplayer" or user_input.lower != "single player":
                single_player = False
            else:
                single_player = True

# Prompts user for a gester from the rpsls_list
    def get_gester(self, rpsls_list):
        user_input = ""
        gester_is_there = False

        while gester_is_there == False:
            self.print_list(rpsls_list)
            user_input = input("Please enter in a gester from the given list: ")
            if self.check_gester(user_input) == True:
                gester_is_there = True
            else:
                gester_is_there = False
        
        return user_input


# Checks to see if the gester passed is in the rpsls_list
    def check_gester(self, gester, rpsls_list):
        gester_is_there = False

        if gester_is_there == False:
            for item in rpsls_list:
                if item == gester.lower:
                    gester_is_there = True
                    break
                elif item != gester.lower:
                    gester_is_there = False

        return gester_is_there
