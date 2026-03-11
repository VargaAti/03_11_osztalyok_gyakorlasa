class Allat:
    def __init__(self, nev_, faj_, eletkor_, elohely_, meret_):
        self.nev = nev_
        self.faj = faj_
        self.eletkor = int(eletkor_)
        self.elohely = elohely_
        self.meret = meret_

    def __str__(self):
        return f"{self.nev}, faj: {self.faj}, életkor: {self.eletkor}, élőhelye: {self.elohely}, méret: {self.meret}"