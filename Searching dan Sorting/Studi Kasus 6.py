def linear_search(arr, target): 
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nilai_mahasiswa = [75, 80, 65, 90, 85]
nilai_dicari = 90

hasil = linear_search(nilai_mahasiswa, nilai_dicari)
if hasil != -1:
    print("Nilai", nilai_dicari, "ditemukan pada indeks ke-", hasil)
else:
    print("Nilai tidak ditemukan dalam list.")












    












    