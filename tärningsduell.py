from random import randint
from os import system

class Tarningsspel:
    def __init__(self, spelare):
         self.spelare = spelare
         self.resultat = []
         self.runda = 0

    def spela_runda(self):
        system("cls")
        self.resultat = []
        self.runda += 1
        print(f"Runda {self.runda}")
        for P in range(3):
            self.resultat.append(self.spelare[P].kasta())
            print(f"{str(self.spelare[P].namn) + " slog:":<{max(len(self.spelare[0].namn), len(self.spelare[1].namn)) + 8}}{self.spelare[P].tärningar[0].slag} {self.spelare[P].tärningar[1].slag}", end=" ")
            if self.spelare[P].tärningar[0].slag == 6 and self.spelare[P].tärningar[1].slag == 6:
                self.spelare[P].poäng += 2
                print("och får två extrapoäng")
            elif self.spelare[P].tärningar[0].slag == 6 or self.spelare[P].tärningar[1].slag == 6:
                self.spelare[P].poäng += 1
                print("och får ett extrapoäng")
            else:
                print("")
        self.resultat = sorted(self.resultat, reverse=True)
        print(self.resultat)
        if self.resultat[0][0] == self.resultat[1][0]:
            print("\nOavgjort\n")
        else:
            self.spelare[self.resultat[0][1]].vinn_runda()

        prnt_score()
        input("")

class Spelare:
    def __init__(self, namn="", idnum=0):
        self.namn = namn
        self.idnum = idnum
        self.poäng = 0
        self.rundor_vunnit = 0
        self.tärningar = [Tarning(), Tarning()]
    
    def kasta(self):
        for k in range(2):
            self.tärningar[k].kasta()
        return [self.tärningar[0].slag + self.tärningar[1].slag, self.idnum]
    
    def vinn_runda(self):
        self.poäng += 1
        self.rundor_vunnit += 1
        print(f"\n{self.namn} vann rundan\n")

class Tarning:
    def __init__(self):
        self.slag = 0

    def kasta(self):
        self.slag = randint(1, 6)

def prnt_score():
    for P in range(3):
        print(f"{str(tarningsspel.spelare[P].namn) + ":":<{max(len(tarningsspel.spelare[0].namn), len(tarningsspel.spelare[1].namn), len(tarningsspel.spelare[2].namn)) + 2}}{tarningsspel.spelare[P].poäng} poäng")

spelar = True
while spelar:
    system("cls")
    tarningsspel = Tarningsspel([Spelare(input("Spelare1 namn: "), 0), Spelare(input("Spelare2 namn: "), 1), Spelare(input("Spelare3 namn: "), 2)])
    while True:
        try:
            vinst_poäng = int(input("Poäng för att vinna: "))
            break
        except ValueError:
            print("Måste vara ett heltal")

    while tarningsspel.spelare[0].poäng < vinst_poäng and tarningsspel.spelare[1].poäng < vinst_poäng and tarningsspel.spelare[2].poäng < vinst_poäng:
        tarningsspel.spela_runda()

    system("cls")
    if tarningsspel.spelare[0].poäng == tarningsspel.spelare[1].poäng and tarningsspel.spelare[2].poäng <= tarningsspel.spelare[0] or tarningsspel.spelare[2].poäng == tarningsspel.spelare[1].poäng and tarningsspel.spelare[0].poäng <= tarningsspel.spelare[2] or tarningsspel.spelare[0].poäng == tarningsspel.spelare[2].poäng and tarningsspel.spelare[1].poäng <= tarningsspel.spelare[0]:
        print("Oavgjort")
    else:
        print(f"{tarningsspel.spelare[max([tarningsspel.spelare[0].poäng, 0], [tarningsspel.spelare[1].poäng, 1], [tarningsspel.spelare[2].poäng, 2])[1]].namn} vann!\n")
    prnt_score()
    print("")
    for P in range(3):
        print(f"{tarningsspel.spelare[P].namn} vann {tarningsspel.spelare[P].rundor_vunnit} rundor")
    input("")
    system("cls")

    while True:
        fortsätt = input("Vill ni köra igen? (Y/N) ")
        if fortsätt.lower() == "n":
            spelar = False
        elif fortsätt.lower() != "y":
            print("inte Y eller N")
            continue
        break