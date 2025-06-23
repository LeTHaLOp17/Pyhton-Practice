import random

'''
-1 = Rock
0 = Paper
1 = Scissor

'''
computer = random.choice([-1, 0, 1])
choiceDict = {'R' : -1, 'P' : 0, 'S' : 1}
reverseDict = {-1 : 'Rock', 0 : 'Paper', 1 : 'Scissor'}
youstr = input("Enter your choice (R for Rock, P for Paper, S for Scissor): ").upper()
if youstr not in choiceDict:
    print("Invalid input!")
    exit()

you = choiceDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1): 
        print("You Lose!")

    elif(computer == -1 and you == 0):
        print("You Win!")

    elif(computer == 1 and you == -1):
        print("You Win!")

    elif(computer == 1 and you == 0):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Lose!")

    elif(computer == 0 and you == 1):
        print("You Win!")

    else:
        print("Something went wrong!")