from klasy_zadanie2 import Informatyk
from klasy_zadanie3 import Student

class StudiujacyInformatyk(Informatyk, Student):
    def __init__(self, imie, nazwisko, pensja):
        Informatyk.__init__(self, imie, nazwisko, pensja)
        Student.__init__(self, imie, nazwisko)


studentInformatyk_Janek = StudiujacyInformatyk("Janek", "Pacek", 1500)
print()
print(studentInformatyk_Janek.imie, studentInformatyk_Janek.nazwisko)
studentInformatyk_Janek.programuj()
print(studentInformatyk_Janek.pensja)
studentInformatyk_Janek.dodaj_ocene("4+")
print(studentInformatyk_Janek.oceny)
