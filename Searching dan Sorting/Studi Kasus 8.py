dokumen = "LAPORAN NILAI MAHASISWA TEKNOLOGI INFORMASI"
kata_kunci = "MAHASISWA"

ditemukan = False
for i in range(len(dokumen) - len(kata_kunci) + 1):
    if dokumen[i:i+len(kata_kunci)] == kata_kunci:
        print(f"Kata '{kata_kunci}' ditemukan pada indeks ke-{i}")
        ditemukan = True

if not ditemukan:
    print(f"Kata '{kata_kunci}' tidak ditemukan dalam dokumen.")










    