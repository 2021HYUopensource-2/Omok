import re

def function44():
    if (row[y][x+1] == 'O' and row[y][x+2] == 'O' and row[y][x+3] == 'O') or (row[y][x+1] == 'O' and row[y][x+2] == 'O' and row[y][x-1] == 'O') or (row[y][x+1] == 'O' and row[y][x-1] == 'O' and row[y][x-2] == 'O') or (row[y][x-1] == 'O' and row[y][x-2] == 'O' and row[y][x-3] == 'O'):
        if (row[y+1][x] == 'O' and row[y+2][x] == 'O' and row[y+3][x] == 'O') or (row[y+1][x] == 'O' and row[y+2][x] == 'O' and row[y-1][x] == 'O') or (row[y+1][x] == 'O' and row[y-1][x] == 'O' and row[y-2][x] == 'O') or (row[y-1][x] == 'O' and row[y-2][x] == 'O' and row[y-3][x] == 'O'):
            return False
    if (row[y+1][x] == 'O' and row[y+2][x] == 'O' and row[y+3][x] == 'O') or (row[y+1][x] == 'O' and row[y+2][x] == 'O' and row[y-1][x] == 'O') or (row[y+1][x] == 'O' and row[y-1][x] == 'O' and row[y-2][x] == 'O') or (row[y-1][x] == 'O' and row[y-2][x] == 'O' and row[y-3][x] == 'O'):
        if (row[y][x + 1] == 'O' and row[y][x + 2] == 'O' and row[y][x + 3] == 'O') or (row[y][x + 1] == 'O' and row[y][x + 2] == 'O' and row[y][x - 1] == 'O') or (row[y][x + 1] == 'O' and row[y][x - 1] == 'O' and row[y][x - 2] == 'O') or (row[y][x - 1] == 'O' and row[y][x - 2] == 'O' and row[y][x - 3] == 'O'):
            return False
    if (row[y+1][x+1] == 'O' and row[y+2][x+2] == 'O' and row[y+3][x+3] == 'O') or (row[y+1][x+1] == 'O' and row[y+2][x+2] == 'O' and row[y-1][x-1] == 'O') or (row[y+1][x+1] == 'O' and row[y-1][x-1] == 'O' and row[y-2][x-2] == 'O') or (row[y-1][x-1] == 'O' and row[y-2][x-2] == 'O' and row[y-3][x-3] == 'O'):
        if (row[y+1][x-1] == 'O' and row[y+2][x-2] == 'O' and row[y+3][x-3] == 'O') or (row[y+1][x-1] == 'O' and row[y+2][x-2] == 'O' and row[y+1][x-1] == 'O') or (row[y+1][x+1] == 'O' and row[y-1][x+1] == 'O' and row[y-2][x+2] == 'O') or (row[y-1][x+1] == 'O' and row[y-2][x+2] == 'O' and row[y-3][x+3] == 'O'):
            return False
    if (row[y + 1][x - 1] == 'O' and row[y + 2][x - 2] == 'O' and row[y + 3][x - 3] == 'O') or (row[y + 1][x - 1] == 'O' and row[y + 2][x - 2] == 'O' and row[y + 1][x - 1] == 'O') or (row[y + 1][x + 1] == 'O' and row[y - 1][x + 1] == 'O' and row[y - 2][x + 2] == 'O') or (row[y - 1][x + 1] == 'O' and row[y - 2][x + 2] == 'O' and row[y - 3][x + 3] == 'O'):
        if (row[y + 1][x + 1] == 'O' and row[y + 2][x + 2] == 'O' and row[y + 3][x + 3] == 'O') or (row[y + 1][x + 1] == 'O' and row[y + 2][x + 2] == 'O' and row[y - 1][x - 1] == 'O') or (row[y + 1][x + 1] == 'O' and row[y - 1][x - 1] == 'O' and row[y - 2][x - 2] == 'O') or (row[y - 1][x - 1] == 'O' and row[y - 2][x - 2] == 'O' and row[y - 3][x - 3] == 'O'):
            return False

