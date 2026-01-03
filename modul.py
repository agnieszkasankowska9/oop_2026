#przekazywanie argumentów do funkcji

#argumenty pozycyjne



# *args - wiele argumentów

# def dodaj2(*args):
#     wynik = 0  #zmienna lokalna wynik
#     for arg in args:
#         wynik += arg
#     return wynik

#zmianna globalna
# wynik = dodaj2(1,2,3,4)
# #print(wynik)


def dodaj3(*args, verbose=False):
    if verbose == True:
        print(f"Wykonam działanie dodawania. Dodam {args}")
    wynik = 0  #zmienna lokalna wynik
    for arg in args:
        wynik += arg
    return wynik

wynik = dodaj3(1,2,3,4,verbose=True)
print(wynik)


#argumenty słownikowe
def funkcja(**kwargs):
    print(kwargs)
    print(type(kwargs))

funkcja(verbose=True, parametr ="wartość")