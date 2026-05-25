def linear_search(arr, target): 
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1
data = [4, 7, 1, 9]
angka_dicari = 1

hasil = linear_search(data, angka_dicari)
if hasil != -1:
    print("Angka", angka_dicari, "ada indeks ke", hasil)
else:
    print("Angka", angka_dicari, "tidak ditemukan")









    