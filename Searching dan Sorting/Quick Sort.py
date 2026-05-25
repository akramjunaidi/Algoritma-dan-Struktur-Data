def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
    return quick_sort(left) + middle + quick_sort(right)

data = [10, 7, 8, 9]
hasil = quick_sort(data)
print("Hasil sorting:", hasil)






