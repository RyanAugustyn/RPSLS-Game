class Player:
    def __init__(self):
        self.round_wins = 0
        self.gesture_choice = ''



# Prompts user for a gesture from the rpsls_list
    def get_gesture(self, rpsls_list):
        user_input = ""
        gesture_is_there = False

        while gesture_is_there == False:
            user_input = input("Please enter in a gesture from the given list: ")
            if user_input in rpsls_list:
                gesture_is_there = True
            else:
                gesture_is_there = False
        
        return user_input

