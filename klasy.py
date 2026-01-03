class Czlowiek:
    gatunek = "Homo Sapiens"  #atrybut klasy

    #atrybuty obiektu:
    def __init__(self, imie, plec):
        self.imie = imie
        self.plec = plec
        print(f"Niech powstanie czlowiek o imieniu {imie}")

    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imie {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("mezczyzna")
        else:
            print("kobieta")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

# adam = Czlowiek("Adam", "M")
# adam.przedstaw_sie()
# ewa = Czlowiek("Ewa", "K")
# ewa.przedstaw_sie()


class Dziecko(Czlowiek):
    def baw_sie(sel):
        print("Ale zabawa!!! xd")

    def przedstaw_sie(self):
        print(f"Czesc, jestem {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("chlopcem")
        else:
            print("dziewczynka")


kain = Dziecko("Kain", "M")
kain.baw_sie()
kain.przedstaw_sie()

