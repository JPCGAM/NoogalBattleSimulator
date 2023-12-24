import random

infdeaths = []
armyinfleftover = []

army1inf = int(input("How many infantry does army 1 have? "))
army2inf = int(input("How many infantry does army 2 have? "))
army1left = random.randint(0,army1inf)
army2left = random.randint(0,army2inf)
armyinfleftover.append(army1left)
armyinfleftover.append(army2left)
army1_infdeath = army1inf-army1left
army2_infdeath = army2inf-army2left
infvictory = max(armyinfleftover)
infvictoryteam = armyinfleftover.index(infvictory)+1
print(infvictoryteam,"won. Team 1 got",army1left,"infantry left and",army1_infdeath,"dead infantry. Team 2 got",army2left,"infantry left and",army2_infdeath,"dead infantry.")
