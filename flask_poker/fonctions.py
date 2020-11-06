import pandas as pd
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


def decompose_jeu(tirage):
    dic = {}
    indices = range(len(tirage))
    valeur =[]
    couleur= []
    for i,x in zip(indices, tirage):
        dic[i] = x.split('-')
    for x in dic:
        valeur.append(dic[x][0])
        couleur.append(dic[x][1])
    return valeur, couleur

def convert_carte(liste):
    for e,i in zip(liste, range(5)):
        try:
            liste[i] = int(e)
        except:
            if e == 'J':
                liste[i] = 11
            elif e == 'Q':
                liste[i] = 12
            elif e == 'K':
                liste[i] = 13
            elif e == 'A':
                liste[i] = 1
            else:
                continue
    return liste

#Paire : 2 cartes identiques => 1 fois la mise

def paire(tirage):
    valeur, couleur = decompose_jeu(tirage)
    val_1 = pd.Series(valeur)
    uniques = val_1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 4 and sorted(count) == [1,1,1,2]:
        return True
    else:
        return False
   
    
#Double Paire : deux fois 2 cartes identiques => 2 fois la mise

def double_paire(tirage):
    valeur, couleur = decompose_jeu(tirage)
    val_1 = pd.Series(valeur)
    uniques = val_1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1,2,2]:
        return True
    else:
        return False
    

#Brelan : 3 cartes identiques => 3 fois la mise

def brelan(tirage):
    valeur, couleur = decompose_jeu(tirage)
    val_1 = pd.Series(valeur)
    uniques = val_1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 1, 3]:
        return True
    else:
        return False
    
    
#Quinte : 5 cartes identiques => 4 fois la mise

def quinte(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e,i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 or valeur == [1, 10 ,11 ,12, 13]:
        return True
    else:
        return False


#Flush : 5 cartes de la même couleur => 6 fois la mise

def flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    val_1 = pd.Series(couleur)
    if couleur.count(couleur[0]) == 5:
        return True
    else:
        return False
    
    
#Full : 1 paire + 1 brelan => 9 fois la mise

def full(tirage):
    valeur,couleur = decompose_jeu(tirage)
    val_1 = pd.Series(valeur)
    uniques = val_1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [2, 3]:
        return True
    else: 
        return False
    

#Carré : 4 cartes identiques => 25 fois la mise

def carre(tirage):
    valeur,couleur = decompose_jeu(tirage)
    val_1 = pd.Series(valeur)
    uniques = ()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [1, 4]:
        return True
    else: 
        return False
    

#Quinte Flush : 1 quinte de la même couleur => 50 fois la mise

tirage = ['5-h', '7-h', '6-h', '8-h', '4-h']

def quinte_flush(tirage):
    valeur, couleur = decompose_jeu(tirage)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e,i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('True')
    if suite.count('True') == 4 and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False
    

#Quinte Flush Royale : 1 quinte flush avec as, roi, dame, valet, 10 => 250 fois la mise.

def quinte_flush_royale(tirage):
    valeur_gagnante = ['10' , 'J', 'Q' , 'K' , 'A']
    valeur, couleur = decompose_jeu(tirage)
    if sorted(valeur_gagnante) == sorted(valeur) and couleur.count(couleur[0]) == 5:
        return True
    else:
        return False
    
    
def gain(tirage, mise):
    if quinte_flush_royale(tirage) == True :
        gain = mise*250
        message = "***** WIN! Quinte Flush Royale!!! ***** ==> " + str(gain) + " €"
    elif quinte_flush(tirage) == True :
        gain = mise*50
        message = "WIN! Quinte Flush!! ==> " + str(gain) + " €"
    elif carre(tirage) == True :
        gain = mise*25
        message = "WIN! Carré ==> " + str(gain) + " €"
    elif full(tirage) == True :
        gain = mise*9
        message = "WIN! Full ==> " + str(gain) + " €"
    elif flush(tirage) == True :
        gain = mise*6
        message = "WIN! Flush ==> " + str(gain) + " €"
    elif quinte(tirage) == True :
        gain = mise*4
        message = "WIN! Quinte ==> " + str(gain) + " €"
    elif brelan(tirage) == True :
        gain = mise*3
        message = "WIN' Brelan ==> " + str(gain) + " €"
    elif double_paire(tirage) == True :
        gain = mise*2
        message = "WIN! Double Paire ==> " + str(gain) + " €"
    elif paire(tirage) == True :
        gain = mise*1
        message = "WIN! Paire! ==> " + str(gain) + " €"
    else:
        gain = 0
        message = "Lose... try again!"
        
    return gain, message


def partie(mise, bankroll):
    bankroll = bankroll - mise
    main = machine()
    g, resultat = gain(main, mise)
    bankroll += g
    return resultat, bankroll


def video_poker():
    bankroll = int(input("Insert money : "))
    mise_joueur = int(input("Add your bet : "))
    
    while bankroll - mise_joueur < 0:
        print("Not enough money... please insert money.")
        bankroll = int(input("Insert money : "))
        mise_joueur = int(input("Add your bet : "))
    
    
    while bankroll - mise_joueur >= 0:
        resultat, bankroll = partie(mise_joueur, bankroll)
        print('resultat : ', resultat)
        print("Bank : ", str(bankroll), "€")
        if bankroll == 0:
            print("Game Over!!")
            break
        else:
            mise_joueur = int(input("Add you bet : "))
            #if bankroll - mise_joueur < 0:
            while bankroll - mise_joueur < 0:
                print("Bet too high! please try again.")
                mise_joueur = int(input("Add you bet : "))
                
            