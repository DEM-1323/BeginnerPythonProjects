class Quiz:
    '''Models a quiz with a question set'''
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.questions = []

    def import_questions(self, question_set):
        '''Take a set of questions from a listed
        dictionary and creates new Question objects'''
        '''Questions must be in this format:[
        {"text": "prompt here", "answer": "answer here"},
        ]'''
        for question in question_set:
            self.questions.append(Question(question['text'],
                                           question['answer']))


class Question:
    '''Models a question'''
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
