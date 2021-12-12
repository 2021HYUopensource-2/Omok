import csv
class Login:
    login_member=[]   
    def f_register(self,member): #파일에 리스트로 저장
        t=open('member.csv','a',newline='')
        wr = csv.writer(t)
        wr.writerow(member)
        print("회원가입 완료")
        t.close()

    def check(self,check_id,what): #0은 중복 확인 /1은 아이디 정보 확인
        with open("member.csv","r") as t:
            rdr = csv.reader(t)
            cnt=0
            for line in rdr:
                if(line[1]==check_id):
                    if(what==0):
                        return -1
                    else:
                        return line
                cnt+=1
            if what==1:
                return 0
            else:
                return cnt
        
    def save_member(self,player1,player2): #player1, player2 정보 반환
        self.login_member.append(player1)
        self.login_member.append(player2)
        return self.login_member

    def control(self):
        print("환영합니다:)")
        cnt=0
        while(1):
            print("---------------")
            print("1.로그인\n2.회원가입\n3.랭킹\n4.나가기\n메뉴를 선택하세요: ",end="")
            ########################예외처리하기##########################
            user_input=int(input())
            print("---------------")
            if user_input==1:
                search_id=input("아이디를 입력해주세요: ")
                c=self.check(search_id,1)
                if (cnt==0 and c!=0):
                    search_pw=input("비밀번호를 입력해주세요: ")
                    if c[2]==search_pw:
                        cnt+=1
                        player1=c
                        print("\nplayer1 로그인 성공")
                        continue
                    else:
                        print("비밀번호가 틀립니다.")
                        continue
                elif (c!=0 and cnt==1 and search_id!=player1[1] and search_id==c[1]) :
                    search_pw=input("비밀번호를 입력해주세요: ")
                    if c[2]==search_pw:
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
                c=self.check(new_id,0)
                while(c==-1):
                    new_id=input("이미 있는 아이디입니다.\n아이디를 다시 입력해주세요: ")
                    c=self.check(new_id,0)
                new_pw=input("비밀먼호를 입력해주세요: ")
                while(len(new_pw)<8):
                    new_pw=input("비밀번호를 8자 이상이어야합니다. 비밀번호를 다시 입력해주세요: ")
                self.f_register([c,new_id,new_pw,0,0]) #[번호,아이디,비밀번호,이긴횟수,진 횟수]
            if user_input == 3:
                data = []
                with open("member.csv","r") as t:
                    rdr = csv.reader(t)
                    for line in rdr:
                        data += [[line[3],line[4],line[1]]] #( win , lose , id )
                data.sort(reverse=True)
                print("\t\t Rank   top5")
                if(len(data)>0):
                    print("1. " + data[0][2] + "\t\t\t ( win / lose : " + data[0][0] + " / " + data[0][1] + " )")
                    if(len(data)>1):
                        print("2. " + data[1][2] + "\t\t\t ( win / lose : " + data[1][0] + " / " + data[1][1] + " )")
                        if(len(data)>2):
                            print("3. " + data[2][2] + "\t\t\t\t ( win / lose : " + data[2][0] + " / " + data[2][1] + " )")
                            if(len(data)>3):
                                print("4. " + data[3][2] + "\t\t\t\t ( win / lose : " + data[3][0] + " / " + data[3][1] + " )")
                                if(len(data)>4):
                                    print("5. " + data[4][2] + "\t\t\t\t ( win / lose : " + data[4][0] + " / " + data[4][1] + " )")
                else:
                    print('\n' + "No one challenged! Start the game and record your score!")
            else:
                return 0
    