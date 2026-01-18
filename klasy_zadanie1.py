class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__pensja = pensja

    # Getter dla imienia
    @property
    def imie(self):
        return self.__imie

    # Setter dla imienia
    @imie.setter
    def imie(self, nowe_imie):
        self.__imie = nowe_imie

    # Getter dla nazwiska
    @property
    def nazwisko(self):
        return self.__nazwisko

    # Setter dla nazwiska
    @nazwisko.setter
    def nazwisko(self, nowe_nazwisko):
        self.__nazwisko = nowe_nazwisko

    # Getter dla pensji
    @property
    def pensja(self):
        return self.__pensja

    # Setter dla pensji
    @pensja.setter
    def pensja(self, nowa_pensja):
        self.__pensja = nowa_pensja


gniewomir_bak = Pracownik("Gniewomir", "Bąk", 5000)
robert_kowalski = Pracownik("Robert", "Kowalski", 6000)
piotr_raczek = Pracownik("Piotr", "Raczek", 7000)


print(gniewomir_bak.imie)
gniewomir_bak.imie = "Gniewko"
print(gniewomir_bak.imie)
print(gniewomir_bak.pensja)
print("-"*10)
print(robert_kowalski.nazwisko)
robert_kowalski.nazwisko = "Kowal"
print(robert_kowalski.nazwisko)
print("-"*10)
print(piotr_raczek.pensja)
piotr_raczek.pensja = 7500
print(piotr_raczek.pensja)
print("-"*10)


