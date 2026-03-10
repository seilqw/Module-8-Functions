# Seil Tekinaeva
# 03/10/2026
# Milestone 3 - Chapter 3 Module
# Choose actions before treatment

def chapter3(score):
    actions_done = 0
    max_actions = 2

    print("----- Chapter 3 -----")
    print("Choose actions before treatment.")

    while actions_done < max_actions:
        print("\nChoose an action:")
        print("1. Prepare tools")
        print("2. Review chart")
        print("3. Call nurse")

        action_choice = input("Enter action choice (1, 2, or 3): ")

        if action_choice == "1":
            score = score + 2
            actions_done = actions_done + 1
            print("Tools prepared.")

        elif action_choice == "2":
            score = score + 1
            actions_done = actions_done + 1
            print("Patient chart reviewed.")

        elif action_choice == "3":
            score = score + 1
            actions_done = actions_done + 1
            print("Nurse assists preparation.")

        else:
            print("Invalid choice")

    print("\nMaximum actions reached")
    print("Evaluate score")
    print("Current score:", score)

    return score
