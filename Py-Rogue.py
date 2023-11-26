import random
import time

vit = 1

def menu(vit):
    """
    la fonction menu affiche un menu qui permet d'afficher les crédits ou encore de lancer le jeu
    """
    print("        menu :        ")
    print(">>>lancer la partie<<<")
    print("      >>crédit<<      ")
    print("    >>paramètres<<    ")
    print("       >>tuto<<       \n\n")
    click = input("  tapez le numéro de votre choix : ")

    #lance la partie
    if click == "1":
        classChoos = ""
        for c in range(6):
            print("\n")
            time.sleep(0.25*vit)
        Pclass = classChoix(classChoos,vit)
        start(Pclass,vit)
    #affiche les crédits
    if click == "2":
        for c in range(6):
            print("\n")
            time.sleep(0.25*vit)
        print("Py-Rogue")
        time.sleep(1*vit)
        print("Développement : Hector.D")
        time.sleep(1*vit)
        print("Merci à Pablo.N pour ses idées")
        time.sleep(1*vit)
        print("ainsi qu'à Oliver.A pour son aide")
        time.sleep(1.5*vit)
        print("bon jeu, et bonne chance...")
        time.sleep(1*vit)
        print("\n\n\n\n")
        menu(vit)
    #permet de changer certains paramètres
    if click == "3":
        for c in range(6):
            print("\n")
            time.sleep(0.25*vit)
        print("changer vitesse")
        print("difficulté (Béta)")
        print("")
        choix = input("tapez le numéro de votre choix ")
        if choix == "1":
            print("1=double, 2=normal, 4=moitié")
            vit = input("choisissez la vitesse voulue")
            if vit == "1" or vit == "2" or vit == "4":
                vit =  int(vit) / 2
                print("\n\n\n\n")
                menu(vit)
        else:
            print("vous allez être réorienté vers le menu")
            menu(vit)
    #affiche un 'tutoriel'
    if click == "4":
        for c in range(6):
            print("\n")
            time.sleep(0.25*vit)
        print("malheureusement, il n'y a pas de tutoriel,")
        time.sleep(1*vit)
        print("seul conseil que je peux donner, notez")
        time.sleep(1*vit)
        print("notez un max de trucs pour vous en souvenir")
        time.sleep(1*vit)
        print("bon courage")
        time.sleep(1*vit)
        print("\n\n\n\n")
        menu(vit)

