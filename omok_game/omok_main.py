from login import *
from omok_def import *
   
def game(): #게임 진행
    login=Login()
    login_member=login.control()
    if login_member!=0:
        player1=login_member[0]
        player2=login_member[1]
        print_board()
        cnt=0
        while (cnt<225):
            if user_input('O') == 1:
                print_board()
                game_end(player1,player2) #이긴사람,진사람 
                break
            print_board()
            cnt+=1
            if user_input('X') == 1:
                print_board()
                game_end(player2,player1)
                break
            print_board()
            cnt+=1
game()
