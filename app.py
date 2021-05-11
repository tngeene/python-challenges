from question import Question
import sys

question_prompts = [
    "Which is the biggest country in the world?\n(a) Russia\(b)Brazil\(c)Sudan\n\n",
    "Select the longest River in the world.\n(a)Mississipi River\(b)The Amazon River\n(c)River Nile\n\n",
    "Name the driest desert in the world.\n(a)Sahara Desert\n(b)Namib Desert\n(c)Atacama Desert\n"
]

questions  = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

# logic for tracking correct answers
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " +  str(score) + "/" + str(len(questions)) + " correct" )


def main():
    run_test(questions)

if __name__  == '__main__':
    main()


