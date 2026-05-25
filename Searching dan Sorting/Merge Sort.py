def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Rekursif: memecah bagian kiri dan kanan
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        # Proses membandingkan dan menggabungkan (Merging)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Mengecek apakah ada elemen yang tersisa di bagian kiri
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # Mengecek apakah ada elemen yang tersisa di bagian kanan
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# data yang mau diurutkan
data = [8, 4, 2, 6]
# panggil fungsi
hasil = merge_sort(data)
# tampilkan hasil
print("Hasil sorting:", hasil)





