import random

infdeaths = []
armyinfleftover = []

army1inf = int(input("How many infantry does army 1 have? "))
army2inf = int(input("How many infantry does army 2 have? "))
if army1inf >= army2inf:
    probbigger1 = round((army1inf-army2inf)/army1inf,0)
    choice1 = random.random()
    if choice1 > probbigger1:
        army1_infdeath = random.randint(army2inf-round(army2inf/2,0),army1inf)
    elif choice1 <= probbigger1:
        army1_infdeath = random.randint(0,army2inf)
    infdeaths.append(army1_infdeath)
    army2_infdeath = random.randint(0,army2inf)
    infdeaths.append(army2_infdeath)
    army1infleft = army1inf-army1_infdeath
    army2infleft = army2inf-army2_infdeath
    armyinfleftover.append(army1infleft)
    armyinfleftover.append(army2infleft)

elif army2inf > army1inf:
    probbigger2 = round((army2inf-army1inf)/army2inf,0)
    choice2 = random.random()
    army1_infdeath = random.randint(0,army1inf)
    infdeaths.append(army1_infdeath)
    if choice2 > probbigger2:
        army2_infdeath = random.randint(army1inf-round(army1inf/2,0),army2inf)
    elif choice2 <= probbigger2:
        army2_infdeath = random.randint(0,army1inf)
    infdeaths.append(army2_infdeath)
    army1infleft = army1inf-army1_infdeath
    army2infleft = army2inf-army2_infdeath
    armyinfleftover.append(army1infleft)
    armyinfleftover.append(army2infleft)
infvictory = max(armyinfleftover)
infvictoryteam = armyinfleftover.index(infvictory)+1
print(infvictoryteam,"won. Team 1 got",army1infleft,"infantry left and",army1_infdeath,"dead infantry. Team 2 got",army2infleft,"infantry left and",army2_infdeath,"dead infantry.")
