import random

infdeaths = []
armyinfleftover = []
Army1InfLeft = 0
Army1InfDead = 0
Army1InfWounded = 0
Army2InfLeft = 0
Army2InfDead = 0
Army2InfWounded = 0
#survive, die, wounded
infOutcomes = ["survive","die","wounded"]
infDefenceStats = [0.65,0.2,0.15]
infAttackStats = [0.35,0.5,0.15]

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
    elif A1InfOutcome == "wounded":
        Army1InfWounded = Army1InfWounded +1
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
    elif A2InfOutcome == "wounded":
        Army2InfWounded = Army2InfWounded +1
armyinfleftover.append(Army1InfLeft)
armyinfleftover.append(Army2InfLeft)
infvictory = max(armyinfleftover)
infdefeat = min(armyinfleftover)
inflooser = armyinfleftover.index(infdefeat)
armies_left_looser  = int(armyinfleftover[inflooser])
infvictoryteam = armyinfleftover.index(infvictory)+1
looserfled = random.randint(0,armies_left_looser)
loosercaptured = armies_left_looser-looserfled
print(f"Team {infvictoryteam} won. Team 1 got {Army1InfLeft} infantry left, {Army1InfWounded} wounded infantry and {Army1InfDead} dead infantry. Team 2 got {Army2InfLeft} infantry left, {Army2InfWounded} wounded infantry and {Army2InfDead} dead infantry.")
print(f"The loosing team had {loosercaptured} infantry captured and {looserfled} infantry fled.")
