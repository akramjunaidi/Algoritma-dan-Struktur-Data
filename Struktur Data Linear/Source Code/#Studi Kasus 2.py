#Queue antrian mahasiswa

from collections import deque

antrean_mahasiswa = deque()

print("Budi, Siti, dan Joko masuk antrean.")
antrean_mahasiswa.append("Budi")
antrean_mahasiswa.append("Siti")
antrean_mahasiswa.append("Joko")

print("Kondisi antrean saat ini:", antrean_mahasiswa)
yang_dilayani = antrean_mahasiswa.popleft()
print("Saat ini sedang melayani:", yang_dilayani)

print("Kondisi antrean setelahnya:", antrean_mahasiswa)






