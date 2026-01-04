# Napisz klasę FiguraGeometryczna, która będzie zawierała
# metody:
# policz_pole()
# policz_obwód()

# Napisz klasy Prostokąt, Kwadrat, Koło i Trojkat
# oraz zaimplementuj metody z interfejsu FiguraGeometryczna

# Stwórz instancje tych klas i sprawdź ich działanie

from math import pi


class FiguraGeometryczna:   #tu wpisujemy co można zrobić, ale bez obliczeń szczegółowych, np. policzyc pole

    def policz_pole(self):
        pass

    def policz_obwod(self):
        pass


class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def policz_obwod(self):
        return f"Obwod: {self.a *2 + self.b * 2}"

    def policz_pole(self):
        return f"Pole: {self.a * self.b}"



class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)



class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r

    def policz_pole(self): # pi * r **2
        return f"Pole: {pi * self.r **2:.2f}"

    def policz_obwod(self): # 2 * pi * r
        return f"Obwod: {2 * pi * self.r:.2f}"


class Trojkat(FiguraGeometryczna):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def policz_pole(self):
        p = (self.a + self.b +self.c)/2
        return f"Pole: {(p*(p-self.a)*(p-self.b)*(p-self.c))**0.5:.2f}"

    def policz_obwod(self):
        return f"Obwod: {self.a + self.b + self.c}"




prostokat1 = Prostokat(5, 4)
print(prostokat1.policz_pole(), prostokat1.policz_obwod())

kwadrat1 = Kwadrat(10)
print(kwadrat1.policz_pole(), kwadrat1.policz_obwod())

kolo1 = Kolo(5)
print(kolo1.policz_pole(), kolo1.policz_obwod())

trojkat1 = Trojkat(2, 3, 4)
print(trojkat1.policz_pole(), trojkat1.policz_obwod())