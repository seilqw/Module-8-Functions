# Seil Tekinaeva
# 03/10/2026
# Milestone 3 - Chapter 4 Module
# Respond to a complication during treatment

def chapter4(score):
    responses_done = 0
    max_responses = 2

    print("----- Chapter 4 -----")
    print("A complication happens. Choose your response.")

    while responses_done < max_responses:
        print("\nChoose a response:")
        print("1. Stop bleeding")
        print("2. Call senior surgeon")
        print("3. Wait too long")

        choice = input("Enter choice (1, 2, or 3): ")

        if choice == "1":
            score = score + 2
            responses_done = responses_done + 1
            print("Bleeding controlled.")

        elif choice == "2":
            score = score + 1
            responses_done = responses_done + 1
            print("Senior surgeon helps stabilize patient.")

        elif choice == "3":
            score = score - 1
            responses_done = responses_done + 1
            print("Delay worsens the complication.")

        else:
            print("Invalid choice")

    print("\nComplication phase complete.")
    print("Current score:", score)

    return score