def start(Pclass,vit):
    """
    la fonction start lance une partie du jeu et... ne renvoie rien
    """
    #si vous avez besoin d'expliquation pour ça je ne peux rien pour vous
    choose = input("quelle arme voulez vous ? (épée,hache,arc,dague) ")
    print("\n\n\n\n")

    # définir les armes de départ et le joueur
    Startweapon = {"épée" : {"name" : "épée", "dam": 1.5, "critL": 5, "critDam": 1.3, "def": 2}, "hache" : {"name" : "hache", "dam": 2, "critL": 3, "critDam": 1.1}, "arc" : {"name" : "arc", "dam": 1.25, "critL": 10, "critDam": 1.2}, "dague" : {"name" : "dague","dam": 1, "critL": 20, "critDam": 1.3}}
    player = {"gold": 50, "atk": 15,"maxatk" : 15, "def": 10, "critL": 10, "critDam": 2, "health": 200, "maxhealth": 200, "endurance": 15,
              "mana": 50, "maxendurance": 15, "maxmana": 50}

    #définir les bonus de classe
    if Pclass["comp"] == "M":
        player["mana"] += 50
        player["maxmana"] += 50
    if Pclass["comp"] == "A":
        player["critL"] += 5
        player["critDam"] += 0.2
    if Pclass["comp"] == "T":
        player["def"] += 10
        player["maxhealth"] += 50
        player["health"] += 50


    # définir la liste des armes disponible dans le jeu (trié par type d'arme, puis chaque arme dans un dictionnaire)
    weaponList = [[{"name": "fire sword", "dam": 1.5, "critL": 5, "critDam": 1.3, "feu": 10}],
                  [{"name": "ice axe", "dam": 2, "critL": 3, "critDam": 1.1, "taunt": 10}],
                  [{"name" : "explosive bow", "dam" : 1.25, "critL" : 10, "critDam" : 1.2, "explode" : True}],
                  [{"name": "shadow dagger", "dam": 1, "critL": 20, "critDam": 1.3,"esquive": 10}]]

    itemsList = [
                 {"type" : "regenV", "name" : "potion de soin", "regenV" : 50,"mes" : "c'est sucré ! la potion vous soigne 50 PV"},
                 {"type" : "regenE", "name" : "potion d'endurance", "regenE" : 10, "mes" : "vous vous sentez revigoré ! la potion vous rend 10 d'endurance"},
                 {"type" : "regenM", "name" : "potion de mana", "regenM" : 50, "mes" : "la magie infuse en vous ! la potion vous rend 50 point de mana"},
                 {"type" : "regenC", "name" : "potion critique", "regenC" : 0.2, "mes" : "si tranchant ! vous avez plus de chance d'infliger un coup critique"},
                 {"type" : "gainG", "name" : "bourse de pièce", "gainG" : 50, "mes" : "ça brille ! vous gagnez 50 Gold"},
                 {"type" : "gainG", "name" : "bourse de pièce", "gainG" : 100, "mes" : "quel trésor !! vous gagnez 100 Gold"},
                 {"type" : "gainG", "name" : "bourse de pièce", "gainG" : 25, "mes" : "ça brille ! vous gagnez 25 Gold"},
                 {"type" : "gainG", "name" : "bourse de pièce", "gainG" : 10, "mes" : "ça brille, un peu ?! vous gagnez 10 Gold"},
                 {"type" : "gainG", "name" : "bourse de pièce", "gainG" : 0, "mes" : "euh c'est quoi ça ?! vous gagnez 0 Gold"}
                 ]

    # définir la liste des sorts
    spells = {"feu": {"zone": True, "trueDam": 20, "auto heal": 0, "cost": 15},
              "zap": {"zone": False, "trueDam": 50, "auto heal": 0, "cost": 15},
              "heal": {"zone": False, "trueDam": 0, "auto heal": 20, "cost": 25}}

    # équiper l'arme choisi par le joueur
    if choose in Startweapon:
        activeWeapon = Startweapon[choose]
    else:
        start(Pclass)


    inv = {"armList" : [], "item" : [], "activeWeapon" : {}}

    inv["activeWeapon"] = activeWeapon

    # définir la liste des monstres pouvant apparaitre
    monsterList = [{"type": "zombie", "atk": 7, "def": 1, "critL": 10, "critDam": 1.2, "health": 100},
                   {"type": "squelette", "atk": 5, "def": 2, "critL": 10, "critDam": 1.5, "health": 100},
                   {"type": "zombie ELITE !", "atk": 15, "def": 4, "critL": 15, "critDam": 1.3, "health": 200},
                   {"type": "loup", "atk": 10, "def": 1, "critL": 5, "critDam": 2, "health": 150}]


    # définition d'une fonction simulant un combat entre un monstre (1ère variable), le joueur (2ème variable), l'arme équippé, est également renseigné
    def fight(monster, player, activeWeapon,vit):
        # lancer une boucle ne se stoppant que si un des deux opposants meurs
        while player["health"] > 0 and monster["health"] > 0:

            if Pclass["comp"] == "B":
                if player["health"] < player["maxhealth"] and (player["maxhealth"] - player["health"])//10 >= 1:
                    atkBon = (player["maxhealth"] - player["health"])//10
                    print("la rage vous insuffle",atkBon,"points de force")
                    player["atk"] = player["maxatk"] + atkBon

            # appliquer les bonus de défense de son arme et les reset
            if "def" in activeWeapon:
                activeDef = player["def"] + activeWeapon["def"]
            else:
                activeDef = player["def"]

            # demander au joueur l'action voulant etre executé
            action = input(
                "quelle action voulez vous executer ?\n(ne pas marquer 'attaque' avant le nom de l'action)\n(attaque simple,attaque puissante,attaque double,sort,défense) ")
            print("\n")

            # //////////////////////////////////////////////////////////////////////////
            # action attaque simple
            if action == "simple":
                # tester si il y a coup critique et appliquer si oui
                if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                    plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                else:
                    # attaque sans coup critique + calcul des dégats
                    plAt = player["atk"] * activeWeapon["dam"]
                # affichage des dégats et appliquation
                print("vous infligez à l'ennemi", round(plAt), "dégats !")
                monster["health"] -= round(plAt)
                # tester si le monstre à été tué suite à l'action
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break

            # //////////////////////////////////////////////////////////////////////////

            # action attaque puissante (attaque infligeant 2.5 fois plus de dégats)
            elif action == "puissante":
                # tester si le joueur à assez d'endurance pour lancer l'attaque, si non cela relance le tour
                if player["endurance"] < 5:
                    print("vous n'avez plus assez d'endurance")
                    fight(monster, player, activeWeapon,vit)
                # tester si l'arme et un arc, qui coute moins d'endurance (simulé en rajoutant de l'endurance)
                if "arc" in activeWeapon:
                    player["endurance"] += 1
                else:
                    # tester si il y a coup critique et appliquer si oui
                    if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                        plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                    else:
                        plAt = player["atk"] * activeWeapon["dam"]
                    # appliquer le bonus de dégat
                    plAt = plAt * 2.5
                    # afficher les dégats et les appliquer
                    print("vous infligez à l'ennemi", round(plAt), "dégats !")
                    monster["health"] -= round(plAt)
                    player["endurance"] -= 5
                    # tester si le monstre est mort
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break


            # action attaque double (attaque 2 fois en 1 tour)
            elif action == "double":
                # tester si le joueur à assez d'endurance pour lancer l'attaque, si non cela relance le tour
                # j'ai vraiment besoin de détailler, les trucs identiques ?
                if player["endurance"] < 5:
                    print("vous n'avez plus assez d'endurance")
                    fight(monster, player, activeWeapon,vit)
                if "arc" in activeWeapon:
                    player["endurance"] += 1
                else:
                    # lancer 2 fois l'action d'attaque simple
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


            # quand on lance un sort (ils infligent des truedamage, qui esquivent le bouclier)
            elif action == "sort":
                # choix du sort
                launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
                print("\n")
                # tester si le joueur à encore assez de mana
                if player["mana"] < spells[launchSp]["cost"]:
                    print("vous n'avez plus assez de mana")
                    fight(monster, player, activeWeapon,vit)
                # appliquer les dégats du sort et afficher
                monster["health"] -= spells[launchSp]["trueDam"]
                print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                # appliquer les heals du sort
                player["health"] += spells[launchSp]["auto heal"]
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
                # consommer le mana
                player["mana"] -= spells[launchSp]["cost"]
                if monster["health"] <= 0:
                    print("vous avez vaincu !")
                    break

            # acion de défense qui regenère des stats et augmente temporairement la défense
            elif action == "défense":
                # augmentation défense
                activeDef = activeDef * 2
                # soin et limitation au max
                player["health"] += 5
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
                # regeneration de l'endurance et limitation au max
                player["endurance"] += 4
                if player["endurance"] > player["maxendurance"]:
                    player["endurance"] = player["maxendurance"]
                # regeneration de mana et limitation au max
                player["mana"] += 10
                if player["mana"] > player["maxmana"]:
                    player["mana"] = player["maxmana"]

            # si il y a une faute de frappe (= pas d'action)
            elif action != "défense" and action != "sort" and action != "double" and action != "puissante" and action != "simple":
                fight(monster, player, activeWeapon,vit)

            # appliquer les dégats de feu de l'arme fire sword
            if action != "sort" and "feu" in activeWeapon:
                print("le feu inflige 10 dégat à l'adversaire")
                monster["health"] -= 10

            # tester si le joueur est mort
            if player["health"] <= 0:
                print("vous êtes mort...")
                print("vous avez parcouru",c,"salles")
                input("\ntapez entrer pour terminer")
                break
            # tester si il y a un coup critique de la part du monstre
            if random.randint(0, 100) <= monster["critL"]:
                moAt = monster["atk"] * monster["critDam"]
            else:
                moAt = monster["atk"]

            # tester si le joueur esquive (avec la shadow dagger)
            if ("esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]) or (Pclass["comp"] == "A" and random.randint(0, 100) <= 5):
                print("esquive !")
                moAt = 0

            # appliquer la réduction des dégats par la défense
            moAt =  moAt - ((moAt * activeDef)//100)

            #attaque spécial de boss (1 chance sur 5)
            if random.randint(1,5) == 1 and "fire breath" in monster:
                player["health"] -= 40
                print("le dragon vous crache un déluge de flamme dessus et vous inflige 40 dégat")

            else:
                # appliquer le pouvoir taunt de la ice axe
                if "taunt" in activeWeapon:
                    if random.randint(0, 99) >= activeWeapon["taunt"]:
                        print("l'ennemi vous inflige", round(moAt), "dégats !")
                        player["health"] -= round(moAt)
                    else:
                        print("Taunt ! l'ennemi n'a pas réussi à attaquer")
                else:
                    print("l'ennemi vous inflige", round(moAt), "dégats !")
                    player["health"] -= round(moAt)

            # affichage de fin de tour (vie,stat,etc)
            print("votre vie :", player["health"], "-- vie du monstre 1 :", monster["health"])
            print("mana : ", player["mana"], "endurance : ", player["endurance"])
            time.sleep(1*vit)
            print("\n\n")

            if monster["health"] <= 0:
                print("vous avez vaincu !")
                break

        # lors de la fin du combat donner des récompenses
        if player["health"] > monster["health"]:
            addG = random.randint(0, 4)
            if addG == 0:
                armeR = weaponList[random.randint(0, len(weaponList) - 1)][0]
                inv["armList"].append(armeR)
                print("vous trouvez ? une arme ! Vous gagnez", armeR["name"])
            if addG == 1:
                itemR = itemsList[random.randint(0,len(itemsList)-1)]
                inv["armList"].append(armeR)
                print("vous remarquez un objet sur le monstre, vous gagnez", itemR["name"])
            else:
                addG = random.randint(0, 100)
                print("vous gagnez", addG, "gold")
                player["gold"] += addG
        else:
            print("vous êtes mort...")
            print("vous avez parcouru", c, "salles")
            input("\ntapez entrer pour terminer")


    # ////////////////////////////////////////////////////////////////
    #combat contre 2 monstre en même temps
    def fight2(monsterA, monsterB, player, activeWeapon,vit):
        while player["health"] > 0 and (monsterA["health"] > 0 or monsterB["health"] > 0):

            if Pclass["comp"] == "B":
                if player["health"] < player["maxhealth"] and (player["maxhealth"] - player["health"])//10 >= 1:
                    atkBon = (player["maxhealth"] - player["health"])//10
                    print("la rage vous insuffle",atkBon,"points de force")
                    player["atk"] = player["maxatk"] + atkBon

            #calcul de votre défense
            if "def" in activeWeapon:
                activeDef = player["def"] + activeWeapon["def"]
            else:
                activeDef = player["def"]
            action = input(
                "quelle action voulez vous executer ?\n(ne pas marquer 'attaque' avant le nom de l'action)\n(attaque simple,attaque puissante,attaque double,sort,défense) ")
            print("\n")

            if action == "simple":
                # tester puis appliquer des dégats explosif (de zone)
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

                # viser l'ennemi puis attaquer cet ennemi (comme en 1V1)
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
                # si faute, relancer le tour
                else:
                    fight2(monsterA, monsterB, player, activeWeapon,vit)
                if monsterA["health"] <= 0 and monsterB["health"] <= 0:
                    print("vous avez vaincu !")
                    break

            # attaque puissante mais il faut viser l'ennemi
            elif action == "puissante":
                if player["endurance"] < 5:
                    print("vous n'avez plus assez d'endurance")
                    fight2(monsterA, monsterB, player, activeWeapon,vit)
                #tester si l'arme fait des attaques de zones
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
                    player["endurance"] -= 5

                #si l'arme ne fait pas d'attaque de zone
                if "explode" not in activeWeapon:
                    vise = int(input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? "))
                    if vise == 1 and monsterA["health"] >= 0 and "explode" not in activeWeapon:
                        if player["endurance"] < 5:
                            print("vous n'avez plus assez d'endurance")
                            fight2(monsterA, monsterB, player, activeWeapon,vit)
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
                            fight2(monsterA, monsterB, player, activeWeapon,vit)
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

            #attaque deux fois le même monstre
            elif action == "double":
                #test si l'attaque est en zone
                if "explode" in activeWeapon:
                    if player["endurance"] < 5:
                        print("vous n'avez plus assez d'endurance")
                        fight2(monsterA, monsterB, player, activeWeapon,vit)
                    for atk in range(2):
                        if random.randint(0, 100) <= player["critL"] + activeWeapon["critL"]:
                            plAt = player["atk"] * (player["critDam"] + activeWeapon["critDam"]) * activeWeapon["dam"]
                        else:
                            plAt = player["atk"] * activeWeapon["dam"]
                        print("vous infligez aux ennemis", round(plAt), "dégats !")
                        monsterA["health"] -= round(plAt)
                        monsterB["health"] -= round(plAt)
                    player["endurance"] -= 5
                #si l'attaque n'est pas de zone
                if "explode" not in activeWeapon:
                    vise = int(input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? "))
                    if vise == 1 and monsterA["health"] >= 0 and "explode" not in activeWeapon:
                        if player["endurance"] < 5:
                            print("vous n'avez plus assez d'endurance")
                            fight2(monsterA, monsterB, player, activeWeapon,vit)
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
                                monsterA["health"] -= round(plAt)
                            player["endurance"] -= 5

                    if vise == 2 and monsterB["health"] >= 0 and "explode" not in activeWeapon:
                        if player["endurance"] < 5:
                            print("vous n'avez plus assez d'endurance")
                            fight2(monsterA, monsterB, player, activeWeapon,vit)
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
                                monsterB["health"] -= round(plAt)
                            player["endurance"] -= 5

                if monsterB["health"] <= 0 and monsterA["health"] <= 0:
                    print("vous avez vaincu !")
                    break

            #lancer un sort
            elif action == "sort":
                launchSp = input("quel sort voulez vous lancer ? (feu,zap,heal) ")
                print("\n")
                #sort de boule de feu (zone)
                if launchSp == "feu":
                    if player["mana"] < spells[launchSp]["cost"]:
                        print("vous n'avez plus assez de mana")
                        fight2(monsterA, monsterB, player, activeWeapon,vit)
                    monsterA["health"] -= spells[launchSp]["trueDam"]
                    print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                    player["health"] += spells[launchSp]["auto heal"]
                    if player["health"] > player["maxhealth"]:
                        player["health"] = player["maxhealth"]

                    if player["mana"] < spells[launchSp]["cost"]:
                        print("vous n'avez plus assez de mana")
                        fight2(monsterA, monsterB, player, activeWeapon,vit)
                    monsterB["health"] -= spells[launchSp]["trueDam"]
                    print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                    player["health"] += spells[launchSp]["auto heal"]
                    if player["health"] > player["maxhealth"]:
                        player["health"] = player["maxhealth"]
                    player["mana"] -= spells[launchSp]["cost"]
                #autres sorts (pas de zone)
                else:
                    vise = int(input("(ne mettre que le numéro)\nvoulez vous attaquer l'ennemi 1 où 2 ? "))

                    if vise == 1 and monsterA["health"] >= 0 and "explode" not in activeWeapon:
                        print("\n")
                        if player["mana"] < spells[launchSp]["cost"]:
                            print("vous n'avez plus assez de mana")
                            fight2(monsterA, monsterB, player, activeWeapon,vit)
                        monsterA["health"] -= spells[launchSp]["trueDam"]
                        print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                        player["health"] += spells[launchSp]["auto heal"]
                        if player["health"] > player["maxhealth"]:
                            player["health"] = player["maxhealth"]
                        player["mana"] -= spells[launchSp]["cost"]

                    if vise == 2 and monsterB["health"] >= 0 and "explode" not in activeWeapon:
                        print("\n")
                        if player["mana"] < spells[launchSp]["cost"]:
                            print("vous n'avez plus assez de mana")
                            fight2(monsterA, monsterB, player, activeWeapon,vit)
                        monsterB["health"] -= spells[launchSp]["trueDam"]
                        print("vous infligez à l'ennemi", spells[launchSp]["trueDam"], "dégats !")
                        player["health"] += spells[launchSp]["auto heal"]
                        if player["health"] > player["maxhealth"]:
                            player["health"] = player["maxhealth"]
                        player["mana"] -= spells[launchSp]["cost"]

                if monsterA["health"] <= 0 and monsterB["health"] <= 0:
                    print("vous avez vaincu !")
                    break
            #action de défense, regeneration et tanker les dégats sont monnaie courante ici...
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

            #si vous avez fait une faute, ça recommence le tour
            elif action != "défense" and action != "sort" and action != "double" and action != "puissante" and action != "simple":
                fight2(monsterA,monsterB, player, activeWeapon,vit)

            # appliquer les dégats de feu de l'arme fire sword
            if action != "sort" and "feu" in activeWeapon:
                print("le feu inflige 10 dégat aux adversaires")
                monsterA["health"] -= 10
                monsterB["health"] -= 10

            #tester la mort du joueur et attaque des monstres
            if player["health"] <= 0:
                print("vous êtes mort...")
                print("vous avez parcouru", c, "salles")
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

            #tester si vous esquivez l'attaque
            if "esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]:
                print("esquive !")
                moAtA = 0

            #tester si vous esquivez l'attaque
            if "esquive" in activeWeapon and random.randint(0, 100) <= activeWeapon["esquive"]:
                print("esquive !")
                moAtB = 0

            #calcul de défense
            moAtA =  moAtA - ((moAtA * activeDef)//100)

            moAtB =  moAtB - ((moAtB * activeDef)//100)

            #attaque des ennemis et test de taunt
            if "taunt" in activeWeapon:
                if random.randint(0, 99) >= activeWeapon["taunt"] and monsterA["health"] > 0:
                    print("l'ennemi vous inflige", round(moAtA), "dégats !")
                    player["health"] -= round(moAtA)
            else:
                if monsterA["health"] >= 0:
                    print("l'ennemi vous inflige", round(moAtA), "dégats !")
                    player["health"] -= round(moAtA)

            if "taunt" in activeWeapon:
                if random.randint(0, 99) >= activeWeapon["taunt"] and monsterB["health"] > 0:
                    print("l'ennemi vous inflige", round(moAtB), "dégats !")
                    player["health"] -= round(moAtB)
            else:
                if monsterB["health"] >= 0:
                    print("l'ennemi vous inflige", round(moAtB), "dégats !")
                    player["health"] -= round(moAtB)

            #affichages d'état du combat, test de vie du joueur et des monstres
            print("votre vie :", player["health"], "-- vie du monstre 1 :", monsterA["health"], "-- vie du monstre 2 :",
                  monsterB["health"])

            print("mana : ", player["mana"], "endurance : ", player["endurance"])

        if (monsterA["health"] <= 0 and monsterB["health"] <= 0) and player["health"] > 0:
            addG = random.randint(0, 4)
            if addG == 0:
                armeR = weaponList[random.randint(0, len(weaponList) - 1)][0]
                inv["armList"].append(armeR)
                print("vous trouvez ? une arme ! Vous gagnez", armeR["name"])
            else:
                addG = random.randint(0, 100)
                print("vous gagnez", addG, "gold")
                player["gold"] += addG

        elif player["health"] <= 0:
            print("vous êtes mort...")
            print("vous avez parcouru", c, "salles")
            input("\ntapez entrer pour terminer")

    #///////////////////////////////////////////////////////////////////////////////

    #definition des combats de boss et de leurs stats
    def dragBoss(player,activeWeapon):
        monster = {"type": "dragon", "atk": 25, "def": 10, "critL": 10, "critDam": 1.5, "health": 750,"fire breath" : True}
        fight(monster,player,activeWeapon,vit)
    def golBoss(player,activeWeapon):
        monster = {"type": "géant", "atk": 20, "def": 5, "critL": 20, "critDam": 1.2, "health": 500}
        fight(monster, player, activeWeapon,vit)
    #def goblinKing(player,activeWeapon):


    #definition du lancement de la rencontre avec le boss (ou autre surprise...)
    def boss(player,activeWeapon):
        event = random.randint(1,100)
        if event <3:
            print("vous entrez dans une caverne...")
            print("et vous tombez nez à nez avec ?")
            time.sleep(1*vit)
            print("un dragon ? \n")
            time.sleep(0.5*vit)
            print("je pensais qu'ils étaient tous éteints \n")
            time.sleep(0.5*vit)
            dragBoss(player,activeWeapon)
        if 3<= event <=100:
            print("la colline sur lequel vous vous trouvez se met à bouger")
            time.sleep(1*vit)
            print("mais ce n'était pas une colline...")
            time.sleep(0.5*vit)
            print("un géant vous attaque !")
            golBoss(player,activeWeapon)
        if event == 100:
            print("alors que vous marchez dans la forêt, vous apercevez une lueur")
            print("alors que vous vous faufilez à travers les branchages")
            print("vous entrez dans le royaume gobelin")
            #goblinKing(player,activeWeapon)


    #///////////////////////////////////////////////////////////////////////////////

    #boucle de 30 salles puis LE BOSS !
    for c in range(30):


        eventP = random.randint(0, 9)

        #definition des monstres (plus pratique si je segmente en zones, et en plus ça reset leurs stat)
        monsterList = [{"type": "zombie", "atk": 7, "def": 1, "critL": 10, "critDam": 5, "health": 100},
                       {"type": "squelette", "atk": 5, "def": 2, "critL": 10, "critDam": 1.5, "health": 100},
                       {"type": "zombie ELITE !", "atk": 15, "def": 4, "critL": 15, "critDam": 3, "health": 200},
                       {"type": "loup", "atk": 10, "def": 1, "critL": 10, "critDam": 2, "health": 150}]

        if eventP <= 5:
            event = "M"
        elif 5 < eventP <= 7:
            event = "C"
        elif 7 < eventP <= 9:
            event = "S"
        #else:
            #event = "F"

        if event == "M":

            #lance un combat contre un ou deux monstre(s) et remplis les paramètres
            monsterSpe = random.randint(0, 10)
            if monsterSpe == 0:
                monsterA = monsterList[random.randint(0, 3)]
                #en fait si on affronte 2 monstres identique, ça fait un bug où les deux se prennent les mêmes dégats, du coup cette ligne permet de ne pas avoir le même monstre
                time.sleep(0.01)
                monsterB = monsterList[random.randint(0, 3)]
                while monsterA == monsterB:
                    #pareil que le commentaire précedent
                    monsterB = monsterList[random.randint(0, 3)]
                print("quoi ?!", monsterA["type"], "et", monsterB["type"], "vous attaquent")
                fight2(monsterA, monsterB, player, activeWeapon,vit)
                player["atk"] = player["maxatk"]
                player["health"] += 30
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
                player["mana"] += 15
                if player["mana"] > player["maxmana"]:
                    player["mana"] = player["maxmana"]
                player["endurance"] += 6
                if player["endurance"] > player["maxendurance"]:
                    player["endurance"] = player["maxendurance"]
                print("vos statistiques ont été (un peu) restoré")

            else:
                Rmonster = random.randint(1, 10)
                if Rmonster == 1:
                    Rmonster = 2
                elif 4 >= Rmonster > 1:
                    Rmonster = 0
                elif 7 >= Rmonster > 4:
                    Rmonster = 1
                elif 10 >= Rmonster > 7:
                    Rmonster = 3

                monsterE = monsterList[Rmonster]
                print("un", monsterE["type"], "vous attaque")
                fight(monsterE, player, activeWeapon,vit)
                player["atk"] = player["maxatk"]
                player["health"] += 15
                if player["health"] > player["maxhealth"]:
                    player["health"] = player["maxhealth"]
                player["mana"] += 7.5
                if player["mana"] > player["maxmana"]:
                    player["mana"] = player["maxmana"]
                player["endurance"] += 3
                if player["endurance"] > player["maxendurance"]:
                    player["endurance"] = player["maxendurance"]
                print("vos statistiques ont été (un peu) restoré")

        #je crois bien que en l'état cette ligne est inutile ici...
        if player["health"] <= 0:
            break

        #génération et affichage d'une salle de trésor
        if event == "C":
            print("salle de trésor !")
            addG = random.randint(20, 100)
            print("vous gagnez", addG, "gold")
            player["gold"] += addG
            if random.randint(0, 10) <= 2:
                print("")

        #génération et affichage du magasin
        if event == "S":
            achat = 0
            AR = False
            A = False
            IR = False
            I = False
            armeR = weaponList[random.randint(0, len(weaponList) - 1)][0]
            itemR = itemsList[random.randint(0,len(itemsList) - 1)]
            while achat != "stop":
                print("vous entrez dans le magasin :")
                print("vous avez", player["gold"], "gold")
                print("vie : 25 G : V")
                print("augmentation vie : 50 G : V+")
                print("endurance : 50 : E")
                print("augmentation endurance : 75 G : E+")
                print("mana : 75 G : M")
                print("augmentation de force : 50 G : S")
                print("augmentation défense : 75 G : D")
                if AR != True:
                    print("arme aléatoire : 50 G : AR")
                if A != True:
                    print("arme :", armeR["name"], "100 G : A")
                if IR != True:
                    print("objet aléatoire : 40 G : IR")
                if I != True:
                    print("arme :", itemR["name"], "75 G : I")
                print("")
                print("tapez stop pour sortir")
                achat = input("que voulez vous acheter ")

                #gestion des achats
                if achat == "A" and player["gold"] >= 100:
                    inv["armList"].append(armeR)
                    player["gold"] -= 100
                    A = True

                elif achat == "IR" and player["gold"] >= 40:
                    inv["item"].append(itemsList[random.randint(0,len(itemsList) - 1)])
                    player["gold"] -= 40
                    IR = True

                elif achat == "I" and player["gold"] >= 75:
                    inv["item"].append(itemR)
                    player["gold"] -= 75
                    I = True

                elif achat == "V" and player["gold"] >= 25:
                    player["health"] += 40
                    player["gold"] -= 25
                    if player["health"] > player["maxhealth"]:
                        player["health"] = player["maxhealth"]

                elif achat == "V+" and player["gold"] >= 50:
                    player["maxhealth"] += 10
                    player["health"] += 10
                    player["gold"] -= 50

                elif achat == "E" and player["gold"] >= 50:
                    player["endurance"] += 10
                    player["gold"] -= 50

                elif achat == "E+" and player["gold"] >= 50:
                    player["maxendurance"] += 2.5
                    player["endurance"] += 2.5
                    player["gold"] -= 50

                elif achat == "M" and player["gold"] >= 75:
                    player["mana"] = player["maxmana"]
                    player["gold"] -= 75

                elif achat == "S" and player["gold"] >= 50:
                    player["atk"] += 2
                    player["maxatk"] += 2
                    player["gold"] -= 50

                elif achat == "D" and player["gold"] >= 75:
                    player["def"] += 2
                    player["gold"] -= 75

                elif achat == "AR" and player["gold"] >= 50:
                    inv["armList"].append(weaponList[random.randint(0, len(weaponList) - 1)][0])
                    player["gold"] -= 50
                    AR = True

                elif achat == "stop":
                    break

                else:
                    print("vous n'avez pas assez d'argent")

        #euuuuuuh, je verrai ça plus tard...
        """
        if event == "F":
            print("vous entrez dans une forge isolée")
            time.sleep(0.5*vit)
        """

        #message de fin de tour + affichage de l'inventaire
        cont = input("tapez 'inv' pour acceder à l'inventaire, ou rien pour continuer ")
        if cont == "inv":
            act = 0
            #affichage et action sur l'inventaire
            while act != "stop":
                print("vous avez",player["gold"],"gold,",player["health"],"points de vie\n",player["mana"],"mana et",player["endurance"],"points d'endurance")
                print("vous utilisez :",inv["activeWeapon"]["name"])
                time.sleep(0.5*vit)
                print("cette arme inflige",inv["activeWeapon"]["dam"])
                time.sleep(0.5*vit)
                print("elle vous octroie","+"+str(inv["activeWeapon"]["critL"])+"%","de chance d'infliger un coup critique")
                time.sleep(0.5*vit)
                print("elle multiplie les dégats critique par",inv["activeWeapon"]["critDam"])
                time.sleep(0.5*vit)
                print("vous pensez tout de même pas qu'on va vous donnez les stats caché de l'arme en plus non ?\n")
                time.sleep(1.25*vit)
                print("vous avez : ")
                #affichage des armes (et objet mais faudrait déjà que je les rajoute avant)
                for i in range(0,len(inv["armList"])):
                    print(inv["armList"][i]["name"])
                for i in range(0,len(inv["item"])):
                    print(inv["item"][i]["name"])
                act = input("si vous voulez changer d'arme tapez son nom\npour utiliser un objet, écrivez son nom\nsinon tapez 'stop' ")
                #équipement d'une arme
                for i in range(0,len(inv["armList"])):
                    if act == inv["armList"][i]["name"]:
                        inv["armList"].append(activeWeapon)
                        activeWeapon = inv["armList"].pop(i)
                        inv["activeWeapon"] = activeWeapon

                for i in range(0,len(inv["item"])):

                    if act == inv["item"][i]["name"]:

                        if inv["item"][i]["type"] == "regenV":
                            player["health"] += inv["item"][i]["regenV"]
                            if player["health"] > player["maxhealth"]:
                                player["health"] = player["maxhealth"]
                            print(inv["item"][i]["mes"])

                        elif inv["item"][i]["type"] == "regenE":
                            player["endurance"] += inv["item"][i]["regenE"]
                            if player["endurance"] > player["maxendurance"]:
                                player["endurance"] = player["maxendurance"]
                            print(inv["item"][i]["mes"])

                        elif inv["item"][i]["type"] == "regenM":
                            player["mana"] +=inv["item"][i]["regenM"]
                            if player["mana"] > player["maxmana"]:
                                player["mana"] = player["maxmana"]
                            print(inv["item"][i]["mes"])

                        elif inv["item"][i]["type"] == "regenC":
                            player["critL"] += inv["item"][i]["regenC"]
                            print(inv["item"][i]["mes"])

                        elif inv["item"][i]["type"] == "gainG":
                            player["gold"] += inv["item"][i]["gainG"]
                            print(inv["item"][i]["mes"])

                        inv["item"].pop(i)
                        time.sleep(1*vit)
                        print("\n\n\n")
                        break

        input("tapez pour continuer")
        print("\n\n")
        #si la dernière salle est finie : boss
        if c == 29:
            boss(player,activeWeapon)

#choix des classes (et application)
def classChoix(classChoos,vit):
    classList = [{"name" : "barbare", "desc" : "un fameux guerrier, il gagne de la force quand il est blessé", "comp" : "B"},
                 {"name" : "assassin", "desc" : "un combattant de l'ombre, certains de ses coup sont dévastateurs", "comp" : "A"},
                 {"name" : "mage", "desc" : "le magicien du royaume, plus de magie !", "comp" : "M"},
                 {"name" : "tanker", "desc" : "un chevalier intuable", "comp" : "T"},
                 #comment ça ont peut pas les choisirs... oui c'est vrai mais ça arrive..
                 {"name" : "draco-barbare", "desc" : "il poursuit l'héritage draconique", "comp" : "DM"},
                 {"name" : "draco-assassin", "desc" : "il poursuit l'héritage draconique", "comp" : "DA"},
                 {"name" : "draco-mage", "desc" : "il poursuit l'héritage draconique", "comp" : "DM"},
                 {"name" : "draco-tanker", "desc" : "un chevalier intuable", "comp" : "DT"},
                 {"name" : "???", "desc" : "???", "comp" : "?"}
                 ]
    print("classes disponibles : ")
    time.sleep(0.5*vit)
    for c in range(0,len(classList)):
        if classList[c]["name"] != "???" and classList[c]["comp"][0] != "D":
            print(classList[c]["name"])
            time.sleep(0.5*vit)
    Choix = input("choisissez votre classe : ")
    for c in range(0,len(classList)):
        if Choix == classList[c]["name"] and Choix != "???":
            print("un",classList[c]["name"]+",",classList[c]["desc"])
            Cv = input("validez vous ce choix ? (O/N) ")
            if Cv == "O":
                print("\n\n\n\n")
                classChoos = classList[c]
            else:
                print("vous avez dit non...")
                classChoos = classChoix(classChoos)
                return classChoos
        elif Choix == "???":
            print("mais qu'est-ce que ?")
    if classChoos != "":
        return classChoos
    else:
        classChoos = classChoix(classChoos)
        return classChoos

#ça c'est le truc qui lance tout...
menu(vit)