import random

infdeaths = []
armyinfleftover = []
army1_inf_pick_list = []
army2_inf_pick_list = []
Army1InfLeft = 0
Army1InfDead = 0
Army1InfWounded = 0
Army2InfLeft = 0
Army2InfDead = 0
Army2InfWounded = 0
###### terrain: soft attack, defence, hard attack
plains = [1,1,1]
hills = [0.85,1.1,0.75]
mountains = [0.6,1.6,0.3]
river = [0.8,1.2,0.95]
forest = [0.95, 1.1, 0.5]
jungle = [0.7,1.2,0.4]
urban = [1.2,1.4,0.9]
desert = [1,0.8,1]
terrain_chosen = []
########
army1_inf_regroup = 0
army1_inf_flee = 0
army1_inf_POW = 0
army2_inf_regroup = 0 
army2_inf_flee = 0
army2_inf_POW = 0
#soft attack, hp, hard attack, armour
infBaseDefenceStats = [0.7, 2.5, 0.1,0]
infBaseAttackStats = [0.35, 1, 0.05,0]
artHowBaseStats = [25,0,0.5,0]
medTankBaseStats = [12,0,5,2]
#after battle: regroup, flee, POW
after_battle_infantry_choice = ["regroup","flee","POW"]
infAfterAttSuccessStats = [0.99, 0.01, 0.0] #if succesful
infAfterAttFailStats = [0.45, 0.3, 0.25]
infAfterDefSuccessStats = [0.9, 0.1, 0.0] #if succesful
infAfterDefFailStats = [0.25, 0.35, 0.4]
# wounded and death
infCassualtyOutcomes = ["wounded","died"]
infAttackCassualtiesStats = [0.25, 0.75]
infDefenceCassualtiesStats = [0.67,0.33]
army1_inf_wounded = 0
army1_inf_died = 0
army2_inf_wounded = 0
army2_inf_died = 0
###############
terrain_type = input("What type of terrain is this being done at. Options: plains, hills, mountains, river, forest, jungle, urban, desert. ")
if terrain_type =="plains":
    terrain_chosen = plains
elif terrain_type == "hills":
    terrain_chosen = hills
elif terrain_type == "mountains":
    terrain_chosen = mountains
elif terrain_type == "river":
    terrain_chosen = river
elif terrain_type == "forest":
    terrain_chosen = forest
elif terrain_type == "jungle":
    terrain_chosen = jungle
elif terrain_type == "urban":
    terrain_chosen = urban
elif terrain_type == "desert":
    terrain_chosen = desert
##############
army1inf = int(input("How many infantry does army 1 have? "))
army1_artHow = int(input("How many artillery (howitzer) does army 1 have? "))
army1_medTank = int(input("How many medium tanks does army 1 have? "))
army1Tacktic = input("What is army 1 doing: attack or defend? ")
army1_moralle = float(input("What is the moralle like for army 1 in general? 0 is none and 1 is the normal amount, with 2 being hyper: "))
army1_training = float(input("What is the AVERAGE amount of training army 1 has? 0 is NONE, 1 is standard and 2 is battle hardened: "))
army1_supply = float(input("How supplied is army 1 in AVERAGE? 0 means NOTHING at all, and 1 means all they could need: "))
if army1Tacktic == "attack":
    army1_used_stats_tactic = infBaseAttackStats
elif army1Tacktic == "defend":
    army1_used_stats_tactic = infBaseDefenceStats
army2inf = int(input("How many infantry does army 2 have? "))
army2_artHow = int(input("How many artillery (howitzer) does army 2 have? "))
army2_medTank = int(input("How many medium tanks does army 2 have? "))
army2Tacktic = input("What is army 2 doing: attack or defend? ")
army2_moralle = float(input("What is the moralle like for army 2 in general? 0 is none and 1 is the normal amount, with 2 being hyper: "))
army2_training = float(input("What is the AVERAGE amount of training army 2 has? 0 is NONE, 1 is standard and 2 is battle hardened: "))
army2_supply = float(input("How supplied is army 2 in AVERAGE? 0 means NOTHING at all, and 1 means all they could need: "))
if army2Tacktic == "attack":
    army2_used_stats_tactic = infBaseAttackStats
