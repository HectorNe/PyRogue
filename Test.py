import random
import time

choose = input("quelle arme voulez vous ? (épée,hache,arc,dague) ")


#définir les armes de départ et le joueur
Startweapon = {"épée" : {"dam" : 1.5, "critL" : 5, "critDam" : 1.3, "def" : 2}, "hache" : {"dam" : 2, "critL" : 3, "critDam" : 1.1},"arc" : {"dam" : 1.25, "critL" : 10, "critDam" : 1.2}, "dague" : {"dam" : 1, "critL" : 20, "critDam" : 1.3}}
player = {"gold" : 0, "atk" : 10, "def" : 2, "critL" : 10, "critDam" : 2, "health" : 100,"maxhealth" : 100, "endurance" : 10, "mana" : 50, "maxendurance" : 10, "maxmana" : 50}

#définir la liste des armes disponible dans le jeu (trié par type d'arme, puis chaque arme dans un dictionnaire)
weaponList = [[{"name" : "fire sword", "dam" : 1.5, "critL" : 5, "critDam" : 1.3, "feu" : 10}], [{"name" : "ice axe", "dam" : 2, "critL" : 3, "critDam" : 1.1, "taunt" : 10}],[{"name" : "shadow dagger", "dam" : 1, "critL" : 20, "critDam" : 1.3, "esquive" : 10}]]#,[{"name" : "explosive bow", "dam" : 1.25, "critL" : 10, "critDam" : 1.2, "explode" : True}]

#définir la liste des sorts
spells = {"feu" : {"zone" : True, "trueDam" : 20, "auto heal" : 0, "cost" : 15}, "zap" : {"zone" : False, "trueDam": 50, "auto heal" : 0, "cost" : 15}, "heal" : {"zone" : False, "trueDam": 0, "auto heal" : 20, "cost" : 25}}

#équiper l'arme choisi par le joueur
activeWeapon = Startweapon[choose]

#définir la liste des monstres pouvant apparaitre
monsterList = [{"type" : "zombie", "atk" : 7, "def" : 1, "critL" : 10, "critDam" : 5, "health" : 100},{"type" : "squelette", "atk" : 5, "def" : 2, "critL" : 10, "critDam" : 1.5, "health" : 100},{"type" : "zombie ELITE !", "atk" : 15, "def" : 4, "critL" : 15, "critDam" : 3, "health" : 200},{"type" : "loup", "atk" : 10, "def" : 1, "critL" : 10, "critDam" : 2, "health" : 150}]

#définition d'une fonction simulant un combat entre un monstre (1ère variable), le joueur (2ème variable), l'arme équippé, est également renseigné
def fight(monster, player, activeWeapon,):

    #lancer une boucle ne se stoppant que si un des deux opposants meurs
    while player["health"] > 0 and monster["health"] > 0:

        #appliquer les bonus de défense de son arme et les reset
        if "def" in activeWeapon:
            activeDef = player["def"] + activeWeapon["def"]
        else:
            activeDef = player["def"]

        #demander au joueur l'action voulant etre executé
        action = input("quelle action voulez vous executer ?\n(ne pas marquer 'attaque' avant le nom de l'action)\n(attaque simple,attaque puissante,attaque double,sort,défense) ")
        print("\n")

#//////////////////////////////////////////////////////////////////////////
        #action attaque simple
        if action == "simple":
            #tester si il y a coup critique et appliquer si oui
            if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
            else:
                #attaque sans coup critique + calcul des dégats
                plAt = player["atk"] * activeWeapon["dam"]
            #affichage des dégats et appliquation
            print("vous infligez à l'ennemi", round(plAt), "dégats !")
            monster["health"] -= round(plAt)
            #tester si le monstre à été tué suite à l'action
            if monster["health"] <= 0:
                print("vous avez vaincu !")
                break

