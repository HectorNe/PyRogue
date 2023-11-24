import random
import time

choose = input("quelle arme voulez vous ? (épée,hache,arc,dague) ")

Startweapon = {"épée" : {"dam" : 1.5, "critL" : 5, "critDam" : 1.3, "def" : 2}, "hache" : {"dam" : 2, "critL" : 3, "critDam" : 1.1},"arc" : {"dam" : 1.25, "critL" : 10, "critDam" : 1.2}, "dague" : {"dam" : 1, "critL" : 20, "critDam" : 1.3}}
player = {"gold" : 0, "atk" : 10, "def" : 2, "critL" : 10, "critDam" : 2, "health" : 100,"maxhealth" : 100, "endurance" : 10, "mana" : 50, "maxendurance" : 10}

weaponList = [[{"name" : "fire sword", "dam" : 1.5, "critL" : 5, "critDam" : 1.3, "feu" : 10}], [{"name" : "ice axe", "dam" : 2, "critL" : 3, "critDam" : 1.1, "taunt" : 10}],[{"name" : "explosive bow", "dam" : 1.25, "critL" : 10, "critDam" : 1.2}],[{"name" : "shadow dagger", "dam" : 1, "critL" : 20, "critDam" : 1.3, "esquive" : 10}]]

spells = {"feu" : {"zone" : True, "trueDam" : 20, "auto heal" : 0, "cost" : 15}, "zap" : {"zone" : False, "trueDam": 50, "auto heal" : 0, "cost" : 15}, "heal" : {"zone" : False, "trueDam": 0, "auto heal" : 20, "cost" : 25}}

activeWeapon = Startweapon[choose]

monsterList = [{"type" : "zombie", "atk" : 7, "def" : 1, "critL" : 10, "critDam" : 5, "health" : 100},{"type" : "squelette", "atk" : 5, "def" : 2, "critL" : 10, "critDam" : 1.5, "health" : 100},{"type" : "zombie ELITE !", "atk" : 15, "def" : 4, "critL" : 15, "critDam" : 3, "health" : 200},{"type" : "loup", "atk" : 10, "def" : 1, "critL" : 10, "critDam" : 2, "health" : 150}]

def fight(monster, player, activeWeapon,):
    while player["health"] > 0 and monster["health"] > 0:

        if "def" in activeWeapon:
            activeDef = player["def"] + activeWeapon["def"]
        else:
            activeDef = player["def"]
        action = input(
            "quelle action voulez vous executer ?\n(ne pas marquer 'attaque' avant le nom de l'action)\n(attaque simple,attaque puissante,attaque double,sort,défense) ")
        print("\n")

        if action == "simple":
            if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
            else:
                plAt = player["atk"] * activeWeapon["dam"]
            print("vous infligez à l'ennemi", round(plAt), "dégats !")
            monster["health"] -= round(plAt)
            if monster["health"] <= 0:
                print("vous avez vaincu !")
                break

        elif action == "puissante" and player["endurance"] >= 5:
            if player["endurance"] < 5:
                print("vous n'avez plus assez d'endurance")
                fight(monster,player,activeWeapon)
            if "arc" in activeWeapon:
                plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
            else:
                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                plAt = plAt * 2.5
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monster["health"] -= round(plAt)
                player["endurance"] -= 5
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break


        elif action == "double" and player["endurance"] >= 5:
            if player["endurance"] < 5:
                print("vous n'avez plus assez d'endurance")
                fight(monster,player,activeWeapon)
            if "arc" in activeWeapon:
                plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
            else:
                for atk in range(2):
                    if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        plAt = player["atk"] * activeWeapon["dam"]
                    print("vous infligez à l'ennemi", round(plAt), "dégats !")
                    monster["health"] -= round(plAt)
                player["endurance"] -= 5
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break


        elif action == "sort":
            launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
            print("\n")
            if player["mana"] < spells[launchSp]["cost"]:
                print("vous n'avez plus assez de mana")
                fight(monster,player,activeWeapon)
            monster["health"] -= spells[launchSp]["trueDam"]
            print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
            player["health"] += spells[launchSp]["auto heal"]
            if player["health"] > player["maxhealth"]:
                player["health"] = player["maxhealth"]
            player["mana"] -= spells[launchSp]["cost"]
            if monster["health"] <= 0:
                print("vous avez vaincu !")
                break

        elif action == "défense":
            activeDef = activeDef * 2
            player["health"] += 5
            if player["health"] > player["maxhealth"]:
                player["health"] = player["maxhealth"]
            player["endurance"] += 4
            if player["endurance"] > player["maxendurance"]:
                player["endurance"] = player["maxendurance"]
            player["mana"] += 10

        elif action != "défense" and action != "sort" and action != "double" and action != "puissante" and action != "simple":
            fight(monster,player,activeWeapon)

        if player["health"] <= 0:
            print("vous êtes mort...")
        if random.randint(0, 100) <= monster["critL"]:
            moAt = monster["atk"] * monster["critDam"]
        else:
            moAt = monster["atk"]

        if "esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]:
            print("esquive !")
            moAt = 0

        if round(moAt) < activeDef:
            moAt = 0
        else:
            moAt -= activeDef
        if "taunt" in activeWeapon:
            if random.randint(0,99) >= activeWeapon["taunt"]:
                print("l'ennemi vous inflige", round(moAt), "dégats !")
                player["health"] -= round(moAt)
        else:
            print("l'ennemi vous inflige", round(moAt), "dégats !")
            player["health"] -= round(moAt)

        print("votre vie :", player["health"], "-- vie du monstre 1 :", monster["health"])
        print("mana : ", player["mana"], "endurance : ", player["endurance"])
    if player["health"] > monster["health"]:
        addG = random.randint(0, 4)
        if addG == 0:
            armeR = weaponList[random.randint(0, len(weaponList) - 1)][0]
            print("vous trouvez ? une arme ! Vous gagnez", armeR["name"])
            activeWeapon = armeR
        else:
            addG = random.randint(0, 100)
            print("vous gagnez", addG, "gold")
            player["gold"] += addG
    else:
        print("vous êtes mort...")

