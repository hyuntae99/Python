# 정규식

# 주민등록번호
# 991202 - 1009510

# 이메일 주소
# hyuntae9912@naver.com

# 차량 번호
# 11가 1234

################################################################
import re
# 뺑소니범 차량번호 ca?e 였음

p = re.compile("ca.e") 
# . : 하나의 문자를 의미 > care, cafe / caffe X (2글자는 안됨)
# ^ : (^de) -> 문자열의 시작 > desk, destination / fade X (de로 시작)
# $ : (se$) -> 문자열의 끝 > case, base / face x (se로 끝나야함)

def print_match(m):
    if m: # 매치가 되었을때
        print("m.group() : ", m.group()) # 매치되지 않으면 에러 발생함
        print("m.string : ", m.string) # 입력받은 문자열
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 인덱스
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 인덱스
        print("m.span() : ", m.span()) # 일치하는 문자열의 시작, 끝 인덱스
    else:
        print("매칭되지 않음")
        
# m = p.match("case") # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)


# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트로 반환
print(lst) # care, cafe


#######################################################################################

# 기초 양식
# 1. p = re.compile("원하는 형태") 
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부텅 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트"형태로 반환

# 원하는 형태 : 정규식
# . : 하나의 문자를 의미 > care, cafe / caffe X (2글자는 안됨)
# ^ : (^de) -> 문자열의 시작 > desk, destination / fade X (de로 시작)
# $ : (se$) -> 문자열의 끝 > case, base / face x (se로 끝나야함)