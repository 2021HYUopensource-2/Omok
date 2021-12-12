def mode():
    print("플레이할 모드를 선택해주세요.\n")
    while(1):
        user_input = int(input("1.렌주룰, 2.일반룰: "))
        if(user_input == 1):
            return 1
        elif(user_input == 2):
            return 2
        else:
            print("다시입력해주세요.")