import logging

from test_creator import TestGenerator

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

dummy_test = "\n\nQ1. What is the syntax for declaring a variable in Python?\nA. #var my_variable\nB. {name = 'John'}\nC. counter == 0\nD. my_variable = 42"


class Teacher:
    def __init__(self):
        print("Welcome! Run create_full_test() to create a test.")

    def create_full_test(self):
        topic = input("What topic would you like to create a test on? ")
        num_possible_answers = int(input("How many possible questions would you like to have? "))
        num_questions = int(input("How many possible answers per question would you like to have? "))

        self.test_creator = TestGenerator(topic, num_possible_answers, num_questions)
        test = self.test_creator.run()
        # test = dummy_test
        # logging.info(test)
        student_view = self.create_student_view(test, num_questions)
        answers = self.extract_answers(test, num_questions)
        return student_view, answers

    def create_student_view(self, test, num_questions):
        student_view = {1: ""}
        question_number = 1
        for line in test.split("\n"):
            if not line.startswith("Correct Answer:"):
                student_view[question_number] += line + "\n"
            else:
                if question_number < num_questions:
                    question_number += 1
                    student_view[question_number] = ""
        return student_view

    def extract_answers(self, test, num_questions):
        answers = {1: ""}
        question_number = 1
        for line in test.split("\n"):
            if line.startswith("Correct Answer:"):
                answers[question_number] += line + "\n"

                if question_number < num_questions:
                    question_number += 1
                    answers[question_number] = ""
        return answers


if __name__ == '__main__':
    teacher = Teacher()
    student_view, answers = teacher.create_full_test()
    print(student_view)
    print(answers)