"""
#en cours de développement
def fight2(monsterA,monsterB, player, activeWeapon,):
    while player["health"] > 0 and monsterA["health"] > 0 and monsterB["health"]:

        if "def" in activeWeapon:
            activeDef = player["def"] + activeWeapon["def"]
        else:
            activeDef = player["def"]
        action = input("quelle action voulez vous executer ?\n(ne pas marquer 'attaque' avant le nom de l'action)\n(attaque simple,attaque puissante,attaque double,sort,défense) ")
        print("\n")

        if action == "simple":
            vise = input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? ")
            if vise == 1 and monsterA["health"] >= 0:
                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monsterA["health"] -= round(plAt)

            elif vise == 2 and monsterB["health"] >= 0:
                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monsterB["health"] -= round(plAt)
            else:
                fight2(monsterA, monsterB, player, activeWeapon, )
            if monsterA["health"] <= 0 and monsterB["health"] <= 0:
                print("vous avez vaincu !")
                break

        elif action == "puissante" and player["endurance"] >= 5:
            vise = input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? ")
            if vise == 1 and monsterA["health"] >= 0:
                if player["endurance"] < 5:
                    print("vous n'avez plus assez d'endurance")
                    fight(monsterA,monsterB,player,activeWeapon)
                if "arc" in activeWeapon:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        plAt = player["atk"] * activeWeapon["dam"]
                    plAt = plAt * 2.5
                    print("vous infligez à l'ennemi", round(plAt), "dégats !")
                    monsterA["health"] -= round(plAt)
                    player["endurance"] -= 5

            elif vise == 2 and monsterB["health"] >= 0:
                if player["endurance"] < 5:
                    print("vous n'avez plus assez d'endurance")
                    fight2(monsterA,monsterB, player, activeWeapon)
                if "arc" in activeWeapon:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        plAt = player["atk"] * activeWeapon["dam"]
                    plAt = plAt * 2.5
                    print("vous infligez à l'ennemi", round(plAt), "dégats !")
                    monsterB["health"] -= round(plAt)
                    player["endurance"] -= 5
            else:
                if monsterB["health"] <= 0 and monsterA["health"] <= 0:
                    print("vous avez vaincu !")
                    break


        elif action == "double" and player["endurance"] >= 5:
            vise = input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? ")
            if vise == 1 and monsterA["health"] >= 0:
                if player["endurance"] < 5:
                    print("vous n'avez plus assez d'endurance")
                    fight(monster,player,activeWeapon)
                if "arc" in activeWeapon:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    for atk in range(2):
                        if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                            plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                        else:
                            plAt = player["atk"] * activeWeapon["dam"]
                        print("vous infligez à l'ennemi", round(plAt), "dégats !")
                        monster["health"] -= round(plAt)
                    player["endurance"] -= 5


                    if player["endurance"] < 5:
                        print("vous n'avez plus assez d'endurance")
                        fight(monster, player, activeWeapon)
                    if "arc" in activeWeapon:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        for atk in range(2):
                            if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                                plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon[
                                    "dam"]
                            else:
                                plAt = player["atk"] * activeWeapon["dam"]
                            print("vous infligez à l'ennemi", round(plAt), "dégats !")
                            monster["health"] -= round(plAt)
                        player["endurance"] -= 5
                    
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break


        elif action == "sort":
            launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
            print("\n")
            if player["mana"] < spells[launchSp]["cost"]:
                print("vous n'avez plus assez de mana")
                fight(monster,player,activeWeapon)
            monster["health"] -= spells[launchSp]["trueDam"]
            print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
            player["health"] += spells[launchSp]["auto heal"]
            if player["health"] > player["maxhealth"]:
                player["health"] = player["maxhealth"]
            player["mana"] -= spells[launchSp]["cost"]
            if monster["health"] <= 0:
                print("vous avez vaincu !")
                break

        elif action == "défense":
            activeDef = activeDef * 2
            player["health"] += 5
            if player["health"] > player["maxhealth"]:
                player["health"] = player["maxhealth"]
            player["endurance"] += 4
            if player["endurance"] > player["maxendurance"]:
                player["endurance"] = player["maxendurance"]
            player["mana"] += 10


        if player["health"] <= 0:
            print("vous êtes mort...")
        if random.randint(0, 100) <= monster["critL"]:
            moAt = monster["atk"] * monster["critDam"]
        else:
            moAt = monster["atk"]

        if "esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]:
            print("esquive !")
            moAt = 0

        if round(moAt) < activeDef:
            moAt = 0
        else:
            moAt -= activeDef
        if "taunt" in activeWeapon:
            if random.randint(0,99) >= activeWeapon["taunt"]:
                print("l'ennemi vous inflige", round(moAt), "dégats !")
                player["health"] -= round(moAt)
        else:
            print("l'ennemi vous inflige", round(moAt), "dégats !")
            player["health"] -= round(moAt)

        print("votre vie :", player["health"], "-- vie du monstre 1 :", monster["health"])
        print("mana : ", player["mana"], "endurance : ", player["endurance"])
    if player["health"] > monster["health"]:
        addG = random.randint(0, 4)
        if addG == 0:
            armeR = weaponList[random.randint(0, len(weaponList) - 1)][0]
            print("vous trouvez ? une arme ! Vous gagnez", armeR["name"])
            activeWeapon = armeR
        else:
            addG = random.randint(0, 100)
            print("vous gagnez", addG, "gold")
            player["gold"] += addG
    else:
        print("vous êtes mort...")"""
