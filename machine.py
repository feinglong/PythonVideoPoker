import random

def premier_tirage(deck):
    tirage = random.sample(deck, 5)
    for x in tirage:
        deck.remove(x)
    return tirage, deck

def choix_cartes(tirage):
    jeu = []
    for x in tirage:
        choix = input('Keep this card ['+ x +'] ? y/n : ')
        if choix == 'y':
            jeu.append(x)
    return jeu

def deuxieme_tirage(deck, main):
    reste = 5 - len(main)
    tirage = random.sample(deck, reste)
    main.extend(tirage)
    return main

def machine():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    pt_jeu, nv_deck  = premier_tirage(deck)
    print('premier tirage :', pt_jeu)
    main = choix_cartes(pt_jeu)
    dt_jeu = deuxieme_tirage(nv_deck, main)
    print('dernier finale :',dt_jeu)
    return dt_jeu