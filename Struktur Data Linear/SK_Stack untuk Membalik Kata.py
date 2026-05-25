# Stack untuk Membalik Kata

stack = []

# Push - masukkan karakter ke stack
kata = "HELLO"
for karakter in kata:
    stack.append(karakter)   # push

print("Stack setelah push:", stack)

# Pop - keluarkan karakter (terbalik)
hasil = ""
while stack:
    hasil += stack.pop()     # pop (LIFO)

print("Kata terbalik:", hasil)