from operator import eq
def file_len(fname):
    lines = 0
    for line in open(fname):
        lines += 1
    return lines

def login():
    while True:
        print("환영합니다.\n"
              "로그인: 1\n"
              "회원가입: 2\n"
              "나가기: 3")
        user_input = int(input())
        if user_input == 1:
            user_id = input("닉네임을 입력해주세요: \n")



        elif user_input == 2 :
            new_id = input("새로운 닉네임을 입력해주세요: \n")
            while True:
                with open("user_data.txt","r") as f:
                    cnt = 0
                    num_lines = file_len("user_data.txt")
                    for i in range(num_lines):
                        if new_id in f.readline():
                            cnt = 1
                    if cnt == 1:
                        new_id = input("닉네임이 중복됩니다. 닉네임을 다시 입력해주세요: ")
                    else:
                        break
            with open("user_data.txt", "a") as f:
                f.write(new_id)
                f.write(" ")
            new_password = input("새로운 비밀번호를 입력해주세요: \n"
                                  "(8자 이상이어야 합니다.)\n")
            while True:
                with open("user_data.txt", "r") as f:
                    if len(new_password) < 8:
                        new_password = input("입력한 비밀번호가 8자 미만입니다. 다시 입력해주세요: ")
                    else:
                        break
            with open("user_data.txt", "a") as f:
                f.write(new_password)
                f.write("\n")
            print("회원가입이 완료되었습니다. 이제 로그인해주세요.\n")
        elif user_input == 3:
            exit(1)
        else:
            print("잘못 입력하셨습니다.")

login()

