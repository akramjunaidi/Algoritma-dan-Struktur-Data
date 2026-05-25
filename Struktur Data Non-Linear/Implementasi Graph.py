# Representasi Adjacency List
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print("Adjacency List:")
for node in graph:
    print(node, "->", graph[node])