elif army2Tacktic == "defend":
    army2_used_stats_tactic = infBaseDefenceStats
###############################
if army1Tacktic == "attack":
    army1_soft_attack = round((army1inf*army1_used_stats_tactic[0]*random.uniform(0.8,1.2)+artHowBaseStats[0]*army1_artHow+army1_medTank*medTankBaseStats[0])*terrain_chosen[0]*army1_moralle*army1_training*army1_supply,3)
    army1_hp = round((army1_used_stats_tactic[1]*army1inf*random.uniform(0.8,1.2))*army1_moralle*army1_training*army1_supply,3)
    army1_hard_attack = round((army1_used_stats_tactic[2]*army1inf*random.uniform(0.8,1.2)+artHowBaseStats[2]*army1_artHow+army1_medTank*medTankBaseStats[2])*terrain_chosen[2]*army1_moralle*army1_training*army1_supply,3)
    army1_armour = 1+round(army1_medTank*medTankBaseStats[3]*army1_moralle*army1_training*army1_supply,2)
elif army1Tacktic == "defend":
    army1_soft_attack = round((army1inf*army1_used_stats_tactic[0]*random.uniform(0.8,1.2)+artHowBaseStats[0]*army1_artHow+army1_medTank*medTankBaseStats[0])*army1_moralle*army1_training*army1_supply,3)
    army1_hp = round((army1_used_stats_tactic[1]*army1inf*random.uniform(0.8,1.2))*terrain_chosen[1]*army1_moralle*army1_training*army1_supply,3)
    army1_hard_attack = round((army1_used_stats_tactic[2]*army1inf*random.uniform(0.8,1.2)+artHowBaseStats[2]*army1_artHow+army1_medTank*medTankBaseStats[2])*army1_moralle*army1_training*army1_supply,3)
    army1_armour = 1+round(army1_medTank*medTankBaseStats[3]*army1_moralle*army1_training*army1_supply,2)

if army2Tacktic == "attack":
    army2_soft_attack = round((army2inf*army2_used_stats_tactic[0]*random.uniform(0.8,1.2)+artHowBaseStats[0]*army2_artHow+army2_medTank*medTankBaseStats[0])*terrain_chosen[0]*army2_moralle*army2_training*army2_supply,3)
    army2_hp = round(army2_used_stats_tactic[1]*army2inf*random.uniform(0.8,1.2)*army2_moralle*army2_training*army2_supply,3)
    army2_hard_attack = round((army2_used_stats_tactic[2]*army2inf*random.uniform(0.8,1.2)+artHowBaseStats[2]*army2_artHow+army2_medTank*medTankBaseStats[2])*terrain_chosen[2]*army2_moralle*army2_training*army2_supply,3)
    army2_armour = 1+round(army2_medTank*medTankBaseStats[3]*army2_moralle*army2_training*army2_supply,2)
elif army2Tacktic == "defend":
    army2_soft_attack = round((army2inf*army2_used_stats_tactic[0]*random.uniform(0.8,1.2)+artHowBaseStats[0]*army2_artHow+army2_medTank*medTankBaseStats[0])*army2_moralle*army2_training*army2_supply,3)
    army2_hp = round((army2_used_stats_tactic[1]*army2inf*random.uniform(0.8,1.2))*terrain_chosen[1]*army2_moralle*army2_training*army2_supply,3)
    army2_hard_attack = round((army2_used_stats_tactic[2]*army2inf*random.uniform(0.8,1.2)+artHowBaseStats[2]*army2_artHow+army2_medTank*medTankBaseStats[2])*army2_moralle*army2_training*army2_supply,3)
    army2_armour = 1+round(army2_medTank*medTankBaseStats[3]*army2_moralle*army2_training*army2_supply,2)

#print(army1_soft_attack, army1_hp, army1_hard_attack)
#print(army2_soft_attack, army2_hp, army2_hard_attack)

