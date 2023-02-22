from player import Player

class Human_Player(Player):
    def __init__(self):
        super().__init__()



    # Prompts user for a gesture from the rpsls_list
    def get_gesture(self, rpsls_list):
        gesture_is_there = False

        while gesture_is_there == False:
            user_input = input("Please enter in a gesture from the given list: ")
            if user_input in rpsls_list:
                gesture_is_there = True
            else:
                gesture_is_there = False
                print("Incorrect input, please try again")
        
        return user_input.lower()
