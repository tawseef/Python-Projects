import random

l = ["Rock", "Scissor", "Paper"]
while True:
    CompCount = 0
    UserCount = 0
    uc = int(input('''
        Press 1 to Start Game............
        Press 2 or more to  Exit...
        '''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''

            1. Rock
            2. Scissor
            3. Paper

            '''))

            if (userInput == 1 or userInput == 2 or userInput == 3):
                if userInput == 1:
                    uchoice = "Rock"
                elif userInput == 2:
                    uchoice = "Scissor"
                elif userInput == 3:
                    uchoice = "Paper"

                CompChoice = random.choice(l)

                if (CompChoice == uchoice):
                    print("GAME DRAW")
                    print("Computer Choose is ", CompChoice)
                    print("User Choose is ", uchoice)

                elif (uchoice == "Rock" and CompChoice == "Scissor") or (
                    uchoice == "Scissor" and CompChoice == "Paper") or (uchoice == "Paper" and CompChoice == "Rock"):
                    print("....................USER WIN....................")
                    print("Computer Choose is ", CompChoice)
                    print("User Choose is ", uchoice)
                    UserCount = UserCount + 1

                else:
                    print("....................COMPUTER WIN....................")
                    print("Computer Choose is ", CompChoice)
                    print("User Choose is ", uchoice)
                    CompCount = CompCount + 1


                if (UserCount == CompCount):
                    print("............FINAL GAME DRAW............")
                    print("Computer Win is ", CompCount)
                    print("User win is ", UserCount)
                elif (UserCount > CompCount):
                    print("............USER IS WINNER OF THE GAME............")
                    print("Computer Win is ", CompCount)
                    print("User Win is ", UserCount)
                else:
                    print("............COMPUTER IS WINNER OF THE GAME............")
                    print("Computer Win is ", CompCount)
                    print("User Win is ", UserCount)
            else:
                print("Invalid Input............................")
                uc = 0
                break;
    else:
        break;


