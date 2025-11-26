import random
import time

while True:
    difficulty = input("\nChoose your difficulty: Easy (e) ; Medium (m) ; Hard (h): ").lower()
    total_time = 0
    wrong_answers = 0
    total_guess = 0
    if difficulty == "e":
        said_difficulty = "easy"
        OPERATORS = ["+" , "-"]
        MIN_INT = 1
        MAX_INT = 30
        NUMBER_OF_OPERATION = 1
        break

    elif difficulty == "m":
        said_difficulty = "medium"
        OPERATORS = ["+", "-", "*"]
        MIN_INT = 2
        MAX_INT = 10
        NUMBER_OF_OPERATION = 2
        break

    elif difficulty == "h":
        said_difficulty = "hard"
        OPERATORS = ["+", "-", "*"]
        MIN_INT = 2
        MAX_INT = 20
        NUMBER_OF_OPERATION = 3
        break
    
    else:
        print("Invalid input.")

while True:
    number_of_question = input("Choose the number of question: ")
    if number_of_question.isdigit():
        number_of_question = int(number_of_question)
        if number_of_question > 0:
            print("You chose to have %d question(s). Get Ready! " %number_of_question)
            time.sleep(2)
            for i in range(3):
                print(3-i)
                time.sleep(1)
            print("Go!")
            break
    print("Invalid input. Must provid a number of 1 or higher.")

for _ in range(number_of_question):
    operations = []
    for i in range(NUMBER_OF_OPERATION):
        operations.append(OPERATORS[random.randrange(0,len(OPERATORS))])

    variables = []
    for i in range(NUMBER_OF_OPERATION + 1):
        variables.append(random.randint(MIN_INT, MAX_INT))

    string_operation = str(variables[0])
    for i in range(len(operations)):
        string_operation += str(operations[i]) + str(variables[i+1])

    result = str(eval(string_operation))

    time_start = time.time()
    while True:
        total_guess += 1
        print("Question:", string_operation, "= ", end="")
        answer = input("")
        if answer == result:
            time_end = time.time()
            total_time += time_end - time_start
            break
        else:
            print("Wrong answer, try again.")
            wrong_answers += 1

print("Congrats on completing this challenge! You've answered a total of %d questions in %.4f seconds on %s difficulty!\n(You made %d errors. Accuracy: %.1f pts)" %(number_of_question, total_time, said_difficulty, wrong_answers, ((total_guess - wrong_answers) / total_guess * 100)))