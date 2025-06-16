import random

'''
-1 = Rock
0 = Paper
1 = Scissor

'''
computer = random.choice([-1, 0, 1])
choiceDict = {'R' : -1, 'P' : 0, 'S' : 1}
revDict = {-1 : 'Rock', 0 : 'Paper', 1 : 'Scissor'}
youstr = input("Enter your choice (R for Rock, P for Paper, S for Scissor): ").upper()
if youstr not in choiceDict:
    print("Invalid input!")
    exit()

you = choiceDict[youstr]