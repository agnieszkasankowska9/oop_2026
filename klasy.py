class Czlowiek:
    gatunek = "Homo Sapiens"  #atrybut klasy

    #atrybuty obiektu:
    def __init__(self, imie, plec):
        self.imie = imie
        self.plec = plec
        print(f"Niech powstanie człowiek o imieniu {imie}.")

    def __add__(self, other):
        pass

    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imię {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("mezczyzną.")
        else:
            print("kobietą.")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

adam = Czlowiek("Adam", "M")
# adam.przedstaw_sie()
ewa = Czlowiek("Ewa", "K")
# ewa.przedstaw_sie()


class Dziecko(Czlowiek):
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


kain = Dziecko("Kain", "M")
# kain.baw_sie()
# kain.przedstaw_sie()
print(kain)
