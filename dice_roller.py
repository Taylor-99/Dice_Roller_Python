import random

numDiceRoll = input("How many dice would you like to roll? \n")
print("\n")

numDiceRoll = int(numDiceRoll)

diceRoll = 0

while (diceRoll < numDiceRoll) :

    dieNum = random.randint(1,6)

    if dieNum == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if dieNum == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if dieNum == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if dieNum == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if dieNum == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if dieNum == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

    print("\n")

    diceRoll = diceRoll + 1