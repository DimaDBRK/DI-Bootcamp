# Week3 Day5
#Dmityr Dubrov
# Mini-Project: Rock, Paper, Scissors
#rock-paper-scissors.py – 
# this will contain functions to show the main menu, handle user’s input, 
# and show the game summary before exiting.

# import
from game import Game #im game add condition not to start code
#functions
def get_user_menu_choice() :
    """
    this should display a simple menu, get the user’s choice 
    (with data validation), and return the choice. 
    No looping should occur here.
    The possibles choices are : Play a new game or Show scores or Quit
    """
    conf_in = "123psq"
    return_dict = {'p':'Play a new game', '1':'Play a new game', 's':'Show scores', '2':'Show scores','q':'Quit', '3':'Quit'}
    print("Menu:")
    print("(1)(g) - Play a new game")
    print("(2)(s) - Show scores")
    print("(3)(q) - Quit")
    
    user_in = input("Input menu item: ").lower()
    if user_in not in conf_in :
        print("Wrong symbol input")
        res = "typeerror"
    else:
        res = return_dict[user_in]
    return res       
def print_results(results) :
    """ This should print the results of the games played. 
    It should have a single parameter named results; 
    which will be a dictionary of the results of the games played. 
    It should display these results in a user-friendly way, and thank 
    the user for playing.
    results should be in this form: {win: 2,loss: 4,draw: 3}
    """
    str_out = '\nGame Results:\n'
    for keys,values in results.items():
        s = "s" if values > 2 else ""
        str_out += f'   You {keys} {values} time{s}\n'
    print(str_out)
    
def main() :
    conf_in = ['Play a new game','Show scores','Quit','typeerror']
    play1 = Game()
    while True:
        res = get_user_menu_choice()
        if res == conf_in[2] :
            print(f'You chose: {conf_in[2]}')
            break
        elif res == conf_in[0] :
            iteration_res = play1.play()
            # print(iteration_res)
            # print("res", play1.games_res)
            # play1.games_res += 1
            # print("res before :", play1.games_res)
            play1.games_res[iteration_res] += 1
            # print("res after :", play1.games_res)
            
        elif res == conf_in[1]:
            print_results(play1.games_res)
            


#Driver

#Tests
# print(get_user_menu_choice())
# print_results({"win": 1,"loss": 4,"draw": 3})
main() 
