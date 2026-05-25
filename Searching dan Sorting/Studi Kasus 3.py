def linear_search(arr, target): 
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data_latihan_1 = [4, 7, 1, 9]
angka_dicari_1 = 1

hasil = linear_search(data_latihan_1, angka_dicari_1)
if hasil != -1:
    print("Angka", angka_dicari_1, "ada di indeks ke-", hasil)
else:
    print("Angka", angka_dicari_1, "tidak ditemukan")






