a = int(input("Masukkan angka 1: "))
b = int(input("Masukkan angka 2: "))
c = int(input("Masukkan angka 3: "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print("Terbesar:", terbesar)
