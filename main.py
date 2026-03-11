from allat import Allat
from emlos import Emlos, Macska, Kutya

allat1 = Allat("Bodri", "kutya", 5, "kert", "közepes")
allat2 = Allat("Cirmi", "macska", 3, "ház", "közepes")

print(f"Allat 1: {allat1}")
print(f"Allat 2: {allat2}")

print("\nEmlősök:\n")

emlos1 = Emlos("Morzsi", "kutya", 5, "kert", "barna")
emlos2 = Emlos("Cirmi", "Macska", 3, "Hát", "cirmos")

print(emlos1)
print(emlos2)

print("\nMacska:\n")

macska1 = Macska("Cirmi", 4,"ház", "sziámi")

print(macska1)
macska1.dorombol()

print("\nKuya:\n")

kutya1 = Kutya("Morzsa", 5, "kert", "barna")
print(kutya1)
kutya1.ugat()