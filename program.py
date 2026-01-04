from klasy import Czlowiek

adam = Czlowiek("Adam", "M")
# adam.przedstaw_sie()
ewa = Czlowiek("Ewa", "K")
# ewa.przedstaw_sie()

# kain = Dziecko("Kain", "M")
# # kain.baw_sie()
# # kain.przedstaw_sie()
# print(kain)


dziecko = adam + ewa
print(dziecko)