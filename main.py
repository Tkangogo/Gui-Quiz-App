from question_class import Question
from data import question_data
from quiz_brain_class import QuizBrain
from ui_class import QuizInterface

question_bank = []
for data in question_data:
    q1 = data["question"]
    a1 = data["correct_answer"]
    incorrect_choices = data["incorrect_answers"]
    question_bank.append(Question(q1,a1))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

