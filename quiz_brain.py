class QuizBrain:
    def __init__(self,question_list):
        self.question=0
        self.question_list=question_list
        self.score=0

    def still_has_questions(self):
        if self.question<len(self.question_list):
            return True
        else:
            return False

    def next_method(self):
        current_question=self.question_list[self.question]
        self.question+=1
        user_answer=input(f"q.{self.question}:{current_question.text} true/false:")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("you got it right!")
            self.score+=1

        else:
            print("the answer was wrong")
        print(f"the correct answer is {correct_answer}.")
        print(f"the current score is {self.score}/{self.question}")
        print("\n")
