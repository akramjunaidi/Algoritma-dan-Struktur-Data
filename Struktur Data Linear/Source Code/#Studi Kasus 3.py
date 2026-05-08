#Linked List Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node("Data Pertama")
n2 = Node("Data Kedua")
n3 = Node("Data Ketiga")

n1.next = n2
n2.next = n3

print("Mulai menelusuri Linked List:")

gerbong_saat_ini = n1 # Kita mulai dari gerbong terdepan (n1)

while gerbong_saat_ini != None:
    print("Membaca:", gerbong_saat_ini.data) 
    gerbong_saat_ini = gerbong_saat_ini.next 
print("Selesai menelusuri!")




