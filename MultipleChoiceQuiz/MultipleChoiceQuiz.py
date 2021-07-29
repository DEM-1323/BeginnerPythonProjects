from questions import question


def main():

    question_prompts = [
        'What color are apples?\n\n (a) Red/Green\n (b) Purple\n (c) Orange\n',
        'What color are bananas?\n\n (a) Teal\n (b) Magenta\n (c) Yellow\n',
        'What color are strawberries?\n\n (a) Yellow\n (b) Red\n (c) Blue\n'
    ]

    questions = [
        question(question_prompts[0], 'a'),
        question(question_prompts[1], 'c'),
        question(question_prompts[2], 'b')
    ]

    answers = []

    run_test(questions, answers)
    questions_correct = check_answers(questions, answers)

    print('\nYou Answered ' + str(questions_correct) + '/' +
          str(len(questions)) + ' Questions Correct\n')


def run_test(questions, answers):
    for index in range(len(questions)):
        print('\n' + questions[index].prompt)
        answers.append(str(input('Enter Your Answer: ')).lower())
    return answers


def check_answers(questions, answers):
    questions_correct = 0
    for index in range(len(questions)):
        if answers[index] != questions[index].answer:
            print('\n Question ' + str(index + 1) + ' is incorrect')
        else:
            print('\n Question ' + str(index + 1) + ' is correct')
            questions_correct += 1
    return questions_correct


main()
