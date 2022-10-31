from collections import deque

adj_list = {"A": ["B", "D"],
            "B": ["A", "C"],
            "C": ["B"],
            "D": ["A", "E", "F"],
            "E": ["D", "F", "G"],
            "F": ["D", "E", "H"],
            "G": ["E", "H"],
            "H": ["G", "F"]}

visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = deque()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

start_node = "A"
visited[start_node] = True
level[start_node] = 0
queue.appendleft(start_node)

while queue:
    working_node = queue.pop()
    bfs_traversal_output.append(working_node)

    for child in adj_list[working_node]:
        if not visited[child]:
            visited[child] = True
            parent[child] = working_node
            level[child] = level[working_node] + 1
            queue.appendleft(child)
print(bfs_traversal_output)

