class Masin():
    def __init__(self, marka, reng, suret, silindir):
        self.marka = marka
        self.reng = reng
        self.suret = suret
        self.silindir = silindir

    def yukseksuretli(self, yukseksuretli=False):
        if yukseksuretli:
            return f"{self.marka} masin suretlidir"
        else:
            return f"{self.marka} masin yavasdir"
    
    def suret_artir(self, artis):
        self.suret += artis
        return f"{self.marka} masinin suret {self.suret}-dir."
    
    def rengi_guncelle(self, yeni_reng):
        self.reng = yeni_reng
        return f"{self.marka} masinin yeni rengi {self.reng}-dir."

Mercedes = Masin("Mercedes", "qara", 250, 4)
BMW = Masin("BMW", "ag", 230, 4)
RangeRover = Masin("Range Rover", "qirmizi", 180, 4)

print(f"{Mercedes.marka}-in {Mercedes.reng} var ve max sureti {Mercedes.suret}-dir. Onun {Mercedes.silindir} silindiri var")

print(Mercedes.rengi_guncelle("mavi"))

print(RangeRover.suret_artir(20))