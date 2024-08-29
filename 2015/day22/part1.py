best = 1000000


def fight(turn, hp, mana, mana_spent, bhp, bd, shield_timer, poison_timer, recharge_timer):
    global best
    if best != 1000000 and mana_spent > best:
        return
    bhp -= 3 if poison_timer > 0 else 0
    poison_timer = max(0, poison_timer - 1)
    if bhp <= 0:
        best = min(best, mana_spent)
    else:
        armor = 7 if shield_timer > 0 else 0
        shield_timer = max(0, shield_timer - 1)
        mana += 101 if recharge_timer > 0 else 0
        recharge_timer = max(0, recharge_timer - 1)
        if turn == "Boss":
            damage = max(1, bd - armor)
            if hp - damage > 0:
                fight("Player", hp - damage, mana, mana_spent, bhp, bd, shield_timer, poison_timer, recharge_timer)
        else:
            for spell in ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]:
                if spell == "Magic Missile":
                    if mana >= 53:
                        if bhp - 4 <= 0:
                            best = min(best, mana_spent + 53)
                        else:
                            fight("Boss", hp, mana - 53, mana_spent + 53, bhp - 4, bd, shield_timer, poison_timer, recharge_timer)
                elif spell == "Drain":
                    if mana >= 73:
                        if bhp - 2 <= 0:
                            best = min(best, mana_spent + 73)
                        else:
                            fight("Boss", hp + 2, mana - 73, mana_spent + 73, bhp - 2, bd, shield_timer, poison_timer, recharge_timer)
                elif spell == "Shield":
                    if shield_timer == 0 and mana >= 113:
                        fight("Boss", hp, mana - 113, mana_spent + 113, bhp, bd, 6, poison_timer, recharge_timer)
                elif spell == "Poison":
                    if poison_timer == 0 and mana >= 173:
                        fight("Boss", hp, mana - 173, mana_spent + 173, bhp, bd, shield_timer, 6, recharge_timer)
                elif recharge_timer == 0 and mana >= 229:
                        fight("Boss", hp, mana - 229, mana_spent + 229, bhp, bd, shield_timer, poison_timer, 5)


bhp, bd = [int(l.split(': ')[1]) for l in open(0).read().splitlines()]
fight("Player", 50, 500, 0, bhp, bd, 0, 0, 0)
print(best)