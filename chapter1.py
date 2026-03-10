# Seil Tekinaeva
# 03/10/2026
# Milestone 3 - Chapter 1 Module
# Patient choice after car accident

def chapter1():
    score = 0
    patient_choice = ""

    print("Three patients waiting")
    print("1. Car accident victim")
    print("2. Broken arm")
    print("3. Minor cut")

    while patient_choice not in ["1", "2", "3"]:
        patient_choice = input("Enter patient choice (1, 2, or 3): ")

        if patient_choice not in ["1", "2", "3"]:
            print("Invalid choice")

    if patient_choice == "1":
        score = score + 2
        patient = "car accident victim"

    elif patient_choice == "2":
        score = score + 1
        patient = "broken arm"

    else:
        score = score + 0
        patient = "minor cut"

    print("You chose patient:", patient)
    print("Score updated:", score)

    return score

