class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class Quiz_brain:

    def __init__(self, q_list):
        self.quiz_number = 0
        self.score = 0
        self.question_list = q_list

    def question_check(self):
        return self.quiz_number < len(self.question_list)

    def next_quiz(self):
        use_answer = input(f"Q{self.quiz_number}. {self.question_list[self.quiz_number].text} ")
        if use_answer.lower() == self.question_list[self.quiz_number].answer:
            self.score += 1
            print("You're right !!")
        self.quiz_number += 1

    def print_score(self):
        print(f"You're score : {self.score}")