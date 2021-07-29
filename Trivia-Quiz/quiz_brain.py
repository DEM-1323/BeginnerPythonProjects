import random


class QuizBrain:
    def __init__(self):
        self.score = 0
        self.questions_asked = []
        self.user_answers = []

    def run_test(self, questions):
        for index in range(len(questions)):
            prompt = random.choice(questions)
            questions.remove(prompt)
            self.questions_asked.append(prompt)
            print('\n' + prompt.prompt)
            self.user_answers.append(str(input('True or False: ')
                                         ).capitalize())
        return self.user_answers

    def check_answers(self, questions_asked, answers):
        for index in range(len(questions_asked)):
            if answers[index] != questions_asked[index].answer:
                print('\n Question ' + str(index + 1) + ' is incorrect')
            else:
                print('\n Question ' + str(index + 1) + ' is correct')
                self.score += 1
        return self.score
