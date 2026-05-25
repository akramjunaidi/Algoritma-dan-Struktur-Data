def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

nilai_belum_urut = [75, 80, 65, 90, 85]
nilai_terurut = bubble_sort(nilai_belum_urut.copy())

print("Nilai sebelum diurutkan:", nilai_belum_urut)
print("Nilai setelah diurutkan:", nilai_terurut)








