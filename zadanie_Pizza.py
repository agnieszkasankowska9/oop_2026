# https://github.com/kkolanski/oop_2026
# Korzystając ze stworzonych uprzednio  figur geometrycznych,
# stwórz klasę Pizza.

# Ma ona bazować na Kole oraz posiadać:
# cenę
# metodę liczącą opłacalność

# Pizza posiada listę składników
# Pizza jest w stanie sprawdzić, czy w składnikach znajduje się alergen

# USER STORIES:
# Jako konsument pizzy chciałbym, żeby aplikacja była w stanie policzyć opłacalność pizzy, żeby móc
# porównywać pizze ze sobą.

# Jako konsument pizzy, chciałbym wiedzieć, czy pizza zawiera alergen na który jestem uczulony.



from zadanie_figury import Kolo

class Pizza(Kolo):
    def __init__(self, d, cena, *args):
        self.cena = cena
        r = d / 2
        super().__init__(r)
        self.args = args


    def oplacalnosc(self):
        self.cena_cm_2 = self.cena / self.policz_pole()
        print(f"Cena za cm2 to: {self.cena_cm_2:.2f} zł")

    def alergeny(self):
        self.alergeny = {
            "ciasto": ["pszenica", "gluten"],
            "sos pomidorowy": ["gluten", "gorczyca", "jaja", "mleko", "seler", "sezam", "soja"],
            "ser": ["mleko", "laktoza"],
            "szynka": ["szynka"],
            "boczek": ["boczek"],
            "pomidor": ["pomidor"],
            "ananas": ["ananas"],
            "pieczarki": ["pieczarki"],
            "cecula": ["cecula"]
        }
        print("-" *25)
        print("Składniki i alergeny:")
        for i in self.args:
            print(f"-{i}: {', '.join(self.alergeny[i])}")
        print("-" * 25)



pizza1 = Pizza(30,80, "ciasto", "ser", "sos pomidorowy", "ananas")
pizza1.oplacalnosc()
pizza1.alergeny()
