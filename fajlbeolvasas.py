from allat import Madar, Keteltu, Hullo
from emlos import Macska, Kutya


allatok = []
with open('adatok/allatok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, faj, eletkor, szorzet_szine = sor.strip().split(',')
        if faj == "kutya":
            allatok.append(Kutya(nev, int(eletkor),"udvar", szorzet_szine))
        if faj == "macska":
            allatok.append(Macska(nev, int(eletkor),"ház", szorzet_szine))
        if faj == "madar":
            allatok.append(Madar(nev, int(eletkor),"kalitka", "kicsi"))
        if faj == "hullo":
            allatok.append(Hullo(nev, int(eletkor),"szikla", "kicsi"))
        if faj == "keteltu":
            allatok.append(Keteltu(nev, int(eletkor),"tópart", "kicsi"))

for allat in allatok:
    print(allat)
    if isinstance(allat, Macska):
        allat.dorombol()
    elif isinstance(allat, Kutya):
        allat.ugat()
    elif isinstance(allat, Madar):
        allat.csiripel()
    elif isinstance(allat, Keteltu):
        allat.brekeg
    elif isinstance(allat, Hullo):
        allat.napozik()