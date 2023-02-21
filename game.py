class Game: 
    def __init__(self):
        self.rpsls_list = ["rock", "paper", "scissors", "lizard", "spock"]
        self.single_player = False

    def run_game():
        pass



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
