batas_atas = int(input("Masukkan batas angka (N): "))
list_prima = []

for num in range(2, batas_atas + 1):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break 
            

    if is_prime:
        list_prima.append(num)

print(f"List Bilangan Prima hingga {batas_atas}: {list_prima}")
