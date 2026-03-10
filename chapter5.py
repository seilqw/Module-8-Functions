# Seil Tekinaeva
# 03/10/2026
# Milestone 3 - Chapter 5 Module
# Final score, ending, and menu choice

def chapter5(score):
    menu_choice = "0"

    print("----- Chapter 5 -----")
    print("Shift ends. Final score is shown.")

    if score >= 7:
        ending = "Excellent ending"
        print("\nEnding:", ending)
        print("You handled the shift very well.")

    elif score >= 4:
        ending = "Normal ending"
        print("\nEnding:", ending)
        print("You finished the shift with mixed results.")

    else:
        ending = "Rough ending"
        print("\nEnding:", ending)
        print("The shift ended with a difficult outcome.")

    while menu_choice not in ["1", "2"]:
        print("\nChoose an option:")
        print("1. View ending / Exit game")
        print("2. Game over")

        menu_choice = input("Enter menu choice (1 or 2): ")

        if menu_choice not in ["1", "2"]:
            print("Invalid choice")

    if menu_choice == "1":
        print("\nDisplay final score and ending")
        print("Final score:", score)
        print("Final ending:", ending)

    else:
        print("\nGame over")
