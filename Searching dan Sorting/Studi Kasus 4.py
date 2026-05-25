def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1 

data_latihan_2 = [2, 4, 6, 8, 10]
angka_dicari_2 = 8

hasil = binary_search(data_latihan_2, angka_dicari_2)
if hasil != -1:
    print("Angka", angka_dicari_2, "ada di indeks ke-", hasil)
else:
    print("Angka tidak ditemukan")




