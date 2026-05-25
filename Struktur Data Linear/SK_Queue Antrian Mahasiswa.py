# Queue Antrian Mahasiswa

from collections import deque

queue = deque()

# Enqueue - mahasiswa datang mengantri
queue.append("Andi")
queue.append("Budi")
queue.append("Citra")

print("Antrian:", list(queue))

# Dequeue - mahasiswa dilayani (FIFO)
dilayani = queue.popleft()
print("Dilayani:", dilayani)

print("Sisa antrian:", list(queue))