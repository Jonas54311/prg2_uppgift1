from random import randint
from os import system

class Spelare:
    def __init__(self, namn=""):
        self.namn = namn
        self.poäng = 0
    
    def kasta(self):
        return randint(1, 6)
    
    def vinn_runda(self):
        self.poäng += 1
        print(f"\n{self.namn} vann rundan\n")

def prnt_score():
    for s in range(2):
        print(f"{str(spelare[s].namn) + ":":<{max(len(spelare[0].namn), len(spelare[1].namn)) + 2}}{spelare[s].poäng} poäng")
    input("")

while True:
    spelare = []
    resultat = [0, 0]

    for s in range(2):
        spelare.append(Spelare(input("Spelare1 namn: ")))

    while spelare[0].poäng < 5 and spelare[1].poäng < 5:
        system("cls")
        for s in range(2):
            resultat[s] = spelare[s].kasta() 
            print(f"{str(spelare[s].namn) + " kastade:":<{max(len(spelare[0].namn), len(spelare[1].namn)) + 10}}{resultat[s]}")

        if resultat[0] == resultat[1]:
            print("\nOavgjort\n")
        else:
            spelare[max([resultat[0], 0], [resultat[1], 1])[1]].vinn_runda()

        prnt_score()

    system("cls")
    print(f"{spelare[max([spelare[0].poäng, 0], [spelare[1].poäng, 1])[1]].namn} vann!\n")
    prnt_score()
    system("cls")

    choosing = True
    while choosing:
        fortsätt = input("Vill ni köra igen? (Y/N) ")
        if fortsätt.lower() == "n":
            choosing = False
        elif fortsätt.lower() == "y":
            break
        else:
            print("inte Y eller N")
    else:
        break
    system("cls")