import dice

def dicethrow():
    dice1=dice.dice()
    dice2=dice.dice()
    dices=dice1,dice2
    return dices

print("dice throw: ",dicethrow())