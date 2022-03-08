class Word:
    def __init__(self, ques, answer1, answer2, choice):
        self.ques = ques
        self.answer1 = answer1
        self.answer2 = answer2
        self.choice = choice
    
    def show_question(self):
        print("\"{}\" 의 뜻은?".format(self.ques))
        print("1. {}".format(self.answer1))
        print("2. {}".format(self.answer2))
        
    def check_answer(self):
        user_answer = int(input("==> "))
        if user_answer == int(self.choice):
            print("정답입니다!")
        else:
            print("틀렸습니다!")
            

word = Word("얼죽아", "얼어죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer()