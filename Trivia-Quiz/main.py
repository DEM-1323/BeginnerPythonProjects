# %%
from quiz import Quiz
# %%
from quiz_brain import QuizBrain
# %%
import data
# %%
quiz = Quiz('Trivia Night', 'True or False', )
quiz.name = 'Trivia Night'
quiz.type = 'True or False'
quiz_brain = QuizBrain()
# %%
quiz.import_questions(data.question_data)
# %%
quiz_brain.run_test(quiz.questions)
# %%
quiz_brain.check_answers(quiz_brain.questions_asked, quiz_brain.user_answers)
