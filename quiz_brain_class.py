import html
from html import unescape


class QuizBrain:
    def __init__(self,quiz_list):
        self.question_number = 0
        self.quiz_list = quiz_list
        self.score = 0
        self.current_question = None
        self.current_answer = None

    def still_has_question(self):
        number_of_questions = len(self.quiz_list)
        if self.question_number < number_of_questions:
            return True
        else:
            return False

    def next_question(self):
        current_question = unescape(self.quiz_list[self.question_number].question)
        self.current_answer = self.quiz_list[self.question_number].answer
        self.question_number += 1
        return f"Q{self.question_number}: {current_question} (True/False): "


    def check_answer(self,user_answer):
        if self.current_answer == user_answer:
            self.score += 1
            return True




