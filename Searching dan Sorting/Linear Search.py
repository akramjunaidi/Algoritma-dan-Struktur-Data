def linear_search(arr, target): 
     for i in range (len(arr)):
         if arr[i] == target:
             return i
     return -1
data = [12, 7, 25, 9, 15]
angka_dicari = 9
hasil = linear_search(data, angka_dicari)
if hasil != -1:
    print("Angka", angka_dicari, "ada indeks ke", hasil)
else:
    print("Angka", angka_dicari, "tidak ditemukan")