#//////////////////////////////////////////////////////////////////////////

        # action attaque puissante (attaque infligeant 2.5 fois plus de dégats)
        elif action == "puissante":
            #tester si le joueur à assez d'endurance pour lancer l'attaque, si non cela relance le tour
            if player["endurance"] < 5:
                print("vous n'avez plus assez d'endurance")
                fight(monster,player,activeWeapon)
            #tester si l'arme et un arc, qui coute moins d'endurance (simulé en rajoutant de l'endurance)
            if "arc" in activeWeapon:
                player["endurance"] += 1
            else:
                # tester si il y a coup critique et appliquer si oui
                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                #appliquer le bonus de dégat
                plAt = plAt * 2.5
                #afficher les dégats et les appliquer
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monster["health"] -= round(plAt)
                player["endurance"] -= 5
                #tester si le monstre est mort
            if monster["health"] <= 0:
                print("vous avez vaincu !")
                break


        # action attaque double (attaque 2 fois en 1 tour)
        elif action == "double":
            #tester si le joueur à assez d'endurance pour lancer l'attaque, si non cela relance le tour
            #j'ai vraiment besoin de détailler, les trucs identiques ?
            if player["endurance"] < 5:
                print("vous n'avez plus assez d'endurance")
                fight(monster,player,activeWeapon)
            if "arc" in activeWeapon:
                player["endurance"] += 1
            else:
                #lancer 2 fois l'action d'attaque simple
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


        #quand on lance un sort (ils infligent des truedamage, qui esquivent le bouclier)
        elif action == "sort":
            #choix du sort
            launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
            print("\n")
            #tester si le joueur à encore assez de mana
            if player["mana"] < spells[launchSp]["cost"]:
                print("vous n'avez plus assez de mana")
                fight(monster,player,activeWeapon)
            #appliquer les dégats du sort et afficher
            monster["health"] -= spells[launchSp]["trueDam"]
            print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
            #appliquer les heals du sort
            player["health"] += spells[launchSp]["auto heal"]
            if player["health"] > player["maxhealth"]:
                player["health"] = player["maxhealth"]
            #consommer le mana
            player["mana"] -= spells[launchSp]["cost"]
            if monster["health"] <= 0:
                print("vous avez vaincu !")
                break

        #acion de défense qui regenère des stats et augmente temporairement la défense
        elif action == "défense":
            #augmentation défense
            activeDef = activeDef * 2
            #soin et limitation au max
            player["health"] += 5
            if player["health"] > player["maxhealth"]:
                player["health"] = player["maxhealth"]
            #regeneration de l'endurance et limitation au max
            player["endurance"] += 4
            if player["endurance"] > player["maxendurance"]:
                player["endurance"] = player["maxendurance"]
            #regeneration de mana et limitation au max
            player["mana"] += 10
            if player["mana"] > player["maxmana"]:
                player["mana"] = player["maxmana"]

        #si il y a une faute de frappe (= pas d'action)
        elif action != "défense" and action != "sort" and action != "double" and action != "puissante" and action != "simple":
            fight(monster,player,activeWeapon)

        #appliquer les dégats de feu de l'arme fire sword
        if action != "sort" and "feu" in activeWeapon:
            print("le feu inflige 5 dégat à l'adversaire")
            monster["health"] -= 5

        #tester si le joueur est mort
        if player["health"] <= 0:
            print("vous êtes mort...")
            input("\ntapez entrer pour terminer")
            break
        #tester si il y a un coup critique de la part du monstre
        if random.randint(0, 100) <= monster["critL"]:
            moAt = monster["atk"] * monster["critDam"]
        else:
            moAt = monster["atk"]

        #tester si le joueur esquive (avec la shadow dagger)
        if "esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]:
            print("esquive !")
            moAt = 0

        #appliquer la réduction des dégats par la défense
        if round(moAt) < activeDef:
            moAt = 0
        else:
            moAt -= activeDef

        #appliquer le pouvoir taunt de la ice axe
        if "taunt" in activeWeapon:
            if random.randint(0,99) >= activeWeapon["taunt"]:
                print("l'ennemi vous inflige", round(moAt), "dégats !")
                player["health"] -= round(moAt)
        else:
            print("l'ennemi vous inflige", round(moAt), "dégats !")
            player["health"] -= round(moAt)

        #affichage de fin de tour (vie,stat,etc)
        print("votre vie :", player["health"], "-- vie du monstre 1 :", monster["health"])
        print("mana : ", player["mana"], "endurance : ", player["endurance"])

    #lors de la fin du combat donner des récompenses
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
        input("\ntapez entrer pour terminer")

