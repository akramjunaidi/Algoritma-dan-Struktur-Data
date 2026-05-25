def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Tukar posisi
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

data_latihan_3 = [9, 3, 5, 1]
print("Data awal:", data_latihan_3)

hasil_sorting = selection_sort(data_latihan_3)
print("Hasil sorting:", hasil_sorting)









