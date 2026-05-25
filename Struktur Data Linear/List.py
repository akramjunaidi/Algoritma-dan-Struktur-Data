#List 

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))  # 2
print(fruits.count('tangerine')) # 0

print(fruits.index('banana'))  # 3
print(fruits.index('banana', 4)) # 6

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop()) # menampilkan yang dihapus
print(fruits)  # list setelah pop