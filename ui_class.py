from tkinter import *
from quiz_brain_class import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_files:QuizBrain):
        self.quiz = quiz_files
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR,font=("Arial",18,"normal"),fg="white")
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150,125,text="gg",width = 250, fill=THEME_COLOR, font=("Arial",15,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        x_image = PhotoImage(file="false.png")
        self.x_button = Button(image=x_image, command=self.false_pressed)
        self.x_button.grid(row=2,column=0)

        tick_image = PhotoImage(file="true.png")
        self.tick_button = Button(image=tick_image, command=self.true_pressed)
        self.tick_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.canvas_text, fill=THEME_COLOR)
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text,text="You have reached the end of the quiz.")
            self.tick_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def get_check_answer(self,user_answer):
        right_answer = self.quiz.check_answer(user_answer)
        if right_answer:
            self.canvas.config(bg="green yellow")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="tomato")
            self.canvas.itemconfig(self.canvas_text, fill="white")
        self.window.after(1000, self.get_next_question)

    def true_pressed(self):
        user_answer = "True"
        self.get_check_answer(user_answer)


    def false_pressed(self):
        user_answer = "False"
        self.get_check_answer(user_answer)