####################################################################

for c in range(10):

    eventP = random.randint(0,9)

    monsterList = [{"type": "zombie", "atk": 7, "def": 1, "critL": 10, "critDam": 5, "health": 100},
                   {"type": "squelette", "atk": 5, "def": 2, "critL": 10, "critDam": 1.5, "health": 100},
                   {"type": "zombie ELITE !", "atk": 15, "def": 4, "critL": 15, "critDam": 3, "health": 200},
                   {"type": "loup", "atk": 10, "def": 1, "critL": 10, "critDam": 2, "health": 150}]

    if eventP <= 5:
        event = "M"
    elif 5 < eventP <=7:
        event = "C"
    else:
        event = "S"

    if event == "M":
        """
        monsterSpe = random.randint(0,10)
        if monsterSpe == 0:
            monsterA = monsterList[random.randint(0, 3)]
            monsterB = monsterList[random.randint(0, 3)]
            print("quoi ?!",monsterA,"et",monsterB,"vous attaque")
            fight2(monsterA,monsterB, player, activeWeapon)

        else:"""
        monsterE = monsterList[random.randint(0, 3)]
        print("un", monsterE["type"], "vous attaque")
        fight(monsterE,player,activeWeapon)

        """print("un", monster["type"], "vous attaque")

        while player["health"] > 0 and monster["health"] > 0:

            if "def" in activeWeapon:
                activeDef = player["def"] + activeWeapon["def"]
            else:
                activeDef = player["def"]
            action = input("quelle action voulez vous executer ?\n(ne pas marquer 'attaque' avant le nom de l'action)\n(attaque simple,attaque puissante,attaque double,sort,défense) ")
            print("\n")


            if action == "simple":
                if random.randint(0,100) <= player["critL"]+activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monster["health"] -= round(plAt)
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break

            elif action == "puissante" and player["endurance"] >= 5:
                if "arc" in activeWeapon:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    if random.randint(0,100) <= player["critL"]+activeWeapon["critL"]:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        plAt = player["atk"] * activeWeapon["dam"]
                    plAt = plAt * 2.5
                    print("vous infligez à l'ennemi", round(plAt), "dégats !")
                    monster["health"] -= round(plAt)
                    player["endurance"] -= 5
                    if monster["health"] <= 0:
                        print("vous avez vaincu !")
                        break


            elif action == "double" and player["endurance"] >= 5:
                if "arc" in activeWeapon:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    for atk in range(2):
                        if random.randint(0,100) <= player["critL"]+activeWeapon["critL"]:
                            plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                        else:
                            plAt = player["atk"] * activeWeapon["dam"]
                        print("vous infligez à l'ennemi", round(plAt), "dégats !")
                        monster["health"] -= round(plAt)
                    player["endurance"] -= 5
                    if monster["health"] <= 0:
                        print("vous avez vaincu !")
                        break


            elif action == "sort":
                launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
                print("\n")
                monster["health"] -= spells[launchSp]["trueDam"]
                print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                player["health"] += spells[launchSp]["auto heal"]
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
                player["mana"] -= spells[launchSp]["cost"]
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break

            elif action == "défense":
                activeDef = activeDef * 2
                player["health"] += 5
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
                player["endurance"] += 4
                if player["endurance"] > player["maxendurance"]:
                    player["endurance"] = player["maxendurance"]
                player["mana"] += 10

            elif player["health"] <= 0:
                print("vous êtes mort...")
            if random.randint(0,100) <= monster["critL"]:
                moAt = monster["atk"] * monster["critDam"]
            else:
                moAt = monster["atk"]

            if "esquive" in activeWeapon and random.randint(0,100) <= activeWeapon["esquive"]:
                print("esquive !")
                moAt = 0

            if round(moAt) < activeDef:
                moAt = 0
            else:
                moAt -= activeDef
            print("l'ennemi vous inflige", round(moAt), "dégats !")
            player["health"] -= round(moAt)

            print("votre vie :", player["health"],"-- vie du monstre 1 :", monster["health"])
            print("mana : ", player["mana"], "endurance : ", player["endurance"])
        if player["health"] > monster["health"]:
            addG = random.randint(0,4)
            if addG == 0:
                armeR = weaponList[random.randint(0, len(weaponList) - 1)][0]
                print("vous trouvez ? une arme ! Vous gagnez", armeR["name"])
                activeWeapon = armeR
            else:
                addG = random.randint(0,100)
                print("vous gagnez", addG)
                player["gold"] += addG
        else:
            print("vous êtes mort...")"""

    if event == "C":
        print("salle de trésor !")
        addG = random.randint(20,100)
        print("vous gagnez",addG,"gold")
        player["gold"] += addG
        if random.randint(0,10) <= 2:
            print("")

    if event == "S":
        achat = 0
        while achat != "stop":
            print("vous entrez dans le magasin :")
            print("vous avez", player["gold"], "gold")
            print("vie : 25 G : V")
            print("augmentation vie : 50 G : V+")
            print("augmentation endurance : 75 G : E+")
            print("arme aléatoire : 50 G : R")
            armeR = weaponList[random.randint(0,len(weaponList)-1)][0]
            print("arme :",armeR["name"], "100 G : A")
            print("tapez stop pour sortir")
            achat = input("que voulez vous acheter")
            if achat == "A" and player["gold"] >= 100:
                activeWeapon = armeR
                player["gold"] -= 100
            elif achat == "V" and player["gold"] >= 25:
                player["health"] += 25
                player["gold"] -= 25
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
            elif achat == "V+" and player["gold"] >= 50:
                player["maxhealth"] += 5
                player["gold"] -= 50
            elif achat == "E+" and player["gold"] >= 50:
                player["maxendurance"] += 2.5
                player["gold"] -= 50
            elif achat == "R" and player["gold"] >= 50:
                activeWeapon = weaponList[random.randint(0, len(weaponList) - 1)][0]
                player["gold"] -= 50
            elif achat == "stop":
                break
            else:
                print("vous n'avez pas assez d'argent")
    input("tapez entrez pour continuer")
    print("\n\n")