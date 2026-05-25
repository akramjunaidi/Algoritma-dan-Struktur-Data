text = "DATA STRUKTUR DATA"
pattern = "DATA"

for i in range(len(text) - len(pattern) + 1):

    if text[i:i+len(pattern)] == pattern:
        print("ketemu di indeks", i)











        
