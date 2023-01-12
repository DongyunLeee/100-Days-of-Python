from data import quiz_list
from quiz import Question, Quiz_brain


question = []
for quiz in quiz_list:
    quiz_text = quiz["question"]
    quiz_answer = quiz["correct_answer"]
    new_quiz = Question(quiz_text, quiz_answer)
    question.append(new_quiz)

Q = Quiz_brain(question)
while Q.question_check():
    Q.next_quiz()

Q.print_score()
