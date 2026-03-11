class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = int(eletkor_)
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f"{self.nev}, faj: {self.faj}, életkor: {self.eletkor}, élőhelye: {self.elohely}, méret: {self.meret}"

class Madar(Allat):
    def __init__(self, nev_, eletkor_, elohely_, meret_):
        super().__init__(nev_, "madár", eletkor_, elohely_, meret_)
    
    def csiripel(self):
        print(f"{self.nev} csiripel." )

class Keteltu(Allat):
    def __init__(self, nev_, eletkor_, elohely_, meret_):
        super().__init__(nev_, "kétéltű", eletkor_, elohely_, meret_)
    
    def brekeg(self):
        print(f"{self.nev} brekeg.")

class Hullo(Allat):
    def __init__(self, nev_, eletkor_, elohely_, meret_):
        super().__init__(nev_, "hüllő", eletkor_, elohely_, meret_)

    def napozik(self):
        print(f"{self.nev} napozik a kövön.")