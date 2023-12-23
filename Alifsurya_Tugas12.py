class Hewan:
    nama =""
    Makanan = ""
    jenis = ""
    def __init__(self, nama, makanan, jenis):
        self.nama = nama
        self.makanan = makanan
        self.jenis = jenis
    def cetak(self):
        print(f'{self.nama} adalah salah satu hewan {self.jenis}.\n{self.nama} makanan utamanya adalah {self.makanan}.')
class Spesies(Hewan):
    habitat = ""
    hidup = ""

    def __init__(self, nama, makanan, jenis, habitat, hidup):
        super().__init__(nama, makanan, jenis)
        self.habitat = habitat
        self.hidup = hidup
    
    def cetak(self):
        super().cetak()
        print(f'{self.nama} habitat hidupnya di {self.habitat}.\n{self.nama} masa hidupnya {self.hidup}.\n--------------------------------------')
        
badak = Spesies("Badak","Tumbuhan","Herbivora", "daratan","40 tahun")
badak.cetak()
kelinci = Spesies("Kelinci","Tumbuhan","Herbivora","daratan","2 Tahun")
kelinci.cetak()
anjing = Spesies("Anjing","Daging","Karnivora","daratan","10 Tahun")
anjing.cetak() 
