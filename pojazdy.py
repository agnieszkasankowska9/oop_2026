class Pojazd:
    def jedz(self):
        print("Jadę....")

    def hamuj(self):
        print("Hamuję....")

class Samochod(Pojazd):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Honda(Samochod):
    def __init__(self, model):
        super().__init__("Honda", model)


audi = Samochod("Audi", "A4")
audi.jedz()

honda = Honda("Civic")
honda.hamuj()
