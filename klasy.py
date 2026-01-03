class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self):
        print("Niech powstanie czlowiek")


adam = Czlowiek()
# print(type(adam))
# print(dir(adam))
# print(dir(Czlowiek))
print(adam.gatunek)