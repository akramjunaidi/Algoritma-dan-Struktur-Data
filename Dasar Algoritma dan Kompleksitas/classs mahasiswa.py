class mahasiswa:
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim

    def getnama(self):
        return self.__nama
    
    def getnama(self):
        return self.__nim
    
    def setnama(self, nama):

    def setnim(self, nim):
        self.__nim = nim

mhs1 = mahasiswa("budi", "12345")
print("nama mahasiswa:", mhs1.getnama())
print("nim mahasiswa:", mhs1.getnim())

mhs1.setnama("andi")
print("nama mahasiswa setelah diubah:", mhs1.getnama())
print("nim mahasiswa setelah diubah:", mhs1.getnama())