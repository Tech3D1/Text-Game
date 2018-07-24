#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:10:52 2018
@author: stem
"""
import random as rand
import time
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
# Player Weapons    
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
                    print ("John missed the", e_name, "with the", p_wep_name, "!")
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
                 print("The enemy hit John")
                 print("John has", p_hp, "Health")
            elif did_hit == "miss":
                 print ("The enemy missed John")
                 print("John has", p_hp, "Health")
                    
    if e_hp <= 0 and p_hp > 0:
        print("The", e_name, "was killed by John!")
        return ("John Wins")
        return
    elif p_hp <= 0 and e_hp > 0:
        print("John was mortally wounded, and died!")
        exit()
    else:
        print("Something went wrong")
# ---------------------
# ---------------------
dig1 = rand.randint(0, 9)
dig2 = rand.randint(0, 9)
dig3 = rand.randint(0, 9)
dig4 = rand.randint(0, 9)
# ---------------------
play_hp = 50
player_wep = knife()
#combat(HP, "ENEMY NAME", player_wep, enemy_wep, "Player wep name", player's hp)
# ---------------------
print("John was a average man he loved taking hikes, exploring nature, and his desk job.")
time.sleep(3)
print("One day John was out on a mountain trail enjoying his weekend off, when he encountered a cave.")
time.sleep(3)
print("John ventured inside, not seeing the signs of recent human activity...")
time.sleep(3)
c1 = input("Leaping from the shadows, a stranger in a ski mask, and heavy jacket screams and jabs at John! What does he do? (Attack, or Surrender): ")
c1 = c1.upper()
divide()
if c1 == "ATTACK":
    masked_wep = knife()
    combat(20, "Masked Man", player_wep, masked_wep, "knife", play_hp)

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
        c3 = input("Do you dare venture into the Mansion, or do you flee into the woods...(woods/house)")
        c3.upper()
        if c3 == "HOUSE":
            time.sleep()
        else:
            time.sleep(2)
            print("John flees into the woods, and heads towards civilization. ")
            time.sleep()
    else:
        print("John is lifted out of the trunk, and carried into the mansion.")
        time.sleep(1)
        print("Carried downstairs, and thrown into a cell, John looks around and through the darkness of the cell.")
        time.sleep(1)
        print("Looking around the cell, and into the hall John can see a guard making rounds past the cells, he aslo notices some worn bricks at the back of his cell.")
        time.sleep(1)
        c4 = input("What does John do?...(dig/distract)")
        if c4 == ("dig"):
            time.sleep(4)
            print("3 months later... John emerges into sunlight into a hill behind the mansion.")
            time.sleep(1)
            c5 = input("John, now facing a dilema may venture into the mansion to seek vengance or flee to the woods...(flee/vengance)")
        
        
        
        
        
        