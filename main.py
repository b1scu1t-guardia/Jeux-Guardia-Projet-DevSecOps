import random
import time

lvl = 1
life = 100
power = 50


def combat(nom_ennemi, ennemi_pv, degats_min, degats_max):
    """Lance un combat contre un ennemi. Retourne 'victoire', 'defaite' ou 'nul'."""
    global life
    monsterlife = ennemi_pv

    print(f"\nAttention ! {nom_ennemi} vous attaque !")
    time.sleep(1.5)

    while life > 0 and monsterlife > 0:
        degats = random.randint(5, 150)
        degatsmonstre = random.randint(degats_min, degats_max)

        monsterlife = max(0, monsterlife - degats)
        life = max(0, life - degatsmonstre)

        print(f"Vous infligez {degats} dégâts. {nom_ennemi} en inflige {degatsmonstre}.")
        time.sleep(1)
        print(f"Il vous reste {life} PV, {nom_ennemi} a {monsterlife} PV.")
        print("-" * 40)
        time.sleep(1.5)

    if life <= 0 and monsterlife <= 0:
        return "nul"
    elif monsterlife <= 0:
        return "victoire"
    else:
        return "defaite"


nom = input("Entrez votre nom : ")
classe = input("Quelle est votre classe ? (Guerrier, Mage, Voleur) : ")

print(f"Bienvenue {nom}, le {classe} ! Vous commencez votre aventure avec {life} points de vie et {power} points de puissance et vous êtes niveau {lvl}")
time.sleep(1.5)

# Combat 1 : le monstre
resultat = combat("Le monstre", 100, 5, 150)

if resultat == "victoire":
    lvl += 1
    print(f"\nBravo vous avez vaincu le monstre ! Vous passez au niveau {lvl} !")
    time.sleep(2)

    # Combat 2 : le golem
    print("\nLe sol tremble... un Golem de pierre surgit devant vous !")
    time.sleep(2)
    resultat = combat("Le Golem", 200, 5, 100)

    if resultat == "victoire":
        lvl += 1
        print(f"\nIncroyable ! Vous avez détruit le Golem ! Vous passez au niveau {lvl} !")
    elif resultat == "nul":
        print("\nMatch nul... vous et le Golem tombez ensemble.")
    else:
        print("\nLe Golem vous a écrasé...")
elif resultat == "nul":
    print("\nMatch nul... vous tombez tous les deux.")
else:
    print("\nVous avez été vaincu par votre ennemi...")