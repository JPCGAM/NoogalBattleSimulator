import random

infdeaths = []
armyinfleftover = []
Army1InfLeft = 0
Army1InfDead = 0
Army1InfWounded = 0
Army2InfLeft = 0
Army2InfDead = 0
Army2InfWounded = 0
#soft attack, defend, hard attack
##infOutcomes = ["survive","die","wounded"]
infBaseDefenceStats = [1.5, 2.5, 0.5]
infBaseAttackStats = [1.25, 1, 0.25]

army1inf = int(input("How many infantry does army 1 have? "))
army1Tacktic = input("What is army 1 doing: attack or defend? ")
if army1Tacktic == "attack":
    army1_used_stats_tactic = infBaseAttackStats
elif army1Tacktic == "defend":
    army1_used_stats_tactic = infBaseDefenceStats
army2inf = int(input("How many infantry does army 2 have? "))
army2Tacktic = input("What is army 2 doing: attack or defend? ")
if army2Tacktic == "attack":
    army2_used_stats_tactic = infBaseAttackStats
elif army2Tacktic == "defend":
    army2_used_stats_tactic = infBaseDefenceStats
###############################
army1_soft_attack = army1inf*army1_used_stats_tactic[0]
army1_hp = army1_used_stats_tactic[1]*army1inf
army1_hard_attack = army1_used_stats_tactic[2]*army1inf

army2_soft_attack = army2inf*army2_used_stats_tactic[0]
army2_hp = army2_used_stats_tactic[1]*army2inf
army2_hard_attack = army2_used_stats_tactic[2]*army2inf

print(army1_soft_attack, army1_hp, army1_hard_attack)
print(army2_soft_attack, army2_hp, army2_hard_attack)


#army 1 choosing
army1_left_hp = army1_hp - army2_soft_attack
army1_left_inf = int(round(army1_left_hp/army1_used_stats_tactic[1],0))
army2_left_hp = army2_hp - army1_soft_attack
army2_left_inf = int(round(army2_left_hp/army2_used_stats_tactic[1],0))
print(f"Army 1 has remaining {army1_left_hp} HP and {army1_left_inf} remaining infantry. Army 2 has remaining {army2_left_hp} HP and {army2_left_inf} remaining infantry. ")
