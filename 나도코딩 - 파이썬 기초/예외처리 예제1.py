# try: 
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}" .format(num1, num2, round(num1/num2,2)))

# except ValueError:
#     print("에러가 발생했습니다.")
# except ZeroDivisionError:
#     print("오류")

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2])) 
    #nums[2]는 존재하지 않음.
    
# except:
#     print("알 수 없는 에러 발생!")

# err를 사용하면 어떤 에러인지 파악가능!
except Exception as err:
    print("알 수 없는 에러 발생!")
    print(err)
    
    
