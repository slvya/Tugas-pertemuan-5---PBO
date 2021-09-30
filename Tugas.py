class Binatang:
    def intro(self):
        print("Beberapa binatang memakan makanan yang berbeda-beda ")
    def makanan(self):
        print("Mayoritas binatang memakan rumput , namun ada beberapa yang tidak memakan rumput")

class Kambing(Binatang):
    def makanan(self):
        print("Kambing memakan rumput")

class Harimau(Binatang):
    def makanan(self):
        print("Harimau tidak memakan rumput , tetapi memakan daging-dagingan")

obj_binatang = Binatang()
obj_Kambing= Kambing()
obj_Harimau = Harimau()

obj_binatang.intro()
obj_binatang.makanan()

obj_Kambing.intro()
obj_Kambing.makanan()

obj_Harimau.intro()
obj_Harimau.makanan()




