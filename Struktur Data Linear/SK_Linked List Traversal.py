# Linked List Traversal

# Definisi Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer ke node berikutnya

# Definisi Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Tambah node di akhir
    def append(self, data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node_baru

    # Traversal - kunjungi semua node
    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Penggunaan
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Linked List:")
ll.traversal()