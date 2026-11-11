import random
import time
import json
import os

list_pouvoir = ["1 - coup d'épée", "2 - lance de dague", "3 - boule de feu"]
inventaire = ["Potion de vie", "Potion de mana", "Piece d'or"]

lvl = 1
life = 100
monsterlife = 10
power = 0
inventairesize = 6

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

#INVENTAIRE

print(f"Vous avez débloqué votre inventaire !! le voici: {inventaire} la taille de votre inventaire est de {inventairesize} objets maximum.")
boire = input("Voulez-vous boire une potion de vie ou de mana ? (vie/mana) : ")
if boire == "vie":
    if "Potion de vie" in inventaire:
        life += 50
        inventaire.remove("Potion de vie")
        print(f"Vous avez bu une potion de vie ! Il vous reste {life} PV.")
    else:
        print("Vous n'avez pas de potion de vie dans votre inventaire.")
elif boire == "mana":
    if "Potion de mana" in inventaire:
        life += 30
        inventaire.remove("Potion de mana")
        print(f"Vous avez bu une potion de mana ! Il vous reste {life} PV.")
    else:
        print("Vous n'avez pas de potion de mana dans votre inventaire.")

#COFFRE
time.sleep(1.5)
print("Vous trouvez un coffre !")
time.sleep(1.5)
print("Le jeu est simple, 3 chances, si vous trouvez le bon nombre entre 1 et 10, vous gagnez une epee magique ! si vous trouvez pas je vous prend votre piece d'or !")
numerocoffre = random.randint(1, 10)
chance = 3
numerojoueur = input("Entrez un nombre entre 1 et 10 : ")
if numerojoueur == numerocoffre:
    print("Félicitations ! Vous avez trouvé le bon nombre et gagné une épée magique !")
    inventaire.append("Épée magique")
else:
    chance -= 1
    print(f"Dommage ! Il vous reste {chance} chance(s).")
    while chance > 0:
        numerojoueur = input("Entrez un nombre entre 1 et 10 : ")
        if numerojoueur == numerocoffre:
            print("Félicitations ! Vous avez trouvé le bon nombre et gagné une épée magique !")
            inventaire.append("Épée magique")
            break
        else:
            chance -= 1
            print(f"Dommage ! Il vous reste {chance} chance(s).")
    if chance == 0:
        print("Vous n'avez pas trouvé le bon nombre... Vous perdez votre pièce d'or.")
        inventaire.remove("Piece d'or")
        print (f"Votre inventaire actuel : {inventaire}")

print("Vous continuez l'aventure !")
time.sleep(1.5)
print("Vous arrivez devant un danjon ! \n Vous devez passez 3 salles !")
print("Un squelette arrive !")

#SQUELETTE
monsterlife = 30
if life > 0 and monsterlife > 0:
    while life > 0 and monsterlife > 0:
        degats = random.randint(5, 15)
        degatsmonstre = random.randint(5, 15)

        monsterlife = max(0, monsterlife - degats)
        life = max(0, life - degatsmonstre)

        print(f"Vous infligez {degats} dégâts. Le squelette en inflige {degatsmonstre}.")
        time.sleep(1)
        print(f"Il vous reste {life} PV, le squelette a {monsterlife} PV.")
        time.sleep(1.5)

    if life <= 0 and monsterlife <= 0:
        print("Match nul... vous et le squelette tombez ensemble.")
    elif monsterlife <= 0:
        lvl += 1
        print(f"Bravo ! Vous avez vaincu le squelette ! Vous passez au niveau {lvl} !")
    else:
        print("Le squelette vous a vaincu...")

code = random.randint(100, 999)
print(f"Vous devez trou{code[0]}vez le code d'u{code[1]}ne porte pour pa{code[3]}sser à la salle suivante !")
codejoueur = input("Entrez un code à 3 chiffres : ")
if codejoueur == str(code):
    print("Félicitations ! Vous avez trouvé le bon code et passez à la salle suivante !")
else:
    print(f"Dommage ! Le bon code était {code}. Vous ne pouvez pas passer à la salle suivante.")


#GOLEM FINAL
if life > 0 and codejoueur == str(code):
    print("\nLa porte s'ouvre... Le Golem final vous attend !!!")
    time.sleep(2)

    monsterlife = 80
    epee_utilisee = False

    while life > 0 and monsterlife > 0:
        print(f"\nVos PV : {life} | PV du Golem : {monsterlife}")
        print("Que voulez-vous faire ?")
        print("1 - Attaquer avec un pouvoir")
        print("2 - Voir mon inventaire")
        print("3 - Utiliser l'épée magique")
        print("4 - Me soigner")
        choix = input("> ")

        action_faite = False  # le Golem n'attaque que si vous avez fait une action
        degats = 0

        if choix == "1":
            pouvoirchoisi = input(f"Choisissez votre pouvoir :\n{chr(10).join(list_pouvoir)}\n> ")
            if pouvoirchoisi == "1":
                degats = random.randint(10, 14)
            elif pouvoirchoisi == "2":
                degats = random.randint(2, 22)
            elif pouvoirchoisi == "3":
                degats = random.choice([0, 20])
            else:
                print("Pouvoir invalide !")
                continue
            print(f"Vous infligez {degats} dégâts au Golem !")
            action_faite = True

        elif choix == "2":
            print(f"Votre inventaire : {inventaire}")
            continue  # voir l'inventaire ne coûte pas de tour

        elif choix == "3":
            if "Épée magique" in inventaire and not epee_utilisee:
                degats = random.randint(25, 35)
                epee_utilisee = True
                print(f"Vous brandissez l'épée magique ! Elle inflige {degats} dégâts !")
                action_faite = True
            elif epee_utilisee:
                print("L'épée magique s'est brisée après son utilisation...")
                continue
            else:
                print("Vous n'avez pas d'épée magique !")
                continue

        elif choix == "4":
            soin = input("Quelle potion ? (vie/mana) : ")
            if soin == "vie" and "Potion de vie" in inventaire:
                life += 50
                inventaire.remove("Potion de vie")
                print(f"Vous buvez une potion de vie ! Vous avez maintenant {life} PV.")
                action_faite = True
            elif soin == "mana" and "Potion de mana" in inventaire:
                life += 30
                inventaire.remove("Potion de mana")
                print(f"Vous buvez une potion de mana ! Vous avez maintenant {life} PV.")
                action_faite = True
            else:
                print("Vous n'avez pas cette potion !")
                continue

        else:
            print("Choix invalide !")
            continue

        if action_faite:
            monsterlife = max(0, monsterlife - degats)
            if monsterlife > 0:
                degatsmonstre = random.randint(8, 18)
                life = max(0, life - degatsmonstre)
                print(f"Le Golem vous frappe et inflige {degatsmonstre} dégâts !")
            time.sleep(1.5)

    if life <= 0 and monsterlife <= 0:
        print("Match nul... vous et le Golem final tombez ensemble.")
    elif monsterlife <= 0:
        lvl += 1
        print(f"VICTOIRE ! Vous avez détruit le Golem final ! Vous avez gagbné le jeu et passez au niveau {lvl} ! Félicitations, {nom} le {classe} !")
    else:
        print("Le Golem final vous a écrasé... GAME OVER")

