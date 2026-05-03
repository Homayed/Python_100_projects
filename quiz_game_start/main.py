from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_item = item["text"]
    answer_item = item["answer"]
    new_question = Question(question_item,answer_item)
    question_bank.append(new_question)


print(question_bank)

quiz_b = QuizBrain(question_bank)

while quiz_b.still_have_question():
    quiz_b.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz_b.score}/{len(question_bank)}")




