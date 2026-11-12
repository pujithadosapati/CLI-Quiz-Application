import json
import random
quiz_data = [
    {"question": "What is the full form of CPU?",
     "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit", "Control Processing Unit"],
     "answer": "A"},

    {"question": "Which language is used for Python programming?",
     "options": ["HTML", "Python", "CSS", "SQL"],
     "answer": "B"},

    {"question": "Which symbol is used for comments in Python?",
     "options": ["//", "#", "/*", "&"],
     "answer": "B"},

    {"question": "Which data type stores True or False?",
     "options": ["String", "Integer", "Boolean", "Float"],
     "answer": "C"},

    {"question": "Which keyword defines a function?",
     "options": ["function", "def", "fun", "define"],
     "answer": "B"},

    {"question": "Which function displays output?",
     "options": ["input()", "print()", "display()", "show()"],
     "answer": "B"},

    {"question": "Which data structure uses key-value pairs?",
     "options": ["List", "Tuple", "Dictionary", "Set"],
     "answer": "C"},

    {"question": "Which loop iterates over a sequence?",
     "options": ["if", "for", "switch", "break"],
     "answer": "B"},

    {"question": "Which operator is used for multiplication?",
     "options": ["+", "-", "*", "/"],
     "answer": "C"},

    {"question": "Which module generates random values?",
     "options": ["math", "random", "time", "os"],
     "answer": "B"}
]

# Convert Python data into JSON and load it
questions = json.loads(json.dumps(quiz_data))

random.shuffle(questions)

def start_quiz():
    score = 0
    total = len(questions)

    print("=" * 40)
    print("       WELCOME TO PYTHON QUIZ")
    print("=" * 40)

    name = input("Enter your name: ").strip()

    if not name:
        name = "Student"

    for i, q in enumerate(questions, 1):
        print("\nQuestion", i, "of", total)
        print(q["question"])

        for j, option in enumerate(q["options"]):
            print(chr(65 + j) + ".", option)

        while True:
            answer = input("Enter A/B/C/D: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input! Try again.")

        if answer == q["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", q["answer"])

    percentage = (score / total) * 100

    print("\n" + "=" * 40)
    print("          FINAL QUIZ RESULT")
    print("=" * 40)
    print("Name:", name)
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print("Final Score:", score, "/", total)
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 50:
        print("Performance: Good!")
    else:
        print("Performance: Keep Practicing!")

    print("=" * 40)
    print("Thank you for participating!")

start_quiz()
