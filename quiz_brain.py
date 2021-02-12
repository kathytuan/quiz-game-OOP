class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # TODO: 3. checking if we are at the end of the quiz
    def still_has_questions(self):
        total_question = len(self.question_list)
        return self.question_number < total_question

    # TODO: 1. asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    # TODO: 2. checking if the answer was correct
    def check_answer(self, user_answer, current_answer):
        if current_answer.lower() == user_answer.lower():
            self.score += 1
            print("Bingo!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {current_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
