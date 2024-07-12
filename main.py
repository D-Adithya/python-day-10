from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for i in range(len(question_data)):
    text=question_data[i]["question"]
    answer=question_data[i]["correct_answer"]
    question_bank.append(Question(text,answer))

quiz=QuizBrain(question_bank)
while quiz.still_has_questions()==True:
    quiz.next_method()

print("congrats on completing the quiz!")
print(f"your final score is  {quiz.score}/{quiz.question}:")