def function33(cell_type,vector_x,vector_y):
    idx = 1
    keep = cell_type
    if y + vector_y*idx < 15 and x + vector_x*idx < 15:
        while row[y + vector_y*idx][x + vector_x*idx] == cell_type or row[y + vector_y*idx][x + vector_x*idx] == CELL_EMPTY:
            if row[y + vector_y*idx][x + vector_x*idx] == CELL_EMPTY:
                keep += CELL_EMPTY
                break
            keep += cell_type
            idx += 1
    idx = 1
    if y - vector_y*idx >= 0 and x - vector_x*idx >= 0:
        while row[y - vector_y*idx][x - vector_x*idx] == cell_type or row[y - vector_y*idx][x - vector_x*idx] == CELL_EMPTY:
            if row[y - vector_y*idx][x - vector_x*idx] == CELL_EMPTY:
                keep += CELL_EMPTY
                break
            keep += cell_type
            idx += 1

    numO = re.findall('[' + cell_type + ']', keep)
    num = re.findall('[' + CELL_EMPTY + ']', keep)     
    if len(numO) + len(num) == 5:
        return 1
    else:
        return 0

def functionV(cell_type,vector_x,vector_y):
    idx = 0
    keep = ''
    if y+vector_y*idx < 15 and x+vector_x*idx < 15:
        while row[y + vector_y*idx][x + vector_x*idx] == cell_type:
            keep += cell_type
            idx += 1
    idx = 1
    if y - vector_y*idx >= 0 and x - vector_x*idx >= 0:
        while row[y - vector_y*idx][x - vector_x*idx] == cell_type:
            keep += cell_type
            idx += 1

    if keep == cell_type*5:
        return 1
    else:
        return 0

MAX_LENGTH = 15
CELL_EMPTY = '+'
PLAYER_1 = 'O'
PLAYER_2 = 'X'

row = [[CELL_EMPTY for i in range(MAX_LENGTH)] for j in range(MAX_LENGTH)]

cnt = 0
while cnt < MAX_LENGTH**2:
    cnt += 1
    is_player_1 = cnt % 2 == 1
    x = ''
    y = ''

    # 입력
    while True:
        while True:
            x = input('x: ')
            if x != '' and int(x) >= 0 and int(x) < 15:
                x = int(x)
                break
        while True:
            y = input('y: ')
            if y != '' and int(y) >= 0 and int(y) < 15:
                y = int(y)
                break       
        if row[y][x] == CELL_EMPTY:
            break
    
    # 33불가
    if is_player_1:
        while function33(PLAYER_1,1,0)+function33(PLAYER_1,0,1)+function33(PLAYER_1,1,1)+function33(PLAYER_1,1,-1) >= 2:
            x = int(input("33불가 x: "))
            y = int(input("33불가 y: "))
    if is_player_1 is False:
        while function33(PLAYER_2,1,0)+function33(PLAYER_2,0,1)+function33(PLAYER_2,1,1)+function33(PLAYER_2,1,-1) >= 2:
            x = int(input("33불가 x: "))
            y = int(input("33불가 y: "))
    if is_player_1:
        while function44() == False:
            x = int(input("44불가 x: "))
            y = int(input("44불가 y: "))


    if is_player_1:
        row[y][x] = PLAYER_1
        
    if is_player_1 is False:
        row[y][x] = PLAYER_2

    # 최종출력
    for i in range(MAX_LENGTH-1,-1,-1):
        print(' '.join(row[i]), i)
    print ('0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 !')

    # 승리조건
    if is_player_1:
        if functionV(PLAYER_1,1,0) + functionV(PLAYER_1,0,1) + functionV(PLAYER_1,1,1) + functionV(PLAYER_1,1,-1) >= 1:
            print('Win-player O')
            break
    
    if is_player_1 is False:
        if functionV(PLAYER_2,1,0) + functionV(PLAYER_2,0,1) + functionV(PLAYER_2,1,1) + functionV(PLAYER_2,1,-1) >= 1:
            print('Win-player X')
            break
