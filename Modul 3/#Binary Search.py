#Binary Search

def binary_search(arr, target):
    n = len(arr) 
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

data_terurut = [10, 20, 30, 40, 50]
angka_dicari = 40

hasil_pencarian = binary_search(data_terurut, angka_dicari)

if hasil_pencarian != -1:
    print(f"Angka {angka_dicari} ditemukan di index: {hasil_pencarian}")
else:
    print(f"Angka {angka_dicari} tidak ditemukan.")