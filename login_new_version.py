import csv
class Login:
    member=[]
    login_member=[]   
    def f_register(self): #파일에 리스트로 저장
        t=open('member.csv','a',newline='')
        wr = csv.writer(t)
        wr.writerow(self.member)
        print("회원가입 완료",end="")
        t.close()

    def check(self,check_id,what): #0은 중복 확인 /1은 아이디 정보 확인
        with open("member.csv","r") as t:
            rdr = csv.reader(t)
            for line in rdr:
                if(line[0]==check_id):
                    if(what==0):
                        return 1
                    else:
                        return line
            return 0
        
    def save_member(self,player1,player2):
        self.login_member.append(player1)
        self.login_member.append(player2)
        return self.login_member
    def control(self):
        print("환영합니다:)")
        cnt=0
        while(1):
            print("---------------")
            print("1.로그인\n2.회원가입\n3.나가기\n메뉴를 선택하세요: ",end="")
            user_input=int(input())
            print("---------------")
            if user_input==1:
                search_id=input("아이디를 입력해주세요: ")
                c=self.check(search_id,1)
                if (cnt==0 and c!=0):
                    search_pw=input("비밀번호를 입력해주세요: ")
                    if c[1]==search_pw:
                        cnt+=1
                        player1=c
                        print("player1 로그인 성공")
                        continue
                elif (cnt==1 and search_id!=player1[0]) :
                    search_pw=input("비밀번호를 입력해주세요: ")
                    if c[1]==search_pw:
                        player2=c
                        print("player2 로그인 성공 \n")
                        print("---------------")
                        print("게임을 시작합니다.")
                        return self.save_member(player1,player2)
                    else:
                        print("비밀번호가 틀립니다.")
                        continue
                else:
                    print("잘못된 아이디입니다.")
                    continue
            if user_input==2:
                new_id=input("아이디를 입력해주세요: ")
                while(self.check(new_id,0)==1):
                    new_id=input("이미 있는 아이디입니다.\n아이디를 다시 입력해주세요: ")
                new_pw=input("비밀먼호를 입력해주세요: ")
                while(len(new_pw)<8):
                    new_pw=input("비밀번호를 8자 이상이어야합니다. 비밀번호를 다시 입력해주세요: ")
                self.member+=[new_id,new_pw,0,0] #[아이디,비밀번호,이긴횟수,진 횟수]
                self.f_register()
            else:
                return 0
