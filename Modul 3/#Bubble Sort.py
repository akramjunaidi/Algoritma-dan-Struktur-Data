#Booble Sort

def bubble_sort(arr):
    
    n = len(arr)

    for i in range(n):

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# data yang mau diurutkan
data = [5, 3, 8, 1, 2]

# panggil fungsi
hasil = bubble_sort(data)

# tampilkan hasil
print("Data sebelum sorting:", [5, 3, 8, 1, 2])
print("Data setelah sorting:", hasil)
