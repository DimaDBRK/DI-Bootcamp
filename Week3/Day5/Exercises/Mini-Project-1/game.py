# Week3 Day5
#Dmityr Dubrov
# Mini-Project: Rock, Paper, Scissors
# game.py – 
# this will contain a Game class which will have functions to play a single 
# game of rock-paper-scissors against the computer, determine the game’s result,
# and return the result.

#imports
import random

#classes
class Game :
    
    def __init__(self):
        self.games_res = {"win": 0,"loss": 0,"draw": 0}
        
    
    def get_user_item(self) :
        """Ask the user to select an item (rock/paper/scissors). 
        Keep asking until the user has selected one of the items – 
        use data validation and looping. Return the item at the end of 
        the function.
        """
        while True:
            conf_in = "r1p2s3q"
            return_dict = {'r':'rock', '1':'rock', 'p':'paper', '2':'paper','s':'scissors', '3':'scissors', 'q': 'q'}
            user_in = input("Select rock(r,1), paper(p,2) or scissors(s,3): ").lower()
            if user_in not in conf_in :
                print("Wrong symbol input. Try egain or input (q) for exit.")
            else:
                res = return_dict[user_in]
                break #check if q will work
            
        return res
        
        
    def get_computer_item(self) :
        """Select rock/paper/scissors at random for the computer. 
        Return the item at the end of the function. 
        Uses python’s random.choice() 
        """
        return_dict = {'r':'rock', '1':'rock', 'p':'paper', '2':'paper','s':'scissors', '3':'scissors', 'q': 'q'}
        return return_dict[str(random.randint(1,3))]
    
    def get_game_result(self, user_item, computer_item) :
        """Determine the result of the game.
    Parameters:
    user_item – the user’s chosen item (rock/paper/scissors)
    computer_item – the computer’s chosen (random) item (rock/paper/scissors)
    Return either win, draw, or loss. Where win means that the user has won, 
    draw means the user and the computer got the same item, and loss means that 
    the user has lost.
          """
        #dict with variants for user to loss. Key - computer, value - user
        game_variants_user_lose = {'rock': 'scissors','paper':'rock','scissors': 'paper'}
        res_user = "win"
        if user_item == computer_item :
            res_user = "draw"
        elif game_variants_user_lose[computer_item] == user_item:
            res_user = "loss"
        return res_user
    
    def play(self) :
        """the function that will be called from outside the class 
        (ie. from rock-paper-scissors.py). It will do 3 things:
        1. Get the user’s item (rock/paper/scissors) and remember it
        2. Get a random item for the computer (rock/paper/scissors) and remember it
        3. Determine the results of the game by comparing the user’s item and 
        the computer’s item
        """
        # Get the user’s item (rock/paper/scissors) and remember it
        user_item = self.get_user_item()
        # Get a random item for the computer (rock/paper/scissors) and remember it
        computer_item = self.get_computer_item()
        res = self.get_game_result(user_item, computer_item) 
        print(f'You selected {user_item}. The computer selected {computer_item}. You {res}')
        
        return res
        
#Driver

#tets
# a = Game()
# #print(a.get_user_item())
# print(a.get_computer_item())
# print("Tests who win (user vs computer):")
# if a.get_game_result("rock","scissors") == "win": print("Ok") 
# else: print("Nok")
# if a.get_game_result("scissors", "rock") == "loss": print("Ok") 
# else: print("Nok")
# if a.get_game_result("rock", "rock") == "draw": print("Ok") 
# else: print("Nok")
# if a.get_game_result("paper", "scissors") == "loss": print("Ok") 
# else: print("Nok")

# a.play()