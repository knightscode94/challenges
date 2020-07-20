import dice

def dicethrow():
    dice1=dice.dice()
    dice2=dice.dice()
    dices=dice1,dice2
    return dices

def d2():
    return "Dice1: " + str(dice.dice()) + "\n"+"Dice2: " + str(dice.dice())

print("dice throw: ",dicethrow())
print("\n")
print(d2())