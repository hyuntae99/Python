# for i in range(1,51):
#     report = open("{}주차.txt".format(i), "w", encoding="utf8")
#     report.write("- {}주차 주간보고 -\n" .format(i))
#     report.write("부서 : \n")
#     report.write("이름 : \n")
#     report.write("업무 요약 : \n")
# report.close()


for i in range(1,51):
    with open("{}주차.txt".format(i), "w", encoding="utf8") as report:
        report.write("- {}주차 주간보고 -\n" .format(i))        
        report.write("부서 : \n")
        report.write("이름 : \n")
        report.write("업무 요약 : \n")
    