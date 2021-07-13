import random
import time

# Name input. Possibly add list or dict to keep name for later on. A high score list for each difficulty and time
NameEntry = input("Welcome to Math Challenge 2021\n\nEnter your name please:\n")
print("Hello" + " " + NameEntry + "!\n")


def Question():
    # Main menu
    print("\nEquation Types:\n\nAddition(1)\nSubtraction(2)\nMultiplication(3)\nDivision(4)\nQuit(5)")
    # Entry selections
    entry = input("Please make a selection: ")
    if entry == "1":
        entry = "+"
    elif entry == "2":
        entry = "-"
    elif entry == "3":
        entry = "*"
    elif entry == "4":
        entry = "//"
    elif entry == "5":
        # Quit option
        Quit = input("Quit?\n (y/n): ")
        if Quit == "y":
            print("Thanks for playing!")
            quit()
        else:
            return Question()
    else:
        print("\nInvalid Selection!\n")
        return Question()

    # Difficulty level menu. Numbers increase by power of level selected
    level = input("\nDifficulty:\n\n(1)Beginner\n(10 Questions, numbers 1-10)\n\n"
                  "(2)Intermediate\n(20 Questions number 1-100)\n\n(3)Advanced\n"
                  "(30 Questions, number 1-1000)\n\n(B)Back\nPlease make your selection: ")
    if level == "1":
        int(level)
    elif level == "2":
        int(level)
    elif level == "3":
        int(level)
    elif level == "B":
        Question()
    else:
        print("\nInvalid Selection!\n")
        return level

    # counter for keep score at the end of the set of questions
    counter = 0
    # Number of questions to the power of the difficulty level
    questions = 10 * int(level)
    # Start of timer. Is always active during game but might like to make it optional
    start_time = time.perf_counter()

    # Equation for loop. Determines the bigger of the two and places it on the top of the equation.
    # If the user selects division the int changes to 1 out of (numbers) to avoid ZeroDivisionError.
    for i in range(questions):
        if entry == "//":
            minRange = 1
        else:
            minRange = 0
        x = random.randint(minRange, 10 ** int(level))
        y = random.randint(minRange, 10 ** int(level))
        maxXY = max(x, y)
        minXY = min(x, y)

        # Format does not quite line up with all fo the equations sets i.e.
        #  x         x
        # +Y  may be +y because of the digit change from single to double and so on.
        eq = (" {} \n"
        "{}{} = ".format(maxXY, entry, minXY))
        answer = eval(str(maxXY) + entry + str(minXY))
        if str(input(eq)) == str(answer):
            print("\nCorrect!\n")
            counter = counter + 1
        else:
            print("\nIncorrect!\n\nThe correct answer is" + " " + str(answer) + "." + "\n")
    print(NameEntry + " your score is" + " " + str(counter) + " " + "out of" + " " + str(questions) + "!")
    end_time = time.perf_counter()
    print("\nand your time was" + " " + str(time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))) + "!")
    return


while True:
    Question()
# First fully functional game. Some minor issues need to be worked out
# to add in the high score/ best time board if desired or optional timer.
