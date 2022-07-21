class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}:{question.text} (True / False)?: ")
        self.check_answer(guess, question.answer)

    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print("You're right")
        else:
            print("You're wrong")
        print(f"The correct answer was: {answer}")
        print(f"Current score: {self.score}/ {self.question_number}")
        print('\n')
