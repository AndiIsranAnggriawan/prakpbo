class Bangun_Ruang:
    __vendor_message = "Layang Layang"
    nama           =""
    diameter1      =""
    diameter2      =""
    luas           =""

    def __init__(self, nama):
        self.nama = nama

    def get_vendor_message(self):
        print(self.__vendor_message)

    def set_diameter1(self,diameter1):
        self.diameter1 = diameter1

    def set_diameter2(self,diameter2):
        self.diameter2 = diameter2
 
    def set_luas(self,luas ):
        self.luas = luas

ly = Bangun_Ruang("Objek Layang-layang Pertama")
ly1 = Bangun_Ruang("Objek Layang-layang Kedua")
ly2 = Bangun_Ruang("Objek Layang-layang Ketiga")

ly.set_diameter1(14)
ly1.set_diameter1(16)
ly2.set_diameter1(18)

ly.set_diameter2(10)
ly1.set_diameter2(12)
ly2.set_diameter2(14)

ly.luas = 0.5 * ly.diameter1*ly.diameter2
ly1.luas = 0.5 * ly1.diameter1*ly1.diameter2
ly2.luas = 0.5 * ly2.diameter1*ly2.diameter2

print("%s\nDiameter 1  adalah : %d \nDiameter 2  adalah : %d \nLuas Layang-layang adalah : %s\n" % (ly.nama,ly.diameter1, ly.diameter2,ly.luas))
print("%s\nDiameter 1  adalah : %d \nDiameter 2  adalah : %d \nLuas Layang-layang adalah : %s\n" % (ly1.nama,ly1.diameter1, ly1.diameter2,ly1.luas))
print("%s\nDiameter 1  adalah : %d \nDiameter 2  adalah : %d \nLuas Layang-layang adalah : %s\n" % (ly2.nama,ly2.diameter1, ly2.diameter2,ly2.luas))
