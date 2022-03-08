def profile(name, age, *language): # *을 사용하면 가변인수로 무한대
    print("이름 = {0}, 나이 = {1}," .format(name, age), end=" ")
    print("언어 =", end=" ")
    for i in language:
        print(str(i) + ",", end=" ") # 이런식으로 출력가능
    print()


profile("A", 24, "파이썬", "C++", "자바")
profile("B", 23, "파이썬")
profile("C", 27, "파이썬", "C++", "자바", "안드로이드", "IOS")
