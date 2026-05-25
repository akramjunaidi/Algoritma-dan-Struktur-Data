#Set

# set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("Isi basket:", basket)

# Mengecek keanggotaan
print('orange' in basket)
print('crabgrass' in basket)

# Set dari dua kata (huruf unik)
a = set('abracadabra')
b = set('alacazam')

print("Set a:", a)
print("Set b:", b)

# Operasi set
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)