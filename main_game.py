# Seil Tekinaeva
# 03/10/2026
# Milestone 3 - Main Game File

import chapter1
import chapter2
import chapter3
import chapter4
import chapter5


def main():
    score = 0

    print("====================================")
    print(" Hospital Night Shift Adventure Game ")
    print("====================================")

    score = chapter1.chapter1()
    score = chapter2.chapter2(score)
    score = chapter3.chapter3(score)
    score = chapter4.chapter4(score)
    chapter5.chapter5(score)


if __name__ == "__main__":
    main()
    
