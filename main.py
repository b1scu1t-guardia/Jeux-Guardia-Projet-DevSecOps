import random

lvl = 1
life = 100
monsterlife = 100
power = 50

nom = input("Entrez votre nom : ")
classe = input("Quelle est votre classe ? (Guerrier, Mage, Voleur) : ")

print(f"Bienvenue {nom}, le {classe} ! Vous commencez votre aventure avec {life} points de vie et {power} points de puissance et vous êtes niveau {lvl}")

print("Attention ! Votre ennemi vous attaque !")

while life > 0 and monsterlife > 0:
    degats = random.randint(5, 150)       
    degatsmonstre = random.randint(5, 150)   

    monsterlife = max(0, monsterlife - degats)
    life = max(0, life - degatsmonstre)

    print(f"Vous infligez {degats} dégâts. Le monstre en inflige {degatsmonstre}.")
    print(f"Il vous reste {life} PV, le monstre a {monsterlife} PV.")

if life <= 0 and monsterlife <= 0:
    print("Match nul... vous tombez tous les deux.")
elif monsterlife <= 0:
    lvl += 1
    print(f"Bravo vous avez vaincu le monstre ! Vous passez au niveau {lvl} !.")
else:
    print("Vous avez été vaincu par votre ennemi...")