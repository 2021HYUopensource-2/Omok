from login import *

board = [['-' for i in range(15)] for j in range(15)] #오목판 만들기
def print_board(): 
    for i in range(15):
        print('  '.join(board[i]),i)
    print ('0  1  2  3  4  5  6  7  8  9  10 11 12 13 14')

def user_input(): #입력받기 
    while True:
        x = input('x좌표 값을 입력해주세요: ')
        if x != '' and int(x) >= 0 and int(x) < 15:
            x = int(x)
            break
    while True:
        y = input('y좌표 값을 입력해주세요: ')
        if y != '' and int(y) >= 0 and int(y) < 15:
            y = int(y)
            break       
    if board[y][x] == '-':
        board[y][x] = 'O'
    else:
        print("다시 입력하세요")
        user_input()
    
def game(): #게임 시작
    login=Login()
    login_member=login.control()
    print(login_member)
    player1=login_member[0]
    player2=login_member[1]
