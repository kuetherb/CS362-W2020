# -*- coding: utf-8 -*-
"""
Created on 1/18/2020

@author: Braeden Kuether
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = testUtility.getNames()

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Get box dict from testUtility.py file
box = testUtility.getBoxes(nV)

#Test scenario #2, removing three different values from the box dictionary
del box['Woodcutter']
del box['Village']
del box['Chancellor']

#Get supply order from testUtility.py file
supply_order = testUtility.getSupplyOrder()

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])
#Get supply cards from testUtility.py file
testUtility.supplyCards(nC, nV, player_names, supply)

#initialize the trash
trash = testUtility.getTrash()

#Costruct the Player objects
players = testUtility.getPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
