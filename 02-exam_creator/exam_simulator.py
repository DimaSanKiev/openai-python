import datetime


class Exam:
    def __init__(self, student_view, answers, store_test=False, topic=""):
        self.student_view = student_view
        self.answers = answers

        if store_test:
            self.store_test(topic)

    def take(self):
        answers = {}
        for question, question_view in self.student_view.items():
            print(question_view)
            answer = input("Enter your answer: ")
            answers[question] = answer
        return answers

    def grade(self, answers):
        correct_answers = 0
        for question, answer in answers.items():
            if answer.upper() == self.answers[question].upper()[16]:
                correct_answers += 1
        grade = 100 * correct_answers / len(answers)
        rounded_grade = round(grade)

        passed = "Passed" if rounded_grade >= 60 else "Not passed"
        return f"{correct_answers} out of {len(answers)} correct! You achieved: {rounded_grade}% : {passed}!"

    def store_test(self, topic):
        with open(f'tests_log/Test_{topic}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt', "w") as file:
            for question, question_view in self.student_view.items():
                file.write(question_view)
                file.write("\n")
                file.write(self.answers[question])
                file.write("\n")
