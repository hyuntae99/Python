# 내장함수

# input : 사용자 입력을 받는 함수
# language = str(input("무슨 언어를 좋아하세요?"))
# print("{}는 아주 좋은 언어입니다!".format(language))


# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random #외장함수
# print(dir()) #random이 추가됨
# import pickle
# print(dir())

# print(dir(random)) #random 함수 내 사용가능한 변수, 함수들을 표시

# 사용가능한 변수, 함수들 표시
# list = [1,2,3]
# print(dir(list))
# name = "cho"
# print(dir(name))


# list of python builtins 를 검색하면 파이썬 내 사용가능한 함수들 표시됨.


# --------------------------------------------------------------------

# 외장함수

# list of python modules 를 구글에 검색하면 나옴

# glob : 경로 내의 폴더, 파일 목록 조회
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일


# os : 운영체제에서 제공하는 기본기능
# import os
# print(os.getcwd()) #현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print("폴더를 삭제했습니다.")
# else:
#     os.mkdir(folder)
#     print(folder, "폴더를 생성했습니다.")

# print(os.listdir()) #glob와 비슷함


# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S")) #년-월-날 시:분:초

import datetime
print("오늘 날짜는 ", datetime.date.today()) #년 월 날

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 ", today + td)