print()
#A1C
if army1_armour > army2_hard_attack:
    army1_left_hp = army1_hp- (army2_soft_attack/army1_armour)
    print("Army 1's tanks survived.")
elif army1_armour < army2_hard_attack:
    army1_tank_destroyed_div = army1_armour/army2_hard_attack
    army1_left_hp = army1_hp- (army2_soft_attack/(army1_armour*army1_tank_destroyed_div))
    army1_tank_destroyed = round(army1_medTank*army1_tank_destroyed_div*random.random(),0)
    army1_tank_damaged = round((army1_medTank*army1_tank_destroyed_div) - army1_tank_destroyed,0)
    print(f"{army1_tank_destroyed} of Army's 1 tanks were destroyed and {army1_tank_damaged} were damaged. The rest survived.")

if army1_left_hp > army1_hp:
    army1_left_hp = army1_hp

army1_left_inf = int(round(army1_left_hp/army1_used_stats_tactic[1],0))
if army1_left_hp < 0:
    army1_left_hp = 0
if army1_left_inf < 0:
    army1_left_inf = 0
if army1_left_inf > army1inf:
    army1_left_inf = army1inf


if army2_armour > army1_hard_attack:
    army2_left_hp = army2_hp- (army1_soft_attack/army2_armour)
    print("Army 2's tanks survived.")
elif army2_armour < army1_hard_attack:
    army2_tank_destroyed_div = army2_armour/army1_hard_attack
    army2_left_hp = army2_hp- (army1_soft_attack/(army2_armour*army2_tank_destroyed_div))
    army2_tank_destroyed = round(army2_medTank*army2_tank_destroyed_div*random.random(),0)
    army2_tank_damaged = round((army2_medTank*army2_tank_destroyed_div) - army2_tank_destroyed,0)
    print(f"{army2_tank_destroyed} of Army's 2 tanks were destroyed and {army2_tank_damaged} were damaged. The rest survived.")

if army2_left_hp > army2_hp:
    army2_left_hp = army2_hp

army2_left_inf = int(round(army2_left_hp/army2_used_stats_tactic[1],0))
if army2_left_hp < 0:
    army2_left_hp = 0
if army2_left_inf < 0:
    army2_left_inf = 0
if army2_left_inf > army2inf:
    army2_left_inf = army2inf
print(f"Army 1 has {army1_left_inf} remaining infantry. Army 2 has {army2_left_inf} remaining infantry.")
###### now for death and wounded
army1_inf_death = army1inf-army1_left_inf
if army1Tacktic == "attack":
    army1_death_outcome_list = infAttackCassualtiesStats
if army1Tacktic == "defend":
    army1_death_outcome_list = infDefenceCassualtiesStats
army1_inf_death_counter = 0
for army1_inf_death_counter in range(army1_inf_death):
    army1_inf_death_choice = random.choices(infCassualtyOutcomes,army1_death_outcome_list)[0]
    if army1_inf_death_choice == "wounded":
        army1_inf_wounded = army1_inf_wounded +1
    elif army1_inf_death_choice == "died":
        army1_inf_died= army1_inf_died +1
print(f"Total of {army1_inf_death} army 1 infantry cassualties. {army1_inf_wounded} infantry were wounded and {army1_inf_died} were killed.")

army2_inf_death = army2inf-army2_left_inf
if army2Tacktic == "attack":
    army2_death_outcome_list = infAttackCassualtiesStats
if army2Tacktic == "defend":
    army2_death_outcome_list = infDefenceCassualtiesStats
army2_inf_death_counter = 0
for army2_inf_death_counter in range(army2_inf_death):
    army2_inf_death_choice = random.choices(infCassualtyOutcomes,army2_death_outcome_list)[0]
    if army2_inf_death_choice == "wounded":
        army2_inf_wounded = army2_inf_wounded +1
    elif army2_inf_death_choice == "died":
        army2_inf_died= army2_inf_died +1
print(f"Total of {army2_inf_death} army 2 infantry cassualties. {army2_inf_wounded} infantry were wounded and {army2_inf_died} were killed.")

