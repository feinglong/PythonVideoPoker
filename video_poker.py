from machine import *
from gain import *

def partie(mise, bankroll):
    bankroll = bankroll - mise
    main = machine()
    g, resultat = gain(main, mise)
    bankroll += g
    return resultat, bankroll


def video_poker():
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
            while bankroll - mise_joueur < 0 :
                print("Bet too high! please try again.")
                mise_joueur = int(input("Add you bet : "))
                
                
video_poker()