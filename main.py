import random
import time

list_pouvoir = ["coup d'épée", "lance de dague", "boule de feu"]

lvl = 1
life = 100
monsterlife = 10
power = 0

degatssepee = random.randint(10, 14)
degatslance = random.randint(2, 22)
degatsbouledefeu = random.randint(0, 20)


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
    print(f"Vous gagnez trois pouvoir ! {list_pouvoir} ")

    time.sleep(2)

    print("Un golem apparait !!! !")
    time.sleep(2)

    monsterlife = 50
    print("Vous repartez avec 100 PV !")
    life = 100

    #GOLEME

    while life > 0 and monsterlife > 0:

        pouvoirchoisi = input(f"Choisissez votre pouvoir : {list_pouvoir} : ")
        if pouvoirchoisi == "coup d'épée":
            degats = degatssepee
        elif pouvoirchoisi == "lance de dague":
            degats = degatslance
        elif pouvoirchoisi == "boule de feu":
            degats = degatsbouledefeu
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
