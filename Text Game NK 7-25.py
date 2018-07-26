#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:10:52 2018
@author: stem
"""
import random as rand
import time
import winsound as win
import os

player_wep_name = ""


def divide():
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def hit_attempt():
    hit_chance = rand.randint(1, 20)
    if hit_chance == 1:
        return "crit"
    elif hit_chance > 15:
        return "miss"
    else:
        return "hit"


# ---------- Sound Effects -----------
def gunshot():
    win.PlaySound('Gunshot', win.SND_FILENAME)


def death():
    print("John has died...")
    win.PlaySound('Death', win.SND_FILENAME)


def vamp():
    win.PlaySound('Vampire', win.SND_FILENAME)


def wolf():
    win.PlaySound('Wolf Howl', win.SND_FILENAME)

#----- Weapons ------
def vamp_claws():
    damage = rand.randint(15, 20)
    return damage


def silver_revolver():
    # revolver does 20 - 100 damage
    damage = rand.randint(20, 100)
    return damage


def winchester_rifle():
    damage = rand.randint(15, 20)
    return damage


def zombie_fist():
    damage = rand.randint(1, 3)
    return damage


def knife():
    # knife does 1 - 4 damage.
    damage = rand.randint(3, 4)
    return damage


def fists():
    # fists do 1 - 2 damage.
    damage = rand.randint(1, 2)
    return damage


def axe():
    # axe does 4 - 6 damage.
    damage = rand.randint(4, 6)
    return damage


def dev_gun():
    # does all the damage
    damage = 100000000000000
    return damage


def revolver(ammo):
    if ammo > 0:
        # revolver does 20 - 100 damage
        damage = rand.randint(20, 100)
        return damage
    else:
        print("The revolver is out of ammo...")


def baseball_bat():
    damage = 6
    return damage


def pistol():
    damage = rand.randrange(5, 20)
    return damage


def werewolf_claws():
    damage = rand.randint(10, 20)
    return damage


def big_gun():
    damage = rand.randint(10, 30)
    return damage


def old_mg():
    damage = rand.randint(10, 15)
    return damage


def player_old_mg():
    damage = rand.randint(20, 25)
    return damage


def thompson():
    damage = rand.randint(15, 20)
    return damage

# ---------- Combat Functions ----------
def combat(e_hp, e_name, p_weapon, e_dmg, p_wep_name, p_hp):
    e_tp = 0
    p_tp = 0
    while p_hp > 0 and e_hp > 0:
        while e_tp >= p_tp:
            turn = input("Would you like to Attack or Heal: ")
            turn = turn.upper()
            if turn == "ATTACK":
                p_tp = p_tp + 1
                # print("Player points", p_tp)
                did_hit = hit_attempt()
                if did_hit == "hit":
                    e_hp = e_hp - p_weapon
                    print("John's", p_wep_name, "hit for", p_weapon, "damage!")
                    print("The Enemy has", e_hp)
                elif did_hit == "crit":
                    e_hp = e_hp - (int(p_weapon) * 2)
                    print("John's", p_wep_name, "struck true, and crit", e_name)
                    print("The Enemy has", e_hp)
                elif did_hit == "miss":
                    print("John missed the", e_name, "with the", p_wep_name, "!")
            elif turn == "HEAL":
                p_tp = p_tp + 1
                if p_hp >= 50:
                    print("You are already at or above Max Health")
                elif p_hp < 50:
                    heal_amount = rand.randint(1, 4)
                    p_hp + heal_amount
                    print("John used scraps of cloth to heal himself for", heal_amount, "!")

        while e_tp < p_tp:
            e_tp = e_tp + 1
            # print("Enemy points:", e_tp)
            did_hit = hit_attempt()
            if did_hit == "hit":
                p_hp = (p_hp - e_dmg)
                print(e_name, "hit John")
                print("John has", p_hp, "Health")
            elif did_hit == "miss":
                print(e_name, "missed John")
                print("John has", p_hp, "Health")

    if e_hp <= 0 and p_hp > 0:
        print("The", e_name, "was killed by John!")
        return ("John Wins")
    elif p_hp <= 0 and e_hp > 0:
        print("John was mortally wounded, and died!")
        win.PlaySound('Death', win.SND_FILENAME)
        time.sleep(4)
        os.system("cls")
        exit()
    else:
        print("Neither John, nor ", e_name, "Won the fight")
        win.PlaySound('Death', win.SND_FILENAME)
        time.sleep(4)
        os.system("cls")
        exit()


def werewolf_combat(e_hp, p_weapon, e_dmg, p_wep_name, p_hp):
    e_tp = 0
    p_tp = 0
    while p_hp > 0 and e_hp > 0:
        while e_tp >= p_tp:
            turn = input("Would you like to Attack or Heal: ")
            turn = turn.upper()
            if turn == "ATTACK":
                p_tp = p_tp + 1
                # print("Player points", p_tp)
                did_hit = hit_attempt()
                if did_hit == "hit":
                    e_hp = e_hp - p_weapon
                    print("John's", p_wep_name, "hit for", p_weapon, "damage!")
                    print("The Enemy has", e_hp)
                elif did_hit == "crit":
                    e_hp = e_hp - (int(p_weapon) * 2)
                    print("John's", p_wep_name, "struck true, and brutally wounded the Werewolf")
                    print("The Werewolf has", e_hp)
                elif did_hit == "miss":
                    print("John missed the, Werewolf with the", p_wep_name, "!")
            elif turn == "HEAL":
                p_tp = p_tp + 1
                if p_hp >= 60:
                    print("You are already at or above Max Health")
                elif p_hp < 60:
                    heal_amount = rand.randint(8, 16)
                    p_hp + heal_amount
                    print("John used scraps of cloth to heal himself for", heal_amount, "!")
        while e_tp < p_tp:
            e_tp = e_tp + 1
            # print("Enemy points:", e_tp)
            did_hit = hit_attempt()
            if did_hit == "hit":
                p_hp = (p_hp - e_dmg)
                print("The Werewolf hit John with a brutal strike")
                print("John has", p_hp, "Health")
            elif did_hit == "miss":
                print("The Werewolf swiped at John, but John was too quick!")
                print("John has", p_hp, "Health")

    if e_hp <= 0 and p_hp > 0:
        print("John killed the Werewolf")
        return ("John Wins")
    elif p_hp <= 0 and e_hp > 0:
        print("John was outmatched by the Werewolf, and was slain...")
        death()
        exit()
    else:
        print("Neither John, nor the Werewolf were victorious...")
        death()
        exit()


def mob_boss_combat_p1(e_hp, p_weapon, e_dmg, p_wep_name, p_hp):
    e_tp = 0
    p_tp = 0
    while p_hp > 0 and e_hp > 0:
        while e_tp >= p_tp:
            turn = input("Would you like to Attack or Heal: ")
            turn = turn.upper()
            if turn == "ATTACK":
                p_tp = p_tp + 1
                # print("Player points", p_tp)
                did_hit = hit_attempt()
                if did_hit == "hit":
                    e_hp = e_hp - p_weapon
                    print("John's", p_wep_name, "hit for", p_weapon, "damage!")
                    print("The Enemy has", e_hp)
                elif did_hit == "crit":
                    e_hp = e_hp - (int(p_weapon) * 2)
                    print("John's", p_wep_name, "struck true, and brutally wounded the Mob Boss")
                    print("The Werewolf has", e_hp)
                elif did_hit == "miss":
                    print("John missed the, Mob_Boss with the", p_wep_name, "!")
            elif turn == "HEAL":
                p_tp = p_tp + 1
                if p_hp >= 60:
                    print("You are already at or above Max Health")
                elif p_hp < 60:
                    heal_amount = rand.randint(8, 16)
                    p_hp + heal_amount
                    print("John used scraps of cloth to heal himself for", heal_amount, "!")
        while e_tp < p_tp:
            e_tp = e_tp + 1
            # print("Enemy points:", e_tp)
            did_hit = hit_attempt()
            if did_hit == "hit":
                p_hp = (p_hp - e_dmg)
                print("The Boss shot John")
                print("John has", p_hp, "Health")
            elif did_hit == "miss":
                print("The Mob boss shot at John, but John was too quick!")
                print("John has", p_hp, "Health")

    if e_hp <= 0 and p_hp > 0:
        print("John killed the Werewolf")
        return ("John Wins")
    elif p_hp <= 0 and e_hp > 0:
        print("John was outmatched by the Mob Boss, and was slain...")
        death()
        exit()
    else:
        print("Neither John, nor the Boss were victorious...")
        death()
        exit()


def mob_boss_combat_p2(e_hp, p_weapon, e_dmg, p_wep_name, p_hp):
    e_tp = 0
    p_tp = 0
    while p_hp > 0 and e_hp > 0:
        while e_tp >= p_tp:
            turn = input("Would you like to Attack or Heal: ")
            turn = turn.upper()
            if turn == "ATTACK":
                p_tp = p_tp + 1
                # print("Player points", p_tp)
                did_hit = hit_attempt()
                if did_hit == "hit":
                    e_hp = e_hp - p_weapon
                    print("John's", p_wep_name, "hit for", p_weapon, "damage!")
                    print("The Enemy has", e_hp)
                    time.sleep(1)
                elif did_hit == "crit":
                    e_hp = e_hp - (int(p_weapon) * 2)
                    print("John's", p_wep_name, "struck true, and wounded the Vampire")
                    print("The Werewolf has", e_hp)
                    time.sleep(1)
                elif did_hit == "miss":
                    print("John missed the, Vampire with the", p_wep_name, "!")
                    time.sleep(1)
            elif turn == "HEAL":
                p_tp = p_tp + 1
                if p_hp >= 80:
                    print("You are already at or above Max Health")
                    time.sleep(1)
                elif p_hp < 80:
                    heal_amount = rand.randint(8, 16)
                    p_hp + heal_amount
                    print("John used scraps of cloth to heal himself for", heal_amount, "!")
                    time.sleep(1)
        while e_tp < p_tp:
            e_tp = e_tp + 1
            # print("Enemy points:", e_tp)
            did_hit = hit_attempt()
            if did_hit == "hit":
                p_hp = (p_hp - e_dmg)
                e_hp = e_hp + (e_dmg / 4)
                print("The Vampire hit John with a brutal bite")
                time.sleep(1)
                print("As the vampire hits John, some of his wounds close...")
                print("John has", p_hp, "Health")
            elif did_hit == "miss":
                print("The Vampire swiped at John, but John was too quick!")
                print("John has", p_hp, "Health")

    if e_hp <= 0 and p_hp > 0:
        print("The vampire staggers as John breaks off a chair leg, and stabs the vampire.")
        time.sleep(2)
    elif p_hp <= 0 and e_hp > 0:
        print("John was outmatched by the Vampire, and was slain...")
        exit()
    else:
        print("Neither John, nor the Vampire were victorious...")
        exit()
# --------------------------------------
def bossroom():
    time.sleep(2)
    print("John glances around the room, seeing a man in a fine suit sitting in a chair in front of a fireplace.")
    time.sleep(2)
    print("Mob Boss: So, you made it this far! I should congratulate you, but instead I'll kill you!")
    time.sleep(2)
    print("The boss stands up from his chair, and readies his gun.")
    time.sleep(2)
    print("John grabs an antique shotgun off the mantle, and braces himself...")
    player_wep = player_old_mg()
    player_wep_name = "Shotgun"
    play_hp = 140
    divide()
    mob_boss_combat_p1(200, player_wep, thompson(), player_wep_name, play_hp)
    divide()
    time.sleep(2)
    print("The Mob Boss rocks backwards, swaying on his feet.")
    time.sleep(2)
    vamp()
    print("As the mob boss leans forward, he hisses, revealing a pair of vampiric fangs!")
    time.sleep(2)
    divide()
    mob_boss_combat_p2(300, player_wep, vamp_claws(), player_wep_name, play_hp)
    divide()
    exit()


def woods():
    play_hp = 60
    player_wep = knife()
    player_wep_name = "Knife"
    print("John, in his desperation flees into the woods...")
    time.sleep(1)
    print("Looking around in the woods John sees an old wood shed.")
    time.sleep(1)
    wood1 = input("Where does John go?.. (Shed/Woods): ")
    wood1 = wood1.upper()
    while wood1 == "SHED":
        win.PlaySound('door', win.SND_FILENAME)
        time.sleep(1)
        print("John looks around the old wood shed, and quickly finds an old wood axe...")
        player_wep = axe()
        time.sleep(2)
        player_wep_name = "Axe"
        print("John leaves the shed.")
        wood1 = "WOODS"
    else:
        time.sleep(2)
        print("The Woods are dark and spooky, likely home to many creatures...")
        time.sleep(2)
        print("John runs through the woods for an hour or so, stopping to catch his breath he hears a howl in the distance...")
        time.sleep(2)
        print("Coming into a clearing, John spots a series of three graves. Each of these graves seems to have been recently disturbed.")
        time.sleep(2)
        print("The four graves each have a marking on the headstone, describing the treasure that could be inside.")
        time.sleep(2)
        grave = input("John may only dig up one grave, which grave does he dig up? (1/2/3): ")
        if grave == "1":
            time.sleep(2)
            print(
                "John digs up the grave, glancing around... His hand strikes cold flesh as a Zombie with an axe rises from the grave...")
            zombie_wep = axe()
            combat(20, "Zombie", player_wep, zombie_wep, player_wep_name, play_hp)  # Maybe make a special Zombie Combat
        elif grave == "2":
            time.sleep(2)
            print("digging through the grave, John finds a revolver, and several silver bullets...")
            player_wep = silver_revolver()
            player_wep_name = "Sliver Bullet Revolver"
            time.sleep(2)
            print("Again John hears the growling and the howling deep in the woods, but it sounds almost human...")
        elif grave == "13":
            time.sleep(2)
            print("Overcome with curiosity, John looks around...")
            time.sleep(2)
            print("looking behind a massive tree, John sees a hollowed out trunk. Inside he finds a strange weapon.")
            player_wep = dev_gun()
            player_wep_name = "Alien Gun"
        else:
            time.sleep(2)
            print("John looks around, and decides to dig up the third grave. In this grave John finds a Medkit, and uses it to patch himself up.")
            time.sleep(2)
            play_hp = 140
        print("After digging up a grave, John continues to walk, deeper into the woods.")
        time.sleep(2)
        print("John walking through the dark eeire wood hears a strange sound... A human-like growling, followed by a howl.")
        time.sleep(2)
        print("Stepping into a clearing, John comes face to face with an old grizzled man...")
        time.sleep(2)
        print("The man upon seeing John, screams, and hunches. As hair beins sprouting from his back, and he grows sharp lethal claws...")
        time.sleep(3)
        wolf()
        werewolf_combat(200, player_wep, werewolf_claws(), player_wep_name, play_hp)
        divide()
        time.sleep(2)
        print("John, now escapes into the wilderness and back to civilization.")
        divide()
        exit()


def mansion():
    player_wep = knife()
    play_hp = 60
    player_wep_name = "Knife"
    time.sleep(2)
    print("Venturing into the mansion, John steps into a massive foyer")
    time.sleep(2)
    print("Glancing around, the walls are decorated with artifacts, and art pieces.")
    time.sleep(2)
    mani = "main"
    while mani == "main":
        mansion1 = input(
            "lining the ground floor of this massive room, there are 3 doors. Which does john enter? (d1/d2/d3)")
        while mansion1 == "d1":
            win.PlaySound('door', win.SND_FILENAME)
            print("The door leads into a large room.")
            time.sleep(2)
            print(
                "Sitting at a card table in the center of this room, two gang members see John, and pull their pistols...")
            divide()
            gunshot()
            combat(15, "Mobster", player_wep, pistol(), player_wep_name, play_hp)
            time.sleep(2)
            print("John takes a brief moment to grab the mobster's pistol, and engages the other mobster.")
            player_wep = pistol()
            player_wep_name = "Pistol"
            time.sleep(2)
            divide()
            gunshot()
            combat(15, "Mobster", player_wep, pistol(), player_wep_name, play_hp)
            time.sleep(1)
            print("Glancing around the room, John looks at the carnage he caused and tends his wounds...")
            time.sleep(2)
            mansion2 = input(
                "Looking around, this card room seems to lead into another room, likely a dining hall. Do you venture in, or go back?: (Back/in)")
            mansion2 = mansion2.upper()
            if mansion2 == "IN":
                time.sleep(2)
                print(
                    "Venturing into the next room, John finds himself in a large dining hall. Sitting in the corner is a man wearing a tank top and a gold chain.")
                time.sleep(2)
                print("Mobster: Heh, you killed my boys. You're gonna answer to the boss now!")
                time.sleep(2)
                print("John: what do you want with me?")
                time.sleep(2)
                mansion3 = input("Mobster: You can do this peacefully or I can kill you! (Fight/Surrender): ")
                mansion3 = mansion3.upper()
                while mansion3 == "FIGHT":
                    player_wep = winchester_rifle()
                    player_wep_name = "Winchester rifle"
                    time.sleep(2)
                    print("John leaps to the  wall, and grabs a winchester rifle out of the display case.")
                    divide()
                    time.sleep(2)
                    gunshot()
                    combat(45, "Big Mobster", big_gun(), player_wep, player_wep_name, play_hp)
                    divide()
                    print(
                        "Searching the dying mobster, John finds a paper, with the following printed on it: Digit 1 =",
                        dig1)
                    mansion3 = "OTHER"
                if mansion3 == "SURRENDER":
                    time.sleep(2)
                    print("The mobster grabs John, and carries him upstairs to the Bosses Room...")
                    bossroom()
                elif mansion3 == "OTHER":
                    time.sleep(3)
                    print("John leaves the room clutching the note")
                    mani = "main"
                    mansion1 = ""
                else:
                    mansion3 = "FIGHT"
        if mansion1 == "d2":
            win.PlaySound('door', win.SND_FILENAME)
            print("John steps into an empty room, the walls are lined with hunting trophies.")
            time.sleep(1)
            d2search = input("would you like to search this room?(yes/no): ")
            d2search = d2search.upper()
            if d2search == "YES":
                time.sleep(4)
                print("John looks around and finds a piece of paper marked: Digit 2 =", dig2)
                time.sleep(1)
                mani = "main"
            else:
                time.sleep(2)
                print("John leaves the room unsearched.")
                time.sleep(2)
                mani = "main"
        elif mansion1 == "d3":
            time.sleep(2)
            print("The door has a two part combo lock on it.")
            time.sleep(2)
            mansion4 = input("Are you ready to answer? (Yes/No)")
            mansion4 = mansion4.upper()
            if mansion4 == "YES":
                time.sleep(2)
                ans_1 = input("what is Digit 1: ")
                ans1 = int(ans_1)
                ans_2 = input("What is Digit 2: ")
                ans2 = int(ans_2)
                if ans1 == dig1 and ans2 == dig2:
                    time.sleep(2)
                    print("The door swings open, and John steps into a large room with a massive staircase.")
                    mani = "thru"
                else:
                    time.sleep(2)
                    print("after attempting to unlock the door, John realizes that he doesn't have the code")
                    time.sleep(2)
                    print("As john turns around he sees another Mobster come through the door behind him...")
                    time.sleep(2)
                    divide()
                    combat(35, "Mobster", player_wep, baseball_bat(), player_wep_name, play_hp)
    else:
        time.sleep(2)
        print("On either side of the staircase, there is a door.")
        time.sleep(2)
        main_room = "TRUE"
        while main_room == "TRUE":
            mpastdoor = input("What does John do? (LDoor/RDoor/Stairs): ")
            mpastdoor = mpastdoor.upper()
            while mpastdoor == "LDOOR":
                time.sleep(2)
                print("Through the left door, there is a room with a safe, and 3 tapestries.")
                time.sleep(1)
                note_chek = input("In the center of the room, there is a table covered in files. Do you wish to check it? (YES/NO): ")
                note_chek = note_chek.upper()
                while note_chek == "YES":
                    time.sleep(3)
                    print("After sifting through the papers, John finds the following note:")
                    time.sleep(1)
                    print("*************** NOTE ***************")
                    print("*   The first digits: 3, and 5.    *")
                    print("* The others are in a room each,   *")
                    print("* At the top of the stairs enter!  *")
                    print("************************************")
                    note_chek = "NO"
                else:
                    time.sleep(2)
                    print("Looking around the room there are 3 tapestries, and a safe.")
                    time.sleep(2)
                    tapestries = input("What would you like to examine? (Art/Safe): ")
                    tapestries = tapestries.upper()
                    while tapestries == "ART":
                        time.sleep(2)
                        checked = input("Each of the scenes depicted on the tapestries, are of nature. Which do you examine? (Sheep/Mountains/River/Back): ")
                        checked = checked.upper()
                        while checked == "SHEEP":
                            time.sleep(2)
                            print("The tapestry is a depiction of several sheep on a hill.")
                            time.sleep(2)
                            print("Towards the bottom of the art piece, a 6 with a sub-notation of 1 is stitched to the corner.")
                            checked = ""
                        while checked == "MOUNTAINS":
                            time.sleep(2)
                            print("The tapestry is a depiction of a vast mountain range.")
                            time.sleep(2)
                            print("Towards the bottom of the art piece, a 3 with a sub-notation of 2 is stitched to the corner.")
                            checked = ""
                        while checked == "RIVER":
                            time.sleep(2)
                            print("The Tapestry is a depiction of a wide river, with a grassy bank.")
                            time.sleep(2)
                            print("At the bottom of the tapestry, there is a 8 with a sub notation of 3")
                            checked = ""
                        if checked == "BACK":
                            mpastdoor = "LDOOR"
                    while tapestries == "SAFE":
                        time.sleep(2)
                        print("John approaches the safe to find a 3 part code lock.")
                        codelck = input("Do you want to attempt to enter the code?: (YES/NO): ")
                        codelck = codelck.upper()
                        if codelck == "YES":
                            cd1 = input("What is the first number?: ")
                            cd1 = int(cd1)
                            time.sleep(2)
                            cd2 = input("What is the second number?: ")
                            cd2 = int(cd2)
                            time.sleep(2)
                            cd3 = input("What is the third number?: ")
                            cd3 = int(cd3)
                            if cd1 == 6 and cd2 == 3 and cd3 == 8:
                                time.sleep(2)
                                print(
                                    "As John opens the safe, he finds a piece of paper with a 6 in bold text, and a 4 in the corner.")
                                time.sleep(2)
                                print("John leaves the room, and heads back into the hall.")
                                tapestries = ""
                                mpastdoor = ""
            while mpastdoor == "RDOOR":
                print("John enters the right door, into a large armory.")
                time.sleep(2)
                print("Looking around inside this room, John a large man polishing an antique machine gun.")
                time.sleep(2)
                print("The man stands up and grunts at John, loading his gun...")
                divide()
                gunshot()
                combat(50, "Grunt", player_wep, old_mg(), player_wep_name, play_hp)
                divide()
                print("John takes the man's machine gun, and finds a letter in his coat.")
                player_wep = player_old_mg()
                player_wep_name = "Old Machine Gun"
                print("The letter has a 8 with a subscript of 3 in the corner.")
                mpastdoor = ""
            while mpastdoor == "STAIRS":
                print(
                    "John climbs the elaborate set of stairs, at the top he finds a barred iron door, with a code lock.")
                quesstdoor = input("Does john have the combination? (YES/NO): ")
                quesstdoor = quesstdoor.upper()
                if quesstdoor == "YES":
                    time.sleep(2)
                    css1 = input("What is the first number: ")
                    css1 = int(css1)
                    time.sleep(2)
                    css2 = input("What is the second number: ")
                    css2 = int(css2)
                    time.sleep(2)
                    css3 = input("What is the third number: ")
                    css3 = int(css3)
                    time.sleep(2)
                    css4 = input("What is the fourth number: ")
                    css4 = int(css4)
                    time.sleep(1)
                    print("processing...")
                    time.sleep(3)
                    if css1 == 3 and css2 == 5 and css3 == 8 and css4 == 6:
                        bossroom()


# ---------------------
dig1 = rand.randint(0, 9)
dig2 = rand.randint(0, 9)
dig3 = rand.randint(0, 9)
dig4 = rand.randint(0, 9)
# ---------------------
play_hp = 60
player_wep = knife()
# ---------------------


print("John was a average man he loved taking hikes, exploring nature, and his desk job.")
time.sleep(2)
print("One day John was out on a mountain trail enjoying his weekend off, when he encountered a cave.")
time.sleep(3)
print("John ventured inside, not seeing the signs of recent human activity...")
time.sleep(3)
print("A masked man jumps out from behind a boulder, screaming: HANDS UP OR I SHOOT")
time.sleep(2)
print("The masked man throws a burlap sack over John's head, and hits him...")
time.sleep(2)
print("John awakens in darkness, with the sounds of a car around him...")
time.sleep(2)
print("John quickly realizes that he is in a car's trunk.")
time.sleep(2)
print("John hears voices coming around the car, and sees that he has a chance to escape by kicking the trunk open...")
time.sleep(2)
c2 = input("What does John do?: (Wait, or Escape): ")
c2 = c2.upper()
if c2 == "ESCAPE":
    print("John Kicks the trunk open with a loud THUD, as one of the gang members in knocked out. However one still stands...")
    divide()
    bounce_wep = knife()
    combat(25, "Bouncer", player_wep, bounce_wep, "knife", play_hp)
    time.sleep(2)
    print("John looks around him, and sees two options, a massive gothic mansion, or a dense dark wood")
    time.sleep(2)
    c3 = input("Do you dare venture into the Mansion, or do you flee into the woods...(Woods/House): ")
    c3 = c3.upper()
    if c3 == "HOUSE":
        time.sleep(2)
        mansion()

    else:
        time.sleep(2)
        woods()
else:
    print("John is lifted out of the trunk, and carried into the mansion.")
    time.sleep(2)
    print("Carried downstairs, and thrown into a cell, John looks around and through the darkness of the cell.")
    time.sleep(2)
    print("Looking around the cell, and into the hall John can see a guard making rounds past the cells, he aslo notices some worn bricks at the back of his cell.")
    time.sleep(2)
    c4 = input("What does John do?...(dig/distract): ")
    c4 = c4.upper()
    if c4 == ("DIG"):
        time.sleep(4)
        print("3 months later... John emerges into sunlight into a hill behind the mansion.")
        time.sleep(2)
        print("John ventures into the woods in search of freedom...")
        woods()
        time.sleep(2)
        c5 = input("John, now facing a dilemma may venture into the mansion to seek vengeance or flee to the woods...(Woods/House): ")
        c5 = c5.upper()
        if c5 == "WOODS":
            time.sleep(2)
            woods()
        else:
            time.sleep(2)
            print("John decides to enter the house to extract his revenge...")
            mansion()
    elif c4 == ("DISTRACT"):
        time.sleep(1)
        print("As the guard passes by John's cell, John reaches out and grabs the keys from the bouncer's pockets.")
        time.sleep(1)
        print("John waits to make his escape when he escapes, he is met with the option to either explore the mansion, or escape to the woods.")
        time.sleep(2)
        c6 = input("What does John do: (Woods/House): ")
        c6 = c6.upper()
        if c6 == ("WOODS"):
            time.sleep(2)
            print("John makes a break to the back door, and enters the woods")
            woods()
        elif c6 == ("HOUSE"):
            time.sleep(2)
            print("John makes a break for the stairs, and enters the mansion...")
            mansion()
# We are missing like an hours of work