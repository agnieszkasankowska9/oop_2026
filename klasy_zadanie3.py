class Student:
    def __init__(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko
        self.__oceny = []

    # getter dla imienia
    @property
    def imie(self):
        return self._imie

    # setter dla imienia
    @imie.setter
    def imie(self, nowe_imie):
        self._imie = nowe_imie

    # getter dla nazwiska
    @property
    def nazwisko(self):
        return self._nazwisko

    # setter dla nazwiska
    @nazwisko.setter
    def nazwisko(self, nowe_nazwisko):
        self._nazwisko = nowe_nazwisko

    # getter dla ocen
    @property
    def oceny(self):
        return self.__oceny


    def nadpisz_oceny(self, oceny):
        self.__oceny = oceny

    def dodaj_ocene(self, ocena):
        self.__oceny.append(ocena)

    def popraw_ocene(self, index, poprawiona_ocena):
        self.__oceny[index] = poprawiona_ocena

    def usun_ocene(self, ocena):
        self.__oceny.remove(ocena)


marek_zegarek = Student("Marek", "Zegarek")
print(marek_zegarek.imie, marek_zegarek.nazwisko)
marek_zegarek.nadpisz_oceny([5, 5, 5])
print(marek_zegarek.oceny)
marek_zegarek.dodaj_ocene(1)
print(marek_zegarek.oceny)
marek_zegarek.popraw_ocene(3, "3+")
print(marek_zegarek.oceny)
marek_zegarek.usun_ocene(5)
print(marek_zegarek.oceny)
print()

jolanta_iks = Student("Jolanta", "Iks")
print(jolanta_iks.imie, jolanta_iks.nazwisko)
jolanta_iks.nadpisz_oceny([1,2,3,4,5,6])
print(jolanta_iks.oceny)
print()

gustaw_san = Student ("Gustaw", "San")
print(gustaw_san.imie, gustaw_san.nazwisko)
gustaw_san.dodaj_ocene(6)
print(gustaw_san.oceny)