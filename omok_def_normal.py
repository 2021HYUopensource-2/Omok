import re
import csv

board = [['-' for i in range(15)] for j in range(15)] #오목판 만들기
def print_board(): 
    for i in range(14,-1,-1):
        print('  '.join(board[i]),i)
    print ('0  1  2  3  4  5  6  7  8  9  10 11 12 13 14')
    print()

def user_input(player): #입력받기
    ########################예외처리하기##########################
    while True:
        x = int(input('x좌표 값을 입력해주세요: '))
        if x >= 0 and x < 15:
            y = int(input('y좌표 값을 입력해주세요: '))
            if y >= 0 and y < 15:
                return check_input(player,x,y)
        else:
            print("잘못된 값입니다.")

def check_input(player,x,y): #올바른 입력값인지 확인
     if board[y][x] =='-':
        if function33(player,1,0,x,y)+function33(player,0,1,x,y)+function33(player,1,1,x,y)+function33(player,1,-1,x,y) >= 2:
            print("33불가")
            user_input(player)
            return 0
        else:
            board[y][x]=player
            if functionV(player,1,0,x,y) + functionV(player,0,1,x,y) + functionV(player,1,1,x,y) + functionV(player,1,-1,x,y) >= 1:
                return 1 
     else:
        print("잘못된 값입니다.")
        user_input(player)
        
def function33(player,vector_x,vector_y,x,y): #x,y == 입력받은 x,y
    idx = 1
    keep = player
    while True:
        if y + vector_y*idx < 15 and x + vector_x*idx < 15 and y + vector_y*idx >=0 and x + vector_x*idx >= 0 :
            if board[y + vector_y*idx][x + vector_x*idx] == '-':
                keep += '-'
                break
        else:
            break
        keep += player
        idx += 1
    idx = 1
    while True:
        if y - vector_y*idx >= 0 and x - vector_x*idx >= 0 and  y - vector_y*idx <15 and x - vector_x*idx <15 :
            if board[y - vector_y*idx][x - vector_x*idx] == '-':
                keep += '-'
                break
        else:
            break
        keep += player
        idx += 1
    numO = re.findall('[' + player + ']', keep)
    num = re.findall('[' + '-' + ']', keep)
    if len(numO) + len(num) == 5:
        return 1
    else:
        return 0

def functionV(player,vector_x,vector_y,x,y): #win?
    idx = 0
    keep = ''
    while True:
        if y + vector_y*idx < 15 and x + vector_x*idx < 15 and y + vector_y*idx >=0 and x + vector_x*idx >= 0 :
            if board[y + vector_y*idx][x + vector_x*idx] == player:
                keep += player
        else:
            break
        idx += 1
    idx = 1
    while True:
        if y - vector_y*idx >= 0 and x - vector_x*idx >= 0 and y - vector_y*idx <15 and x - vector_x*idx <15 :
            if board[y - vector_y*idx][x - vector_x*idx] == player:
                keep += player

        else:
            break
        idx += 1
    if keep == player*5:
        return 1
    else:
        return 0
    
def game_end(winner,loser): ###############파일 업데이트, 게임 마무리 ##################### winer[0]은 파일에서 멤버정보 있는 줄 인덱스임을 참고
    print("Winner! : " + winner[1])
    print("Lose : " + loser[1])
    with open('member.csv','r') as t:
        rdr = csv.reader(t)
        ftemp = []
        for line in rdr:
            if(line[1] == winner[1]):
                temp = int(line[3])
                temp += 1
                line[3] = str(temp)
            elif(line[1] == loser[1]):
                temp = int(line[4])
                temp += 1
                line[4] = str(temp)
            ftemp.append(line)
    
    with open('member.csv','w',newline = '') as f:
        wr = csv.writer(f)
        wr.writerows(ftemp)
