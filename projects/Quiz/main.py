from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    questions_bank.append(Question(text, answer))

quiz_brain = QuizBrain(questions_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz_brain.score}/{len(questions_bank)}")
