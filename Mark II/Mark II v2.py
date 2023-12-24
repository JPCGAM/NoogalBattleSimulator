import random

infdeaths = []
armyinfleftover = []
Army1InfLeft = 0
Army1InfDead = 0
Army2InfLeft = 0
Army2InfDead = 0
#survive, die, wounded
infOutcomes = ["survive","die"]
infDefenceStats = [0.7, 0.3]
infAttackStats = [0.5,0.5]

army1inf = int(input("How many infantry does army 1 have? "))
army1Tacktic = input("What is army 1 doing: attack or defend? ")
army2inf = int(input("How many infantry does army 2 have? "))
army2Tacktic = input("What is army 2 doing: attack or defend? ")
#army 1 choosing
army1InfChoose = 0
for army1InfChoose in range(int(army1inf)):
    if army1Tacktic == "attack":
        A1InfOutcome = random.choices(infOutcomes,infAttackStats)[0]
    elif army1Tacktic == "defend":
        A1InfOutcome = random.choices(infOutcomes,infDefenceStats)[0]
    if A1InfOutcome == "survive":
        Army1InfLeft = Army1InfLeft +1
    elif A1InfOutcome == "die":
        Army1InfDead = Army1InfDead +1
#army 2 choosing
army2InfChoose = 0
for army2InfChoose in range(int(army2inf)):
    if army2Tacktic == "attack":
        A2InfOutcome = random.choices(infOutcomes,infAttackStats)[0]
    elif army2Tacktic == "defend":
        A2InfOutcome = random.choices(infOutcomes,infDefenceStats)[0]
    if A2InfOutcome == "survive":
        Army2InfLeft = Army2InfLeft +1
    elif A2InfOutcome == "die":
        Army2InfDead = Army2InfDead +1
armyinfleftover.append(Army1InfLeft)
armyinfleftover.append(Army2InfLeft)
infvictory = max(armyinfleftover)
infvictoryteam = armyinfleftover.index(infvictory)+1
print("Team",infvictoryteam,"won. Team 1 got",Army1InfLeft,"infantry left and",Army1InfDead,"dead infantry. Team 2 got",Army2InfLeft,"infantry left and",Army2InfDead,"dead infantry.")
