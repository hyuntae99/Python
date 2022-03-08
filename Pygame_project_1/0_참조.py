lst = ["가", "나", "다"]
 
for lst_idx, lst_val in enumerate(lst):
    print(lst_idx, lst_val)
    
# 인덱스 번호와 그에 따른 값 출력가능


############################################################################
balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("ball : ", ball_val)
    
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapon : ", weapon_val)
        if ball_val == weapon_val:
            print("ball collision with weapon")
            break
            # 이 break를 통해야만 바깥쪽 for문 break로 갈 수 있음.
        
    else:
        continue
    print("바깥 for문 break")
    break
        
# 이중 for문이기때문에 break를 한번만 쓰면 충돌 후에도 볼 4번까지 실행됨.
# 이중 for문에서 바로 탈출하고 싶을때 쓸 수 있는 구문


# for 바깥조건:
#     바깥동작
#     for 안쪽조건:
#         안쪽동작
#         if 충돌하면:
#             break
#     else:
#         continue
#     break
