#Stack untuk membalikkan kata

kata_asli = "KAMPUS"
stack = [] 
kata_terbalik = ""

for huruf in kata_asli:
    stack.append(huruf)

while stack != []: 
    huruf_terakhir = stack.pop() 
    kata_terbalik = kata_terbalik + huruf_terakhir 

print("Kata asli:", kata_asli)
print("Kata dibalik:", kata_terbalik)














