A = [4, 12, 7, 15, 9]

max_val = A[0]

for i in range(1, len(A)):
    if A[i] > max_val:
        max_val = A[i]  

print("Nilai maksimum dalam array adalah:", max_val)

