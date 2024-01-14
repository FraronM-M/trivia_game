import random


def start_game():
    print("Welcome to the trivia game")
    print("Choose one of the following topics: ")
    print("Overwatch or Boxing")
    initial_choice()


def initial_choice():
    choice = input("Enter choice here: ")
    if choice.lower() == "overwatch":
        Overwatch_Trivia()

    elif choice.lower() == "boxing":
        Boxing_Trivia()

    else:
        print("Choose either Overwatch or Boxing")
        initial_choice()
        

def Overwatch_Trivia():
    questions = [
        ("What is the name of the character who says 'Cheers, love! The cavalry's here!'?", "tracer"),
        ("What is the real name of the character known as 'Reaper'?", "gabriel reyes")

    ]
    random.shuffle(questions)
    run_trivia(questions)


def Boxing_Trivia():
    questions = [

        ("Who is known for the phrase float like a butterlfy sting like a bee", "Muhammad Ali")

    ]
    random.shuffle(questions)
    run_trivia(questions)


def run_trivia(questions):
    score = 0
    total_num_questions = len(questions)
    for question, answer in questions:
        user_answer = input(f"\nQuestion: {question}\nYour answer: ").lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The right answer is {answer}.")

    print(f"\nYour score: {score}/{total_num_questions}")
    play_again()


def play_again():
    answer = input("Would you like to play again, Answer Yes or No: ")
    if answer.lower() == "yes":
        print()
        start_game()
    elif answer.lower() == "no":
        quit()
    else:
        print("Answer Yes or No")
        play_again()


start_game()
