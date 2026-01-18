from klasy_zadanie1 import Pracownik


class Informatyk(Pracownik):

    def programuj(self):
        print("Programuję....")

class Ksiegowy(Pracownik):

    def wylicz_roczna_pensja(self, pracownik):
        return pracownik.pensja * 12


marek_informatyk = Informatyk("Marek", "Talarek", 10000)
marek_informatyk.programuj()
print("-"*10)
jan_ksiegowy = Ksiegowy("Jan", "Kos", 9000)
roczna_pensja_Marka_informatyka = jan_ksiegowy.wylicz_roczna_pensja(marek_informatyk)
print(f"Roczna pensja informatyka Marka to: {roczna_pensja_Marka_informatyka}")