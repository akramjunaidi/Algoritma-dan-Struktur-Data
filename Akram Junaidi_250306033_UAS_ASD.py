# Task 1 - Algoritma Dasar
 
# # data mahasiswa berisi nim, nama, dan nilai
# mahasiswa = [
#     [23001, "Andi", 75],
#     [23002, "Budi", 90],
#     [23003, "Citra", 65],
#     [23004, "Dedi", 85],
#     [23005, "Eka", 80]
# ]
 
# # fungsi untuk menentukan kategori nilai mahasiswa
# def kategori_nilai(nilai):
#   # jika nilai lebih dari atau sama dengan 85 maka kategori A
#     if nilai >= 85:
#         return "A"
#   # jika nilai antara 70 sampai 84 maka kategori B
#     elif nilai >= 70:
#         return "B"
#   # jika nilai kurang dari 70 maka kategori C
#     else:
#         return "C"
 
# # looping untuk menampilkan kategori seluruh mahasiswa
# for mhs in mahasiswa:
#     nim = mhs[0]
#     nama = mhs[1]
#     nilai = mhs[2]
#     kategori = kategori_nilai(nilai)
#     print("NIM:", nim, "| Nama:", nama, "| Nilai:", nilai, "| Kategori:", kategori)



# Task 2 - Struktur Data Linear
# from collections import deque

# def enqueue(antrian, nama):
#     antrian.append(nama)

# # fungsi untuk melayani mahasiswa terdepan dari antrian
# def dequeue(antrian):
#     return antrian.popleft()

# # membuat antrian praktikum
# antrian_praktikum = deque()

# # memasukkan mahasiswa ke dalam antrian sesuai urutan
# enqueue(antrian_praktikum, "Andi")
# enqueue(antrian_praktikum, "Budi")
# enqueue(antrian_praktikum, "Citra")
# enqueue(antrian_praktikum, "Dedi")
# enqueue(antrian_praktikum, "Eka")

# print("Kondisi antrian awal:", list(antrian_praktikum))

# # melayani 2 mahasiswa pertama
# # yang_dilayani_1 = dequeue(antrian_praktikum)
# print("Sedang melayani:", yang_dilayani_1)

# # yang_dilayani_2 = dequeue(antrian_praktikum)
# print("Sedang melayani:", yang_dilayani_2)

# print("Kondisi antrian setelah 2 mahasiswa dilayani:", list(antrian_praktikum))

# # fungsi untuk menyimpan mahasiswa yang selesai praktikum ke stack
# def push(stack, nama):
#     stack.append(nama)

# # membuat stack riwayat mahasiswa selesai praktikum
# riwayat_selesai = []

# # Andi selesai praktikum, masuk ke stack
# push(riwayat_selesai, yang_dilayani_1)
# print("Stack setelah Andi selesai:", riwayat_selesai)

# # Budi selesai praktikum, masuk ke stack
# push(riwayat_selesai, yang_dilayani_2)
# print("Stack setelah Budi selesai:", riwayat_selesai)
 


# Task 3 - Searching

# data mahasiswa dari task 1
# mahasiswa = [
#     [23001, "Andi", 75],
#     [23002, "Budi", 90],
#     [23003, "Citra", 65],
#     [23004, "Dedi", 85],
#     [23005, "Eka", 80]
# ]

# # fungsi linear search untuk mencari mahasiswa berdasarkan NIM
# def linear_search(data, nim_dicari):
#     for i in range(len(data)):
#         # cek apakah NIM di posisi i sama dengan NIM yang dicari
#         if data[i][0] == nim_dicari:
#             return i
#     # kembalikan -1 jika NIM tidak ditemukan
#     return -1

# # fungsi binary search untuk mencari mahasiswa berdasarkan NIM
# def binary_search(data, nim_dicari):
#     left = 0
#     right = len(data) - 1

#     #selama batas kiri dan kanan belum bersilang
#     while left <= right:
#         # cari indeks tengah
#         mid = (left + right) // 2
#         if data[mid][0] == nim_dicari:
#             # ketemu, kembalikan posisinya
#             return mid
#         elif nim_dicari < data[mid][0]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     # kembalikan -1 jika NIM tidak ditemukan
#     return -1

# nim_input = int(input("Masukkan NIM yang dicari: "))

# # proses linear search
# print("Hasil Linear Search")
# hasil_linear = linear_search(mahasiswa, nim_input)
# if hasil_linear != -1:
#     print("Nama       :", mahasiswa[hasil_linear][1])
#     print("Nilai      :", mahasiswa[hasil_linear][2])
#     print("Posisi data:", hasil_linear)
# else:
#     print("Mahasiswa dengan NIM", nim_input, "tidak ditemukan")

# # proses binary search
# print("Hasil Binary Search")
# hasil_binary = binary_search(mahasiswa, nim_input)
# if hasil_binary != -1:
#     print("Nama       :", mahasiswa[hasil_binary][1])
#     print("Nilai      :", mahasiswa[hasil_binary][2])
#     print("Posisi data:", hasil_binary)
# else:
#     print("Mahasiswa dengan NIM", nim_input, "tidak ditemukan")



# Task 4 - Sorting

# # data mahasiswa dari task 1
# mahasiswa = [
#     [23001, "Andi", 75],
#     [23002, "Budi", 90],
#     [23003, "Citra", 65],
#     [23004, "Dedi", 85],
#     [23005, "Eka", 80]
# ]

# # fungsi bubble sort untuk mengurutkan nilai mahasiswa dari tertinggi ke terendah
# def bubble_sort(data):
#     n = len(data)

#     for i in range(n):
#         for j in range(n - i - 1):
#             # jika nilai sekarang lebih kecil dari nilai berikutnya, tukar posisi
#             if data[j][2] < data[j + 1][2]:
#                 # tampilkan proses pertukaran
#                 print("Tukar:", data[j][1], "(", data[j][2], ") <->", data[j + 1][1], "(", data[j + 1][2], ")")
#                 # proses pertukaran data
#                 data[j], data[j + 1] = data[j + 1], data[j]

#     return data

# print("Data sebelum sorting:")
# for mhs in mahasiswa:
#     print("NIM:", mhs[0], "| Nama:", mhs[1], "| Nilai:", mhs[2])

# print("Proses pertukaran data:")
# hasil = bubble_sort(mahasiswa)

# print("Hasil akhir sorting (tertinggi ke terendah):")
# for mhs in hasil:
#     print("NIM:", mhs[0], "| Nama:", mhs[1], "| Nilai:", mhs[2])