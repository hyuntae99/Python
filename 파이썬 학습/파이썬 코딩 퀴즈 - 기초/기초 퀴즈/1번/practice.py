print("유투버 이름을 입력해주세요.")
print("이름을 다 등록하셨으면 ENTER 를 입력하세요.")
names = []
while True:
    name = str(input())
    names.append(name)
    
    if len(name) == 0: #ENTER키 활용 
        break

for i in range(len(names)-1): #ENTER키도 입력되므로 -1
    msg = open("{}.txt".format(names[i]), "w", encoding="utf8")
    # msg.write("안녕하세요? {}님\n\n".format(names[i]))
    # msg.write("(주)나도출판 편집자 니코입니다.\n")
    # msg.write("현재 저희 출판사는 파이썬에 대한 책을 출간하려고 합니다.\n")
    # msg.write("{}님의 유투브 영상을 보고 연락을 드리게 되었습니다.\n".format(names[i]))
    # msg.write("자세한 내용은 첨부드리는 제안서를 확인해주세요.\n\n")
    # msg.write("좋은 하루 보내세요 ㅎㅎ \n")
    # msg.write("\n-니코 드림-")
    
    # 이런방식으로 출력도 가능
    contents = (f"안녕하세요? {names[i]}님\n\n"
    "(주)나도출판 편집자 니코입니다.\n"
    "현재 저희 출판사는 파이썬에 대한 책을 출간하려고 합니다.\n"
    f"{names[i]}님의 유투브 영상을 보고 연락을 드리게 되었습니다.\n"
    "자세한 내용은 첨부드리는 제안서를 확인해주세요.\n\n"
    "좋은 하루 보내세요 ㅎㅎ \n"
    "\n-니코 드림-")
    
    msg.write(contents)
    
    msg.close()

