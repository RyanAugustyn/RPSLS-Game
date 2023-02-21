class Game: 
    def __init__(self):
        self.rpsls_list = ["rock", "paper", "scissors", "lizard", "spock"]
        self.single_player = False

    def run_game():
        pass

    def print_list(self, rpsls_list):
        index = 1

        print("")

        for item in rpsls_list:
            print(f"{index}. {item}")
            index += 1