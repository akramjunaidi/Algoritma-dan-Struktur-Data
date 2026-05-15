#Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data = [12, 7, 25, 9, 15]
cari = 9

hasil = linear_search(data, cari)
if hasil != -1:
    print("Angka", cari, "ditemukan di index:", hasil)
else:
    print("angka tidak ditemukan")