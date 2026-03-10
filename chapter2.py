# Seil Tekinaeva
# 03/10/2026
# Milestone 3 - Chapter 2 Module
# Ask up to 2 questions before treatment

def chapter2(score):
    questions_asked = 0
    max_questions = 2

    print("----- Chapter 2 -----")
    print("You may ask two questions before treatment.")

    while questions_asked < max_questions:
        print("\nChoose a question:")
        print("1. Ask about pain")
        print("2. Ask how injury happened")
        print("3. Check allergies")

        q_choice = input("Enter question choice (1, 2, or 3): ")

        if q_choice == "1":
            score = score + 1
            questions_asked = questions_asked + 1
            print("Patient describes severe pain.")

        elif q_choice == "2":
            score = score + 2
            questions_asked = questions_asked + 1
            print("Patient describes how injury happened.")

        elif q_choice == "3":
            score = score + 0
            questions_asked = questions_asked + 1
            print("Allergy information recorded.")

        else:
            print("Invalid choice")

    print("\nMaximum questions reached")
    print("Evaluate score")
    print("Current score:", score)

    return score
