import random
import time
import json
import os

list_pouvoir = ["1 - coup d'épée", "2 - lance de dague", "3 - boule de feu"]

lvl = 1
life = 100
monsterlife = 10
power = 0

nom = input("Entrez votre nom : ")
classe = input("Quelle est votre classe ? (Guerrier, Mage, Voleur) : ")

print(f"Bienvenue {nom}, le {classe} ! Vous commencez votre aventure avec {life} points de vie et {power} points de puissance et vous êtes niveau {lvl}")
time.sleep(1.5)

print("Attention ! Votre ennemi vous attaque !")
time.sleep(1.5)

while life > 0 and monsterlife > 0:
    degats = random.randint(5, 15)
    degatsmonstre = random.randint(5, 15)

    monsterlife = max(0, monsterlife - degats)

    if degats < 10 and monsterlife > 0:
        # Le monstre se moque et n'attaque pas
        print(f"Vous infligez {degats} dégâts... Le monstre se moque de vous et n'attaque pas !")
        degatsmonstre = 0
    else:
        life = max(0, life - degatsmonstre)
        print(f"Vous infligez {degats} dégâts. Le monstre en inflige {degatsmonstre}.")

    time.sleep(1)
    print(f"Il vous reste {life} PV, le monstre a {monsterlife} PV.")
    time.sleep(1.5)

if life <= 0 and monsterlife <= 0:
    print("Match nul... vous tombez tous les deux.")
elif monsterlife <= 0:
    lvl += 1
    print(f"Bravo vous avez vaincu le monstre ! Vous passez au niveau {lvl} !")
    print(f"Vous gagnez trois pouvoirs : {', '.join(list_pouvoir)}")

    time.sleep(2)

    print("Un golem apparait !!!")
    time.sleep(2)

    monsterlife = 50
    print("Vous repartez avec 100 PV !")
    life = 100

    # GOLEM
    while life > 0 and monsterlife > 0:

        pouvoirchoisi = input(f"Choisissez votre pouvoir (1, 2 ou 3) :\n{chr(10).join(list_pouvoir)}\n> ")

        # Les dégâts sont tirés à CHAQUE tour
        if pouvoirchoisi == "1":
            degats = random.randint(10, 14)
        elif pouvoirchoisi == "2":
            degats = random.randint(2, 22)
        elif pouvoirchoisi == "3":
            degats = random.choice([0, 20])
        else:
            print("Pouvoir invalide !")
            continue

        degatsmonstre = random.randint(5, 15)

        monsterlife = max(0, monsterlife - degats)
        life = max(0, life - degatsmonstre)

        print(f"Vous infligez {degats} dégâts. Le Golem en inflige {degatsmonstre}.")
        time.sleep(1)
        print(f"Il vous reste {life} PV, le Golem a {monsterlife} PV.")
        time.sleep(1.5)

    if life <= 0 and monsterlife <= 0:
        print("Match nul... vous et le Golem tombez ensemble.")
    elif monsterlife <= 0:
        lvl += 1
        print(f"Incroyable ! Vous avez détruit le Golem ! Vous passez au niveau {lvl} !")
    else:
        print("Le Golem vous a écrasé...")
else:
    print("Vous avez été vaincu par votre ennemi...")