class Gempa:
#member1 variabel
    lok = ""
    scale = 0
    def __init__(self,lokasi,skala):
        self.lok = lokasi
        self.scale = skala
    def dampak(self):
        if self.scale < 2:
            return "dampak gempa tidak berasa"
        elif self.scale <= 4:
            return "dampak gempa bangunan retak-retak"
        elif self.scale <= 6:
            return "dampak gempa bangunan roboh"
        elif self.scale <= 10:
            return "dampak gempa bangunan roboh dan berpotensi tsunami"
        else:
            return "Data tidak valid"
    def cetak(self):
        print("lokasi\t:",self.lok,
        "\nskala\t:",self.scale,
        "\ndampak\t:",self.dampak(),
        "\n-------------------------------------------------------")