#////////////////////////////////////////////////////////////////
#en cours de développement (combat contre 2 monstres)
def fight2(monsterA,monsterB, player, activeWeapon,):
    while player["health"] > 0 and monsterA["health"] > 0 and monsterB["health"]:

        if "def" in activeWeapon:
            activeDef = player["def"] + activeWeapon["def"]
        else:
            activeDef = player["def"]
        action = input("quelle action voulez vous executer ?\n(ne pas marquer 'attaque' avant le nom de l'action)\n(attaque simple,attaque puissante,attaque double,sort,défense) ")
        print("\n")

        if action == "simple":
            #tester puis appliquer des dégats explosif (de zone)
            if "explode" in activeWeapon:

                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monsterA["health"] -= round(plAt)

                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monsterB["health"] -= round(plAt)

            #viser l'ennemi puis attaquer cet ennemi (comme en 1V1)
            if "explode" not in activeWeapon:
                vise = int(input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? "))
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
            #si faute, relancer le tour
            else:
                fight2(monsterA, monsterB, player, activeWeapon, )
            if monsterA["health"] <= 0 and monsterB["health"] <= 0:
                print("vous avez vaincu !")
                break

        #attaque puissante mais il faut viser l'ennemi
        elif action == "puissante":
            if player["endurance"] < 5:
                print("vous n'avez plus assez d'endurance")
                fight2(monsterA,monsterB,player,activeWeapon)
            if "explode" in activeWeapon:
                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                plAt = plAt * 2.5
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monsterA["health"] -= round(plAt)
                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    plAt = player["atk"] * activeWeapon["dam"]
                plAt = plAt * 2.5
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monsterB["health"] -= round(plAt)

            if "explode" not in activeWeapon:
                vise = int(input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? "))
                if vise == 1 and monsterA["health"] >= 0 and "explode" not in activeWeapon:
                    if player["endurance"] < 5:
                        print("vous n'avez plus assez d'endurance")
                        fight2(monsterA,monsterB,player,activeWeapon)
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

                elif vise == 2 and monsterB["health"] >= 0 and "explode" not in activeWeapon:
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
            if monsterB["health"] <= 0 and monsterA["health"] <= 0:
                print("vous avez vaincu !")
                break


        elif action == "double":
            #if "explode" in activeWeapon:



            if "explode" not in activeWeapon:
                vise = int(input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? "))
                if vise == 1 and monsterA["health"] >= 0 and "explode" not in activeWeapon:
                    if player["endurance"] < 5:
                        print("vous n'avez plus assez d'endurance")
                        fight2(monsterA,monsterB,player,activeWeapon)
                    if "arc" in activeWeapon:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        for atk in range(2):
                            if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                                plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                            else:
                                plAt = player["atk"] * activeWeapon["dam"]
                            print("vous infligez à l'ennemi", round(plAt), "dégats !")
                            monsterA["health"] -= round(plAt)
                        player["endurance"] -= 5

                if vise == 2 and monsterB["health"] >= 0 and "explode" not in activeWeapon:
                    if player["endurance"] < 5:
                        print("vous n'avez plus assez d'endurance")
                        fight2(monsterA,monsterB, player, activeWeapon)
                    if "arc" in activeWeapon:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        for atk in range(2):
                            if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                                plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                            else:
                                plAt = player["atk"] * activeWeapon["dam"]
                            print("vous infligez à l'ennemi", round(plAt), "dégats !")
                            monsterB["health"] -= round(plAt)
                        player["endurance"] -= 5

            if monsterB["health"] <= 0 and monsterA["health"] <= 0:
                print("vous avez vaincu !")
                break


        elif action == "sort":
            launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
            print("\n")
            if launchSp == "feu":
                if player["mana"] < spells[launchSp]["cost"]:
                    print("vous n'avez plus assez de mana")
                    fight2(monsterA,monsterB,player,activeWeapon)
                monsterA["health"] -= spells[launchSp]["trueDam"]
                print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                player["health"] += spells[launchSp]["auto heal"]
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]

                if player["mana"] < spells[launchSp]["cost"]:
                    print("vous n'avez plus assez de mana")
                    fight2(monsterA,monsterB,player,activeWeapon)
                monsterB["health"] -= spells[launchSp]["trueDam"]
                print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                player["health"] += spells[launchSp]["auto heal"]
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
                player["mana"] -= spells[launchSp]["cost"]

            else:
                vise = int(input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? "))
                if vise == 1 and monsterA["health"] >= 0 and "explode" not in activeWeapon:
                    if player["mana"] < spells[launchSp]["cost"]:
                        print("vous n'avez plus assez de mana")
                        fight2(monsterA,monsterB,player,activeWeapon)
                    monsterA["health"] -= spells[launchSp]["trueDam"]
                    print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                    player["health"] += spells[launchSp]["auto heal"]
                    if player["health"] > player["maxhealth"]:
                        player["health"] = player["maxhealth"]
                    player["mana"] -= spells[launchSp]["cost"]

                if vise == 2 and monsterB["health"] >= 0 and "explode" not in activeWeapon:
                    launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
                    print("\n")
                    if player["mana"] < spells[launchSp]["cost"]:
                        print("vous n'avez plus assez de mana")
                        fight2(monsterA,monsterB,player,activeWeapon)
                    monsterB["health"] -= spells[launchSp]["trueDam"]
                    print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                    player["health"] += spells[launchSp]["auto heal"]
                    if player["health"] > player["maxhealth"]:
                        player["health"] = player["maxhealth"]
                    player["mana"] -= spells[launchSp]["cost"]


            if monsterA["health"] <= 0 and monsterB["health"] <= 0:
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
            if player["mana"] > player["maxmana"]:
                player["mana"] = player["maxmana"]


        if player["health"] <= 0:
            print("vous êtes mort...")
            input("\ntapez entrer pour terminer")
            break
        if random.randint(0, 100) <= monsterA["critL"]:
            moAtA = monsterA["atk"] * monsterA["critDam"]
        else:
            moAtA = monsterA["atk"]
        if random.randint(0, 100) <= monsterB["critL"]:
            moAtB = monsterB["atk"] * monsterB["critDam"]
        else:
            moAtB = monsterB["atk"]

        if "esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]:
            print("esquive !")
            moAtA = 0

        if "esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]:
            print("esquive !")
            moAtB = 0

        if round(moAtA) < activeDef:
            moAtA = 0
        else:
            moAtA -= activeDef

        if round(moAtB) < activeDef:
            moAtB = 0
        else:
            moAtB -= activeDef

        if "taunt" in activeWeapon:
            if random.randint(0,99) >= activeWeapon["taunt"]:
                print("l'ennemi vous inflige", round(moAtA), "dégats !")
                player["health"] -= round(moAtA)
        else:
            print("l'ennemi vous inflige", round(moAtA), "dégats !")
            player["health"] -= round(moAtA)

        if "taunt" in activeWeapon:
            if random.randint(0,99) >= activeWeapon["taunt"]:
                print("l'ennemi vous inflige", round(moAtB), "dégats !")
                player["health"] -= round(moAtB)
        else:
            print("l'ennemi vous inflige", round(moAtB), "dégats !")
            player["health"] -= round(moAtB)

        print("votre vie :", player["health"], "-- vie du monstre 1 :", monsterA["health"],"-- vie du monstre 2 :", monsterB["health"])
        print("mana : ", player["mana"], "endurance : ", player["endurance"])
    if monsterA["health"] <= 0 and monsterB["health"] <= 0 and player["healt"] > 0:
        addG = random.randint(0, 4)
        if addG == 0:
            armeR = weaponList[random.randint(0, len(weaponList) - 1)][0]
            print("vous trouvez ? une arme ! Vous gagnez", armeR["name"])
            activeWeapon = armeR
        else:
            addG = random.randint(0, 100)
            print("vous gagnez", addG, "gold")
            player["gold"] += addG
    elif player["health"] <= 0:
        print("vous êtes mort...")
        input("\ntapez entrer pour terminer")
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

        monsterSpe = random.randint(0,1)
        if monsterSpe == 0:
            monsterA = monsterList[random.randint(0, 3)]
            time.sleep(0.01)
            monsterB = monsterList[random.randint(0, 3)]
            print("quoi ?!",monsterA["type"],"et",monsterB["type"],"vous attaquent")
            fight2(monsterA,monsterB, player, activeWeapon)

        else:
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

    if player["health"] <= 0:
        break
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