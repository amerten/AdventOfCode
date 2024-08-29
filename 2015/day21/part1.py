from itertools import permutations

def fight(players, output=False):
    """
    :return: the index of the winner (0=player, 1=boss).
    """
    names = ["player", "boss"]
    pi = 0
    while True:
        opi = (pi + 1) % 2
        dmg = players[pi][1]
        armor = players[opi][2]
        real_dmg = max(1, dmg - armor)
        players[opi][0] -= real_dmg
        if output:
            print("The " + names[pi] + " deals " + str(dmg) + "-" + str(armor) + " = " + str(real_dmg) + " damage; the " + names[opi] + " goes down to " + str(players[opi][0]) + " hit points.")
        if players[opi][0] <= 0:
            return pi
        pi = opi

# Cost, Damage, Armor
weapons = {"Dagger": (8, 4),
           "Shortsword": (10, 5),
           "Warhammer": (25, 6),
           "Longsword": (40, 7),
           "Greataxe": (74, 8)}
armors = {"Cloth": (0, 0),
          "Leather": (13, 1),
          "Chainmail": (31, 2),
          "Splintmail": (53, 3),
          "Bandedmail": (75, 4),
          "Platemail": (102, 5)}
rings = {"Damage +1": (25, 1, 0),
         "Damage +2": (50, 2, 0),
         "Damage +3": (100, 3, 0),
         "Armor +1": (20, 0, 1),
         "Armor +2": (40, 0, 2),
         "Armor +3": (80, 0, 3)}

PRINT = False

bhp, bd, ba = [int(l.split(': ')[1]) for l in open(0).read().splitlines()]
best = (400, None)
for weapon in weapons:
    w_cost, w_dmg = weapons[weapon]
    for armor in armors:
        a_cost, a_arm = armors[armor]
        for nb_rings in range(3):
            for equipped_rings in permutations(rings, nb_rings):
                r_cost, r_dmg, r_arm = 0, 0, 0
                for ring in equipped_rings:
                    r_cost += rings[ring][0]
                    r_dmg += rings[ring][1]
                    r_arm += rings[ring][2]
                full_cost, full_dmg, full_arm = w_cost + a_cost + r_cost, w_dmg + r_dmg, a_arm + r_arm
                winner = fight([[100, full_dmg, full_arm], [bhp, bd, ba]], PRINT)
                if winner == 0 and full_cost < best[0]:
                    best = (full_cost, [weapon] + [armor] + list(equipped_rings))

print(best)