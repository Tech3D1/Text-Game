#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:10:52 2018
@author: stem
"""
import random as rand
import time
import winsound as win

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
    win.PlaySound('Gunshot', win.SND_FILENAME)
    print("John has died...")
    win.PlaySound('Death', win.SND_FILENAME)
    exit()


# ---------- Player Weapons ----------
def silver_revolver():
        #revolver does 20 - 100 damage
        damage = rand.randint(20, 100)
        return int(damage)

def winchester_rifle():
    damage = rand.randint(15, 20)
    return(damage)

def zombie_fist():
    damage = rand.randint(1, 3)
    return int(damage)

def knife():
    #knife does 1 - 4 damage.
    damage = rand.randint(3, 4)
    return int(damage)

def fists():
    #fists do 1 - 2 damage.
    damage = rand.randint(1, 2)
    return int(damage)

def axe():
    #axe does 4 - 6 damage.
    damage = rand.randint(4, 6)
    return int(damage)

def dev_gun():
    #does all the damage
    damage = 100000000000000
    return int(damage)

def revolver(ammo):
    if ammo > 0:
        #revolver does 20 - 100 damage
        damage = rand.randint(20, 100)
        return int(damage)
    else:
        print("The revolver is out of ammo...")

def baseball_bat():
    damage = 6
    return int(damage)

def pistol():
    damage = rand.randrange(5, 20)
    return int(damage)

def werewolf_claws():
    damage = rand.randint(100, 200)
    return(damage)

def big_gun():
    damage = rand.randint(10, 30)
    return(damage)

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
                    print ("John used scraps of cloth to heal himself for", heal_amount, "!")

        while e_tp < p_tp:
            e_tp = e_tp + 1
            # print("Enemy points:", e_tp)
            did_hit = hit_attempt()
            if did_hit == "hit":
                 p_hp = (p_hp - e_dmg)
                 print(e_name, "hit John")
                 print("John has", p_hp, "Health")
            elif did_hit == "miss":
                 print (e_name, "missed John")
                 print("John has", p_hp, "Health")
                    
    if e_hp <= 0 and p_hp > 0:
        print("The", e_name, "was killed by John!")
        return ("John Wins")
    elif p_hp <= 0 and e_hp > 0:
        print("John was mortally wounded, and died!")
        win.PlaySound('Death', win.SND_FILENAME)
        exit()
    else:
        print("Neither John, nor ", e_name, "Won the fight")
        win.PlaySound('Death', win.SND_FILENAME)
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

        exit()
    else:
        print("Neither John, nor the Werewolf were victorious...")
        exit()
# ---------------------
def woods():
    play_hp = 60
    player_wep = knife()
    player_wep_name = "Knife"
    print("John, in his desperation flees into the woods...")
    time.sleep(1)
    print("Looking around in the woods John sees an old wood shed.")
    time.sleep(1)
    wood1 = input("Where does John go?.. (Shed/Woods)")
    wood1 = wood1.upper()
    while wood1 == "SHED":
        time.sleep(1)
        print("John looks around the old wood shed, and quickly finds an old wood axe...")
        player_wep = axe()
        player_wep_name = "Axe"
        print("John leaves the shed.")
        wood1 = "WOODS"
    else:
        print("The Woods are dark and spooky, likley home to many creatures...")
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
            print("John digs up the grave, glancing around... His hand strikes cold flesh as a Zombie with an axe rises from the grave...")
            zombie_wep = axe()
            combat(20, "Zombie", player_wep, zombie_wep, player_wep_name, play_hp) # Maybe make a special Zombie Combat
        elif grave == "2":
            time.sleep(2)
            print("digging through the grave, John finds a revolver, and several silver bullets...")
            player_wep = silver_revolver()
            play_wep_name = "Sliver Bullet Revolver"
            time.sleep(2)
            print("Again John hears the growling and the howling deep in the woods, but it sounds almost human...")
        elif grave == "13":
            time.sleep(2)
            print("Overcome with curiosity, John looks around...")
            time.sleep(2)
            print("looking behind a massive tree, John sees a hollowed out trunk. Inside he finds a strange weapon")
            player_wep = dev_gun()
            play_wep_name = "Alien Gun"
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
        werewolf_combat(200, player_wep, werewolf_claws(), play_wep_name, play_hp)

def Mansion():
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
        mansion1 = input("lining the ground floor of this massive room, there are 3 doors. Which does john enter? (d1/d2/d3)")
        while mansion1 == "d1":
            time.sleep(2)
            print("The door leads into a large room.")
            time.sleep(2)
            print("Sitting at a card table in the center of this room, two gang members see John, and pull their pistols...")
            divide()
            gunshot()
            combat(15, "Mobster",  player_wep, pistol(), player_wep_name, play_hp)
            time.sleep(2)
            print("John takes a brief moment to grab the mobster's pistol, and engages the other mobster.")
            player_wep = pistol()
            player_wep_name = "Pistol"
            time.sleep(2)
            divide()
            gunshot()
            combat(15, "Mobster",  player_wep, pistol(), player_wep_name, play_hp)
            time.sleep(1)
            print("Glancing around the room, John looks at the carnage he caused and tends his wounds...")
            time.sleep(2)
            mansion2 = input("Looking around, this card room seems to lead into another room, likely a dining hall. Do you venture in, or go back?: (Back/in)")
            mansion2 = mansion2.upper()
            if mansion2 == "IN":
                time.sleep(2)
                print("Venturing into the next room, John finds himself in a large dining hall. Sitting in the corner is a man wearing a tank top and a gold chain.")
                time.sleep(2)
                print("Mobster: Heh, you killed my boys. You're gonna answer to the boss now!")
                time.sleep(2)
                print("John: what do you want with me?")
                time.sleep(2)
                mansion3 = input("Mobster: You can do this peacefully or I can kill you! (Fight/Surrender)")
                mansion3 = mansion3.upper()
                while mansion3 == "FIGHT":
                    player_wep = winchester_rifle()
                    player_wep_name = "Winchester rifle"
                    time.sleep(2)
                    print("John leaps to the  wall, and grabs a winchester rifle out of the display case.")
                    divide()
                    time.sleep(2)
                    gunshot()
                    gunshot()
                    combat(45, "Big Mobster", big_gun(), player_wep, player_wep_name, play_hp)
                    divide()
                    print("Searching the dying mobster, John finds a paper, with the following printed on it: Digit 1 =", dig1)
                    mansion3 = "OTHER"
                if mansion3 == "SURRENDER":
                    print("PLACEHOLDER")
                elif mansion3 == "OTHER":
                    mani = "main"
                    mansion1 = ""
        if mansion1 == "d2":
            time.sleep(2)
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

# ---------------------
dig1 = rand.randint(0, 9)
dig2 = rand.randint(0, 9)
dig3 = rand.randint(0, 9)
dig4 = rand.randint(0, 9)
# ---------------------
play_hp = 60
player_wep = knife()
# combat(HP, "ENEMY NAME", player_wep, enemy_wep, "Player wep name", player's hp)
# ---------------------
print("John was a average man he loved taking hikes, exploring nature, and his desk job.")
time.sleep(2)
print("One day John was out on a mountain trail enjoying his weekend off, when he encountered a cave.")
time.sleep(3)
print("John ventured inside, not seeing the signs of recent human activity...")
time.sleep(3)
c1 = input("Leaping from the shadows, a stranger in a ski mask, and heavy jacket screams and jabs at John! What does he do? (Attack, or Surrender): ")
c1 = c1.upper()
divide()
if c1 == "ATTACK":
   Mansion()

   #masked_wep = knife()
    #combat(20, "Masked Man", player_wep, masked_wep, "knife", play_hp)

else:
    print("The masked man throws a burlap sack over John's head, and hits him...")
    time.sleep(2)
    print("John awakens in darkness, with the sounds of a car around him...")
    time.sleep(2)
    print("John quickly realizes that he is in a car's trunk.")
    time.sleep(2)
    print("John hears voices coming around the car, and sees that he has a chance to escape by kicking the trunk open...")
    time.sleep(2)
    c2 = input("What does John do?: (Wait, or Escape):")
    c2 = c2.upper()
    if c2 == "ESCAPE":
        print("John Kicks the trunk open with a loud THUD, as one of the gang members in knocked out. However one still stands...")
        divide()
        bounce_wep = knife()
        combat(35, "Bouncer", player_wep, bounce_wep, "knife", play_hp)
        time.sleep(2)
        print("John looks around him, and sees two options, a missive gothic mansion, or a dense dark wood")
        time.sleep(2)
        c3 = input("Do you dare venture into the Mansion, or do you flee into the woods...(woods/house)")
        c3 = c3.upper()
        if c3 == "HOUSE":
            time.sleep(2)
            print("HOUSE PLACEHOLDER")
            Mansion()

        else:
            time.sleep(2)
            print("John flees into the woods, and heads towards civilization. ")
            time.sleep(2)
            woods()
    else:
        print("John is lifted out of the trunk, and carried into the mansion.")
        time.sleep(2)
        print("Carried downstairs, and thrown into a cell, John looks around and through the darkness of the cell.")
        time.sleep(2)
        print("Looking around the cell, and into the hall John can see a guard making rounds past the cells, he aslo notices some worn bricks at the back of his cell.")
        time.sleep(2)
        c4 = input("What does John do?...(dig/distract)")
        if c4 == ("dig"):
            time.sleep(4)
            print("3 months later... John emerges into sunlight into a hill behind the mansion.")
            time.sleep(2)
            print("John ventures into the woods in search of freedom...")
            woods()
            time.sleep(2)
            c5 = input("John, now facing a dilemma may venture into the mansion to seek vengeance or flee to the woods...(Woods/House)")
            c5 == c5.upper()
            if c5 == "WOODS":
                time.sleep(2)
                print("John decides to flee into the woods...")
                time.sleep(2)
                woods()
            else:
                time.sleep(2)
                print("John decides to enter the house to extract his revenge...")
                Mansion()
