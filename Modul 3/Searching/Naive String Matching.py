#Naive String Matching

#def naive_string_match(text, pattern):
#    n = len(text)
#    m = len(pattern)
#    posisi_ditemukan = [] # Menyimpan di indeks mana saja pattern cocok

    # Menggeser pattern satu per satu di sepanjang teks
#    for i in range(n - m + 1):
#        j = 0
        
        # Mengecek kecocokan karakter satu per satu
#        while j < m and text[i + j] == pattern[j]:
#            j += 1
            
        # Jika j berhasil mencapai panjang pattern, berarti cocok sepenuhnya!
#        if j == m:
#            posisi_ditemukan.append(i)
            
#    return posisi_ditemukan

# --- MENGGUNAKAN DATA DARI GAMBAR ---
#teks_utama = "DATA STRUKTUR DATA"
#kata_dicari = "DATA"

#hasil = naive_string_match(teks_utama, kata_dicari)

# Menampilkan hasil
#print(f"Teks: '{teks_utama}'")
#print(f"Pattern: '{kata_dicari}'")
#if hasil:
#    print(f"Cocok! Pattern ditemukan pada indeks: {hasil}")
#else:
#    print("Pattern tidak ditemukan.")

text = "DATA STRUKTUR DATA"
pattern = "DATA"

for i in range(len(text) - len(pattern) + 1):

    if text[i:i+len(pattern)] == pattern:
        print("Ketemu di index", i)