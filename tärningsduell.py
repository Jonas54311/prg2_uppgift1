from random import randint
from os import system

class Spelare:
    def __init__(self, namn="", position=0):
        self.namn = namn
        self.poäng = 0
        self.position = position
        self.tärning = None
    
    def kasta(self):
        self.tärning = iter([randint(1, 6), self.position])
    
    def vinn_runda(self):
        self.poäng += 1
        print(f"{self.namn} vann rundan\n")

while True:
    spelare = []

    for s in range(2):
        spelare.append(Spelare(input("Spelare1 namn: "), s))

    while spelare[0].poäng < 5 and spelare[1].poäng < 5:
        system("cls")
        for s in range(2):
            spelare[s].kasta() 
            print(f"{spelare[s].namn} kastade: {spelare[s].tärning}\n")

        if next(spelare[0].tärning) == next(spelare[1].tärning):
            print("Oavgjort")
        else:
            spelare[next(max(spelare[0].tärning, spelare[1].tärning))].vinn_runda()
        for s in range(2):
            print(f"{spelare[s].namn}: {spelare[s].poäng} poäng\n")
        input("")

    system("cls")
    if spelare[0].poäng == 5:
        print(f"{spelare1.namn} vann")
    else:
        print(f"{spelare2.namn} vann")
    print(f"\n{spelare1.namn}: {spelare1.poäng} poäng\n{spelare2.namn}: {spelare2.poäng} poäng")
    input("")
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