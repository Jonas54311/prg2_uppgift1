from random import randint
from os import system

class Spelare:
    def __init__(self, namn=""):
        self.namn = namn
        self.poäng = 0
        self.slag = 0
    
    def kasta(self):
        self.slag = randint(1, 6)
    
    def vinn_runda(self):
        self.poäng += 1
        print(f"{self.namn} vann rundan\n")

while True:
    spelare = []

    for s in range(2):
        spelare.append(Spelare(input("Spelare1 namn: ")))

    while spelare[0].poäng < 5 and spelare[1].poäng < 5:
        system("cls")
        for s in range(2):
            spelare[s].kasta() 
            print(f"{spelare[s].namn} kastade: {spelare[s].tärning}\n")

        if spelare[0].tärning == spelare[1].tärning:
            print("Oavgjort")
        else:
            spelare[max([spelare[0].slag, 0], [spelare[1].slag, 1])[1]].vinn_runda()
        for s in range(2):
            print(f"{spelare[s].namn}: {spelare[s].poäng} poäng\n")
        input("")

    system("cls")
    print(f"{spelare[next(max(next(iter([spelare[0].poäng, spelare[0].position])), next(iter([spelare[1].poäng, spelare[1].position]))))].namn} vann!")
    for s in range(2):
        print(f"\n{spelare[s].namn}: {spelare[s].poäng} poäng")
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