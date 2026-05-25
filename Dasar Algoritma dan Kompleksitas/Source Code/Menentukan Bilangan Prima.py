n = int(input("Masukkan angka: "))

if n <= 1:
    print("Bukan bilangan prima")
else:
    is_prima = True
    for i in range(2, n):
        if n % i == 0:
            is_prima = False
            break

    if is_prima:
        print("Bilangan prima")
    else:
        print("Bukan bilangan prima")
