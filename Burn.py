import random as rand
import newDeck

def deal():
    deck = newDeck.listDeck()
    deck.pop()
    deck.pop()
    return deck

playing = True
while(playing):
    deck = deal()
    userHand = {}
    cpuHand = {}
    userFieldUp = {}
    cpuFieldUp = {}
    userFieldDown = {}
    cpuFieldDown = {}
    fieldPile = {}

    