#compare the two, and then somehow decide who wins and then use the after battle thingies
if army1_left_inf/army1inf > army2_left_inf/army2inf:
    print("Army 1 wins.")
    if army1Tacktic == "attack":
        army1_inf_pick_list = (infAfterAttSuccessStats)
    elif army1Tacktic == "defend":
        army1_inf_pick_list =(infAfterDefSuccessStats)
    for army1winattack in range(army1_left_inf):
        army1_inf_choice = random.choices(after_battle_infantry_choice,army1_inf_pick_list)[0]
        if army1_inf_choice == "regroup":
            army1_inf_regroup = army1_inf_regroup +1
        elif army1_inf_choice == "flee":
            army1_inf_flee = army1_inf_flee +1
        elif army1_inf_choice == "POW":
            army1_inf_POW = army1_inf_POW +1 
    #army2
    if army2Tacktic == "attack":
        army2_inf_pick_list =infAfterAttFailStats
    elif army2Tacktic == "defend":
        army2_inf_pick_list = infAfterDefFailStats
    for army2winattack in range(army2_left_inf):
        army2_inf_choice = random.choices(after_battle_infantry_choice,army2_inf_pick_list)[0]
        if army2_inf_choice == "regroup":
            army2_inf_regroup = army2_inf_regroup +1
        elif army2_inf_choice == "flee":
            army2_inf_flee = army2_inf_flee +1
        elif army2_inf_choice == "POW":
            army2_inf_POW = army2_inf_POW +1
    print(f"{army1_inf_flee} infantry from army 1 fled, while {army1_inf_regroup} regrouped and {army1_inf_POW} were taken as POWs.")
    print(f"{army2_inf_flee} infantry from army 2 fled, while {army2_inf_regroup} regrouped and {army2_inf_POW} were taken as POWs.")
elif army2_left_inf/army2inf > army1_left_inf/army1inf:
    print("Army 2 wins.")
    if army1Tacktic == "attack":
        army1_inf_pick_list =infAfterAttFailStats
    elif army1Tacktic == "defend":
        army1_inf_pick_list =  infAfterDefFailStats
    for army1winattack in range(army1_left_inf):
        army1_inf_choice = random.choices(after_battle_infantry_choice,army1_inf_pick_list)[0]
        if army1_inf_choice == "regroup":
            army1_inf_regroup = army1_inf_regroup +1
        elif army1_inf_choice == "flee":
            army1_inf_flee = army1_inf_flee +1
        elif army1_inf_choice == "POW":
            army1_inf_POW = army1_inf_POW +1
    #army2
    if army2Tacktic == "attack":
        army2_inf_pick_list =  infAfterAttSuccessStats
    elif army2Tacktic == "defend":
        army2_inf_pick_list =  infAfterDefSuccessStats
    for army2winattack in range(army2_left_inf):
        army2_inf_choice = random.choices(after_battle_infantry_choice,army2_inf_pick_list)[0]
        if army2_inf_choice == "regroup":
            army2_inf_regroup = army2_inf_regroup +1
        elif army2_inf_choice == "flee":
            army2_inf_flee = army2_inf_flee +1
        elif army2_inf_choice == "POW":
            army2_inf_POW = army2_inf_POW +1
    print(f"{army1_inf_flee} infantry from army 1 fled, while {army1_inf_regroup} regrouped and {army1_inf_POW} were taken as POWs.")
    print(f"{army2_inf_flee} infantry from army 2 fled, while {army2_inf_regroup} regrouped and {army2_inf_POW} were taken as POWs.")
elif  army2_left_inf == army1_left_inf:
    print("No clear winner, both armies were most likely destroyed.")
    if army1_inf_wounded > army2_inf_wounded:
        print(f"Army 1 achieved a pyrrhic victory, having {army1_inf_wounded} wounded vs {army2_inf_wounded} of army 2.")
    if army2_inf_wounded > army1_inf_wounded:
        print(f"Army 2 achieved a pyrrhic victory, having {army2_inf_wounded} wounded vs {army1_inf_wounded} of army 1.")