#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:10:52 2018

@author: stem
"""
import random as rand
import numpy as math
import os
t1 = 2
t2 = math.sqrt(t1)
os.system("clear")


#---------------------

dig1 = rand.randint(0, 9)
dig2 = rand.randint(0, 9)
dig3 = rand.randint(0, 9)
dig4 = rand.randint(0, 9)

#---------------------
player_wep = fists

'''print("WELCOME to text adventure!")
print("John was exploring a cave by himself and got lost deep in the cave. he decides to explore some more and gets lost inside a crypt ")
c1 = int(input("A man wearing a ski mask jumps at you from behind and begins to drag you around. You have a choice (1): Attack (2): Surrender "))
if c1 == 1:
    ###
elif c1 == 2:
    ###
else:
    print("Invalid Input")'''


p_hp = 300

def combat(e_hp, e_name, p_weapon):
    while p_hp > 0 and e_hp > 0:
        p_turns = 0
        e_turns = 0
        turn = input("Would you like to Attack or Heal: ")
        turn = turn.upper()
        if turn == "ATTACK":
            
            did_hit = hit_attempt()
            if did_hit == "hit":
                e_hp - p_weapon
                print("John's", p_weapon, "Hit")
            elif did_hit == "crit":
                e_hp - (int(p_weapon) * 2)
                print("John's", p_weapon, "struck true, and crit", e_name)
            elif did_hit == "miss":
                print ("John missed the", e_name, "with the", p_weapon, "!")
        elif turn == "HEAL":
            if p_hp >= 300:
                print("You are already at or above Max Health")
            elif p_hp < 300:
                 heal_amount = rand.randint(1, 6)
                 p_hp + heal_amount
                 print ("John used scraps of cloth to heal himself for", heal_amount, "!")
    if e_hp == 0 and p_hp > 0:
        print("The", e_name, "was killed by John!")
    elif p_hp == 0 and e_hp > 0:
        print("John was mortally wounded, and died!")
    else:
        print("Something went wrong")
        
        
        
def hit_attempt():
    hit_chance = rand.randint(1, 20)
    if hit_chance == 1:
        return "crit"
    else:
        return "hit"
    if hit_chance > 15:
        return "miss"


# Player Weapons    
def knife():
    #knife does 1 - 4 damage.
    damage = rand.randint(1, 4)
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



