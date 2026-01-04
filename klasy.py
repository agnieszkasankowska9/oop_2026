import random

class Czlowiek:
    gatunek = "Homo Sapiens"  #atrybut klasy

    #atrybuty obiektu:
    def __init__(self, imie, plec):
        self.imie = imie
        self.plec = plec
        print(f"Niech powstanie człowiek o imieniu {imie}.")

    def __add__(self, other):
        if isinstance(other, Czlowiek) and self.plec != other.plec:
            return Dziecko(None, random.choice("M, K"))

    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imię {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("mezczyzną.")
        else:
            print("kobietą.")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")


class Dziecko(Czlowiek):
    def __init__(self, imie, plec):
        super().__init__(imie, plec)
        print(f"Powstaje Dziecko o imieniu {imie}")

    def __str__(self):
        if self.plec=="M":
            return f"Chłopiec {self.imie}"
        else:
            return f"Dziewczynka {self.imie}"

    def baw_sie(sel):
        print("Ale zabawa!!! xd")

    def przedstaw_sie(self):
        print(f"Czesc, jestem {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("chłopcem.")
        else:
            print("dziewczynką.")

