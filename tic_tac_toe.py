import os
import time

logo = """  
 _______  ___   _______    _______  _______  _______    _______  _______  _______ 
|       ||   | |       |  |       ||   _   ||       |  |       ||       ||       |
|_     _||   | |       |  |_     _||  |_|  ||       |  |_     _||   _   ||    ___|
  |   |  |   | |       |    |   |  |       ||       |    |   |  |  | |  ||   |___ 
  |   |  |   | |      _|    |   |  |       ||      _|    |   |  |  |_|  ||    ___|
  |   |  |   | |     |_     |   |  |   _   ||     |_     |   |  |       ||   |___ 
  |___|  |___| |_______|    |___|  |__| |__||_______|    |___|  |_______||_______|
                             
"""
print(logo)
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_is_on = True


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
   
    
def board(pos):   
    game = f' {pos[0]} | {pos[1]} | {pos[2]} \n' \
            f'-----------\n' \
            f' {pos[3]} | {pos[4]} | {pos[5]} \n' \
            f'-----------\n' \
            f' {pos[6]} | {pos[7]} | {pos[8]} \n'
    print(game)


def end_game(game):
    global game_is_on
    win1 = game[0]+ game[3]+ game[6]
    win2 = game[0]+ game[4]+ game[8]
    win3 = game[0]+ game[1]+ game[2]
    win4 = game[1]+ game[4]+ game[7]
    win5 = game[2]+ game[4]+ game[6]
    win6 = game[2]+ game[5]+ game[8] 
    win7 = game[3]+ game[4]+ game[5]
    win8 = game[6]+ game[7]+ game[8]

    if win1=="XXX" or win2=="XXX" or win3=="XXX" or win4=="XXX" or win5=="XXX" or win6 =="XXX"or win7=="XXX" or win8 =="XXX":
        print("Player 1 is the winner")
        game_is_on = False
    if win1 =="OOO" or win2 =="OOO" or win3 =="OOO" or win4 =="OOO" or win5 =="OOO"or win6 =="OOO"or win7=="OOO" or win8 =="OOO":
        print("Player 2 is the winner")
        game_is_on = False

    
board(pos)
print("Player one: X")
print("Player two: O")


game_play = ["","","","","","","","",""]
while game_is_on:
    time.sleep(3)
    clear_terminal()
    if "" in game_play:
        p1 = int(input("Player 1:Select the position you want yout token to go to: ")) - 1 
        if game_play[p1]=="X" or game_play[p1]=="O" :
            p1 = int(input("Oops, try a different position:"))
            game_play[p1]="X"
            board(game_play)
            end_game(game_play)
        else:    
            game_play[p1]="X"
            board(game_play)
            end_game(game_play)

        if game_is_on:
            p2 = int(input("Player 2: Select the position you want yout token to go to: ")) - 1
            if game_play[p2]=="X" or game_play[p1]=="O" :
                p2 = int(input("Oops, try a different position:"))
                game_play[p2]= "O"
                board(game_play)
                end_game(game_play)
                
            else:
                game_play[p2]= "O"
                board(game_play)
                end_game(game_play)
                
                  
    else: 
        print("It's a tie")
        game_is_on = False
       
    
        

        